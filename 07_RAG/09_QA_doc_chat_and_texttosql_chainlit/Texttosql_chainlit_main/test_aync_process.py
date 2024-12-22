"""import time

def do_somthing():
    print("start the task")
    time.sleep(8)
    print("task completed")

print("before task")
do_somthing()
print("after task")"""

# Define above function in asynch IO, we need to use asyncio library like below
# async keyword should use before function/method
# await keyword should use before calling function/method
# This async helps to do run parallely without ant wait or system paus
import asyncio


async def do_somthing():
    print("start the task")
    await asyncio.sleep(8)
    print("task completed")


async def main():
    print("before task")
    await do_somthing()
    print("after task")


asyncio.run(main())


m = [
    {
        "role": "user",
        "content": "\n\nwrite a well written sql query that can you give me a query for fetching data from database\n\n",
    }
]
print(m[0]["content"])
