import sys


def main() -> None:
    try:
        id_ = input("Input Stream active. Enter archivist ID: ")
        report = input("input Stream active. Enter status report: ")
        print(f"\n[STANDARD] Archive status from {id_}: ", end="")
        print(f"{report}")
        comm = "Communication channels verified"
        print(f"[ALERT] System diagnostic: {comm}", file=sys.stderr)
        print("[STANDARD] Data trancmission complete")
        print("\nThree-channel communication test successful")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    main()
