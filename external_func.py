import numpy as np
import datetime as dt


def random_date():
    print('Writing in file')
    d = np.random.randint(1, 11)
    with open('airflow_test_v1.txt', 'a+', encoding='utf8') as f:
        now = dt.datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
        f.write(str(d))
        f.write('\n')
        f.write('Greeted')
