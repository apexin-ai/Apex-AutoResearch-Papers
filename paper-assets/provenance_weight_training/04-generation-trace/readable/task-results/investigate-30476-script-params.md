# investigate 30476 script params

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_30476_script_params_20260517T125045_result.json`
- **Structured JSON:** [`58470aefd5f3f64204b2.json`](../../sessions/58/58470aefd5f3f64204b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## pretrain_weighted.py 支持的关键参数

| 参数 | 支持 |
|---|---|
| `--save_steps` | 支持 |
| `--dataloader_num_workers` | **不支持**（使用 `parser.parse_args()` 严格解析，会报错） |
| `--save_total_limit` | 支持 |
| `--save_only_model` | 支持 |
| `--gradient_checkpointing` | 支持 |
| `--bf16` / `--no_bf16` | 支持 |
| `--adaptive_tau` / `--tau_delta` / `--tau_min` | 支持 |
| `--shuffle_scores` | 支持 |
| `--resume_from_checkpoint` | 支持 |

## 脚本修改结果

**4 个脚本均已移除 `--dataloader_num_workers 0`**（原脚本全都有此参数，会导致启动失败）。

`--save_steps 200` 原已存在于全部 4 个脚本，无需修改。

| 脚本 | save_steps | dataloader_num_workers | 状态 |
|---|---|---|---|
| `run_random_reweight_seed123.sh` | 200 | 已移除 | 就绪 |
| `run_bs8_auto_nmin_seed42.sh` | 200 | 已移除 | 就绪 |
| `run_batch_adaptive_tau_rho06_seed42.sh` | 200 | 已移除 | 就绪 |
| `run_rho02_adaptive_tau09_seed42.sh` | 200 | 已移除 | 就绪 |

## Registry 清理

| exp_id | 原状态 | 现状态 |
|---|---|---|
| `random_reweight_seed123_r3` | PREPARING | DONE (conclusion=failed) |
| `rho02_adaptive_tau09_r4` | PREPARING | DONE (conclusion=failed) |
| `bs8_auto_nmin_r4` | 不存在 | — |
| `batch_adaptive_tau_rho06_r4` | 不存在 | — |

**根因**：上一个 Worker 提交时脚本包含 `--dataloader_num_workers 0`，`pretrain_weighted.py` 不识别该参数导致立即退出。现已修复，4 个脚本可以重新提交。

---
