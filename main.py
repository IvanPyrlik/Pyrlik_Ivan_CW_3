from src.utils import load_operations, get_information_operations, get_executed_operations


def main():
    operations = load_operations()
    information = get_information_operations(operations)
    executed_operation = get_executed_operations(information)



if __name__ == '__main__':
    main()
