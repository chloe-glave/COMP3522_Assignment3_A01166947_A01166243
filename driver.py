from pokeretriever.poke_retriever import PokeRetriever
import asyncio


async def main():
    poke = PokeRetriever()
    print(await poke.execute_request())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
