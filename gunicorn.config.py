import load_model from api
def post_worker_init(worker):
    load_model()