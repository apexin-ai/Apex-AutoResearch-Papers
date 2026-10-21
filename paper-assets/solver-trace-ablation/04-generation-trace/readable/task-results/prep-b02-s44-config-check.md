# prep b02 s44 config check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_b02-s44-config-check_20260516T043159_result.json`
- **Structured JSON:** [`3661f2b0cb14a69242bd.json`](../../sessions/36/3661f2b0cb14a69242bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 预检报告

| 检查项 | 状态 | 详情 |
|--------|------|------|
| **Config b02** | 存在 | `grpo_additive_bonus_b02.yaml` — beta=0.2，其余参数与 b03 一致（同 model/data/lr/batch/steps） |
| **Config b005** | 存在 | `grpo_additive_bonus_b005.yaml`（通用）+ `sweep_isr_b005_s43.yaml`（seed=43 专用，output_dir 已设好） |
| **classify_h7.py** | 就绪 | 支持 `--eval_path`、`--batch`、`--json_out`，检测 H7a/H7b/H1/H8 |
| **b02-s43 进度** | step 138/500 | PID 633515 alive, 运行 22h, checkpoint-100 已存 |
| **b02-s42 进度** | step 158/500 | PID 633657 alive, 运行 22h, checkpoint-150 已存 |

**ETA 估算**: ~7 steps/hour → 还需 ~48h（b02-s43）/ ~49h（b02-s42）才能完成 500 步。

**注意事项**:
- b02 config 的默认 seed=42、output_dir 指向 `sweep_isr_b02_s42`，提交 b02-s44 时需要 CLI 覆盖 `--seed 44 --output_dir /root/autodl-tmp/outputs/sweep_isr_b02_s44`（没有找到 b02-s44 的专用 config）
- b005-s43 有专用 config `sweep_isr_b005_s43.yaml`，可直接使用
- 代码根目录在 `/root/solver-trace-ablation/`，不是 `/root/autodl-tmp/solver-trace-ablation/`

**就绪评估**: configs 和分析脚本全部就绪。b02-s44 缺专用 config（可 CLI 覆盖或创建）。当前 b02 两个 run 预计还需 ~2 天才完成，下一批需等 GPU 释放。

---
