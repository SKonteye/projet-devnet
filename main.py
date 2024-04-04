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
        print(f"Adresse IP: {ip_address}")
        print(f"Version IP: {version}")
        print(f"Devise: {currency}")
        print(f"Pays: {country}")
        print(f"Ville: {city}")
        print(f"Location: {latitude}, {longitude}")
        print(f"Fournisseur: {isp}")
        print(f"ASN: {asn}")
        
        print(data)
    except Exception as e:
        print(f"Erreur lors de la récupération des informations d'adresse IP: {e}")

if __name__ == "__main__":
    get_ip_info()
