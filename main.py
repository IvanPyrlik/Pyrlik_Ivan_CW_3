from src.utils import load_operations, get_information_operations, get_executed_operations, get_sorted_operations


def main():
    operations = load_operations()
    information = get_information_operations(operations)
    executed_operation = get_executed_operations(information)
    sorted_operations = get_sorted_operations(executed_operation)
    for operation in sorted_operations[:5]:
        print(operation)
        print()


if __name__ == '__main__':
    main()
