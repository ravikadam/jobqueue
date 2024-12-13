
from job import Job
from datetime import datetime

class JobQueue:
    def __init__(self):
        self.queue = []

    def add_job(self, job_type, priority, expiry_date):
        job = Job(job_type, priority, expiry_date)
        self.queue.append(job)
        return job

    def remove_job(self, job):
        self.queue.remove(job)

    def get_jobs(self):
        return self.queue

    def __repr__(self):
        return f"JobQueue({self.queue})"
