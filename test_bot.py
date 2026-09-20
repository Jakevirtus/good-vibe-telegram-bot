from bot import get_random_compliment, COMPLIMENTS


def test_compliments_list_is_not_empty():
    """Проверяем, что список комплиментов не пустой."""
    assert len(COMPLIMENTS) > 0


def test_all_compliments_are_strings():
    """Проверяем, что все комплименты — непустые строки."""
    for compliment in COMPLIMENTS:
        assert isinstance(compliment, str)
        assert len(compliment) > 0


def test_get_random_compliment_returns_string():
    """Проверяем, что функция возвращает строку."""
    result = get_random_compliment()
    assert isinstance(result, str)


def test_get_random_compliment_from_list():
    """Проверяем, что функция возвращает элемент из нашего списка."""
    result = get_random_compliment()
    assert result in COMPLIMENTS


def test_get_random_compliment_returns_different_values():
    """Проверяем, что при многократном вызове возвращаются разные значения."""
    results = {get_random_compliment() for _ in range(50)}
    assert len(results) > 1
