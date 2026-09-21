import subprocess
import sys

print("=" * 50)
print("          CROP RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nStarting Crop & Fertilizer Recommendation...\n")

subprocess.run(
    [sys.executable, "src/predict.py"]
)

print("\n" + "=" * 50)
print("              SYSTEM COMPLETED")
print("=" * 50)