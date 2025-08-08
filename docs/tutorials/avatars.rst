Avatars tutorial
================

The most commonly used feature from Gravatar is the avatar.
Avatars are small images that represent a user in various contexts, such as forums, comments, or social media profiles.
Gravatar allows users to associate an avatar with their email address, which can then be displayed across different platforms.

Gravify provides a simple way to retrieve avatars using the :class:`~gravify.AvatarGenerator` class.
The simplest example of its usage is as follows:

>>> from gravify import AvatarGenerator
>>> avatar_generator = AvatarGenerator()
>>> avatar_generator.generate_url('hello@example.com')
'https://gravatar.com/avatar/1753bdb368271a785887ddbfb926164f2f7c6a88f609c07ff0401c5572955206'

In your project, you should generally create one instance of the :class:`~gravify.AvatarGenerator` class and use it to generate avatar URLs for each user.

You can customize the avatar URLs by passing additional parameters to the generator:

>>> from gravify.avatars import DefaultImage, Rating
>>> avatar_generator = AvatarGenerator(
...     size=500,
...     default_image=DefaultImage.IDENTICON,
...     rating=Rating.PG,
... )
>>> avatar_generator.generate_url('hello@example.com')
'https://gravatar.com/avatar/1753bdb368271a785887ddbfb926164f2f7c6a88f609c07ff0401c5572955206?s=500&d=identicon&r=pg'

Notice the added query parameters in the resulting URL.
Gravify will try to keep the URL as short as possible, but it will add the necessary parameters to customize the avatar according to your preferences.
For example, if you set the `size` parameter to its default value of `80`, the URL will not include the `s` parameter, as 80 pixels is already the default size for Gravatar avatars.

You can pass the following parameters to the :class:`~gravify.AvatarGenerator` constructor:

* **size**: The size of the avatar in pixels. The default is 80.
* **default_image**: The default image to use if the user does not have a Gravatar avatar. You can pass a URL string to an image, or a member of the :class:`gravify.avatars.DefaultImage` enum. The default is the Gravatar logo.
* **force_default**: Whether to force the default image to be used even if the user has a Gravatar avatar. The default is `False`.
* **rating**: The rating of the avatar. (Users can define multiple avatars for their profile of various content ratings.) You can pass a member of the :class:`gravify.avatars.Rating` enum. The default is :attr:`gravify.avatars.Rating.G`.
* **initials** or **name**: The initials or name to use for the avatar, if you set the default image to :attr:`~gravify.avatars.DefaultImage.INITIALS`.
