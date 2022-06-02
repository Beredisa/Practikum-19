from api import PetFriends
from settings import val_email, val_password, inval_password, inval_email

pf = PetFriends()

def test_get_api_key_for_valid_user(email=val_email, password=val_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_api_key_for_user_invalid_password(email=val_email, password=inval_password):
    """ Проверяем что запрос api ключа возвращает статус 404 """

    status, result = pf.get_api_key(email, password)

    assert status == 404

def test_get_api_key_for_user_invalid_email(email=inval_email, password=val_password):
    """ Проверяем что запрос api ключа возвращает статус 404 и """

    status, result = pf.get_api_key(email, password)

    assert status == 404

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(val_email, val_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_invalid_name(name=' ', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat.jpg'):
    """Проверяем что нельзя добавить питомца с некорректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(val_email, val_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result


def test_add_new_pet_with_invalid_animal_type(name='Босс', animal_type=' ',
                                     age='4', pet_photo='images/cat.jpg'):
    """Проверяем что нельзя добавить питомца с некорректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(val_email, val_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result

def test_add_new_pet_with_invalid_age(name='Босс', animal_type='двортерьер',
                                     age='фсе', pet_photo='images/cat.jpg'):
    """Проверяем что нельзя добавить питомца с некорректными данными"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(val_email, val_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result


def test_not_successful_update_self_pet_info_invalid_name(name='345', animal_type='Котэ', age=5):
    """Проверяем невозможность обновления информации о питомце с некорректными данными """

    _, auth_key = pf.get_api_key(val_email, val_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 400 и питомец не добавлен
        assert status == 400
        assert result
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_not_successful_update_self_pet_invalid_info_animal(name='Мурзик', animal_type='', age='5'):
    """Проверяем невозможность обновления информации о питомце с некорректными данными """

    _, auth_key = pf.get_api_key(val_email, val_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 400 и питомец не добавлен
        assert status == 400
        assert result
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_not_successful_update_self_pet_info_invalid_age(name='Мурзик', animal_type='Котэ', age='abc'):
    """Проверяем невозможность обновления информации о питомце с некорректными данными """

    _, auth_key = pf.get_api_key(val_email, val_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 400 и питомец не добавлен
        assert status == 400
        assert result
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

