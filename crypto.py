import os

from pathlib import Path
from itertools import repeat, chain

if __name__ == "__main__":
    from transposition import Transposition
else:
    from .transposition import Transposition


def file_io(path, mode, text=None):
    with open(path, mode=mode) as f:
        if mode == 'r':
            text = f.read()
        elif mode == 'w':
            f.write(text)
            if os.path.isfile(path):
                print('저장 완료!!\t주소:', path)
            else:
                print('실패')

        f.close()
    return text


class Crypto(Transposition):
    def cryption(self, text, isCrypted=False):
        def cryptor(char, key):
            return chr(ord(char) + (-key if isCrypted else key))

        result = list(
            map(cryptor, text, chain.from_iterable(repeat(self._keys))))

        return ''.join(result)

    def encryptor(self, plainText):
        return self.cryption(self.encryption(plainText))

    def decryptor(self, cipherText):
        return self.decryption(self.cryption(cipherText, True))


if __name__ == "__main__":
    root = Path('./data').absolute()
    plain = file_io((root/'과제.txt'), mode='r')

    crypto = Crypto(5)
    cipher = crypto.encryptor(plain)
    decipher = crypto.decryptor(cipher)

    file_io((root/'과제_암호화.txt'), mode='w', text=cipher)

    print(
        f"\n\n{'-' * 80}\n\nplain text:\n'{plain}'\n\n{'-' * 80}\n\ncipher text:\n'{cipher}'\n\n==>\n\n'{decipher}'")
