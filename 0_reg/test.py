import os
import random
import numpy as np

print("IP 初期設定")

# Open files
fd_h2c = os.open("/dev/xdma0_h2c_0", os.O_WRONLY)
fd_c2h = os.open("/dev/xdma0_c2h_0", os.O_RDONLY)


print("レジスタアクセス")

wdata = random.randrange(1<<64)
print('wdata', hex(wdata))

os.pwrite(fd_h2c, wdata.to_bytes(8, byteorder='little'), 0x20000000);

rdata = os.pread(fd_c2h, 8, 0x20000000)
wstrb = os.pread(fd_c2h, 4, 0x20000008)

print('rdata', hex(int.from_bytes(rdata,'little')))
print('wstrb', hex(int.from_bytes(wstrb,'little')))

rdata = os.pread(fd_c2h, 4, 0x20000010)
print('lower', hex(int.from_bytes(rdata,'little')))
rdata = os.pread(fd_c2h, 4, 0x20000018)
print('upper', hex(int.from_bytes(rdata,'little')))
