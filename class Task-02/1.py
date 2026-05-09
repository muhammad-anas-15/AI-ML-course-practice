# Chai Stall Calculator

def print_receipt(order):

    prices = {
        "chai": 50,
        "paratha": 40,
        "anda": 30
    }

    subtotal = 0

    print("========== CHAI SPOT RECEIPT ==========")

    # calculate item totals
    for item in order:
        quantity = order[item]
        item_total = prices[item] * quantity
        subtotal += item_total

        print(f"{item.capitalize()} x{quantity} Rs. {item_total}")

    print("------------------------------------")

    # discount
    discount = 0
    if subtotal > 500:
        discount = subtotal * 0.10

    grand_total = subtotal - discount

    print(f"Subtotal: Rs. {subtotal}")
    print(f"Discount (10%): Rs. {int(discount)}")
    print(f"Grand Total: Rs. {int(grand_total)}")

    print("------------------------------------")

    # tip suggestions
    print("Tip Suggestions:")
    print(f"5% -> Rs. {grand_total * 0.05:.2f}")
    print(f"10% -> Rs. {grand_total * 0.10:.2f}")
    print(f"15% -> Rs. {grand_total * 0.15:.2f}")

    print("======================================")


# example order
order = {"chai": 3, "paratha": 2, "anda": 1}
print_receipt(order)