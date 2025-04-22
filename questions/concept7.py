import asyncio
import time


def task(name):
    print(f"INICIANDO LA TAREA  {name}")
    time.sleep(4)
    print(f"FINALIZANDO LA TAREA  {name}")


task("estudiar")
task("cocinar")


async def task(name):
    print("executing the async function")
    print(f"INICIANDO LA TAREA  {name}")
    await asyncio.sleep(4)
    print(f"FINALIZANDO LA TAREA  {name}")


async def main():
    await asyncio.gather(task("nadando"),task("caminando"))

asyncio.run(main())