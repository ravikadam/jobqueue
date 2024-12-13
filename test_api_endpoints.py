
import requests
import json

BASE_URL = 'http://127.0.0.1:5000/api/job/'

def test_create_job(endpoint, priority, expiry_date):
    url = BASE_URL + endpoint
    payload = {
        'priority': priority,
        'expiry_date': expiry_date
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Endpoint: {endpoint}, Status Code: {response.status_code}, Response: {response.json()}")

expiry_date = '2024-12-14 09:02:03'

endpoints = [
    'create_principal_onboarding',
    'create_gift_card_program_creation',
    'create_distributor_onboarding',
    'create_distributor_wallet_management',
    'create_reconciliation',
    'create_fund_transfer_to_principals',
    'create_commission_and_discount_calculation',
    'create_monitoring_and_alerts'
]

for endpoint in endpoints:
    test_create_job(endpoint, 'High', expiry_date)
