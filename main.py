import zlib
import binascii
import struct

replay = open("Коричневый 20 банок сгущёнки.wrpl", "rb")

replay.read(1112)

a = replay.read(4)
length = struct.unpack("i", a)
replay.read(length[0])

unpacked = zlib.decompress(replay.read())
print(len(unpacked))
unpacked_replay = open("unpacked.txt", "wb")
unpacked_replay.write(unpacked)