import asyncio

async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(6-power)
        print(f'Силач {name} поднял {i+1} шар')
    print(f'Силач {name} окончил соревнования')

async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman3 = asyncio.create_task(start_strongman('Apollon', 5))
    await strongman1
    await strongman2
    await strongman3

if __name__ == "__main__":
    asyncio.run(start_tournament())