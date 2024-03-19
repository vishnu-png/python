def main():
    num_loaves = int(input("Enter the number of loaves of day-old bread: "))
    regular_price_per_loaf = 185

    regular_price = num_loaves * regular_price_per_loaf

    discount = regular_price * 0.60

    total_price = regular_price - discount
    print(f"Regular price:   {regular_price:.2f}")
    print(f"Discount:        {discount:.2f}")
    print(f"Total price:     {total_price:.2f}")


if __name__ == "__main__":
    main()
