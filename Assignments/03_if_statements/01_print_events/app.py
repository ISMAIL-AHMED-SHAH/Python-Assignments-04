# Print Even Numbers from 1 to 20


def main():

    for i in range(1,21):
        multiply = i * 2
        if multiply % 2 == 0:
            print(multiply)
        else:
            continue


if __name__ == '__main__':
    main()