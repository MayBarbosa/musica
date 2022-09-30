from msilib.schema import Environment
from os import environ
from motor.motor_asyncio import AsyncIOMotorClient


async def testar_atlas():
    url = environ.get("DATABASE_URI")
    cliente_mongo = AsyncIOMotorClient(url)
    
    bd = cliente_mongo.get_default_database()
    
    colecao_teste01 = bd["teste01"]
    
    await colecao_teste01.insert_one({
        "teste": "Ana Cortez",
        "codigo": 1
    })
    
    print("Pronto!")
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(testar_atlas())
    
    
#não esquecer de instalar o pip install pymongo[srv]
