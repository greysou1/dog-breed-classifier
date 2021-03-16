def post_worker_init(worker):
    import load_model from api
    load_model()