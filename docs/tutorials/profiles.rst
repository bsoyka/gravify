Profiles tutorial
=================

Gravatar allows users to create profiles that can be associated with their email addresses.
These profiles can include various information such as name, bio, location, and links to social media accounts.

Gravify lets you retrieve these profiles using the :class:`~gravify.ProfileAPI` class.
Here's a simple example of how to use it:

>>> from gravify import ProfileAPI
>>> profile_api = ProfileAPI()
>>> profile = profile_api.get_profile('hello@bsoyka.me')
>>> profile
Profile(...)
>>> profile.display_name
'Ben Soyka'

The resulting :class:`~gravify.profiles.models.Profile` object contains various fields that represent the user's profile information.
See the :class:`~gravify.profiles.models.Profile` reference for a complete list of fields.

.. NOTE::

    While most basic data is always visible, some profile fields are only returned if you use a Gravatar API key.
    You can get a free API key by registering your application at `the Gravatar developer portal <https://gravatar.com/developers>`_.
    Then, pass the API key to the :class:`~gravify.ProfileAPI` constructor with the **api_key** parameter.
