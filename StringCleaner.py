import pymem

def main():
    print("String cleaner by ykela")
    print("")


    procname = input("Enter the process name: ").strip()
    try:
        pm = pymem.Pymem(procname)
        print(f"Attached to process: {procname} (PID: {pm.process_id})")
    except Exception as e:
        print(f"Error: Could not attach to process '{procname}'. Make sure it is running and you have the correct name.")
        return

    address = input("Enter the memory address (hex): ").strip()
    try:
        address = int(address, 16)
    except ValueError:
        print("Error: Invalid memory address format. Please enter a valid hexadecimal address.")
        return

    length = input("Enter the length of the string to clean: ").strip()
    try:
        length = int(length)
    except ValueError:
        print("Error: Length must be a valid integer.")
        return

    confirm = input(f"Are you sure you want to overwrite {length} bytes at {hex(address)}? (yes/no): ").strip().lower()
    if confirm not in ("yes", "y"):
        print("Operation canceled.")
        return

    try:
        original_string = pymem.memory.read_string(pm.process_handle, address, length)
        print(f"Original string at {hex(address)}: {original_string}")
        
        overwrite_data = "." * length
        pymem.memory.write_string(pm.process_handle, address, overwrite_data)
        print(f"String overwritten with: {overwrite_data}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        pm.close_process()
        print("Process detached.")

if __name__ == "__main__":
    main()
