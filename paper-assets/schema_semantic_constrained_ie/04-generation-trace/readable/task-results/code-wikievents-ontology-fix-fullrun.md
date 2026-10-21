# code wikievents ontology fix fullrun

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_ontology_fix_fullrun_20260517T173343_result.json`
- **Structured JSON:** [`ec817e037f45a20ba180.json`](../../sessions/ec/ec817e037f45a20ba180.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Second doc: 30.5s, parsed OK. Average ~52s/doc. Estimated ~3.5 hours for 246 docs.

Here's the status summary:

**Part 1: Ontology Fixes - COMPLETE**

All fixes applied to `ontology_constraints_wikievents.json`:

1. **5 missing event types added** (cross-products of intent x modality):
   - `Contact.RequestCommand.Broadcast` → `RequestCommand.Broadcast`
   - `Contact.RequestCommand.Correspondence` → `RequestCommand.Correspondence`
   - `Contact.RequestCommand.Meet` → `RequestCommand.Meet`
   - `Contact.ThreatenCoerce.Broadcast` → `ThreatenCoerce.Broadcast`
   - `Contact.ThreatenCoerce.Correspondence` → `ThreatenCoerce.Correspondence`
   - Role constraints inherited from parent intent types (Communicator, Recipient, Topic, Place)

2. **CRM entity type added** to entity_types (27 total)

3. **ObservedEntity and Observer roles added** to `InvestigateCrime.Unspecified`:
   - Observer: [GPE, ORG, PER] (from data: 24 instances)
   - ObservedEntity: [COM, FAC, ORG, PER, VEH, WEA] (from data: 24 instances)

4. **Consistency validation passed** on all 246 docs:
   - All event types mapped
   - All entity types covered
   - All roles have constraints
   - 1 minor data annotation edge case (VEH as Destination in Transportation, 1 instance)

5. **First-token collisions**: RequestCommand.* and ThreatenCoerce.* groups share first tokens with their `.Unspecified` siblings, disambiguated by the second token after `.`

**Updated meta**: 56 event types, 27 entity types, 80 roles, 245 constraints

**Part 2: Unconstrained Baseline - RUNNING**

- tmux session: `wikievents_unconstrained`
- GPU 1 (RTX PRO 6000 Blackwell, 97GB)
- Data: `data/wikievents/all.jsonl` (246 docs)
- Output: `outputs/wikievents_qwen_unconstrained_full.jsonl`
- Estimated completion: ~3.5 hours (~52s/doc average)
- 2/246 docs completed so far

I'll check back on progress. Want me to monitor and report results when it completes?

---
