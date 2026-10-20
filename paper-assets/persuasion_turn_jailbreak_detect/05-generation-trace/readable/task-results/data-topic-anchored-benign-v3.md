# data topic anchored benign v3

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_topic-anchored-benign-v3_20260517T221500_result.json`
- **Structured JSON:** [`bb07c3141491aceaaec4.json`](../../sessions/bb/bb07c3141491aceaaec4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## HARD STOP: TF-IDF Gate FAIL

**F1 = 0.9900** (threshold: < 0.80 to pass)

### Top 10 Discriminative Features Analysis

| Feature | Coef | Class | Type |
|---------|------|-------|------|
| `so was` | -1.07 | Benign | B - template pattern ("so I was reading...") |
| `or` | -0.86 | Benign | B - option-seeking pattern |
| `you` | +0.83 | Jailbreak | neither - direct address |
| `was thinking` | -0.67 | Benign | B - hedging template |
| `so` | -0.62 | Benign | B - discourse marker |
| `do they` | -0.61 | Benign | B - third-person questions |
| `what if` | +0.50 | Jailbreak | A - hypothetical framing |
| `could` | +0.48 | Jailbreak | neither - modal verb |
| `been` | +0.47 | Jailbreak | neither - narrative past |
| `guess` | -0.56 | Benign | B - hedging template |

**A-type escalation markers: 0, B-type generic request markers: 0** (none of the predefined markers hit, but the separation is from a different axis)

### Root Cause Analysis

V3 casual prompt created a **new register gap** instead of fixing the old one:
1. **V3 benign is TOO uniformly hedging**: "so I was thinking...", "I wonder if...", "not sure about...", "I guess..." appear in nearly every conversation
2. **Crescendo uses direct 2nd-person engagement**: "you", "have you", "what if we", "someone who" - collaborative/hypothetical framing
3. **V3 focuses on 3rd parties**: "do they", "does that", "they" vs Crescendo's "you/we" pronouns

The casual style instructions are being followed too consistently - the model learned a single "casual template" instead of genuine diversity. The core issue isn't formality alone; it's that the user simulator produces monolithic register regardless of prompt.

---
