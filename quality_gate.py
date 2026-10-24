"""Fail CI when model accuracy is below the required threshold."""
import json
from pathlib import Path
import sys

METRICS_PATH = Path(__file__).resolve().parent / "metrics.json"
MINIMUM_ACCURACY = 0.85


def main() -> int:
    if not METRICS_PATH.is_file():
        print("ERROR: metrics.json was not found. Run train_model.py first.")
        return 1
    try:
        metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
        accuracy = float(metrics["accuracy"])
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: Unable to read model accuracy from metrics.json: {exc}")
        return 1

    print(f"Measured model accuracy: {accuracy:.4f}")
    print(f"Required minimum accuracy: {MINIMUM_ACCURACY:.2f}")
    if accuracy < MINIMUM_ACCURACY:
        print("QUALITY GATE FAILED: model accuracy is below the minimum threshold.")
        return 1
    print("QUALITY GATE PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
