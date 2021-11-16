import uvicorn
import nest_asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title='Read IPs and run commands')


# By using @app.get("/") you are allowing the GET method to work for the / endpoint.
@app.get("/")
def home():
    return "Congratulations! "


@app.post("/ui")
def prediction(username, password, ip_count, xml_name):
    with open('ipss.txt') as f:
        ips = f.read().splitlines()
        ips = ips[:int(ip_count)]

    with open('servername.txt') as g:
        srvname = g.read().splitlines()
        srvname = srvname[:int(ip_count)]
        
        
    with open('dnsname.txt') as h:
        dnsname = h.read().splitlines()
        dnsname = dnsname[:int(ip_count)]

        #   with open('hostname.txt') as z:
        #   ips2 = z.read().splitlines()
        #  ips2 = ips2[:int(ip_count)]

        ## returns a json
        # return [f"HPQLOCFG.exe -s {ip} -u {username} -p {password} -f {xml_name}" for ip in ips]

        ## return plain text/html
        body = [f"HPQLOCFG.exe -s {ip} -u {username} -p {password} -f {xml_name}.xml -t servername={srvname},dnsname={dnsname}" for ip, srvname,dnsname in
                zip(ips, srvname,dnsname)]

    html_content = '\n'.join(body)
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == '__main__':
    # Allows the server to be run in this interactive environment
    nest_asyncio.apply()

    # Host depends on the setup you selected (docker or virtual env)
    host = "0.0.0.0" if os.getenv("DOCKER-SETUP") else "127.0.0.1"

    # Spin up the server!    
    uvicorn.run(app, host=host, port=3000)
