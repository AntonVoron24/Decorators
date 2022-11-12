from decorators import test_1, test_2, logger


@logger
def flat_generator(list_of_list):
    for i in list_of_list:
        if isinstance(i, list):
            yield from flat_generator(i)
        else:
            yield i


list_of_lists = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]


if __name__ == '__main__':
    test_1()
    test_2()
    flat_generator(list_of_lists)
