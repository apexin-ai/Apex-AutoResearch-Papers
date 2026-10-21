# ssh verify persist 5epoch recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_persist_5epoch_recompute_20260521T220719_result.json`
- **Structured JSON:** [`febdb7b624ce108ad22b.json`](../../sessions/fe/febdb7b624ce108ad22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 持久化验证

| seed | output/ | artifacts/ | size |
|------|---------|------------|------|
| s42 | ✓ (autodl-5090) | ✓ 已创建 | 902 bytes |
| s123 | ✓ (autodl-5090) | ✓ 已创建 | 905 bytes |
| s456 | ✓ (autodl-5090-c) | — (不同服务器，未复制) | 904 bytes |

## 文件内容摘要

| seed | greedy_f1 | mv_strict_f1 | mv_incl_f1 | oracle_f1 | Δ_SC strict | Δ_SC incl | δ(degen) |
|------|-----------|-------------|-----------|-----------|-------------|-----------|----------|
| s42 | 0.7980 | 0.7935 | 0.7968 | 0.8781 | -0.45pp | -0.12pp | 25.7% |
| s123 | 0.7976 | 0.7941 | 0.7984 | 0.8814 | -0.35pp | +0.08pp | 27.1% |
| s456 | 0.7978 | 0.7950 | 0.7980 | 0.8793 | -0.28pp | +0.02pp | 25.9% |

所有文件内容完整，包含人类可读摘要和 JSON 结构化数据。s42/s123 已复制到 `artifacts/exp_fewnerd_5epoch_s{42,123}/`。s456 在 autodl-5090-c 的 `output/` 中存在，未做跨服务器复制。

---
