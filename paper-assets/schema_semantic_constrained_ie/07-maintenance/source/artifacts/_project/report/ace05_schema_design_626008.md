# ACE05 Event Extraction: Schema Design and Ontology Constraints

## 1. Data Acquisition Status

**ACE 2005 (LDC2006T06)** is a licensed dataset from the Linguistic Data Consortium. Preprocessed versions cannot be freely distributed.

### Current state
- Neither westd-16980 nor westd-21461 has ACE05 data
- Created `data/ace05/` directory on westd-16980 with:
  - `ontology_constraints_ace05.json` (complete ontology constraints)
  - `sample_data.jsonl` (10 synthetic examples for development/testing)

### Data acquisition options
1. **LDC license** (recommended): Purchase from https://catalog.ldc.upenn.edu/LDC2006T06, then preprocess with OneIE scripts
2. **Preprocessing pipeline**: Use `nlpcl-lab/ace2005-preprocessing` or `jeremytanjianle/event-extraction-oneie` to convert raw LDC data to JSON
3. **OneIE format** (ACE05-E+): 17,172 train / 923 dev / 832 test sentences. Preprocessing via `preprocessing/process_ace.py`
4. **DyGIE++ format**: Alternative via `dwadden/dygiepp` preprocessing scripts

### Preprocessing command (once raw data is obtained)
```bash
# OneIE preprocessing
python preprocessing/process_ace.py -i <raw_ace_dir> -o <output_dir> -s resource/splits/ACE05-E -b bert-large-cased -c <cache_dir> -l english
```

---

## 2. ACE05 Event Ontology (33 Event Types)

### 2.1 Event Type Hierarchy

| Supertype (8) | Subtypes |
|---|---|
| **Life** (5) | Be-Born, Marry, Divorce, Injure, Die |
| **Movement** (1) | Transport |
| **Transaction** (2) | Transfer-Ownership, Transfer-Money |
| **Business** (4) | Start-Org, Merge-Org, Declare-Bankruptcy, End-Org |
| **Conflict** (2) | Attack, Demonstrate |
| **Contact** (2) | Meet, Phone-Write |
| **Personnel** (4) | Start-Position, End-Position, Nominate, Elect |
| **Justice** (13) | Arrest-Jail, Release-Parole, Trial-Hearing, Charge-Indict, Sue, Convict, Sentence, Fine, Execute, Extradite, Acquit, Appeal, Pardon |

### 2.2 Entity Types (7)

| Type | Description |
|---|---|
| PER | Person |
| ORG | Organization |
| GPE | Geo-Political Entity |
| LOC | Location |
| FAC | Facility |
| VEH | Vehicle |
| WEA | Weapon |

### 2.3 Argument Roles (22 unique)

Person, Agent, Victim, Attacker, Target, Entity, Instrument, Vehicle, Artifact, Buyer, Seller, Giver, Recipient, Beneficiary, Org, Plaintiff, Defendant, Adjudicator, Prosecutor, Origin, Destination, Place

---

## 3. Complete Argument Constraints (33 Event Types x Roles x Entity Types)

### Life Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Life:Be-Born** | Person | PER |
| | Place | GPE, LOC, FAC |
| **Life:Marry** | Person | PER |
| | Place | GPE, LOC, FAC |
| **Life:Divorce** | Person | PER |
| | Place | GPE, LOC, FAC |
| **Life:Injure** | Agent | PER, ORG, GPE |
| | Victim | PER |
| | Instrument | VEH, WEA |
| | Place | GPE, LOC, FAC |
| **Life:Die** | Person | PER |
| | Agent | PER, ORG, GPE |
| | Victim | PER |
| | Instrument | VEH, WEA |
| | Place | GPE, LOC, FAC |

### Movement Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Movement:Transport** | Agent | PER, ORG, GPE |
| | Artifact | PER, ORG, FAC, VEH, WEA |
| | Vehicle | VEH |
| | Origin | GPE, LOC, FAC |
| | Destination | GPE, LOC, FAC |

### Transaction Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Transaction:Transfer-Ownership** | Buyer | PER, ORG, GPE |
| | Seller | PER, ORG, GPE |
| | Artifact | PER, ORG, FAC, VEH, WEA |
| | Beneficiary | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Transaction:Transfer-Money** | Giver | PER, ORG, GPE |
| | Recipient | PER, ORG, GPE |
| | Beneficiary | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |

### Business Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Business:Start-Org** | Agent | PER, ORG, GPE |
| | Org | ORG, PER |
| | Place | GPE, LOC, FAC |
| **Business:Merge-Org** | Org | ORG, PER |
| **Business:Declare-Bankruptcy** | Org | ORG, PER |
| | Place | GPE, LOC, FAC |
| **Business:End-Org** | Org | ORG, PER |
| | Place | GPE, LOC, FAC |

### Conflict Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Conflict:Attack** | Attacker | PER, ORG, GPE |
| | Target | PER, ORG, GPE, LOC, FAC, VEH, WEA |
| | Victim | PER |
| | Instrument | VEH, WEA |
| | Place | GPE, LOC, FAC |
| **Conflict:Demonstrate** | Entity | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |

### Contact Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Contact:Meet** | Entity | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Contact:Phone-Write** | Entity | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |

### Personnel Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Personnel:Start-Position** | Person | PER |
| | Entity | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Personnel:End-Position** | Person | PER |
| | Entity | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Personnel:Nominate** | Agent | PER, ORG, GPE |
| | Person | PER |
| **Personnel:Elect** | Person | PER |
| | Entity | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |

### Justice Events

| Event Type | Role | Allowed Entity Types |
|---|---|---|
| **Justice:Arrest-Jail** | Person | PER |
| | Agent | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Release-Parole** | Person | PER |
| | Entity | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Trial-Hearing** | Defendant | PER, ORG, GPE |
| | Prosecutor | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Charge-Indict** | Defendant | PER, ORG, GPE |
| | Prosecutor | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Sue** | Plaintiff | PER, ORG, GPE |
| | Defendant | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Convict** | Defendant | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Sentence** | Defendant | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Fine** | Entity | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Execute** | Person | PER |
| | Agent | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Extradite** | Agent | PER, ORG, GPE |
| | Origin | GPE, LOC, FAC |
| | Destination | GPE, LOC, FAC |
| **Justice:Acquit** | Defendant | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| **Justice:Appeal** | Plaintiff | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |
| **Justice:Pardon** | Defendant | PER, ORG, GPE |
| | Adjudicator | PER, ORG, GPE |
| | Place | GPE, LOC, FAC |

---

## 4. JSON Output Schema (Event Extraction)

### 4.1 Design rationale

Compatible with existing RE format:
- RE output: `{"entities": [...], "relations": [...]}`
- EE output: `{"entities": [...], "events": [...]}`

Same `entities` structure, `events` replaces `relations`. Each event has a trigger word and structured arguments with entity type constraints.

### 4.2 Output format

```json
{
  "entities": [
    {"text": "rebels", "type": "PER"},
    {"text": "the city of Fallujah", "type": "FAC"},
    {"text": "Fallujah", "type": "GPE"},
    {"text": "mortars", "type": "WEA"}
  ],
  "events": [
    {
      "trigger": "attacked",
      "event_type": "Conflict:Attack",
      "arguments": [
        {"text": "rebels", "role": "Attacker", "type": "PER"},
        {"text": "the city of Fallujah", "role": "Target", "type": "FAC"},
        {"text": "Fallujah", "role": "Place", "type": "GPE"},
        {"text": "mortars", "role": "Instrument", "type": "WEA"}
      ]
    }
  ]
}
```

### 4.3 Field definitions

| Field | Type | Description |
|---|---|---|
| `entities[].text` | string | Entity mention text span |
| `entities[].type` | string | Entity type from {PER, ORG, GPE, LOC, FAC, VEH, WEA} |
| `events[].trigger` | string | Event trigger word/phrase |
| `events[].event_type` | string | Event type in "Supertype:Subtype" format |
| `events[].arguments[].text` | string | Argument text span (must match an entity) |
| `events[].arguments[].role` | string | Argument role (from 22 defined roles) |
| `events[].arguments[].type` | string | Entity type of the argument |

### 4.4 Ontology constraints for decoding

Three levels of constraint enforcement (matching RE approach):

1. **Event type constraint**: `event_type` must be one of 33 valid types
2. **Role constraint**: Each `role` must be valid for the given `event_type` (from `argument_constraints`)
3. **Entity type constraint**: Each argument's `type` must be compatible with its `role` (from `role_entity_constraints`)

### 4.5 SFT prompt template

```
You are an information extraction system. Extract all entities and events from the following document.

Entity types: PER, ORG, GPE, LOC, FAC, VEH, WEA

Event types:
- Life: Be-Born, Marry, Divorce, Injure, Die
- Movement: Transport
- Transaction: Transfer-Ownership, Transfer-Money
- Business: Start-Org, Merge-Org, Declare-Bankruptcy, End-Org
- Conflict: Attack, Demonstrate
- Contact: Meet, Phone-Write
- Personnel: Start-Position, End-Position, Nominate, Elect
- Justice: Arrest-Jail, Release-Parole, Trial-Hearing, Charge-Indict, Sue, Convict, Sentence, Fine, Execute, Extradite, Acquit, Appeal, Pardon

Document:
{document_text}
```

---

## 5. Constraint Files

| File | Location | Description |
|---|---|---|
| `ontology_constraints_ace05.json` | `westd-16980:/root/schema_semantic_constrained_ie/data/ace05/` | Full ontology with 33 event types, 22 roles, 7 entity types, and cross-product constraints |
| `sample_data.jsonl` | Same directory | 10 synthetic examples covering diverse event types |

### ontology_constraints_ace05.json structure

```
meta                    -- dataset metadata
event_types             -- flat list of 33 event types
event_supertypes        -- hierarchy (8 supertypes -> subtypes)
entity_types            -- 7 entity types
role_entity_constraints -- global role -> entity type mapping (22 roles)
argument_constraints    -- per-event-type role -> entity type mapping
```

---

## 6. Sources

- OneIE event_role.json: https://github.com/jeremytanjianle/event-extraction-oneie/tree/main/resource/valid_patterns_ace
- ACE 2005 Annotation Guidelines v5.4.3 (LDC)
- ACE 2005 Multilingual Training Corpus: https://catalog.ldc.upenn.edu/LDC2006T06
