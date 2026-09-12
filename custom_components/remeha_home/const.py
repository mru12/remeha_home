"""Constants for the Remeha Home integration."""

from homeassistant.components.sensor import (
    SensorEntityDescription,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.components.binary_sensor import (
    BinarySensorEntityDescription,
    BinarySensorDeviceClass,
)
from homeassistant.const import (
    EntityCategory,
    UnitOfEnergy,
    UnitOfTemperature,
    UnitOfPressure,
    UnitOfVolume,
)

DOMAIN = "remeha_home"

APPLIANCE_SENSOR_TYPES = [
    SensorEntityDescription(
        key="waterPressure",
        name="Water Pressure",
        native_unit_of_measurement=UnitOfPressure.BAR,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="activeThermalMode",
        name="Thermal Mode",
    ),
    SensorEntityDescription(
        key="outdoorTemperatureInformation.applianceOutdoorTemperature",
        name="Outdoor Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="outdoorTemperatureInformation.cloudOutdoorTemperature",
        name="Cloud Outdoor Temperature",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="consumptionData.heatingEnergyConsumed",
        name="Heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.hotWaterEnergyConsumed",
        name="Hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.coolingEnergyConsumed",
        name="Cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.heatingEnergyDelivered",
        name="Heating Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.hotWaterEnergyDelivered",
        name="Hot Water Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.coolingEnergyDelivered",
        name="Cooling Energy Delivered",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionCHElectric",
        name="Electric Heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionDHWElectric",
        name="Electric Hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionCoolingElectric",
        name="Electric Cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionTotalElectric",
        name="Total Electric Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionCHElectric",
        name="Electric Heating Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionDHWElectric",
        name="Electric Hot Water Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionCoolingElectric",
        name="Electric Cooling Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionTotalElectric",
        name="Total Electric Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionCHNaturalGas",
        name="Natural Gas Heating Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionDHWNaturalGas",
        name="Natural Gas Hot Water Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionCoolingNaturalGas",
        name="Natural Gas Cooling Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyConsumptionTotalNaturalGas",
        name="Total Natural Gas Energy Consumed",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionCHNaturalGas",
        name="Natural Gas Heating Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionDHWNaturalGas",
        name="Natural Gas Hot Water Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionCoolingNaturalGas",
        name="Natural Gas Cooling Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.energyProductionTotalNaturalGas",
        name="Total Natural Gas Cooling Energy Produced",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="consumptionData.seasonalEfficiencyElectric",
        name="Electric Seasonal Efficiency",
        entity_registry_enabled_default=False,
        native_unit_of_measurement=None,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="applianceConnectionStatus",
        name="Connection Status",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="errorStatus",
        name="Error Status",
    ),
    SensorEntityDescription(
        key="operatingMode",
        name="Operating Mode",
    ),
    SensorEntityDescription(
        key="seasonalMode",
        name="Seasonal Mode",
    ),
    SensorEntityDescription(
        key="outdoorTemperatureInformation.internetOutdoorTemperature",
        name="Internet Outdoor Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="outdoorTemperatureInformation.weatherCode",
        name="Weather",
    ),
    SensorEntityDescription(
        key="outdoorTemperatureInformation.outdoorTemperatureSource",
        name="Outdoor Temperature Source",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="outdoorTemperatureInformation.cloudOutdoorTemperatureStatus",
        name="Cloud Outdoor Temperature Status",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="holidaySchedule.startTime",
        name="Holiday Start",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key="holidaySchedule.endTime",
        name="Holiday End",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
]

# Monthly and yearly energy totals. The API reports these as per-period sums
# that restart at zero when a new period begins.
APPLIANCE_SENSOR_TYPES += [
    SensorEntityDescription(
        key=f"consumptionData{period}.{field}",
        name=f"{label} {period}",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    )
    for period in ("Monthly", "Yearly")
    for field, label in (
        ("heatingEnergyConsumed", "Heating Energy Consumed"),
        ("hotWaterEnergyConsumed", "Hot Water Energy Consumed"),
        ("coolingEnergyConsumed", "Cooling Energy Consumed"),
        ("heatingEnergyDelivered", "Heating Energy Delivered"),
        ("hotWaterEnergyDelivered", "Hot Water Energy Delivered"),
        ("coolingEnergyDelivered", "Cooling Energy Delivered"),
    )
]

APPLIANCE_SENSOR_TYPES += [
    SensorEntityDescription(
        key=f"consumptionData{period}.cop",
        name=f"COP {period}",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=2,
    )
    for period in ("Monthly", "Yearly")
]

ELECTRIC_PRODUCER_SENSOR_TYPES = [
    SensorEntityDescription(
        key="energyConsumptionCH",
        name="Heating Energy Consumed",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="energyConsumptionDHW",
        name="Hot Water Energy Consumed",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="energyConsumptionCooling",
        name="Cooling Energy Consumed",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="energyProductionCH",
        name="Heating Energy Delivered",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="energyProductionDHW",
        name="Hot Water Energy Delivered",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="energyProductionCooling",
        name="Cooling Energy Delivered",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
]

GAS_PRODUCER_SENSOR_TYPES = [
    SensorEntityDescription(
        key="energyConsumptionCH",
        name="Heating Energy Consumed",
        native_unit_of_measurement=UnitOfVolume.CUBIC_METERS,
        device_class=SensorDeviceClass.GAS,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    SensorEntityDescription(
        key="energyConsumptionDHW",
        name="Hot Water Energy Consumed",
        native_unit_of_measurement=UnitOfVolume.CUBIC_METERS,
        device_class=SensorDeviceClass.GAS,
        state_class=SensorStateClass.TOTAL_INCREASING,
    )
]

CLIMATE_ZONE_SENSOR_TYPES = [
    SensorEntityDescription(
        key="roomTemperature",
        name="Room Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="activeComfortDemand",
        name="Status",
    ),
    SensorEntityDescription(
        key="nextSetpoint",
        name="Next Setpoint",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key="nextSwitchTime",
        name="Next Setpoint Time",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key="currentScheduleSetPoint",
        name="Current Schedule Setpoint",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key="controlStrategy",
        name="Control Strategy",
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="temporaryOverride.endTime",
        name="Temporary Override End",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
]

HOT_WATER_ZONE_SENSOR_TYPES = [
    SensorEntityDescription(
        key="dhwTemperature",
        name="Water Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="dhwStatus",
        name="Status",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="dhwCurrentActivity",
        name="Mode",
    ),
    SensorEntityDescription(
        key="nextSwitchTime",
        name="Next Setpoint Time",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key="dhwZoneMode",
        name="Zone Mode",
    ),
    SensorEntityDescription(
        key="targetSetpoint",
        name="Target Setpoint",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key="setPointMin",
        name="Setpoint Min",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="setPointMax",
        name="Setpoint Max",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    SensorEntityDescription(
        key="nextSwitchActivity",
        name="Next Switch Activity",
    ),
    SensorEntityDescription(
        key="boostModeEndTime",
        name="Boost Mode End",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
]

APPLIANCE_BINARY_SENSOR_TYPES = [
    (
        BinarySensorEntityDescription(
            key="applianceOnline",
            name="Online",
            device_class=BinarySensorDeviceClass.CONNECTIVITY,
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        lambda value: bool(value),
    ),
    (
        BinarySensorEntityDescription(
            key="waterPressureOK",
            name="Water Pressure Problem",
            device_class=BinarySensorDeviceClass.PROBLEM,
        ),
        # The API reports pressure being OK, which is the inverse of a problem.
        lambda value: not value,
    ),
    (
        BinarySensorEntityDescription(
            key="holidaySchedule.active",
            name="Holiday Mode",
        ),
        lambda value: bool(value),
    ),
    (
        BinarySensorEntityDescription(
            key="outdoorTemperatureInformation.isDayTime",
            name="Daytime",
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        lambda value: bool(value),
    ),
]

CLIMATE_ZONE_BINARY_SENSOR_TYPES = [
    (
        BinarySensorEntityDescription(
            key="activeComfortDemand",
            name="Status",
            entity_registry_enabled_default=False,
            device_class=BinarySensorDeviceClass.HEAT,
        ),
        lambda value: value
        in ["ProducingHeat", "RequestingHeat", "ProducingCold", "RequestingCold"],
    ),
    (
        BinarySensorEntityDescription(
            key="preHeat.active",
            name="Pre-heat Active",
            device_class=BinarySensorDeviceClass.HEAT,
        ),
        lambda value: bool(value),
    ),
    (
        BinarySensorEntityDescription(
            key="preHeat.enabled",
            name="Pre-heat Enabled",
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        lambda value: bool(value),
    ),
]

HOT_WATER_ZONE_BINARY_SENSOR_TYPES = [
    (
        BinarySensorEntityDescription(
            key="dhwStatus",
            name="Status",
            entity_registry_enabled_default=False,
            device_class=BinarySensorDeviceClass.HEAT,
        ),
        lambda value: value == "ProducingHeat",
    ),
    (
        BinarySensorEntityDescription(
            key="antiLegionellaEnabled",
            name="Anti-legionella Enabled",
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        lambda value: bool(value),
    ),
    (
        BinarySensorEntityDescription(
            key="optimizationEnabled",
            name="Optimization Enabled",
            entity_category=EntityCategory.DIAGNOSTIC,
        ),
        lambda value: bool(value),
    ),
]
