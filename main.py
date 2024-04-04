import requests

def get_ip_info():
    try:
        # Appel à l'API ipapi.co pour obtenir les informations d'adresse IP
        response = requests.get('https://ipapi.co/json/')
        data = response.json()
        # print(data)
        # Extraction des informations pertinentes
        ip_address = data['ip']
        version = data['version']
        currency = data['currency']
        country = data['country']
        city = data['city']
        latitude = data['latitude']
        longitude = data['longitude']
        isp = data['org']
        asn = data['asn']

        # Affichage des informations
        result = f"Adresse IP : {ip_address}\nVersion IP : {version}\nDevise : {currency}\nPays : {country}\nVille : {city}\nLatitude : {latitude}\nLongitude : {longitude}\nFournisseur : {isp}\nASN : {asn}"
        print(result)
        
        print(data)
    except Exception as e:
        print(f"Erreur lors de la récupération des informations d'adresse IP: {e}")

if __name__ == "__main__":
    get_ip_info()
