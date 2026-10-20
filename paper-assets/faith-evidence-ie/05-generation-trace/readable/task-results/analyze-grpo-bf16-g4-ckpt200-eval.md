# analyze grpo bf16 g4 ckpt200 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grpo_bf16_g4_ckpt200_eval_20260518T225559_result.json`
- **Structured JSON:** [`09dc5a841f4f17c6da41.json`](../../sessions/09/09dc5a841f4f17c6da41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常完成，EXIT_CODE=0。

## 结果

| 指标 | ckpt-200 | ckpt-100 | Δ |
|------|----------|----------|---|
| ign_f1 | **0.4446** | 0.4431 | **+0.15pp** |
| f1 | **0.4513** | 0.4511 | **+0.02pp** |
| evi_f1 | **0.8053** | 0.8010 | **+0.43pp** |
| evi_f1_joint | **0.3562** | 0.3532 | **+0.30pp** |
| EDCR | **0.6489** | 0.6453 | **+0.36pp** |

## 与 SFT baseline 对比
- ign_f1 vs SFT baseline (0.4036): **+4.10pp**

## 其他指标
- Format OK: 984/985 (99.9%)
- Truncated: 204/985
- Predictions: 15733
- field_compliance_rate: 79.2%

## 判断
- **学习曲线：轻微改善。** ckpt-200 相比 ckpt-100 所有指标均有小幅提升，但增量很小（ign_f1 仅 +0.15pp），说明 step 100→200 阶段模型接近收敛。
- **vs SFT baseline：显著提升。** GRPO ign_f1 比 SFT baseline 高 4.1pp，证据质量指标（evi_f1、EDCR）也处于较高水平。
- **完成状态：正常。** EXIT_CODE=0，无 error，0 errors in inference。

---
