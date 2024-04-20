def main():
       # Create and print a list named fruit.
    try:
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
        fruit_list.reverse()
        print(f'reversed: {fruit_list}')
        fruit_list.append("orange")
        print(f'append orange: {fruit_list}')
        fruit_list.insert(1,"cherry")
        print(f'insert cherry: {fruit_list}')
        fruit_list.remove("banana")
        print(f'remove banana: {fruit_list}')
        fruit_list.pop()
        print(f'pop orange: {fruit_list}')
        sorted_list = sorted(fruit_list)
        print(f'sorted: {sorted_list}')
        fruit_list.clear()
        print(f'cleared: {fruit_list}')

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

if __name__ == "__main__":
    main()