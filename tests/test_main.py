from gravify import Gravatar
from pytest import raises


def test_plain_email():
    assert (
        Gravatar('bensoyka@icloud.com').url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052'
    )


def test_hash():
    assert (
        Gravatar('bensoyka@icloud.com').hash
        == '7246821a7bf0b1b37794b39cb08ee052'
    )


def test_hash_whitespace():
    assert (
        Gravatar('   \tbensoyka@icloud.com\n').hash
        == '7246821a7bf0b1b37794b39cb08ee052'
    )


def test_hash_to_lowercase():
    assert (
        Gravatar('bEnSoYkA@iClOuD.cOm').hash
        == '7246821a7bf0b1b37794b39cb08ee052'
    )


def test_default_identicon():
    assert (
        Gravatar('bensoyka@icloud.com', default_image='identicon').url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?d=identicon'
    )


def test_size_param():
    assert (
        Gravatar('bensoyka@icloud.com', size=200).url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?s=200'
    )
    assert (
        Gravatar('bensoyka@icloud.com', size=300).url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?s=300'
    )


def test_force_default_param():
    assert (
        Gravatar('bensoyka@icloud.com', force_default=True).url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?f=y'
    )


def test_file_handler():
    assert isinstance(Gravatar('bensoyka@icloud.com').file.read(4), bytes)


def test_ignore_unknown_rating():
    with raises(ValueError):
        Gravatar('bensoyka@icloud.com', max_rating='xyz')


def test_max_rating():
    assert (
        Gravatar('bensoyka@icloud.com', max_rating='g').url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?r=g'
    )
    assert (
        Gravatar(
            'bensoyka@icloud.com', default_image='identicon', max_rating='g'
        ).url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?d=identicon&r=g'
    )


def test_data_type_email():
    gravatar_instance = Gravatar(email='email@email.com')
    assert isinstance(gravatar_instance.email, str)


def test_data_type_verify_email():
    gravatar_instance = Gravatar(email='email@email.com', verify_email=True)
    assert isinstance(gravatar_instance.verify_email, bool)


def test_data_type_and_value_default_image():
    gravatar_instance = Gravatar(email='email@email.com', default_image='404')
    assert isinstance(gravatar_instance.default_image, str)
    assert gravatar_instance.default_image in [
        '404',
        'mp',
        'identicon',
        'monsterid',
        'wavatar',
        'retro',
        'robohash',
        'blank',
    ]


def test_data_type_and_value_size():
    gravatar_instance = Gravatar(email='email@email.com', size=1)
    assert isinstance(gravatar_instance.size, int)
    assert 1 <= gravatar_instance.size <= 2048


def test_data_type_force_default():
    gravatar_instance = Gravatar(email='email@email.com', force_default=False)
    assert isinstance(gravatar_instance.force_default, bool)


def test_data_type_and_value_max_rating():
    gravatar_instance = Gravatar(email='email@email.com', max_rating='g')
    assert isinstance(gravatar_instance.max_rating, str)
    assert gravatar_instance.max_rating in ['g', 'pg', 'r', 'x']
