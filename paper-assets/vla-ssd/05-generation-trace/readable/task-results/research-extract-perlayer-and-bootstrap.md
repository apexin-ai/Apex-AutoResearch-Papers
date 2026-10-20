# research extract perlayer and bootstrap

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_extract_perlayer_and_bootstrap_20260516T032838_result.json`
- **Structured JSON:** [`ba17bbd1e3f54c1c45f9.json`](../../sessions/ba/ba17bbd1e3f54c1c45f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## PART 1: Per-layer RSA at key layers

### trained_with_inst / image_mean
| Layer | RSA |
|-------|-----|
| L0 | 0.6117 |
| L1 | 0.6124 |
| L12 | 0.6282 |
| L22 | 0.5720 |
| L32 | 0.4223 |

### trained_with_inst / last_preaction
| Layer | RSA |
|-------|-----|
| L0 | nan |
| L1 | 0.5682 |
| L12 | 0.6425 |
| L22 | 0.6060 |
| L32 | 0.5843 |

### untrained_with_inst / image_mean
| Layer | RSA |
|-------|-----|
| L0 | 0.6117 |
| L1 | 0.5712 |
| L12 | 0.5496 |
| L22 | 0.5497 |
| L32 | 0.5446 |

### untrained_with_inst / last_preaction
| Layer | RSA |
|-------|-----|
| L0 | nan |
| L1 | 0.6262 |
| L12 | 0.5953 |
| L22 | 0.5927 |
| L32 | 0.5866 |

---

## Full curves (all 33 layers)

### trained_with_inst / image_mean
```
L0:0.6117  L1:0.6124  L2:0.6121  L3:0.6127  L4:0.6137  L5:0.6146  L6:0.6175  L7:0.6201
L8:0.6187  L9:0.6199  L10:0.6198 L11:0.6169 L12:0.6282 L13:0.6266 L14:0.6243 L15:0.6172
L16:0.6128 L17:0.6088 L18:0.6071 L19:0.6072 L20:0.6041 L21:0.5959 L22:0.5720 L23:0.5558
L24:0.5459 L25:0.5346 L26:0.5159 L27:0.5136 L28:0.5125 L29:0.4971 L30:0.4395 L31:0.4328
L32:0.4223
```

### untrained_with_inst / image_mean
```
L0:0.6117  L1:0.5712  L2:0.5604  L3:0.5597  L4:0.5576  L5:0.5576  L6:0.5588  L7:0.5570
L8:0.5553  L9:0.5532  L10:0.5510 L11:0.5509 L12:0.5496 L13:0.5496 L14:0.5494 L15:0.5493
L16:0.5497 L17:0.5495 L18:0.5500 L19:0.5495 L20:0.5488 L21:0.5487 L22:0.5497 L23:0.5497
L24:0.5494 L25:0.5482 L26:0.5480 L27:0.5467 L28:0.5457 L29:0.5454 L30:0.5454 L31:0.5448
L32:0.5446
```

### trained_with_inst / last_preaction
```
L0:nan     L1:0.5682  L2:0.5818  L3:0.5880  L4:0.5892  L5:0.5836  L6:0.5617  L7:0.5430
L8:0.5469  L9:0.5682  L10:0.5577 L11:0.5993 L12:0.6425 L13:0.6395 L14:0.6374 L15:0.6348
L16:0.6303 L17:0.6261 L18:0.6227 L19:0.6194 L20:0.6164 L21:0.6086 L22:0.6060 L23:0.6003
L24:0.5950 L25:0.5855 L26:0.5812 L27:0.5822 L28:0.5814 L29:0.5787 L30:0.5724 L31:0.5703
L32:0.5843
```

### untrained_with_inst / last_preaction
```
L0:nan     L1:0.6262  L2:0.6207  L3:0.6156  L4:0.6119  L5:0.6084  L6:0.6053  L7:0.6029
L8:0.6013  L9:0.6008  L10:0.5977 L11:0.5966 L12:0.5953 L13:0.5939 L14:0.5934 L15:0.5936
L16:0.5941 L17:0.5950 L18:0.5947 L19:0.5945 L20:0.5938 L21:0.5936 L22:0.5927 L23:0.5917
L24:0.5913 L25:0.5907 L26:0.5895 L27:0.5888 L28:0.5879 L29:0.5885 L30:0.5883 L31:0.5870
L32:0.5866
```

---

## PART 2: Bootstrap CI (Method B, per-task paired)

### image_mean (best-vs-best)
- **Trained peak**: L12 = 0.6282
- **Untrained peak**: L0 = 0.6117
- **Δ**: 0.0165
- **95% CI**: [-0.0002, 0.0346] — **not significant** (CI includes 0)
- **p**: 0.0264
- Per-task deltas: [0.0204, 0.0117, 0.0393, 0.0336, 0.0809, -0.0077, 0.0115, 0.0080, -0.0304, -0.0023]
- N = 10

### image_mean same-layer (L12)
- Trained L12: 0.6282, Untrained L12: 0.5496
- **Δ**: 0.0787, **95% CI**: [0.0597, 0.0985], **p**: 0.0000 — **highly significant**

### last_preaction (best-vs-best, NaN excluded)
- **Trained peak**: L12 = 0.6425
- **Untrained peak**: L1 = 0.6262
- **Δ**: 0.0163
- **95% CI**: [0.0001, 0.0312] — **marginally significant** (CI barely excludes 0)
- **p**: 0.0249
- Per-task deltas: [0.0453, -0.0413, 0.0169, 0.0039, 0.0553, 0.0105, 0.0135, 0.0175, 0.0025, 0.0391]
- N = 10

### last_preaction same-layer (L12)
- Trained L12: 0.6425, Untrained L12: 0.5953
- **Δ**: 0.0472, **95% CI**: [0.0240, 0.0712], **p**: 0.0000 — **highly significant**

---

## PART 3: Instruction control (4 conditions)

| Condition | Best Layer | Peak RSA |
|-----------|-----------|----------|
| normal | 12 | 0.6282 |
| no_inst | 13 | 0.6225 |
| random_s0 | 12 | 0.6283 |
| shuffled | 12 | 0.6282 |

---
