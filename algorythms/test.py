import main


def test_profit() -> None:
    '''
    Testing binary_search fucntion
    :return:
    '''
    input_ = [_ for _ in range(100)]

    for el in range(100):
        assert main.binary_search(input_,el) ==el
    input_ = [0, 3, 4, 5, 7, 13]
    assert main.binary_search(input_, 7) == 4
