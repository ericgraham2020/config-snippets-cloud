import requests
import urllib.request
import json
ip = urllib.request.urlopen("http://169.254.169.254/latest/meta-data/local-ipv4").read()
ip = ip.decode("utf-8")

headers = {
    'x-ch-auth-email': '<your_email_here>',
    'x-ch-auth-api-token': '<your_api_token>',
    'accept': 'application/json',
    'Content-Type': 'application/json',
}


data = '{"agent": {"local_ip": "%s" }, "mask": "agent.local_ip" }' % ip

json.dumps(data)

response = requests.patch('https://synthetics.api.kentik.com/synthetics/v202101beta1/agents/1978', headers=headers, data=data)
print(response.text.encode('utf8'))
