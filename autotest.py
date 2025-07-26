import subprocess
import filecmp
import shutil


def run_round_trip():
    print("Running first conversion: YAML → Header")
    subprocess.run(["python3", "main.py"], check=True)

    print("Compiling C program")
    subprocess.run(["make"], check=True)

    print("Running C program: Header → YAML")
    subprocess.run(["./parse"], check=True)

    print("\n[ROUND 2] Using regenerated YAML as input")
    shutil.copyfile("output/regenerated.yaml", "input/add.yaml")

    print("Generating header again from regenerated YAML")
    subprocess.run(["python3", "main.py"], check=True)

    print("Running parse again to regenerate YAML from new header")
    subprocess.run(["./parse"], check=True)

    print("\nComparing output/regenerated.yaml with input/add.yaml...")
    if filecmp.cmp("output/regenerated.yaml", "input/add.yaml", shallow=False):
        print("Success: Round-trip conversion is stable and YAML matches!")
    else:
        print("Failure: Round-trip YAML does not match!")
        subprocess.run(["diff", "input/add.yaml", "output/regenerated.yaml"])

if __name__ == "__main__":
    run_round_trip()
