from fastapi import FastAPI
from uvicorn import Server, Config
from threading import Thread

app = FastAPI()

@app.get('/')
async def main():
    return {"status": "Your bot is alive!"}

def run():
    # Using uvicorn with production settings
    config = Config(
        app=app,
        host="0.0.0.0",
        port=8080,
        workers=1,
        loop="asyncio",
        log_level="info"
    )
    server = Server(config=config)
    server.run()

def keep_alive():
    server = Thread(target=run, daemon=True)
    server.start()
