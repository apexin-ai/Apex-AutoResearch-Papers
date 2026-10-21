# OOV Relation Name Replacement Cases (DocRED, Grammar-Only)

## Overview

When the unconstrained LLM generates an out-of-vocabulary (OOV) relation name, the XGrammar CFG constraint forces token-level selection toward the nearest in-vocabulary relation name. This "nearest" is determined by token-prefix matching, not semantic similarity, which frequently produces semantically absurd replacements and introduces new domain-range (DR) violations.

**Statistics (DocRED, 998 docs):**
- OOV triples in unconstrained output: **5,261** (2,038 unique OOV names)
- OOV triples that grammar replaced with in-vocab names: **4,357**
- Grammar replacements that cause DR violations: **1,594 (36.6%)**

## Case Table

| # | Document | OOV Relation | Replaced With | Semantic? | head → tail | DR Violation? |
|---|----------|-------------|---------------|-----------|-------------|---------------|
| 1 | Amandeep Khare | opponent | operator | No | Amandeep Narayan Khare (PER) → Sri Lanka (LOC) | Yes |
| 2 | Greatest Hits (Queen album) | peaked at | performer | No | Greatest Hits (MISC) → UK Albums Chart (LOC) | No |
| 3 | Allen County, Ohio | population | has part | No | Allen County (LOC) → 106,331 (NUM) | Yes |
| 4 | María de Buenos Aires | instrument | product or material produced | No | María de Buenos Aires (MISC) → bandoneón (MISC) | Yes |
| 5 | Skai TV | available on | operator | No | Skai TV (ORG) → Nova (ORG) | No |

## Detailed Analysis

### Case 1: "opponent" → "operator"

**Document:** Amandeep Khare — Indian cricketer who played against Sri Lanka U-19.

**Context:** "He scored a century for India national under-19 cricket team against Sri Lanka national under-19 cricket team."

The unconstrained model correctly identifies Sri Lanka as an **opponent** of the cricketer. Grammar constraint matches the token prefix "op" and selects "operator" — the closest in-vocabulary string. This produces the nonsensical triple (Amandeep Khare, operator, Sri Lanka), asserting the cricketer "operates" a country. Causes a DR violation: PER→LOC is not a valid entity-type pair for "operator" (P137).

**Mechanism:** Token-prefix match on "op" → "operator" is the only vocabulary item starting with "op".

### Case 2: "peaked at" → "performer"

**Document:** Greatest Hits (Queen album) — compilation album that reached high chart positions.

**Context:** "Greatest Hits ... became the best-selling album... in the UK Albums Chart."

The unconstrained model generates "peaked at" to express chart performance. Grammar forces this to "performer" — the nearest in-vocabulary relation starting with "pe". The resulting triple (Greatest Hits, performer, UK Albums Chart) asserts the album "performs" the chart, inverting the semantic direction entirely. The gold relation for this album is P175 (performer) with Queen as the tail, not the chart.

**Mechanism:** Token-prefix match on "pe" → "performer" (P175). Ironically, "performer" is a valid DocRED relation, but the head-tail pair is wrong — the album should be performed *by* Queen, not *perform* the chart.

### Case 3: "population" → "has part"

**Document:** Allen County, Ohio — a U.S. county with population 106,331.

**Context:** "As of the 2010 census, the population was 106,331."

The unconstrained model generates "population" to link Allen County to the number 106,331. No such relation exists in DocRED's ontology. Grammar replaces it with "has part" (P527), producing (Allen County, has part, 106,331) — asserting a number is a constituent part of the county. Causes a DR violation: LOC→NUM is not a valid pair for "has part."

**Mechanism:** No close token-prefix match; grammar falls back to a generic structural relation. This is an example of the ontology simply lacking a suitable relation — no in-vocabulary replacement would be correct.

### Case 4: "instrument" → "product or material produced"

**Document:** María de Buenos Aires — tango operetta by Ástor Piazzolla.

**Context:** The operetta features bandoneón, violin, and piano in its orchestration.

The unconstrained model generates "instrument" to link the operetta to its musical instruments. Grammar replaces it with "product or material produced" (P1056), producing (María de Buenos Aires, product or material produced, bandoneón) — asserting the operetta *manufactures* a bandoneón. Causes a DR violation: MISC→MISC is not a valid pair for P1056. This replacement is applied to all three instruments (bandoneón, violin, piano), tripling the error count.

**Mechanism:** Token-prefix match on "in" → "product or material produced" is not a prefix match; this is likely a fallback to the most generic "production" relation when no close match exists.

### Case 5: "available on" → "operator"

**Document:** Skai TV — Greek television network available on Nova and Cosmote TV subscription services.

**Context:** "It is available on the subscription-based encrypted services of Nova and Cosmote TV."

The unconstrained model generates "available on" to express platform availability. Grammar replaces with "operator" (P137), producing (Skai TV, operator, Nova). This reverses the semantic direction: "operator" means Nova *operates* Skai TV, when in reality Skai TV is merely *distributed through* Nova's platform. The gold annotation has no such relation — the correct relation is P127 (owned by) linking Skai TV to Skai Group. No DR violation (ORG→ORG is valid for P137), making this a silent semantic error that passes type-checking.

**Mechanism:** No token-prefix overlap between "available on" and "operator." Grammar selects "operator" as the closest ORG→ORG relation available.

## Key Takeaway

Grammar-only constraint replaces OOV names via **token-level prefix matching**, not semantic similarity. This produces three failure modes:
1. **String-similarity traps** — "opponent" → "operator", "peaked at" → "performer" (token prefix coincidence)
2. **Ontology gaps** — "population", "instrument" have no valid DocRED equivalent; any replacement is wrong
3. **Silent semantic errors** — "available on" → "operator" passes DR checks but reverses meaning

These cases explain why Table 3 shows grammar-only constraint *increasing* DR violations compared to unconstrained: 36.6% of OOV replacements introduce new DR violations that did not exist in the original (albeit OOV) output.
