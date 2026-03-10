def main() -> None:
    data = [
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n",
            "[ENTRY 003] Archived by Data Archivist trainees\n"
            ]
    file_name = "new_discovery.txt"
    print("\nInitializing new storage unit:", file_name)
    try:
        file = open(file_name, "w")
        print("Storage unit created successfully...\n")
        for entry in data:
            file.write(entry)
        file.close()
        file = open(file_name, "r")
        lines = file.readlines()
        for line in lines:
            print(line, end="")
        file.close()
        print("\nData inscription complete. Storage unit seald.")
        print(f"Archive '{file_name}' ready for long-term", end=" ")
        print("preservation")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESENTATION SYSTEM ===")
    main()
