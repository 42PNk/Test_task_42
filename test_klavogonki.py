def test_klavogonki(page):
    # Переходим на сайт
    page.goto('https://klavogonki.ru/', timeout=60000)
    # Нажимаем Быстрый "старт"
    page.locator("div.quickstart a.title").click()
    # Закрываем обучалку
    page.locator("div#howtoplay p input[value='Закрыть']").click()
    # Если не нашлось других игроков, для начала игры необходимо нажать на кнопку "Начать игру"
    if page.locator("a#host_start").is_visible():
        page.locator("a#host_start").click()
        page.locator("input#inputtext").click(timeout=60000)
    # Если нашлись другие игроки, игра начнется и без кнопки "Начать игру"
    else:
        page.locator("input#inputtext").click(timeout=60000)
    # Проходим игру, заполняя текст в цикле
    while page.locator("#afterfocus").is_visible():
        wrong_text = str(*page.locator("#typefocus").all_inner_texts())
        right_text = wrong_text.replace('o', 'о').replace('c', 'с')
        page.locator("input#inputtext").fill(right_text, timeout=60000)
        if page.locator("#afterfocus").inner_text() == '.':
            page.locator("input#inputtext").press(".")
        elif page.locator("#afterfocus").inner_text() == '!':
            page.locator("input#inputtext").press("!")
        elif page.locator("#afterfocus").inner_text() == '?':
            page.locator("input#inputtext").press("?")
        page.locator("input#inputtext").press("Space")
    # Фиксируем результаты
    speed = page.locator(".you .stats div:nth-child(2) span span")
    errors = page.locator(".you .stats div:nth-child(3) > span:nth-child(1) span")
    # Выполняем проверку из задания
    assert int(speed.inner_text()) > 400, 'Скорость ниже 400 зн/мин!'
    assert int(errors.inner_text()) == 0, 'Есть ошибка(и) при вводе!'
    # Выводим результаты
    print()
    print(f'Скорость набора = {speed.inner_text()} зн/мин')
    print('Кол-во ошибок =', errors.inner_text())