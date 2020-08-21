def main():
    print("First module's name: {}".format(__name__))
    pass

if __name__ == '__main__':
    print("First module has been run directly")
    main()
else:
    print("First module has been run from import")