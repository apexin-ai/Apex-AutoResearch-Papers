# diagnose eval rsft r2a

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_rsft_r2a_20260515T114602_result.json`
- **Structured JSON:** [`b04724e6468b4c2f075a.json`](../../sessions/b0/b04724e6468b4c2f075a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**mvp2_eval_rsft_r2a → DONE (success)**

| 指标 | r2a | r1 (3ep) | r2b (1ep,α=32) | SFT baseline |
|------|-----|----------|-----------------|-------------|
| rel_f1 | **0.4494** | 0.4449 | 0.4493 | 0.4057 |
| evi_f1 | 0.8108 | **0.8187** | 0.8128 | 0.7979 |
| edcr | 0.6641 | — | 0.6609 | **0.7118** |

关键发现：1 epoch + clean data (r2a) 的 rel_f1 与 3 epoch (r1) 持平甚至略高，说明多 epoch 训练在 clean data 上收益有限。r2a 和 r2b 的 rel_f1 几乎相同，alpha=128 vs 32 对关系抽取影响不大，但高 alpha 在 edcr 上略优。所有 RSFT 变体的 edcr 均低于 SFT baseline（0.66 vs 0.71）。

- Registry: status=DONE, conclusion=success, metrics/notes 已更新
- Cron: 已删除

---
