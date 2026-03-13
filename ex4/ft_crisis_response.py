def main(file_name: str) -> None:
    alert = f"Attempting access to '{file_name}'..."
    response = None
    response_line = None
    status = "Normal operations resumed"
    print("\nCRISIS ALERT:", alert)
    try:
        with open(file_name, "r") as file:
            response_line = file.read()
    except FileNotFoundError:
        response = "RESPONSE: Archive not found in storage matrix"
        status = "Crisis handled, system stable"
    except PermissionError:
        response = "RESPONSE: Read persmission denied"
        status = "Crisis handled, security maintained"
    if response_line:
        print("CRISIS ALERT: ", end="")
        print(f"Archive recovered - ``{response_line}``")
    else:
        print(response)
    print("STATUS:", status)


def test() -> None:
    # file not found
    main("lost_archived.txt")
    # access denied
    main("classified_vault.txt")
    # normal
    main("standard_archive.txt")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    test()
