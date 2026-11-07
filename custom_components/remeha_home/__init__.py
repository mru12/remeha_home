"""The Remeha Home integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow, device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import RemehaHomeOAuth2Implementation, RemehaHomeAPI
from .config_flow import RemehaHomeLoginFlowHandler
from .const import DOMAIN
from .coordinator import RemehaHomeUpdateCoordinator

PLATFORMS: list[Platform] = [
    Platform.BINARY_SENSOR,
    Platform.CLIMATE,
    Platform.NUMBER,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.WATER_HEATER,
]


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Remeha Home."""
    hass.data.setdefault(DOMAIN, {})

    RemehaHomeLoginFlowHandler.async_register_implementation(
        hass,
        RemehaHomeOAuth2Implementation(async_get_clientsession(hass)),
    )

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Remeha Home from a config entry."""
    implementation = (
        await config_entry_oauth2_flow.async_get_config_entry_implementation(
            hass, entry
        )
    )

    oauth_session = config_entry_oauth2_flow.OAuth2Session(hass, entry, implementation)
    api = RemehaHomeAPI(oauth_session)
    coordinator = RemehaHomeUpdateCoordinator(hass, api)

    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinator": coordinator,
    }

    # Register all devices up front: parents first, then children linked by
    # via_device_id. Entities only reference their device by identifiers, because
    # passing via_device through entity device_info is deprecated (an error when
    # entities are re-added at runtime, e.g. after an entity_id rename, and
    # removed in HA 2027.8).
    async_register_devices(hass, entry, coordinator)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


def async_register_devices(
    hass: HomeAssistant, entry: ConfigEntry, coordinator: RemehaHomeUpdateCoordinator
) -> None:
    """Create or update the device registry entries for all coordinator devices."""
    registry = dr.async_get(hass)
    device_infos = coordinator.device_info.values()

    for device_info in device_infos:
        if "via_device" not in device_info:
            registry.async_get_or_create(config_entry_id=entry.entry_id, **device_info)

    for device_info in device_infos:
        if "via_device" not in device_info:
            continue
        info = dict(device_info)
        parent = registry.async_get_device(identifiers={info.pop("via_device")})
        kwargs = {"via_device_id": parent.id} if parent else {}
        registry.async_get_or_create(config_entry_id=entry.entry_id, **info, **kwargs)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
