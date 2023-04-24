#!/usr/bin/env python3

import json
import time
from random import SystemRandom

# Configuration

N_WORDS = 2
_LIMIT = 9999999
DO_BENCHMARK = True


def load_json(file_name):
    with open(f'{file_name}.json') as _file:
        data = json.load(_file)
        return data


def generate():
    if DO_BENCHMARK:
        start_time = time.time()

    file = load_json('cities')

    word_list = [c['name'] for c in file]

    crypto = SystemRandom()

    indexes = [crypto.randrange(len(word_list)) for i in range(N_WORDS)]

    words = [word_list[index] for index in indexes]

    # Process

    words = [word.capitalize() for word in words]
    words = [word.rstrip() for word in words]
    words = [word.replace(" ", '_') for word in words]
    words = [word.replace("'s", '') for word in words]  # remove 's

    pass_phrase = '&'.join(words);
    pin = str(crypto.randrange(_LIMIT))

    print(f"{pass_phrase}- {str(pin)}")

    if DO_BENCHMARK:
        print('\nTotal Time: %s secs ' % str.format('{0:.5f}', (time.time() - start_time)))

    # write json
    with open('passphrase.json', 'w', encoding='utf-8') as f:
        json.dump({'pass_phrase': pass_phrase, 'pin': pin}, f, ensure_ascii=True, indent=4)

if __name__ == '__main__':
    try:
        generate()
    except Exception as e:
        print("Fatal Error" + str(e))
