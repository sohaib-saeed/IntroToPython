def main():
    # t is 2i+j+5k
    tx = 2
    ty = 1
    tz = 5
	
    # m is 3i-2j+4k
    mx = 3
    my = -2
    mz = 4

    # b is 4i-j-2k
    bx = 4
    by = -1
    bz = -2

    print(f"t: ({tx}, {ty}, {tz})")
    print(f"m: ({mx}, {my}, {mz})")
    print(f"b: ({bx}, {by}, {bz})")

    # r is t+b
    rx = tx+bx
    ry = ty+by
    rz = tz+bz
    print(f"t+b: ({rx}, {ry}, {rz})")

    # s is stp ==>  t . m x b
    s = tx * (my*bz - by*mz) - ty * (mx*bz - bx*mz) + tz * (mx*by - bx*my)
    print(f"stp: {s}")

main()