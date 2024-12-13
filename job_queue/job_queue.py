
from job import Job
from datetime import datetime
from persistence.database import get_connection

class JobQueue:
    def __init__(self):
        self.queue = []

    def add_job(self, job_type, priority, expiry_date):
        job = Job(job_type, priority, expiry_date)
        self.queue.append(job)
        self.save_job_to_db(job)
        return job

    def remove_job(self, job):
        self.queue.remove(job)
        self.delete_job_from_db(job)

    def get_jobs(self):
        return self.queue

    def save_job_to_db(self, job):
        conn = get_connection()
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO jobs (job_type, priority, expiry_date, state)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (job.job_type, job.priority, job.expiry_date, job.state))
        conn.commit()
        cursor.close()
        conn.close()

    def delete_job_from_db(self, job):
        conn = get_connection()
        cursor = conn.cursor()
        delete_query = '''
        DELETE FROM jobs WHERE job_type = %s AND priority = %s AND expiry_date = %s AND state = %s
        '''
        cursor.execute(delete_query, (job.job_type, job.priority, job.expiry_date, job.state))
        conn.commit()
        cursor.close()
        conn.close()

    def create_principal_onboarding_job(self, priority, expiry_date):
        return self.add_job('Principal Onboarding', priority, expiry_date)

    def create_gift_card_program_creation_job(self, priority, expiry_date):
        return self.add_job('Gift Card Program Creation', priority, expiry_date)

    def create_distributor_onboarding_job(self, priority, expiry_date):
        return self.add_job('Distributor Onboarding', priority, expiry_date)

    def create_distributor_wallet_management_job(self, priority, expiry_date):
        return self.add_job('Distributor Wallet Management', priority, expiry_date)

    def create_reconciliation_job(self, priority, expiry_date):
        return self.add_job('Reconciliation', priority, expiry_date)

    def create_fund_transfer_to_principals_job(self, priority, expiry_date):
        return self.add_job('Fund Transfer to Principals', priority, expiry_date)

    def create_commission_and_discount_calculation_job(self, priority, expiry_date):
        return self.add_job('Commission and Discount Calculation', priority, expiry_date)

    def create_monitoring_and_alerts_job(self, priority, expiry_date):
        return self.add_job('Monitoring and Alerts', priority, expiry_date)

    def __repr__(self):
        return f"JobQueue({self.queue})"
