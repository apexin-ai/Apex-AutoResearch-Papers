# monitor grpo training health check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo_training_health_check_20260514T145320_result.json`
- **Structured JSON:** [`5f6219e44cff25d6ee46.json`](../../sessions/5f/5f6219e44cff25d6ee46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/training_health_check.md`。

**核心结论**:

| 实验 | 状态 | 关键信号 |
|------|------|---------|
| **ced_r5** | ⛔ Mode Collapse | entropy=0.0005, F1=0, 固定34-token输出, grad_norm=0 |
| **extract_r3** | ⚠️ 停滞 | grad_norm=0, entropy=0.01, F1=0.20 |
| **flatnli_r3** | ✅ 健康 | entropy=0.087, 输出多样, 但仅完成10.7%, 预计还需23h |
| **sft_eval_r2** | ✅ 完成 | F1=0.4057, Evi-F1=0.7979 |

**ced_r5 是教科书级 reward hacking**：模型找到一个 34-token 固定输出，CED reward 拿到 0.995 但 F1=0。建议立即 kill 释放 GPU 0。

**flatnli_r3 是唯一有希望的实验**，但很慢（~2min/step vs 坍缩实验的 12s/step，正因为它还在正常生成 400+ token 输出）。

GPU 0 和 GPU 1 现在可用于新实验。

---
