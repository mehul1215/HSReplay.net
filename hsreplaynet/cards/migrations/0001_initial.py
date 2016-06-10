# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-10 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import hearthstone.enums
import hsreplaynet.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('flavortext', models.TextField(blank=True)),
                ('how_to_earn', models.TextField(blank=True)),
                ('how_to_earn_golden', models.TextField(blank=True)),
                ('artist', models.CharField(blank=True, max_length=255)),
                ('card_class', hsreplaynet.utils.fields.IntEnumField(choices=[(0, 'INVALID'), (1, 'DEATHKNIGHT'), (2, 'DRUID'), (3, 'HUNTER'), (4, 'MAGE'), (5, 'PALADIN'), (6, 'PRIEST'), (7, 'ROGUE'), (8, 'SHAMAN'), (9, 'WARLOCK'), (10, 'WARRIOR'), (11, 'DREAM'), (12, 'COUNT')], default=0, validators=[hsreplaynet.utils.fields.IntEnumValidator(hearthstone.enums.CardClass)])),
                ('card_set', hsreplaynet.utils.fields.IntEnumField(choices=[(0, 'INVALID'), (1, 'TEST_TEMPORARY'), (2, 'CORE'), (3, 'EXPERT1'), (4, 'REWARD'), (5, 'MISSIONS'), (6, 'DEMO'), (7, 'NONE'), (8, 'CHEAT'), (9, 'BLANK'), (10, 'DEBUG_SP'), (11, 'PROMO'), (12, 'NAXX'), (13, 'GVG'), (14, 'BRM'), (15, 'TGT'), (16, 'CREDITS'), (17, 'HERO_SKINS'), (18, 'TB'), (19, 'SLUSH'), (20, 'LOE'), (21, 'OG'), (22, 'OG_RESERVE')], default=0, validators=[hsreplaynet.utils.fields.IntEnumValidator(hearthstone.enums.CardSet)])),
                ('faction', hsreplaynet.utils.fields.IntEnumField(choices=[(0, 'INVALID'), (1, 'HORDE'), (2, 'ALLIANCE'), (3, 'NEUTRAL')], default=0, validators=[hsreplaynet.utils.fields.IntEnumValidator(hearthstone.enums.Faction)])),
                ('race', hsreplaynet.utils.fields.IntEnumField(choices=[(0, 'INVALID'), (1, 'BLOODELF'), (2, 'DRAENEI'), (3, 'DWARF'), (4, 'GNOME'), (5, 'GOBLIN'), (6, 'HUMAN'), (7, 'NIGHTELF'), (8, 'ORC'), (9, 'TAUREN'), (10, 'TROLL'), (11, 'UNDEAD'), (12, 'WORGEN'), (13, 'GOBLIN2'), (14, 'MURLOC'), (15, 'DEMON'), (16, 'SCOURGE'), (17, 'MECHANICAL'), (18, 'ELEMENTAL'), (19, 'OGRE'), (20, 'BEAST'), (21, 'TOTEM'), (22, 'NERUBIAN'), (23, 'PIRATE'), (24, 'DRAGON')], default=0, validators=[hsreplaynet.utils.fields.IntEnumValidator(hearthstone.enums.Race)])),
                ('rarity', hsreplaynet.utils.fields.IntEnumField(choices=[(0, 'INVALID'), (1, 'COMMON'), (2, 'FREE'), (3, 'RARE'), (4, 'EPIC'), (5, 'LEGENDARY'), (6, 'UNKNOWN_6')], default=0, validators=[hsreplaynet.utils.fields.IntEnumValidator(hearthstone.enums.Rarity)])),
                ('type', hsreplaynet.utils.fields.IntEnumField(choices=[(0, 'INVALID'), (1, 'GAME'), (2, 'PLAYER'), (3, 'HERO'), (4, 'MINION'), (5, 'SPELL'), (6, 'ENCHANTMENT'), (7, 'WEAPON'), (8, 'ITEM'), (9, 'TOKEN'), (10, 'HERO_POWER')], default=0, validators=[hsreplaynet.utils.fields.IntEnumValidator(hearthstone.enums.CardType)])),
                ('collectible', models.BooleanField(default=False)),
                ('battlecry', models.BooleanField(default=False)),
                ('divine_shield', models.BooleanField(default=False)),
                ('deathrattle', models.BooleanField(default=False)),
                ('elite', models.BooleanField(default=False)),
                ('evil_glow', models.BooleanField(default=False)),
                ('inspire', models.BooleanField(default=False)),
                ('forgetful', models.BooleanField(default=False)),
                ('one_turn_effect', models.BooleanField(default=False)),
                ('poisonous', models.BooleanField(default=False)),
                ('ritual', models.BooleanField(default=False)),
                ('secret', models.BooleanField(default=False)),
                ('taunt', models.BooleanField(default=False)),
                ('topdeck', models.BooleanField(default=False)),
                ('atk', models.IntegerField(default=0)),
                ('health', models.IntegerField(default=0)),
                ('durability', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('windfury', models.IntegerField(default=0)),
                ('spare_part', models.BooleanField(default=False)),
                ('overload', models.IntegerField(default=0)),
                ('spell_damage', models.IntegerField(default=0)),
                ('craftable', models.BooleanField(default=False)),
                ('image', models.URLField(blank=True, null=True)),
                ('image_gold', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='CardCollectionAuditLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_date', models.DateField()),
                ('card_collection_start', models.DateTimeField()),
                ('card_collection_end', models.DateTimeField(blank=True, null=True)),
                ('num_new_cards_loaded', models.IntegerField(default=0)),
                ('card_collection_succeeded', models.BooleanField(default=False)),
                ('exception_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('digest', models.CharField(max_length=32, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Include',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=1)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cards.Card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Deck')),
            ],
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(through='cards.Include', to='cards.Card'),
        ),
        migrations.AlterUniqueTogether(
            name='include',
            unique_together=set([('deck', 'card')]),
        ),
    ]
