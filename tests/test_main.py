from gravify import Gravatar, DEFAULT_AVATARS


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


def test_default_image_constant():
    assert (
        Gravatar(
            'bensoyka@icloud.com', default_image=DEFAULT_AVATARS['identicon']
        ).url
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
    assert (
        Gravatar('bensoyka@icloud.com', max_rating='xyz').url
        == 'https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052'
    )


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
