# code prep next wave 47453

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_next_wave_47453_20260516T190207_result.json`
- **Structured JSON:** [`0d56efdab1dfc5e24c51.json`](../../sessions/0d/0d56efdab1dfc5e24c51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部就绪。汇总：

| 脚本 | 路径 | 目标 GPU | 数据 | 关键参数 |
|------|------|----------|------|----------|
| `run_batch_adaptive_tau_rho06_seed42.sh` | `/root/provenance_weight_training/scripts/` | cuda:2 | scored_data_rho06.jsonl (371499行) | tau=0.7, adaptive_tau, tau_delta=0.3, tau_min=0.5, n_min=2, ρ=0.6 |
| `run_rho02_adaptive_tau09_seed42.sh` | 同上 | cuda:1 | scored_data_rho02.jsonl (206111行) | tau=0.9, n_min=2, ρ=0.2 |
| `run_bs8_auto_nmin_seed42.sh` | 同上 | cuda:3 | scored_data.jsonl (ρ=0.4) | bs=8, grad_accum=2, n_min=auto(4), tau=0.8 |

**通用确认：**
- ✅ WANDB_MODE=disabled（无 --use_wandb）
- ✅ CUDA_VISIBLE_DEVICES=-1（submit 时改为真实 GPU）
- ✅ gradient_checkpointing=true
- ✅ seed=42
- ✅ output_dir 在 /root/autodl-tmp/output/models/
- ✅ 数据文件均已确认存在

提交时只需 `sed -i 's/CUDA_VISIBLE_DEVICES=-1/CUDA_VISIBLE_DEVICES=X/'` 即可。

---
