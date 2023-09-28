import asyncio
import time


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count(), count(), count(), count(), count())

if __name__ == "__main__":
    startTime = time.time()
    asyncio.run(main())
    print("It takes", time.time() - startTime)
