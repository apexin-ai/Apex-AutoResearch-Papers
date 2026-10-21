"""SCS vs Simple Baselines comparison analysis.

Computes Spearman correlation between pairwise confusion counts and four metrics:
1. SCS (Schema Cosine Similarity) - pre-computed on remote
2. Normalized Levenshtein Similarity - pre-computed on remote
3. WordNet Wu-Palmer Similarity
4. Same-parent Indicator
"""
import json
import itertools
from pathlib import Path

import numpy as np
from scipy import stats

# --------------- Data ---------------
# FewRel: 80 types, 3160 upper-triangle pairs
FEWREL_TYPES = ["after a work by","applies to jurisdiction","architect","characters","child","competition class","composer","constellation","contains administrative territorial entity","country","country of citizenship","country of origin","crosses","developer","director","distributor","father","field of work","followed by","follows","genre","has part","head of government","headquarters location","heritage designation","instance of","instrument","language of work or name","league","licensed to broadcast to","located in or next to body of water","located in the administrative territorial entity","located on terrain feature","location","location of formation","main subject","manufacturer","member of","member of political party","military branch","military rank","mother","mountain range","mouth of the watercourse","movement","nominated for","notable work","occupant","occupation","operating system","operator","original language of film or TV show","original network","owned by","part of","participant","participant of","participating team","performer","place served by transport hub","platform","position held","position played on team","publisher","record label","religion","residence","said to be the same as","screenwriter","sibling","sport","sports season of league or competition","spouse","subsidiary","successful candidate","taxon rank","tributary","voice type","winner","work location"]

FEWNERD_TYPES = ["art-broadcastprogram","art-film","art-music","art-other","art-writtenart","building-airport","building-hospital","building-hotel","building-library","building-other","building-restaurant","building-sportsfacility","building-theater","event-attack/battle/war/militaryconflict","event-disaster","event-other","event-protest","event-sportsevent","location-GPE","location-bodiesofwater","location-island","location-mountain","location-other","location-park","location-road/railway/highway/transit","organization-company","organization-education","organization-government/governmentagency","organization-media/newspaper","organization-other","organization-politicalparty","organization-religion","organization-showorganization","organization-sportsleague","organization-sportsteam","other-astronomything","other-award","other-biologything","other-chemicalthing","other-disease","other-educationaldegree","other-god","other-language","other-law","other-livingthing","other-medical","person-actor","person-artist/author","person-athlete","person-director","person-other","person-politician","person-scholar","person-soldier","product-airplane","product-car","product-food","product-game","product-other","product-ship","product-software","product-train","product-weapon"]

# Confusion counts (upper triangle, sorted type order)
FEWREL_CONF = [0,0,0,0,0,25,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,50,150,0,25,0,0,0,0,0,0,0,0,0,0,125,25,0,25,0,0,0,0,0,50,0,0,0,25,0,75,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,50,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,700,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,500,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,50,0,0,25,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,150,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,50,50,0,0,0,0,0,0,25,300,0,50,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,400,0,0,0,0,0,0,0,0,0,0,150,0,0,0,0,25,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,100,0,0,0,0,0,75,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,125,0,0,0,25,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,25,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,25,0,0,25,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,25,0,0,25,25,0,0,50,0,0,0,0,0,0,25,0,0,250,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,100,0,0,0,0,0,0,0,0,0,50,125,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,25,0,25,0,0,0,0,0,0,0,75,0,50,0,0,0,0,0,0,175,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,25,0,0,125,0,0,0,0,0,0,0,0,0,400,0,25,25,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,225,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,275,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,175,0,25,0,25,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,50,25,0,0,0,0,0,0,0,50,0,0,25,0,0,0,25,25,0,0,0,0,0,275,0,0,0,25,50,0,0,0,0,0,0,0,50,0,1,0,0,0,0,0,0,0,0,250,0,200,0,125,225,0,25,0,25,0,0,0,0,0,0,0,0,125,0,0,0,0,0,25,0,0,0,0,0,50,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,25,25,0,0,75,0,75,0,0,0,0,0,0,225,0,0,0,25,0,25,0,0,0,125,25,25,0,0,0,50,25,0,0,0,50,0,25,0,0,25,50,0,25,0,875,0,75,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,175,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,450,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,50,0,0,0,0,0,0,0,0,0,0,0,0,75,150,0,0,0,0,0,0,0,0,0,250,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,175,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,275,250,100,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,50,175,0,0,0,0,75,0,0,0,0,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,75,50,25,0,0,0,0,0,0,0,100,25,0,0,0,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,25,0,0,0,0,0,0,0,0,0,175,0,0,0,0,0,25,100,25,0,0,0,350,0,0,0,0,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,300,25,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,75,0,25,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,50,350,0,0,0,0,100,0,0,100,0,0,100,0,0,25,100,75,0,100,0,0,0,50,0,0,0,125,25,0,0,0,25,100,0,50,0,0,0,0,50,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,575,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,549,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,225,0,0,0,0,0,0,400,0,0,0,0,0,0,25,0,0,0,0,0,350,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,175,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,150,0,25,0,0,0,0,0,0,350,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0,0,0,0,25,0,0,50,25,0,150,0,25,0,0,0,0,300,0,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,25,0,675,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,25,0,0,0,225,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,250,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0,0,0,125,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0]

FEWNERD_CONF = [2,8,12,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,3,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,2,0,0,0,0,0,2,0,0,0,0,0,2,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,24,1,1,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,5,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,10,1,4,0,0,0,0,0,7,1,0,1,0,0,16,1,3,14,1,9,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,10,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,1,5,0,0,0,3,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,2,0,0,0,4,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,0,1,0,0,1,7,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,24,0,0,0,2,0,0,7,1,0,0,5,7,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,8,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,8,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,2,0,1,0,0,0,0,0,0,4,0,0,0,1,2,0,1,0,3,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,1,2,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,9,0,7,0,0,0,3,0,0,2,0,0,0,0,0,0,0,0,0,0,1,0,0,4,1,0,0,3,0,0,0,3,0,0,1,0,3,0,10,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,14,6,0,0,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,2,0,0,0,0,5,3,4,0,5,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,3,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,4,0,0,0,4,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,9,2,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,0,1,0,0,0,0,0,0,0,0,0,0,1,50,5,2,1,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,93,14,6,0,1,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Pre-computed results from remote
FEWREL_SCS = {"rho": 0.218238, "p": 2.219981737602145e-35, "n_pairs": 3160}
FEWREL_LEV = {"rho": 0.016186, "p": 0.3630431290498525, "n_pairs": 3160}
FEWNERD_SCS = {"rho": 0.16616, "p": 1.4706429598501858e-13, "n_pairs": 1953}
FEWNERD_LEV = {"rho": 0.152227, "p": 1.3563843339646998e-11, "n_pairs": 1953}

OUTPUT_DIR = Path(__file__).parent


def get_pairs(types):
    return list(itertools.combinations(sorted(types), 2))


def normalized_levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    if m == 0 and n == 0:
        return 1.0
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if s1[i-1] == s2[j-1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j-1])
            prev = temp
    return 1.0 - dp[n] / max(m, n)


def wordnet_wup_similarity(name1, name2):
    from nltk.corpus import wordnet as wn

    def get_synset(name):
        name = name.lower().strip()
        # For Few-NERD hierarchical names, take part after hyphen
        if "-" in name:
            name = name.split("-", 1)[1]
        # For multi-word names with slashes, take first part
        if "/" in name:
            name = name.split("/")[0]
        # Clean up
        name = name.replace(" ", "_")

        # Try direct lookup
        synsets = wn.synsets(name, pos=wn.NOUN)
        if synsets:
            return synsets[0]

        # Try individual words (last word first as head noun)
        words = name.replace("_", " ").split()
        for w in reversed(words):
            synsets = wn.synsets(w, pos=wn.NOUN)
            if synsets:
                return synsets[0]

        # Try without pos restriction
        synsets = wn.synsets(name)
        if synsets:
            return synsets[0]
        for w in reversed(words):
            synsets = wn.synsets(w)
            if synsets:
                return synsets[0]

        return None

    s1 = get_synset(name1)
    s2 = get_synset(name2)

    if s1 is None or s2 is None:
        return None
    if s1 == s2:
        return 1.0

    sim = s1.wup_similarity(s2)
    return sim


def same_parent_indicator(name1, name2, dataset):
    if dataset == "fewnerd":
        # Same prefix category
        cat1 = name1.split("-", 1)[0] if "-" in name1 else name1
        cat2 = name2.split("-", 1)[0] if "-" in name2 else name2
        return 1 if cat1 == cat2 else 0
    else:
        # FewRel: check if they share a direct WordNet hypernym
        from nltk.corpus import wordnet as wn

        def get_hypernyms(name):
            name = name.lower().strip().replace(" ", "_")
            synsets = wn.synsets(name, pos=wn.NOUN)
            if not synsets:
                words = name.replace("_", " ").split()
                for w in reversed(words):
                    synsets = wn.synsets(w, pos=wn.NOUN)
                    if synsets:
                        break
            if not synsets:
                synsets = wn.synsets(name)
                if not synsets:
                    words = name.replace("_", " ").split()
                    for w in reversed(words):
                        synsets = wn.synsets(w)
                        if synsets:
                            break
            if not synsets:
                return set()
            return set(h for s in synsets[:2] for h in s.hypernyms())

        h1 = get_hypernyms(name1)
        h2 = get_hypernyms(name2)
        return 1 if h1 & h2 else 0


def compute_metrics(types, conf_array, dataset_name):
    pairs = get_pairs(types)
    n_pairs = len(pairs)
    assert len(conf_array) == n_pairs, f"Expected {n_pairs} pairs, got {len(conf_array)}"

    conf = np.array(conf_array, dtype=float)

    wup_vals = []
    parent_vals = []
    wup_missing = 0

    for i, (t1, t2) in enumerate(pairs):
        wup = wordnet_wup_similarity(t1, t2)
        if wup is None:
            wup_vals.append(np.nan)
            wup_missing += 1
        else:
            wup_vals.append(wup)

        parent_vals.append(same_parent_indicator(t1, t2, dataset_name))

    wup_arr = np.array(wup_vals)
    parent_arr = np.array(parent_vals, dtype=float)

    # WuP correlation (exclude NaN pairs)
    valid_wup = ~np.isnan(wup_arr)
    n_valid_wup = valid_wup.sum()
    if n_valid_wup > 10:
        wup_rho, wup_p = stats.spearmanr(wup_arr[valid_wup], conf[valid_wup])
    else:
        wup_rho, wup_p = float("nan"), float("nan")

    # Same-parent correlation
    parent_rho, parent_p = stats.spearmanr(parent_arr, conf)

    print(f"\n--- {dataset_name} ---")
    print(f"  Total pairs: {n_pairs}")
    print(f"  WuP: valid={n_valid_wup}, missing={wup_missing}, rho={wup_rho:.6f}, p={wup_p:.2e}")
    print(f"  Same-parent: rho={parent_rho:.6f}, p={parent_p:.2e}")
    print(f"  Same-parent=1 count: {int(parent_arr.sum())}")

    return {
        "wup": {"rho": float(wup_rho), "p": float(wup_p), "n_pairs": int(n_valid_wup), "n_missing": wup_missing},
        "same_parent": {"rho": float(parent_rho), "p": float(parent_p), "n_pairs": n_pairs},
    }


def main():
    import nltk
    nltk.download("wordnet", quiet=True)
    nltk.download("omw-1.4", quiet=True)

    print("Computing WordNet WuP and same-parent for FewRel...")
    fewrel_results = compute_metrics(FEWREL_TYPES, FEWREL_CONF, "fewrel")

    print("\nComputing WordNet WuP and same-parent for Few-NERD...")
    fewnerd_results = compute_metrics(FEWNERD_TYPES, FEWNERD_CONF, "fewnerd")

    results = {
        "fewrel": {
            "n_types": len(FEWREL_TYPES),
            "n_pairs": FEWREL_SCS["n_pairs"],
            "metrics": {
                "scs": {"spearman_rho": FEWREL_SCS["rho"], "p_value": FEWREL_SCS["p"]},
                "levenshtein": {"spearman_rho": FEWREL_LEV["rho"], "p_value": FEWREL_LEV["p"]},
                "wordnet_wup": {"spearman_rho": fewrel_results["wup"]["rho"], "p_value": fewrel_results["wup"]["p"], "n_valid_pairs": fewrel_results["wup"]["n_pairs"], "n_missing": fewrel_results["wup"]["n_missing"]},
                "same_parent": {"spearman_rho": fewrel_results["same_parent"]["rho"], "p_value": fewrel_results["same_parent"]["p"]},
            },
        },
        "fewnerd": {
            "n_types": len(FEWNERD_TYPES),
            "n_pairs": FEWNERD_SCS["n_pairs"],
            "metrics": {
                "scs": {"spearman_rho": FEWNERD_SCS["rho"], "p_value": FEWNERD_SCS["p"]},
                "levenshtein": {"spearman_rho": FEWNERD_LEV["rho"], "p_value": FEWNERD_LEV["p"]},
                "wordnet_wup": {"spearman_rho": fewnerd_results["wup"]["rho"], "p_value": fewnerd_results["wup"]["p"], "n_valid_pairs": fewnerd_results["wup"]["n_pairs"], "n_missing": fewnerd_results["wup"]["n_missing"]},
                "same_parent": {"spearman_rho": fewnerd_results["same_parent"]["rho"], "p_value": fewnerd_results["same_parent"]["p"]},
            },
        },
    }

    output_path = OUTPUT_DIR / "results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved results to {output_path}")

    # Summary table
    print("\n" + "=" * 85)
    print(f"{'Dataset':<12} {'Metric':<20} {'Spearman ρ':>12} {'p-value':>14} {'Sig?':>6}")
    print("-" * 85)
    for ds in ["fewrel", "fewnerd"]:
        for metric in ["scs", "levenshtein", "wordnet_wup", "same_parent"]:
            m = results[ds]["metrics"][metric]
            rho = m["spearman_rho"]
            p = m["p_value"]
            sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
            print(f"{ds:<12} {metric:<20} {rho:>12.4f} {p:>14.2e} {sig:>6}")
        print("-" * 85)
    print("=" * 85)


if __name__ == "__main__":
    main()
