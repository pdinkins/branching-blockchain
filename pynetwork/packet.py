import hashlib


class Packet:
    def __init__(self):
        self.data = self.datagen()
        self.hash = self.__hash__()

    def __hash__(self):
        #return hash(self.data)
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8'))
        return sha.hexdigest(), hash(self.data)

    def datagen(self):
        return 'data stufff and stuff'

p = Packet()

print(p.hash)
print(p.data)
