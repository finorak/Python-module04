import sys


def ft_strip(string: str) -> str:
    strings = ""
    for char in string:
        if char == "\n":
            break
        strings += char
    return strings


def main() -> None:
    print("\nInput Stream active. Enter archivist ID: ", end="", flush=True)
    id_ = ft_strip(sys.stdin.readline())
    print("input Stream active. Enter status report: ", end="", flush=True)
    report = ft_strip(sys.stdin.readline())
    sys.stdout.write(f"\n[STANDARD] Archive status from {id_}: ")
    sys.stdout.write(f"All systems norminal: {report}\n")
    comm = "Communication channels verified"
    sys.stderr.write(f"[ALERT] System diagnostic: {comm}\n")
    sys.stdout.write("[STANDARD] Data trancmission complete\n")
    print("\nThree-channel communication test successful")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    main()
