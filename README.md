# 🔁 bruteforce-simulator

A Python simulator that demonstrates brute-force attacks on a 4-digit PIN with a configurable search range and progress reporting.  
Built to teach iteration in Python and to show why embedded devices need brute-force protections (rate limits, lockouts).

## Features
- Accepts a target PIN (1–4 digits)
- Configurable max-range to try (1–10000)
- Verbose mode or periodic progress updates
- Clear summary on completion

## How to run (VS Code)
1. Open `bruteforce_simulator.py` in VS Code.
2. Click **Run Python File in Terminal** (top-right) or right-click → **Run Python File in Terminal**.
3. Follow prompts:
   - Enter the target PIN (e.g., `0428`).
   - Enter max range (e.g., `100` or `10000`).
   - Choose verbose or summary mode and a progress interval.

## Example
- Short test: max range = `100`, target `0428` → returns **No match found**.
- Full test: max range = `10000`, target `0428` → finds the PIN and prints the number of attempts.

## Files
- `bruteforce_simulator.py` — main script
- `README.md` — project documentation

## Author
**OYEDELE HAMEED ABIODUN** 
 Cyber-Physical Hardware Security Enthusiast# Hardware-Key-Brute-Force-Simulator

**Don't Forget to Follow me on here for more exciting Projects!** 