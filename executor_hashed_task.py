import hashlib
import pickle

from creator_hashed_task import SECKRET_KEY


def execute_task():
    with open('task.pkl', 'rb') as f:
        hash_ = f.read(32)
        data = f.read()

        if hashlib.sha256(SECKRET_KEY + data).digest() != hash_:
            raise Exception

        task = pickle.loads(data)

    print(f'Task {task.name} was executed')
    print(f'Result: {task.action}')


if __name__ == '__main__':
    execute_task()
