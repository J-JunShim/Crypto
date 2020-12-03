import random


class Transposition:
    def __init__(self, length):
        self.length = length  # split(key) length
        # make key(this is invisible because of underbar)
        self._keys = self._make_key(length)

    # Transposition encryption
    def encryption(self, plainText):
        cipherText = ''

        # split plain text and transpositioning with key
        for part in self._split_len(plainText):
            for key in sorted(self._keys):  # get sorted keys(same with range)
                # and then get index for it
                index = self._keys.index(key)
                try:
                    # join to cipher text
                    cipherText += part[index]
                except IndexError:
                    # continue for indexing error
                    continue

        return cipherText

    # Transposition decryption
    def decryption(self, cipherText):
        decipherText = ''

        # split cipher text and transpositioning with key
        for part in self._split_len(cipherText):
            for key in self._keys:  # get real position keys
                # and then get index for it in sorted key
                index = sorted(self._keys).index(key)
                try:
                    # join to decipher text
                    decipherText += part[index]
                except IndexError:
                    # continue for indexing error
                    continue

        return decipherText

    # make split text
    def _split_len(self, text):
        length = self.length

        return [text[i:i + length] for i in range(0, len(text), length)]

    # make shuffle key randomly
    @staticmethod
    def _make_key(length):
        keys = list(range(length))
        random.shuffle(keys)

        # tuple is immutable
        return tuple(keys)


# for test
if __name__ == '__main__':
    plain = input('문자 입력: ')

    transpos = Transposition(4)
    cipher = transpos.encryption(plain)
    decipher = transpos.decryption(cipher)

    print(f"plain: '{plain}'\ncipher: '{cipher}' ->\t'{decipher}'")
