from fastapi import FastAPI
import json

app = FastAPI()

@app.post("/webhook")
async def receive_signal(data: dict):
    print("Получен сигнал от TradingView:", json.dumps(data, indent=4))
    
    # Здесь можно добавить анализ полученного сигнала
    response = {"status": "ok", "message": "Сигнал получен"}
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
