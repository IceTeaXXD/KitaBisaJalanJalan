class ControllerBiayaTransportasi:
    def __init__(self, listTransport):
        self.listTransport = listTransport
        self.harga = 0

    def hitungBiaya(self) -> int:
        for t in self.listTransport:
            self.harga += t.getHarga()

        return self.harga