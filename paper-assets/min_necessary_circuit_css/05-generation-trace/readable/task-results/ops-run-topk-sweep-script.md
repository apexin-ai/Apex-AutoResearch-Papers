# ops run topk sweep script

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_run-topk-sweep-script_20260513T040149_result.json`
- **Structured JSON:** [`a82af67503c93960f4ac.json`](../../sessions/a8/a82af67503c93960f4ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行成功，完整输出：

```
Loading scores...

Edge key check:
  Arith: ACDC=32491, EAP-IG=32491, EP=32491
  IOI:   ACDC=32491, EAP-IG=32491, EP=32491
  Arith keys match: True
  IOI keys match: True

======================================================================
  Arithmetic
======================================================================

--- ACDC (Arithmetic) ---
  Total edges: 32491
  Infinity edges: 17
  Unique non-inf values: 5
    0.090000: 9 edges
    0.070000: 8 edges
    0.050000: 10 edges
    0.030000: 26 edges
    0.010000: 32421 edges

--- EAP-IG (Arithmetic) ---
  Total edges: 32491
  Infinity edges: 0
  Unique non-inf values: 32474
  Top-5 abs values: [0.1854, 0.0869, 0.0479, 0.0427, 0.0427]
  Median abs value: 0.000006

--- EP (Arithmetic) ---
  Total edges: 32491
  Infinity edges: 0
  Unique non-inf values: 32474
  Top-5 abs values: [13.176, 5.7434, 4.0426, 3.6395, 3.5172]
  Median abs value: 0.000629

  EAP-IG top-100 edges (fixed)
  EP top-100 edges (fixed)
  J(eapig, ep) = 0.6949
  ACDC isinf edges: 17
  ACDC isinf edge list: ['a7.h10->m10', 'a7.h10->m8', 'a7.h10->m9', 'a8.h11->m8', 'a8.h11->m9', 'a9.h1->logits', 'a9.h1->m9', 'input->m0', 'm0->a7.h10.v', 'm0->a8.h11.v', 'm0->a9.h1.v', 'm10->logits', 'm11->logits', 'm8->m10', 'm8->m9', 'm9->logits', 'm9->m10']

       k |  ACDC |   1/3 |   2/3 |   3/3 | J(ei,ep) | J(ei,ac) | J(ep,ac)
  -------+-------+-------+-------+-------+----------+----------+---------
   isinf |    17 |    36 |    65 |    17 |   0.6949 |   0.1700 |   0.1700
      20 |    20 |    36 |    62 |    20 |   0.6949 |   0.2000 |   0.2000
      50 |    50 |    40 |    39 |    44 |   0.6949 |   0.4151 |   0.4286
      75 |    75 |    51 |    31 |    54 |   0.6949 |   0.4463 |   0.4831
     100 |   100 |    76 |    31 |    54 |   0.6949 |   0.3699 |   0.3986
     150 |   150 |   126 |    31 |    54 |   0.6949 |   0.2755 |   0.2953
     200 |   200 |   176 |    31 |    54 |   0.6949 |   0.2195 |   0.2346

  --- Overlap details ---

  [isinf] ACDC=17 edges
    All 3: 17
    EAP-IG & EP only: 65
    EAP-IG & ACDC only: 0
    EP & ACDC only: 0
    3/3 edges: ['a7.h10->m10', 'a7.h10->m8', 'a7.h10->m9', 'a8.h11->m8', 'a8.h11->m9', 'a9.h1->logits', 'a9.h1->m9', 'input->m0', 'm0->a7.h10.v', 'm0->a8.h11.v', 'm0->a9.h1.v', 'm10->logits', 'm11->logits', 'm8->m10', 'm8->m9', 'm9->logits', 'm9->m10']

  [k=50] ACDC=50 edges
    All 3: 44
    EAP-IG & EP only: 38
    EAP-IG & ACDC only: 0
    EP & ACDC only: 1

  [k=100] ACDC=100 edges
    All 3: 54
    EAP-IG & EP only: 28
    EAP-IG & ACDC only: 0
    EP & ACDC only: 3

======================================================================
  IOI (baseline)
======================================================================

--- ACDC (IOI (baseline)) ---
  Total edges: 32491
  Infinity edges: 14
  Unique non-inf values: 5
    0.090000: 14 edges
    0.070000: 11 edges
    0.050000: 50 edges
    0.030000: 138 edges
    0.010000: 32264 edges

--- EAP-IG (IOI (baseline)) ---
  Total edges: 32491
  Infinity edges: 0
  Unique non-inf values: 32485
  Top-5 abs values: [0.3071, 0.2467, 0.1876, 0.1172, 0.0894]
  Median abs value: 0.000009

--- EP (IOI (baseline)) ---
  Total edges: 32491
  Infinity edges: 0
  Unique non-inf values: 32476
  Top-5 abs values: [10.467, 9.4644, 4.6848, 4.4922, 4.2317]
  Median abs value: 0.001485

  EAP-IG top-100 edges (fixed)
  EP top-100 edges (fixed)
  J(eapig, ep) = 0.3072
  ACDC isinf edges: 14
  ACDC isinf edge list: ['a0.h1->a9.h9.v', 'a10.h0->logits', 'a11.h2->logits', 'a5.h5->a8.h6.v', 'a7.h9->a9.h9.q', 'a8.h6->a9.h6.q', 'a8.h6->a9.h9.q', 'a9.h6->logits', 'a9.h9->logits', 'input->m0', 'm0->a10.h0.v', 'm0->a5.h5.q', 'm0->a9.h6.v', 'm0->a9.h9.v']

       k |  ACDC |   1/3 |   2/3 |   3/3 | J(ei,ep) | J(ei,ac) | J(ep,ac)
  -------+-------+-------+-------+-------+----------+----------+---------
   isinf |    14 |   103 |    45 |     7 |   0.3072 |   0.0962 |   0.0857
      20 |    20 |   100 |    48 |     8 |   0.3072 |   0.1429 |   0.0909
      50 |    50 |    96 |    56 |    14 |   0.3072 |   0.2397 |   0.1719
      75 |    75 |    98 |    60 |    19 |   0.3072 |   0.2868 |   0.2153
     100 |   100 |   108 |    60 |    24 |   0.3072 |   0.2903 |   0.2500
     150 |   150 |   135 |    61 |    31 |   0.3072 |   0.2887 |   0.2563
     200 |   200 |   166 |    69 |    32 |   0.3072 |   0.2500 |   0.2397

  --- Overlap details ---

  [isinf] ACDC=14 edges
    All 3: 7
    EAP-IG & EP only: 40
    EAP-IG & ACDC only: 3
    EP & ACDC only: 2
    3/3 edges: ['a10.h0->logits', 'a11.h2->logits', 'a9.h6->logits', 'a9.h9->logits', 'input->m0', 'm0->a5.h5.q', 'm0->a9.h9.v']

  [k=50] ACDC=50 edges
    All 3: 14
    EAP-IG & EP only: 33
    EAP-IG & ACDC only: 15
    EP & ACDC only: 8
    3/3 edges: ['a10.h0->logits', 'a10.h6->logits', 'a10.h7->logits', 'a11.h2->logits', 'a2.h2->a5.h5.k', 'a4.h11->a5.h5.k', 'a9.h6->logits', 'a9.h8->logits', 'a9.h9->logits', 'input->m0', 'm0->a2.h2.v', 'm0->a3.h0.k', 'm0->a5.h5.q', 'm0->a9.h9.v']

  [k=100] ACDC=100 edges
    All 3: 24
    EAP-IG & EP only: 23
    EAP-IG & ACDC only: 21
    EP & ACDC only: 16
    3/3 edges: ['a10.h0->logits', 'a10.h6->logits', 'a10.h7->logits', 'a11.h2->logits', 'a2.h2->a5.h5.k', 'a3.h7->a5.h5.k', 'a4.h11->a5.h5.k', 'a4.h11->m4', 'a9.h6->logits', 'a9.h7->logits', 'a9.h8->logits', 'a9.h9->logits', 'input->a0.h1.k', 'input->a0.h1.v', 'input->m0', 'm0->a11.h2.v', 'm0->a2.h2.v', 'm0->a3.h0.k', 'm0->a3.h0.q', 'm0->a4.h11.v', 'm0->a5.h5.q', 'm0->a6.h9.q', 'm0->a9.h9.v', 'm10->logits']

======================================================================
  DONE
======================================================================
```

脚本 1.22 秒执行完毕，无报错。

---
