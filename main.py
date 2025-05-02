import http.client
import json
import ssl

def check_hash(api_key, hash_value):
    context = ssl.create_default_context()
    conn = http.client.HTTPSConnection("www.virustotal.com", context=context)
    headers = {
        "x-apikey": api_key
    }

    conn.request("GET", f"/api/v3/files/{hash_value}", headers=headers)
    response = conn.getresponse()

    if response.status == 200:
        data = response.read()
        return json.loads(data.decode("utf-8"))
    else:
        return {"error": f"Error {response.status}: {response.reason}"}

def check_ip(api_key, ip_address):
    context = ssl.create_default_context()
    conn = http.client.HTTPSConnection("www.virustotal.com", context=context)
    headers = {
        "x-apikey": api_key
    }

    conn.request("GET", f"/api/v3/ip_addresses/{ip_address}", headers=headers)
    response = conn.getresponse()

    if response.status == 200:
        data = response.read()
        return json.loads(data.decode("utf-8"))
    else:
        return {"error": f"Error {response.status}: {response.reason}"}

def check_domain(api_key, domain):
    context = ssl.create_default_context()
    conn = http.client.HTTPSConnection("www.virustotal.com", context=context)
    headers = {
        "x-apikey": api_key
    }

    conn.request("GET", f"/api/v3/domains/{domain}", headers=headers)
    response = conn.getresponse()

    if response.status == 200:
        data = response.read()
        return json.loads(data.decode("utf-8"))
    else:
        return {"error": f"Error {response.status}: {response.reason}"}

api_key = input("VirusTotal API anahtarınızı girin: ")
query = input("Sorgulamak istediğiniz dosya hash, IP adresi veya domaini girin: ")


if len(query) == 64 or len(query) == 40:  
    result = check_hash(api_key, query)
elif query.count(".") == 3:  
    result = check_ip(api_key, query)
else:  
    result = check_domain(api_key, query)

with open("data.json", "w") as json_file:
    json.dump(result, json_file, indent=4)



with open("data.json", "r") as json_file:
    data = json.load(json_file)

filtered_data = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})

print(json.dumps(filtered_data, indent=4))
   
