
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

if __name__ == '__main__':
    app.run(debug=True)
