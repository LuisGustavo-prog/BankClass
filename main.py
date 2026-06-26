import asyncio
import uvicorn
from src.database.connection import check_mongo

if __name__ == "__main__":
    if not asyncio.run(check_mongo()):
        raise ConnectionError('database turned off')
    
    uvicorn.run('src.api.main:app', host='0.0.0.0', port=8000, reload=True)
