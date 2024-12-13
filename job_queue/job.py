
class Job:
    def __init__(self, job_type, priority, expiry_date, state='Created'):
        self.job_type = job_type
        self.priority = priority
        self.expiry_date = expiry_date
        self.state = state

    def __repr__(self):
        return f"Job(type={self.job_type}, priority={self.priority}, expiry_date={self.expiry_date}, state={self.state})"
