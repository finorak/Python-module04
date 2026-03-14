def main() -> None:
    file_name = "security_protocols.txt"
    print("Initiating secure vault access...")
    try:
        with open(file_name, "r") as file:
            print("Vault connection established with", end=" ")
            print("failsafe protocols\n")
            lines = file.read()
            print("SECURE EXTRACTION:")
            print(lines)
        with open(file_name, "a") as file:
            print("\nSECURE PRESERVATION:")
            data = """[CLASSIFIED] New security protocols archived
[CLASSIFIED] File is good"""
            file.write(data)
    except Exception as e:
        print(f"ERROR: {e}")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    main()
