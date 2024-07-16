import anyio
import logfire
from asapi import FromPath, Injected, bind, serve
from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool

# logfire.install_auto_tracing("compute")
from compute import fib

app = FastAPI()

logfire.configure(service_name="demo")
logfire.instrument_fastapi(app)
logfire.instrument_psycopg()

POSTGRESQL_DB_URL = "postgres://postgres:postgres@localhost:5432/postgres"


@app.get("/hello/{name}")
async def hello(name: FromPath[str], pool: Injected[AsyncConnectionPool]) -> int:
    async with pool.connection() as conn:
        async with conn.cursor() as cur:
            with logfire.span("postgres_fib"):
                await cur.execute(
                    "SELECT LENGTH('Hello ' || %(name)s || '!')", {"name": name}
                )
                res = await cur.fetchone()
                await anyio.sleep(1)
                assert res is not None
                return fib(res[0])


async def main() -> None:
    async with AsyncConnectionPool(POSTGRESQL_DB_URL) as pool:
        bind(app, AsyncConnectionPool, pool)
        await serve(app, 8000)


if __name__ == "__main__":
    anyio.run(main)
