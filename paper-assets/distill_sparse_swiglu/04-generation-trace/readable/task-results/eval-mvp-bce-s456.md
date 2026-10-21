# eval mvp bce s456

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_bce_s456_20260515T135408_result.json`
- **Structured JSON:** [`d72d4eb4b5eccbdd9536.json`](../../sessions/d7/d72d4eb4b5eccbdd9536.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

mvp_bce_s456 评估完成，registry 已更新。结果汇总：

| 指标 | s456 | s123 (参考) |
|------|------|-------------|
| Dense PPL | 28.14 | 28.38 |
| Sparse PPL | **42.54** | 44.83 |
| PPL increase | **51.2%** | 57.9% |
| Model sparsity | 0.498 | 0.498 |

s456（seed=456）比 s123 表现更好，sparse PPL 低 2.29 点，PPL 增幅少 6.7 个百分点。Per-layer sparsity 分布符合预期：浅层 ~0.44-0.49，深层逐渐增大到 ~0.65。

注：C4 评估因 AutoDL 网络 streaming 卡死被跳过，仅完成 WikiText-2 评估。

---
