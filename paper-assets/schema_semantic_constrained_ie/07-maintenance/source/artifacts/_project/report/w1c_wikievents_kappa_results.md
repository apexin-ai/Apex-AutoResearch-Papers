# WikiEvents Constraint Tightness (κ) Analysis

## 1. κ Distribution Statistics

| Metric | Value |
|--------|-------|
| Total event types | 56 |
| Total roles (event_type, role pairs) | 245 |
| Total entity types | 27 |
| κ min | 0.1481 (23/27 valid types) |
| κ max | 0.9630 (1/27 valid types) |
| κ mean | 0.8204 |
| κ median | 0.8889 |

## 2. Top-10 Tightest Roles (Highest κ)

| Event.Role | κ | Valid Types |
|-----------|------|-------------|
| Dismantle.Components | 0.9630 | 1 (VEH) |
| SensoryObserve.Instrument | 0.9630 | 1 |
| TeachingTrainingLearning.Unspecified.FieldOfKnowledge | 0.9630 | 1 |
| TeachingTrainingLearning.Unspecified.Institution | 0.9630 | 1 |
| Defeat.Unspecified.ConflictOrElection | 0.9630 | 1 |
| DemonstrateWithViolence.VisualDisplay | 0.9630 | 1 |
| Protest.Unspecified.VisualDisplay | 0.9630 | 1 |
| ImpedeInterfereWith.Unspecified.ImpededEvent | 0.9630 | 1 |
| Crash.Unspecified.DriverPassenger | 0.9630 | 1 |
| Crash.Unspecified.Vehicle | 0.9630 | 1 |

All top-tightest roles allow exactly 1 entity type (41 roles total at κ=0.9630).

## 3. Top-10 Loosest Roles (Lowest κ)

| Event.Role | κ | Valid Types |
|-----------|------|-------------|
| Meet.Topic | 0.1481 | 23 |
| Contact.Unspecified.Topic | 0.1481 | 23 |
| Prevarication.Unspecified.Topic | 0.1481 | 23 |
| RequestCommand.Unspecified.Topic | 0.1481 | 23 |
| ThreatenCoerce.Unspecified.Topic | 0.1481 | 23 |
| RequestCommand.Broadcast.Topic | 0.1481 | 23 |
| RequestCommand.Correspondence.Topic | 0.1481 | 23 |
| RequestCommand.Meet.Topic | 0.1481 | 23 |
| ThreatenCoerce.Broadcast.Topic | 0.1481 | 23 |
| ThreatenCoerce.Correspondence.Topic | 0.1481 | 23 |

All loosest roles are "Topic" roles in Communication events (15 roles total at κ=0.1481).

## 4. Histogram (Valid Type Count Distribution)

| Valid Types | κ | # Roles | % |
|-------------|------|---------|-----|
| 1 | 0.9630 | 41 | 16.7% |
| 2 | 0.9259 | 19 | 7.8% |
| 3 | 0.8889 | 69 | 28.2% |
| 4 | 0.8519 | 72 | 29.4% |
| 5 | 0.8148 | 9 | 3.7% |
| 6 | 0.7778 | 2 | 0.8% |
| 7 | 0.7407 | 3 | 1.2% |
| 9 | 0.6667 | 3 | 1.2% |
| 11 | 0.5926 | 3 | 1.2% |
| 13 | 0.5185 | 3 | 1.2% |
| 14 | 0.4815 | 2 | 0.8% |
| 15 | 0.4444 | 2 | 0.8% |
| 17 | 0.3704 | 2 | 0.8% |
| 23 | 0.1481 | 15 | 6.1% |

**Distribution is strongly right-skewed**: 84% of roles have κ >= 0.80 (4 or fewer valid types out of 27). The ontology is highly constraining for most roles.

### Binned Summary

| κ Range | # Roles | % |
|---------|---------|-----|
| [0.0, 0.6) | 27 | 11.0% |
| [0.6, 0.7) | 3 | 1.2% |
| [0.7, 0.8) | 5 | 2.0% |
| [0.8, 0.9) | 150 | 61.2% |
| [0.9, 1.0) | 60 | 24.5% |

## 5. κ vs. Zero-Shot AC Violation Rate

Data source: unconstrained outputs from Qwen + LLaMA on full WikiEvents test (246 docs each), 52 roles with observed arguments, 625 total arguments, 204 AC violations (32.64% overall).

### Binned Analysis

| κ Group | # Roles | # Args | AC Violation Rate | Mean κ |
|---------|---------|--------|-------------------|--------|
| Loose (κ < 0.80) | 5 | 150 | 30.00% | 0.3259 |
| Medium (0.80 ≤ κ < 0.90) | 29 | 271 | 21.03% | 0.8570 |
| Tight (κ ≥ 0.90) | 18 | 204 | 50.00% | 0.9527 |

### Correlation

| Metric | Value |
|--------|-------|
| Pearson r(κ, AC_rate) | 0.3113 |
| Weighted Pearson r(κ, AC_rate) | 0.2515 |

### Per-Role Detail (Sorted by κ desc)

| Event.Role | Args | AC Violations | AC Rate | κ | Valid Types |
|-----------|------|---------------|---------|------|-------------|
| SensoryObserve.Instrument | 3 | 3 | 100.00% | 0.9630 | 1 |
| EndPosition.Unspecified.Position | 4 | 4 | 100.00% | 0.9630 | 1 |
| Sentence.Unspecified.Sentence | 24 | 24 | 100.00% | 0.9630 | 1 |
| Transportation.Unspecified.Vehicle | 9 | 0 | 0.00% | 0.9630 | 1 |
| Convict.Unspecified.Crime | 3 | 3 | 100.00% | 0.9630 | 1 |
| Acquit.Unspecified.Crime | 1 | 1 | 100.00% | 0.9630 | 1 |
| Crash.Unspecified.Vehicle | 1 | 0 | 0.00% | 0.9630 | 1 |
| Injury.Unspecified.BodyPart | 4 | 4 | 100.00% | 0.9630 | 1 |
| ArrestJailDetain.Unspecified.Crime | 2 | 1 | 50.00% | 0.9630 | 1 |
| ChargeIndict.Unspecified.Crime | 7 | 7 | 100.00% | 0.9630 | 1 |
| Sentence.Unspecified.Crime | 4 | 4 | 100.00% | 0.9630 | 1 |
| BlockPassage.Vehicle | 1 | 0 | 0.00% | 0.9630 | 1 |
| InvestigateCrime.Unspecified.Crime | 3 | 3 | 100.00% | 0.9630 | 1 |
| Injury.Unspecified.Victim | 51 | 21 | 41.18% | 0.9259 | 2 |
| DetonateExplode.Instrument | 13 | 8 | 61.54% | 0.9259 | 2 |
| Die.Unspecified.Victim | 71 | 19 | 26.76% | 0.9259 | 2 |
| ManufactureAssemble.Unspecified.Instrument | 1 | 0 | 0.00% | 0.9259 | 2 |
| Diagnosis.Unspecified.Patient | 2 | 0 | 0.00% | 0.9259 | 2 |
| Protest.Unspecified.Target | 15 | 9 | 60.00% | 0.8889 | 3 |
| Transportation.Unspecified.Destination | 37 | 2 | 5.41% | 0.8889 | 3 |
| Damage.Instrument | 34 | 16 | 47.06% | 0.8889 | 3 |
| DemonstrateWithViolence.Target | 8 | 3 | 37.50% | 0.8889 | 3 |
| ... (29 more rows in medium/loose groups) | | | | | |

### Qualitative Analysis

1. **Tight constraints amplify violations**: The κ ≥ 0.90 group has the highest AC violation rate (50%), significantly above the medium group (21%). When only 1-2 entity types are valid, LLMs are much more likely to assign an incorrect type. This is especially pronounced for "Crime" roles (only CRM valid) and "BodyPart" (only BOD valid), where models consistently produce PER or other common types instead.

2. **Non-monotonic pattern in loose group**: The loose κ < 0.80 group shows 30% AC rate, higher than the medium group. This is driven primarily by Attack.Unspecified.Target (126 args, 34% AC rate, κ=0.5926) and GenericCrime.Victim (14 args, 64% AC rate, κ=0.8148). These are high-frequency roles where the model makes systematic errors despite relatively permissive constraints.

3. **Role semantics interact with tightness**: Some very tight roles have 0% AC violation (Transportation.Vehicle, BlockPassage.Vehicle, Crash.Vehicle) because "VEH" is semantically obvious. In contrast, abstract roles like "Crime" (valid: CRM only) or "Sentence" (valid: SEN only) have near-100% AC violations because LLMs don't distinguish fine-grained KAIROS types (CRM, SEN) from common types (PER, ORG).

4. **Key insight for the paper**: κ is necessary but not sufficient to predict violation rate. The interaction between constraint tightness and entity type "prototypicality" (how often LLMs default to common types like PER/ORG/GPE) determines actual violation rates. This supports the motivation for semantic-constrained decoding: tighter constraints create more opportunities for violation, but only when the valid types are non-prototypical.
