# prep 14b eval and grpo step100

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_14b_eval_and_grpo_step100_20260518T133200_result.json`
- **Structured JSON:** [`1e680b7500470d5ae079.json`](../../sessions/1e/1e680b7500470d5ae079.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均通过语法验证。

## 产出总结

### 脚本就绪
- **`/root/autodl-tmp/freige/scripts/eval_14b.sh`** — 14B eval，支持环境变量配置 `MODEL_PATH`/`SFT_ADAPTER`/`OUTPUT_DIR`/`SPLIT`，默认 model_path=sft_output_14b，batch_size=4
- **`/root/autodl-tmp/freige/scripts/eval_grpo_step100.sh`** — GRPO step 100 eval，硬编码 checkpoint-100 路径，含 checkpoint 存在检查，batch_size=4

两个脚本均需在运行时加 `CUDA_VISIBLE_DEVICES=X` 前缀（遵循 C002）。

### GRPO 训练进度
| 指标 | 值 |
|---|---|
| 当前进度 | step 22/200 |
| checkpoint 保存频率 | 每 20 步（save_steps=20） |
| 平均步耗时 | ~126s/step |
| 训练开始时间 | 20:45 (May 18) |
| **step 100 预计时间** | **~00:15 (May 19)**，距现在约 2h45m |
| reward 趋势 | 1.37 → 1.60（step 5→20，上升中） |

checkpoint-100 会自动保存（100 是 20 的倍数）。

---
