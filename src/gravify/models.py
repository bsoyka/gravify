"""Gravatar API data models."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel
from pydantic.networks import EmailStr, HttpUrl


class VerifiedAccount(BaseModel):
    """A verified account associated with a Gravatar profile."""

    service_type: str
    service_label: str
    service_icon: HttpUrl
    url: HttpUrl
    is_hidden: bool


class Language(BaseModel):
    """A language spoken by a Gravatar user."""

    code: str
    name: str
    is_primary: bool
    order: int


class Link(BaseModel):
    """A link associated with a Gravatar profile."""

    label: str
    url: HttpUrl


class Interest(BaseModel):
    """An interest of a Gravatar user."""

    id: int
    name: str
    slug: str


class CryptoWalletAddress(BaseModel):
    """A cryptocurrency wallet address associated with a Gravatar user."""

    label: str
    address: str


class PaymentInformation(BaseModel):
    """Payment information for a Gravatar user."""

    links: list[Link]
    crypto_wallets: list[CryptoWalletAddress]


class ContactInfo(BaseModel):
    """Contact information for a Gravatar user."""

    home_phone: str | None = None
    work_phone: str | None = None
    cell_phone: str | None = None
    email: EmailStr | None = None
    contact_form: HttpUrl | None = None
    calendar: HttpUrl | None = None


class GalleryImage(BaseModel):
    """An image in a Gravatar user's gallery."""

    url: HttpUrl
    alt_text: str | None = None


class SectionVisibility(BaseModel):
    """Visibility settings for sections of a Gravatar profile."""

    hidden_contact_info: bool
    hidden_feeds: bool
    hidden_links: bool
    hidden_interests: bool
    hidden_wallet: bool
    hidden_photos: bool
    hidden_verified_accounts: bool


class Profile(BaseModel):
    """A Gravatar profile."""

    hash: str
    display_name: str
    profile_url: HttpUrl
    avatar_url: HttpUrl
    avatar_alt_text: str
    location: str
    description: str
    job_title: str
    company: str
    verified_accounts: list[VerifiedAccount]
    pronunciation: str
    pronouns: str

    # The remaining fields are optional in the schema, with most marked as
    # "only provided in authenticated API requests."
    timezone: str | None = None
    languages: list[Language] | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_organization: bool | None = None
    header_image: str | None = None
    background_color: str | None = None
    links: list[Link] | None = None
    interests: list[Interest] | None = None
    payments: PaymentInformation | None = None
    contact_info: ContactInfo | None = None
    gallery: list[GalleryImage] | None = None
    number_verified_accounts: int | None = None
    last_profile_edit: datetime | None = None
    registration_date: datetime | None = None
    section_visibility: SectionVisibility | None = None
