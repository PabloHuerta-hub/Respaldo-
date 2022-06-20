import requests
def total_carrito(request):
    total = 0
    url = 'https://mindicador.cl/api/dolar/'
    response = requests.get(url)
    print(' status :' + str(response.status_code))
    datos = response.json()
    dolar_valor = datos['serie'][0]['valor']
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total += round(int(value["acumulado"])/ int(dolar_valor),2)
    return {"total_carrito_dolar": total}