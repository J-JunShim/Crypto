import random


class Transposition:
    def __init__(self, length):
        self.length = length
        self._keys = self._make_key(length)

    def encryption(self, plainText):
        cipherText = ''

        for part in self._split_len(plainText):
            for key in sorted(self._keys):
                index = self._keys.index(key)
                try:
                    cipherText += part[index]
                except IndexError:
                    continue

        return cipherText

    def decryption(self, cipherText):
        decipherText = ''

        for part in self._split_len(cipherText):
            for key in self._keys:
                index = sorted(self._keys).index(key)
                try:
                    decipherText += part[index]
                except IndexError:
                    continue

        return decipherText

    def _split_len(self, seq):
        seq = self._pre_processing(seq)
        length = self.length

        return [seq[i:i + length] for i in range(0, len(seq), length)]

    @staticmethod
    def _pre_processing(text):
        return text.replace(' ', '')

    @staticmethod
    def _make_key(length):
        keys = list(range(length))
        random.shuffle(keys)

        return tuple(keys)


if __name__ == '__main__':
    plain = input('문자 입력: ')

    transpos = Transposition(4)
    cipher = transpos.encryption(plain)
    decipher = transpos.decryption(cipher)

    print(f"plain: '{plain}'\ncipher: '{cipher}' ->\t'{decipher}'")
