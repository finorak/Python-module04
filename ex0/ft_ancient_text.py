def main() -> None:
    file_name = "ancient_fragment.txt"
    print("\nAccessing Storage Vault:", file_name)
    try:
        file = open("./" + file_name, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        lines = file.read()
        print(lines)
        file.close()
        print("\n\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.", end=" ")
        print("Run data generator first.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    main()
