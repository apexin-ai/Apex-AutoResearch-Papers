# analysis eval gsm8k grpo unstructured 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_gsm8k_grpo_unstructured_20_20260519T080416_result.json`
- **Structured JSON:** [`433c3dbc4caac79da79e.json`](../../sessions/43/433c3dbc4caac79da79e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被清理），registry 已更新为 DONE。

## 结果汇总

**eval_gsm8k_grpo_unstructured_20** — DONE ✓

| 指标 | 值 |
|------|-----|
| **GSM8K Accuracy** | **87.64% ± 0.91%** |
| n_correct / n_total | 1156 / 1319 |
| EOS rate | 98.18% (仅 24 条截断) |

**对比（hypothesis 中的 baseline）：**
- Pre-GRPO unstructured 20%: 87.87% → GRPO 后 87.64%（几乎持平，Δ = -0.23%，在 stderr 内）
- Structured GRPO 对比：CKA-only 64.37%、Standard 58.91%、RASP 56.71%

GRPO 对 unstructured pruning 没有带来 GSM8K 提升（训练 reward_mean=0.883 与 eval accuracy 87.64% 一致），但 unstructured 本身远优于所有 structured 方案。

**磁盘清理**：`grpo_unstructured_20/` (~15GB) 的 eval 已完成，结果已保存。如果不再需要该 checkpoint 做进一步实验，可以安全删除以腾出空间给 seed123 训练的最终 checkpoint (~12GB)。建议确认后清理。

---
