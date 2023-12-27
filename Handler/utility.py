from Persistence import DbContext

def text_for_her():
    return send_random(DbContext.tell_here_repo)

def tell_chuck():
    return send_random(DbContext.chuck_repo)

def tell_coding_joke():
    return send_random(DbContext.coding_jokes_repo)

def send_random(repo):
    return repo.get_random()
