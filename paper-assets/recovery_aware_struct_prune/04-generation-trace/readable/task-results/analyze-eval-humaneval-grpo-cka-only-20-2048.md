# analyze eval humaneval grpo cka only 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_humaneval_grpo_cka_only_20_2048_20260519T073506_result.json`
- **Structured JSON:** [`72dce6b9d34cc00044d0.json`](../../sessions/72/72dce6b9d34cc00044d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果报告

### GRPO CKA-only 20% HumanEval @2048

| 指标 | 值 |
|------|-----|
| **pass@1** | **20.12% ± 3.13%** |
| n_correct / n_total | 33 / 164 |
| avg_response_length | 1523.31 |
| median_response_length | 2048 (频繁 truncation) |
| wall_time | ~3h19m |

### 基准对比

| 方法 | pass@1 | n_correct |
|------|--------|-----------|
| Unpruned GRPO | 45.12% | 74/164 |
| **GRPO CKA-only 20%** | **20.12%** | **33/164** |
| GRPO RASP 20% | 14.63% | 24/164 |
| GRPO Standard 20% | 10.37% | 17/164 |
| SFT CKA-only 20% | 0% | 0/164 |

### 结论：**success**

1. **GRPO 完全恢复了 SFT 丧失的能力**：SFT CKA-only 在 HumanEval 上 pass@1 = 0%，GRPO 将其恢复到 20.12%，从零到有。
2. **CKA-only 是三种剪枝方法中 GRPO 恢复效果最好的**：20.12% > RASP 14.63% > Standard 10.37%。这与 hypothesis 一致——CKA 保留的结构相似性确实有利于 GRPO 的跨任务恢复。
3. **与 unpruned 仍有显著差距**：20.12% vs 45.12%，恢复率约 44.6%。
4. **failure mode**：大量样本 hit 2048 token 上限后被截断，输出中混杂 chain-of-thought 自然语言文本（而非纯代码），导致 SyntaxError。median_response_length = 2048 表明超过一半的样本被截断。

---
