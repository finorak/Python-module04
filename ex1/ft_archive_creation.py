def main() -> None:
    data = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainees"""
    file_name = "new_discovery.txt"
    print("\nInitializing new storage unit:", file_name)
    try:
        file = open(file_name, "w")
        print("Storage unit created successfully...\n")
        file.write(data)
        print(data)
        file.close()
        print("\nData inscription complete. Storage unit seald.")
        print(f"Archive '{file_name}' ready for long-term", end=" ")
        print("preservation")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESENTATION SYSTEM ===")
    main()
