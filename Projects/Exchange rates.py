import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
print()
if response.ok == True:
    data = response.json()[0]
    print(data)

    table = data["table"]
    no = data["no"]
    effective_data = data["effectiveDate"]
    print(table, no, effective_data)
    
    rates = data["rates"]

    for rate in rates:
        currency = rate["currency"]
        code = rate["code"]
        mid = rate["mid"]
        print(currency, "code: ", code, "value: ", mid)
