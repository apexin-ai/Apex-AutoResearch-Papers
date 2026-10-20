# analysis cross domain paired bootstrap

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross-domain-paired-bootstrap_20260514T220535_result.json`
- **Structured JSON:** [`b19501cdc71ba6a24fcf.json`](../../sessions/b1/b19501cdc71ba6a24fcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。结果已存在于 `paired_bootstrap_v2.py` 的输出中，经验证方法论正确。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| GB macro_f1 (OH test) | 0.6936 |
| Probe macro_f1 (OH test) | 0.7512 |
| Delta | -5.76pp |
| 95% CI | [-6.87, -4.65] |
| p-value | < 0.001 |

Probe 在跨域 OH test split 上显著优于 Structural GB。GB 从全量 OH 的 0.9674 跌至 test split 的 0.6936，说明其在 instance-level test split 上泛化能力弱于 Probe。

Artifact 已注册：`art_20260514_d7de6a`

---
