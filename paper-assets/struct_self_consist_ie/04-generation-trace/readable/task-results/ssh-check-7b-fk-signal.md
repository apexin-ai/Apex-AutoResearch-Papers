# ssh check 7b fk signal

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-7b-fk-signal_20260520T075556_result.json`
- **Structured JSON:** [`168f1a4e5f23639a1a05.json`](../../sessions/16/168f1a4e5f23639a1a05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## FK Signal 结果

数据已存在于 `llama_fewnerd_s{42,123,456}/report.json` 中，无需补算。

### FK ρ (full, correlation_fleiss_vs_f1_full)

| Seed | FK ρ |
|------|------|
| seed42 | 0.357 |
| seed123 | 0.319 |
| seed456 | 0.173 |
| **3-seed mean** | **0.283 ± 0.097** |

### FK ρ (conditional, correlation_fleiss_vs_f1_conditional)

| Seed | FK ρ |
|------|------|
| seed42 | 0.299 |
| seed123 | 0.259 |
| seed456 | 0.070 |
| **3-seed mean** | **0.209 ± 0.121** |

### FK mean (fleiss_kappa_mean)

| Seed | FK κ |
|------|------|
| seed42 | 0.520 |
| seed123 | 0.512 |
| seed456 | 0.388 |

来源: **已有**（`output/llama_fewnerd_s{42,123,456}/report.json`）

注意：seed456 的 FK ρ 明显低于另两个 seed（full 0.173 vs 0.357/0.319），导致方差较大。Table 5 填值时可能需要注意这一点。

---
