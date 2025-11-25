import argparse
import os
import json
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True)
    parser.add_argument("--test", required=True)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    # For the assignment, a dummy "model" is enough – the focus is MLOps.
    # You can replace this with real TensorFlow code if you like.
    model_info = {
        "trained_at": datetime.utcnow().isoformat(),
        "train_folder": args.train,
        "test_folder": args.test,
        "epochs": args.epochs,
        "note": "Dummy model artifact for MLOps pipeline."
    }

    with open(os.path.join(args.output, "model.json"), "w") as f:
        json.dump(model_info, f)

    print("Training completed, dummy model saved.")

if __name__ == "__main__":
    main()