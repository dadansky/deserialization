import pickle
import hashlib
from task import Task

SECKRET_KEY = b"omqho][p1234qwqe]r/z/s5=45204nyhugo"


def create_task():
    task = Task('my_task', 'jump')
    pickled = pickle.dumps(task)
    hash_ = hashlib.sha256(SECKRET_KEY + pickled).digest()

    with open('task.pkl', mode='wb') as f:
        f.write(hash_)
        f.write(pickled)

if __name__ == '__main__':
    create_task()
