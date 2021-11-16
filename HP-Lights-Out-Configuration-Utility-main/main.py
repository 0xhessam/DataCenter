import uvicorn
import nest_asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title='Read IPs and run commands')

# By using @app.get("/") you are allowing the GET method to work for the / endpoint.
@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:8000/docs."


@app.post("/ui") 
def prediction(username, password, ip_count, xml_name):
    with open('ips.txt') as f:
        ips = f.read().splitlines()
        ips = ips[:int(ip_count)]

    ## returns a json
    # return [f"HPQLOCFG.exe -s {ip} -u {username} -p {password} -f {xml_name}" for ip in ips]
    
    ## return plain text/html
    body = [f"HPQLOCFG.exe -s {ip} -u {username} -p {password} -f {xml_name}" for ip in ips]
    html_content = '\n'.join(body)
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == '__main__':
    # Allows the server to be run in this interactive environment
    nest_asyncio.apply()

    # Host depends on the setup you selected (docker or virtual env)
    host = "0.0.0.0" if os.getenv("DOCKER-SETUP") else "127.0.0.1"

    # Spin up the server!    
    uvicorn.run(app, host=host, port=8000)