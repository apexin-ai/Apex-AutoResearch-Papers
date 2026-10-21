# analysis eval sft cka only 20 n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_sft_cka_only_20_n1319_20260517T234752_result.json`
- **Structured JSON:** [`7ee1fd6efa9aa44daf68.json`](../../sessions/7e/7ee1fd6efa9aa44daf68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**eval_sft_cka_only_20_n1319 最终结果：63.91% accuracy (843/1319), ±1.32% stderr**

| Method (20%) | Post-Prune | Post-SFT (N=1319) | SFT Recovery |
|---|---|---|---|
| Standard | 17.5% | 59.7% | +42.2pp |
| RASP | 29.0% | 61.4% | +32.4pp |
| **CKA-only** | **38.5%** | **63.9%** | +25.4pp |

**Hypothesis 判断**: CKA-only post-SFT 确实最高，排序 CKA-only > RASP > Standard 在 SFT 前后一致。SFT 将 21pp spread 压缩至 4.2pp，部分均等化但未完全抹平差异。Pre-SFT 结构保留质量可预测 post-SFT ranking。

Registry 已更新（hypothesis 已补充，其余字段此前已由 on_complete hook 自动填充：status=DONE, conclusion=success, metrics 完整）。memory.md 已追加全方法对比表和分析。

---
