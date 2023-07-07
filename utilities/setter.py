import os
from base64 import b64decode


def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    with open('service_account.json', 'w') as json_file:
        json_file.write(b64decode(key).decode('utf-8'))
        print(os.path.realpath('service_account.json'))


if __name__ == '__main__':
    main()
