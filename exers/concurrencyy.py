import time
import asyncio

def q():
    print("why can't programmers tell jokes?")
    time.sleep(3)

def a():
    print("Timing")

async def qq():
     print("async why can't programmers tell jokes?")
     await asyncio.sleep(3)
async def aa():
    print("async Timing!")

async def main():
    q()
    a()
    await asyncio.gather(qq(),aa())

# main()
asyncio.run(main())
