import hashlib
import wallet 

class Packet:
    def __init__(self):
        self.wallet_hash = wallet.wallet_data[1]
        self.data = self.datagen()
        self.hash = self.__hash__()

    def __hash__(self):
        #return hash(self.data)
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8'))
        return sha.hexdigest()

    def datagen(self):
        self.packet_data = 'PACKET DATA'
        return self.packet_data


def wallet_genesis():
    wallet.generate_new_wallet()
    wallet.print_cw()
    wallet.write_wallet()



def packet_genesis():
    wallet.parse_wallet()
    p = Packet()
    print('wallet hash: ', p.wallet_hash)
    print('wallet data', p.data)
    print('wallet data hash', p.hash)
    packet2send = [p.wallet_hash, p.data, p.hash]
    return packet2send
