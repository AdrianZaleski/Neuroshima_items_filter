# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Difficulty(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()
    range = models.IntegerField()
    modifier = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'difficulty'

    def __str__(self):
        return self.name


class Damage(models.Model):
    id = models.TextField(unique=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    symbol = models.TextField(primary_key=True)
    effect_on_target = models.TextField(blank=True, null=True)
    flat_modifier = models.IntegerField()
    pain_modifier = models.IntegerField()
    head_description = models.TextField(blank=True, null=True)
    torso_description = models.TextField(blank=True, null=True)
    r_arm_description = models.TextField(blank=True, null=True)
    l_arm_description = models.TextField(blank=True, null=True)
    leg_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'damage'

    def __str__(self):
        return self.name


class Weapon(models.Model):
    id_code = models.TextField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    modifier_10m = models.IntegerField(blank=True, null=True)
    modifier_20m = models.IntegerField(blank=True, null=True)
    modifier_30m = models.IntegerField(blank=True, null=True)
    modifier_40m = models.IntegerField(blank=True, null=True)
    modifier_60m = models.IntegerField(blank=True, null=True)
    modifier_80m = models.IntegerField(blank=True, null=True)
    modifier_100m = models.IntegerField(blank=True, null=True)
    modifier_150m = models.IntegerField(blank=True, null=True)
    modifier_200m = models.IntegerField(blank=True, null=True)
    modifier_250m = models.IntegerField(blank=True, null=True)
    modifier_300m = models.IntegerField(blank=True, null=True)
    modifier_400m = models.IntegerField(blank=True, null=True)
    modifier_600m = models.IntegerField(blank=True, null=True)
    modifier_1000m = models.IntegerField(blank=True, null=True)
    modifier_1500m = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'weapon'

    def __str__(self):
        return self.name


class Ammo(models.Model):
    id_code = models.TextField(primary_key=True)
    ammo_symbol = models.TextField()
    name = models.TextField()
    price = models.IntegerField()
    availability = models.IntegerField()
    crafting_difficulty = models.ForeignKey('Difficulty', on_delete=models.CASCADE, db_column='crafting_difficulty')
    description = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ammo'

    def __str__(self):
        return self.name


class Ranged(models.Model):
    id_code = models.TextField(primary_key=True)
    name = models.TextField()
    weapon_class = models.ForeignKey('Weapon', on_delete=models.CASCADE, db_column='weapon_class')
    ammo = models.ForeignKey(Ammo, models.DO_NOTHING, db_column='ammo')
    magazine = models.IntegerField()
    misfire_roll = models.IntegerField()
    celnosc_w_procentach = models.IntegerField(blank=True, null=True)
    zasieg = models.IntegerField(blank=True, null=True)
    fire_rate = models.IntegerField(blank=True, null=True)
    attack_type = models.TextField(blank=True, null=True)
    reload = models.IntegerField(blank=True, null=True)
    punkty_przebicia = models.IntegerField()
    damage = models.ForeignKey(Damage, on_delete=models.CASCADE, db_column='damage')
    strength = models.IntegerField(blank=True, null=True)
    holster = models.IntegerField()
    price = models.IntegerField()
    availability = models.IntegerField()
    actions = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ranged'

    def __str__(self):
        return self.name
