# data 340m accuracy extract

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_340m-accuracy-extract_20260522T004140_result.json`
- **Structured JSON:** [`6257bc446bebecea2ec0.json`](../../sessions/62/6257bc446bebecea2ec0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the results:

## 340M h3-1
```
              GDN       RetNet     HGRN2
HellaSwag†    0.4090    0.4086     0.4358
PIQA          0.6616    0.6725     0.6785
ARC-Easy      0.5690    0.5905     0.6086
```

## 340M pure
```
              GDN       RetNet     HGRN2
HellaSwag†    0.4151    0.4120     0.4318
PIQA          0.6567    0.6621     0.6687
ARC-Easy      0.5669    0.6044     0.6111
```

## 1.3B h3-1
```
              GDN       RetNet     HGRN2
HellaSwag†    0.6032    0.5777     0.6040
PIQA          0.7378    0.7291     0.7301
ARC-Easy      0.7083    0.6961     0.7205
```

† = acc_norm for HellaSwag; PIQA and ARC-Easy use acc.

---
