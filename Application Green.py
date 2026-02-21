import os,shutil,sys,time
offsetsarr = [
    (0x128DA5, b"\x74", b"\xEB"),
    (0x128DEB, b"\x75", b"\xEB")
]
def select_file():
    if len(sys.argv) > 1:
        return sys.argv[1]
    path = input("drag in exe or paste file patch: ").strip('"')
    return path
def backup_file(path):
    bp = path + ".pbbak"
    if not os.path.exists(bp):
        shutil.copy2(path, bp)
        print(f"created backup: {bp}")
        time.sleep(0.5)
    else:
        print("u already have a backup, skipping backup creation")
def apply_patches(path):
    print("\nopening file")

    with open(path, "r+b") as f:
        for loc, old, new in offsetsarr:
            print(f"\nchecking location offsets {hex(loc)}")

            f.seek(loc)
            current = f.read(len(old))

            print(f"    Current bytes: {current.hex()}")
            time.sleep(0.5)

            if old != b"\x00" and current != old:
                print("    bytes already patched, or unexpected bytes found, skipping")
                continue

            f.seek(loc)
            f.write(new)

            print("    file patched successfuly")

    print("\ndone")
def main():
    print("Welcome to application green")
    target = select_file()
    if not os.path.exists(target):
        print("file doesnt exist")
        return
    print(f"\nTarget: {target}")
    backup_file(target)
    apply_patches(target)
if __name__ == "__main__":
    main()
    input('Press enter to exit...')