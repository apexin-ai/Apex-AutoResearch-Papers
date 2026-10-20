# code prep next batch scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_next_batch_scripts_20260516T144847_result.json`
- **Structured JSON:** [`6d3b9a28c0d2b776017b.json`](../../sessions/6d/6d3b9a28c0d2b776017b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。最后确认 `run_random_reweight_v2.sh` —— 上面搜索确认不存在。

汇总：

| 脚本 | 状态 |
|------|------|
| `run_rho02_adaptive_tau09.sh` | **新建** — adaptive, τ=0.9, n_min=2, ρ=0.2 数据 |
| `run_batch_adaptive_tau_rho06.sh` | **新建** — adaptive + `--adaptive_tau`, ρ=0.6 数据 |
| `run_bs8_auto_nmin.sh` | **新建** — adaptive, bs=8, n_min=4, grad_accum=2, ρ=0.4 数据 |
| `run_random_reweight_v2.sh` | **不存在**，服务器上未找到 |

验证结果：
- `CUDA_VISIBLE_DEVICES=-1` — 3/3 通过
- `WANDB_MODE=disabled` — 3/3 通过，无 `--use_wandb` / `--wandb_project` / `--wandb_run_name`
- `output_dir` 全在 `/root/autodl-tmp/output/models/` — 3/3 通过
- 所有脚本含 `gradient_checkpointing`、`bf16`、`eval_data_path`

`run_random_reweight_v2.sh` 需要单独创建，当前不在服务器上。

---
