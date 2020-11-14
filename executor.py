import pickle


def execute_task():
    with open('task.pkl', 'rb') as f:
        task = pickle.load(f)

    print(f'Task {task.name} was executed')
    print(f'Result: {task.action}')


if __name__ == '__main__':
    execute_task()
