
from flask import Flask, request, jsonify
from job_queue.job_queue import JobQueue
from datetime import datetime

app = Flask(__name__)
job_queue = JobQueue()

@app.route('/api/job/create', methods=['POST'])
def create_job():
    data = request.json
    job_type = data.get('job_type')
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.add_job(job_type, priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/queue', methods=['GET'])
def get_jobs():
    jobs = job_queue.get_jobs()
    return jsonify({'jobs': [repr(job) for job in jobs]}), 200

@app.route('/api/job/create_principal_onboarding', methods=['POST'])
def create_principal_onboarding_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_principal_onboarding_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/create_gift_card_program_creation', methods=['POST'])
def create_gift_card_program_creation_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_gift_card_program_creation_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/create_distributor_onboarding', methods=['POST'])
def create_distributor_onboarding_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_distributor_onboarding_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/create_distributor_wallet_management', methods=['POST'])
def create_distributor_wallet_management_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_distributor_wallet_management_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/create_reconciliation', methods=['POST'])
def create_reconciliation_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_reconciliation_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/create_fund_transfer_to_principals', methods=['POST'])
def create_fund_transfer_to_principals_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_fund_transfer_to_principals_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/create_commission_and_discount_calculation', methods=['POST'])
def create_commission_and_discount_calculation_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_commission_and_discount_calculation_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

@app.route('/api/job/create_monitoring_and_alerts', methods=['POST'])
def create_monitoring_and_alerts_job():
    data = request.json
    priority = data.get('priority')
    expiry_date = data.get('expiry_date')
    expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d %H:%M:%S')
    job = job_queue.create_monitoring_and_alerts_job(priority, expiry_date)
    return jsonify({'job': repr(job)}), 201

if __name__ == '__main__':
    app.run(debug=True)
