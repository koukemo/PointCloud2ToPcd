import glob
import os

def main():
    file_path = "./pcd/*.pcd"
    counter = 0

    # get pcd file name
    b_file_list = glob.glob(file_path)
    print(f"Before: {b_file_list}")

    for f in b_file_list:
        os.rename(f, "./pcd/p_" + str(counter) + ".pcd")
        counter += 1

    # change pcd file name
    a_file_list = glob.glob(file_path)
    print(f"After: {a_file_list}")

if __name__ == "__main__":
    main()
