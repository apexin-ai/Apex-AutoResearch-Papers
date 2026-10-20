# paper appendix 008e s0 nve fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_008e_s0_nve_fix_20260525T165614_result.json`
- **Structured JSON:** [`370d232e87d1549baf5c.json`](../../sessions/37/370d232e87d1549baf5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。Diff:

```diff
-008e_v3 s0 & Mitigation & trn & ON & 15 & 148.0 @105K & 0.60$\times$ & No CIVO$^j$ \\
+008e_v3 s0 & Mitigation & trn & ON & 15 & 148.0 @105K & 0.80$\times$ & No CIVO$^j$ \\

-008e_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.60$\times$ & Healthy \\
+008e_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.61$\times$ & Healthy \\
```

4 个 mitigation seeds NVE 值确认：

| Seed | Exp | NVE | 状态 |
|------|-----|-----|------|
| s0 | exp_070 | **0.80×** | 已修正 (was 0.60) |
| s1 | exp_080 | 0.60× | 无需改动 |
| s2 | exp_081 | 0.50× | 无需改动 |
| s5 | exp_072 | **0.61×** | 已修正 (was 0.60) |

---
