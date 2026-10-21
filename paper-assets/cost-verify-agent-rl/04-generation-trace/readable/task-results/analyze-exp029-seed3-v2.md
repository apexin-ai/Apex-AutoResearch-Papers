# analyze exp029 seed3 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp029_seed3_v2_20260520T225903_result.json`
- **Structured JSON:** [`306361690f581d7827fe.json`](../../sessions/30/306361690f581d7827fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。汇总：

**exp029_seed3_v2 训练结果（15/15 步完成）**

| 指标 | Step 0 (init) | Step 5 | Step 10 | Step 15 (final) |
|------|:---:|:---:|:---:|:---:|
| Val Success | 6.25% | 21.88% | 28.13% | **40.63%** |
| Val Reward@32 | 0.625 | 2.1875 | 2.8125 | **4.0625** |
| Train Success | — | 20.31% | 38.28% | **54.69%** |
| Train Pass@8 | — | 75.00% | 75.00% | **93.75%** |
| Response Length | — | 10942 | 9028 | **7505** |
| Collapse MI | — | 0.123 | 0.132 | **0.227** |

- **Checkpoints**: step 5/10/15 各 21GB，均完整（2 rank model + optimizer + tokenizer）
- **W&B Run**: `0t58u17b`，数据已存 local
- **EXIT_CODE=129**: 仅 W&B teardown BrokenPipeError，训练本身成功
- **无 collapse**：MI 持续上升

报告已写入 `artifacts/exp029_seed3_v2/report/exp029_seed3_v2_analysis.md`。

---
