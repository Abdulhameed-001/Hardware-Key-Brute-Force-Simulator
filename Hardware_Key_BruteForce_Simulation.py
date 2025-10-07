# Hardware Key Brute-Force Simulator

print("=== HARDWARE KEY BRUTE-FORCE SIMULATOR (configurable range) ===")

# --- Get target PIN ---
target = input("Enter target PIN (1 to 4 digits): ").strip()

if not target.isdigit() or not (1 <= len(target) <= 4):
    print("Invalid PIN format. Please enter 1 to 4 digits.")
    exit(1)
target_pin = target.zfill(4)

# --- Get maximum search range ---
range_input = input("Enter max range to try (1-10000, default 10000): ").strip()

if range_input == "":
    max_range = 10000
else:
    try:
        max_range = int(range_input)
        if max_range < 1 or max_range > 10000:
            print("Range out of bounds. Using default 10000.")
            max_range = 10000
    except ValueError:
        print("Invalid number. Using default 10000.")
        max_range = 10000

# --- Verbose or summary mode ---
mode = input("Verbose? (y/N) — 'y' prints every attempt, otherwise summary + progress every N attempts: ").strip().lower()
verbose = (mode == "y")

# --- Progress interval (only used when not verbose) ---
if not verbose:
    interval_input = input("Show progress every N attempts (default 100): ").strip()
    try:
        progress_interval = int(interval_input) if interval_input else 100
        if progress_interval <= 0:
            raise ValueError
    except ValueError:
        print("Invalid interval. Using default: 100")
        progress_interval = 100
else:
    progress_interval = None  # unused in verbose mode

# --- Brute-force loop (uses user-provided max_range) ---
attempts = 0
found = False

# ensure we do not iterate beyond 9999 even if user enters >10000
search_limit = min(max_range, 10000)

for i in range(search_limit):  # 0 .. search_limit-1
    guess = str(i).zfill(4)
    attempts += 1

    if verbose:
        print(f"Trying PIN: {guess}")
    else:
        if attempts % progress_interval == 0:
            print(f"Progress: tried {attempts} PINs (latest: {guess})")

    if guess == target_pin:
        print(f"\nAccess Granted! PIN found after {attempts} attempts → {guess}")
        found = True
        break

# --- Final messages ---
if not found:
    print("\nAll attempted PINs tried. No match found.")
    print(f"Attempts performed: {attempts} (searched up to {str(search_limit-1).zfill(4)})")
else:
    if not verbose:
        print(f"(Summary) Found {target_pin} in {attempts} attempts.")
