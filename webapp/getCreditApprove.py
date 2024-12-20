import requests

def get_approval(data=[]):
    try:
        request_url = "https://creditapprovalml-production.up.railway.app/credit"
        r = requests.post(request_url, json={"form": data})
        r.raise_for_status()
        result = r.json().get("status")
        
        if result == '1':
            return "approved"
        else:
            return "rejected"
        
    except (requests.RequestException, KeyError) as e:
        
        print(f"Error during API call: {e}")
        return "error"
