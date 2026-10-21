# code d048 eval and queue

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d048_eval_and_queue_20260522T132713_result.json`
- **Structured JSON:** [`237c8bab3836c26d9673.json`](../../sessions/23/237c8bab3836c26d9673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 脚本全部创建完毕，语法检查通过。

### 汇总

**Checkpoint 路径：**

| Condition | Path | Epochs |
|-----------|------|--------|
| TG s42 | `runs/phase2_tg_s42_v7/epoch_{0,1,2}` | 3 |
| UG s42 | `runs/phase2_ug_s42/epoch_{0,1,2}` | 3 |
| LO s42 | `runs/phase2_lora_only_s42/epoch_{0,1,2}` | 3 |
| PCGrad s42 | `checkpoints/tg_v9_pcgrad_s42/epoch_{0,1,2}` | 3 |
| SS s42 (d048) | `runs/d048_ss_s42/epoch_0` | 训练中，仅 epoch_0 |
| SS fixed s42 | `checkpoints/tg_v8b_ss_fixed_s42/epoch_{0,1,2}` | 3 |
| Base s42 | 无 checkpoint（base model 直接 eval） | — |

**参数差异（已根据 `--help` 修正）：**
- `eval_phase2_gar.py` 用 `--checkpoint-dir`，`--conversations-path`，`--ar-from-fixed`
- `eval_attention_steering.py` 用 `--checkpoint`（非 `--checkpoint-dir`），`--conversations`，`--mode gen`，`--max-convs`，`--beta`，`--output-name`

**脚本清单：**
1. `scripts/d048_eval_ss_s42.sh` — SS s42 完整 eval（TF 4 组 + AR N=50 + bootstrap CI）
2. `scripts/d048_eval_existing_s42_ar_n50.sh` — 5 个已有 s42 checkpoint 的 AR N=50（Base/TG/UG/LO/PCGrad）
3. `scripts/d048_queue_runner.sh` — 自动队列执行器（train→eval 零延迟，区分 gate/base 两种 eval 路径）

---
