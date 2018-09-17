import numpy

class TH1F(object):

    def __init__(self, nbinsx, xlow, xup):
        self.string = ""
        self.nbinsx = nbinsx
        self.xlow = xlow
        self.xup = xup
        self.fObjlen = 0
        self.bins = []

    def fill(self, bin):
        self.bins.append(bin)

    def values1(self):
        cnt = self.fObjlen - 4
        kByteCountMask = numpy.int64(0x40000000)
        cnt = cnt | kByteCountMask
        vers = 2
        packer = ">IH"
        return cnt, vers, packer

#Unable to figure it out yet
    def values2(self):
        cnt =  533 #?
        cnt = cnt - 4
        kByteCountMask = numpy.int64(0x40000000)
        cnt = cnt | kByteCountMask
        vers = 8
        packer = ">IH"
        return cnt, vers, packer

    def values3(self):
        bytestream = [ 64,   0,   0,  33,   0,   1,   0,   1,   0,   0,   0,   0,   3,
          0,   0,   8,   9, 116, 104,  49, 102,  32, 110,  97, 109, 101,
         10, 116, 104,  49, 102,  32, 116, 105, 116, 108, 101,  64,   0,
          0,   8,   0,   2,   2,  90,   0,   1,   0,   1,  64,   0,   0,
          6,   0,   2,   0,   0,   3, 233,  64,   0,   0,  10,   0,   2,
          0,   1,   0,   1,  63, 128,   0,   0,   0,   0,   0,  12,  64,
          0,   0, 109,   0,  10,  64,   0,   0,  19,   0,   1,   0,   1,
          0,   0,   0,   0,   3,   0,   0,   0,   5, 120,  97, 120, 105,
        115,   0,  64,   0,   0,  36,   0,   4,   0,   0,   1, 254,   0,
          1,   0,   1,   0,  42,  59, 163, 215,  10,  61,  15,  92,  41,
         60, 245, 194, 143,  63, 128,   0,   0,  61,  15,  92,  41,   0,
          1,   0,  42]
        return numpy.frombuffer(bytes(bytestream), dtype=numpy.uint8)

    def values4(self):
        return self.nbinsx, self.xlow, self.xup

    def values5(self):
        bytestream = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  64,   0,
          0, 109,   0,  10,  64,   0,   0,  19,   0,   1,   0,   1,   0,
          0,   0,   0,   3,   0,   0,   0,   5, 121,  97, 120, 105, 115,
          0,  64,   0,   0,  36,   0,   4,   0,   0,   1, 254,   0,   1,
          0,   1,   0,  42,  59, 163, 215,  10,  61,  15,  92,  41,  60,
        245, 194, 143,   0,   0,   0,   0,  61,  15,  92,  41,   0,   1,
          0,  42,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,
          0,  63, 240,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,  64,   0,   0, 109,   0,  10,
         64,   0,   0,  19,   0,   1,   0,   1,   0,   0,   0,   0,   3,
          0,   0,   0,   5, 122,  97, 120, 105, 115,   0,  64,   0,   0,
         36,   0,   4,   0,   0,   1, 254,   0,   1,   0,   1,   0,  42,
         59, 163, 215,  10,  61,  15,  92,  41,  60, 245, 194, 143,  63,
        128,   0,   0,  61,  15,  92,  41,   0,   1,   0,  42,   0,   0,
          0,   1,   0,   0,   0,   0,   0,   0,   0,   0,  63, 240,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   3, 232,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0, 192, 145,  92,   0,   0,
          0,   0,   0, 192, 145,  92,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,  64,   0,   0,  17,   0,   5,   0,   1,   0,   0,   0,
          0,   3,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
          0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,
         12,   0,   0,   0,   0,  64, 192,   0,   0]
        return numpy.frombuffer(bytes(bytestream), dtype=numpy.uint8)

    def values6(self):
        bytestream = [ 64, 192,   0,   0,  64,  64,   0,   0,  64, 160,   0,   0,  64,
        224,   0,   0,  64, 128,   0,   0,  64,   0,   0,   0,  65,  32,
          0,   0,  64, 160,   0,   0,  64, 160,   0,   0,  63, 128,   0,
          0,   0,   0,   0,   0]
        return numpy.frombuffer(bytes(bytestream), dtype=numpy.uint8)
