from draw_helper import DrawHelper


def main():
    draw_helper = DrawHelper(input_file='./teams.json')
    try:
        draw_helper.start()
        print("Final Draw ⚽️")
        for pair in draw_helper.pairs:
            print(pair)
    except Exception as error:
        print(error)
    return


if __name__ == '__main__':
    main()
