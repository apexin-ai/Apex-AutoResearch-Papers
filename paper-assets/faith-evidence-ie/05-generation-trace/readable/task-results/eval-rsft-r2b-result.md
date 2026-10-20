# eval rsft r2b result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rsft_r2b_result_20260515T114356_result.json`
- **Structured JSON:** [`4e042d5ee53f75f416bc.json`](../../sessions/4e/4e042d5ee53f75f416bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp2_eval_rsft_r2b 结果

**Pass** — 两项核心指标均超过 SFT baseline。

| 指标 | r2b (本次) | r1 (3ep, seed=42) | SFT baseline | r2b vs r1 |
|------|-----------|-------------------|-------------|-----------|
| rel_f1 | **0.4493** | 0.4449 | 0.4057 | +0.44pp |
| evi_f1 | **0.8128** | 0.8187 | 0.7979 | -0.59pp |
| edcr | 0.6609 | — | — | — |
| pred_count | 14829 | — | — | — |
| format_ok | 983/985 (99.8%) | — | — | — |
| truncated | 179/985 | — | — | — |

### 对比分析

r2b（1 epoch, alpha=32, lr=1e-5, clean data）vs r1（3 epoch, seed=42）：

- **rel_f1**: r2b 略优 (+0.44pp)，说明保守 LoRA scaling (alpha=32) + 低学习率在关系抽取上不仅没有退化，反而略好
- **evi_f1**: r2b 略低 (-0.59pp)，差距很小，可能是 1 epoch 训练不足导致证据定位能力稍弱
- 总体来看，r2b 用 1/3 的训练量达到了与 r1 接近甚至略好的效果，保守配置是有效的

Registry 已更新为 DONE/success，cron 已删除。

---
