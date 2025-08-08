"""Gravatar API data models."""

from __future__ import annotations

from pydantic import BaseModel


class Profile(BaseModel):
    """Data model for a Gravatar profile."""

    hash: str
    display_name: str
    profile_url: str
    avatar_url: str
    avatar_alt_text: str
    location: str
    description: str
    job_title: str
    company: str
    verified_accounts: list[dict]
    pronunciation: str
    pronouns: str
    timezone: str | None = None
    languages: list[dict] | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_organization: bool | None = None
    header_image: str | None = None
    background_color: str | None = None
    links: list[dict[str, str]] | None = None
    interests: list[dict] | None = None
    payments: dict[str, list[dict[str, str]]] | None = None
    contact_info: dict[str, str] | None = None
    gallery: list[dict[str, str]] | None = None
    number_verified_accounts: int | None = None
    last_profile_edit: str | None = None
    registration_date: str | None = None
    section_visibility: dict[str, bool] | None = None
