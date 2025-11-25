import argparse
import os
import shutil
import random

def collect_files(folder):
    files = []
    for root, dirs, fs in os.walk(folder):
        for f in fs:
            if f.lower().endswith((".jpg", ".jpeg", ".png")):
                files.append(os.path.join(root, f))
    return files

def copy_files(files, base_in, base_out):
    for src in files:
        rel = os.path.relpath(src, base_in)
        dst = os.path.join(base_out, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--animal_1", required=True)
    parser.add_argument("--animal_2", required=True)
    parser.add_argument("--animal_3", required=True)
    parser.add_argument("--split_percentage", type=int, default=20)
    parser.add_argument("--train_out", required=True)
    parser.add_argument("--test_out", required=True)
    args = parser.parse_args()

    os.makedirs(args.train_out, exist_ok=True)
    os.makedirs(args.test_out, exist_ok=True)

    all_folders = [args.animal_1, args.animal_2, args.animal_3]

    for folder in all_folders:
        files = collect_files(folder)
        random.shuffle(files)
        n_test = int(len(files) * args.split_percentage / 100)
        test_files = files[:n_test]
        train_files = files[n_test:]

        copy_files(train_files, folder, args.train_out)
        copy_files(test_files, folder, args.test_out)

    print("Split done.")

if __name__ == "__main__":
    main()