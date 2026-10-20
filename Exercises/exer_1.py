
# Exercise 1 — Bitcoin addresses

# Create a list containing 5 Bitcoin addresses
bitcoin_addresses = [
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "1BoatSLRHtKNngkd XEeobR76b53LETtpyT",
    "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
    "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
    "1dice8EMZmqKvrGE4Qc9bUFf9PX3xaYDp"
]

# Add one address
bitcoin_addresses.append("1BitcoinEaterAddressDontSendf59kuE")

# Remove one address
bitcoin_addresses.remove("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

# Check whether an address exists
address_to_check = "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"

if address_to_check in bitcoin_addresses:
    print("Address exists in the list.")
else:
    print("Address does not exist in the list.")

# Print every address
print("\nBitcoin addresses:")
for address in bitcoin_addresses:
    print(address)
