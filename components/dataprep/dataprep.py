import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--output_data", type=str, required=True)
    args = parser.parse_args()

    os.makedirs(args.output_data, exist_ok=True)

    # Very simple: copy everything over (you can add real preprocessing later)
    if os.path.isdir(args.data):
        for root, dirs, files in os.walk(args.data):
            for f in files:
                src = os.path.join(root, f)
                rel = os.path.relpath(src, args.data)
                dst = os.path.join(args.output_data, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    else:
        raise ValueError("Input --data must be a folder")

    print("Data prep done.")

if __name__ == "__main__":
    main()
