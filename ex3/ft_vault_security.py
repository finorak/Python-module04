def main() -> None:
    file_name = "security_protocols.txt"
    print("Initiating secure vault access...")
    with open(file_name, "r") as file:
        print("Vault connection established with", end=" ")
        print("failsafe protocols\n")
        lines = file.readlines()
        print("SECURE EXTRACTION:")
        for line in lines:
            print(line, end="")
    with open(file_name, "a") as file:
        print("\nSECURE PRESERVATION:")
        data = [
                "[CLASSIFIED] New security protocols archived\n",
                "[CLASSIFIED] File is good\n"
                ]
        for entry in data:
            print(entry, end="")
            file.write(entry)
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    main()
