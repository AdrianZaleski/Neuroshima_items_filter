from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Ammo(Base):
    def __init__(self, id_code, ammo_symbol, name, price, availability, crafting_difficulty, description, effect, image,
                 weight):
        self.id_code = id_code
        self.ammo_symbol = ammo_symbol
        self.name = name
        self.price = price
        self.availability = availability
        self.crafting_difficulty = crafting_difficulty
        self.description = description
        self.effect = effect
        self.image = image
        self.weight = weight

    __tablename__ = "Ammo"

    id_code = Column(String, primary_key=True, unique=True)
    ammo_symbol = Column(String(length=25))
    name = Column(String(length=50))
    price = Column(Integer)
    availability = Column(Integer)
    crafting_difficulty = Column(String(length=25))
    description = Column(String(length=400))
    effect = Column(String(length=50))
    image = Column(String(length=50))
    weight = Column(Integer)

    # Relations:
    ranged_ammo = relationship("Ranged")


class Weapon(Base):
    def __init__(self, id_code, name, description,
                 modifier_10m, modifier_20m, modifier_30m, modifier_40m, modifier_60m, modifier_80m, modifier_100m,
                 modifier_150m, modifier_200m, modifier_250m, modifier_300m, modifier_400m, modifier_600m,
                 modifier_1000m, modifier_1500m
                 ):
        self.id_code = id_code
        self.name = name
        self.description = description
        self.modifier_10m = modifier_10m
        self.modifier_20m = modifier_20m
        self.modifier_30m = modifier_30m
        self.modifier_40m = modifier_40m
        self.modifier_60m = modifier_60m
        self.modifier_80m = modifier_80m
        self.modifier_100m = modifier_100m
        self.modifier_150m = modifier_150m
        self.modifier_200m = modifier_200m
        self.modifier_250m = modifier_250m
        self.modifier_300m = modifier_300m
        self.modifier_400m = modifier_400m
        self.modifier_600m = modifier_600m
        self.modifier_1000m = modifier_1000m
        self.modifier_1500m = modifier_1500m

    __tablename__ = "Weapon"

    id_code = Column(String(length=25), primary_key=True, unique=True),
    name = Column(String(length=25)),
    description = Column(String(length=400)),
    modifier_10m = Column(Integer)
    modifier_20m = Column(Integer)
    modifier_30m = Column(Integer)
    modifier_40m = Column(Integer)
    modifier_60m = Column(Integer)
    modifier_80m = Column(Integer)
    modifier_100m = Column(Integer)
    modifier_150m = Column(Integer)
    modifier_200m = Column(Integer)
    modifier_250m = Column(Integer)
    modifier_300m = Column(Integer)
    modifier_400m = Column(Integer)
    modifier_600m = Column(Integer)
    modifier_1000m = Column(Integer)
    modifier_1500m = Column(Integer)

    # Relations:
    weapon_ranged = relationship("Ranged")


class Ranged(Base):
    def __init__(self, id_ranged, name, weapon_class, ammo, magazine, misfire_roll, accuracy, shot_range, fire_rate,
                 attack_type, reload, penetration, damage, strength, holster, price, availability, actions,
                 description):
        self.id_ranged = id_ranged
        self.name = name
        self.weapon_class = weapon_class
        self.ammo = ammo
        self.magazine = magazine
        self.misfire_roll = misfire_roll
        self.accuracy = accuracy
        self.shot_range = shot_range
        self.fire_rate = fire_rate
        self.attack_type = attack_type
        self.reload = reload
        self.penetration = penetration
        self.damage = damage
        self.strength = strength
        self.holster = holster
        self.price = price
        self.availability = availability
        self.actions = actions
        self.description = description

    __tablename__ = "Ranged"

    id_ranged = Column(String, primary_key=True, autoincrement=True)
    name = Column(String)
    weapon_class = Column(String(length=20), ForeignKey("Weapon.id_code"))
    ammo = Column(String, ForeignKey("Ammo.ammo_symbol"))
    magazine = Column(Integer)
    misfire_roll = Column(Integer)
    accuracy = Column(Integer)
    shot_range = Column(Integer)
    fire_rate = Column(Integer)
    attack_type = Column(String(length=20))
    reload = Column(String(length=20))
    penetration = Column(Integer)
    damage = Column(String(length=20))
    strength = Column(Integer)
    holster = Column(Boolean)
    price = Column(Integer)
    availability = Column(Integer)
    actions = Column(String(length=20))
    description = Column(String(length=20))

    # Relations:
