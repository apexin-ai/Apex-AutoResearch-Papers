# ssh gpu check 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_check_41312_20260517T202225_result.json`
- **Structured JSON:** [`d1977e2fe531aaefd79f.json`](../../sessions/d1/d1977e2fe531aaefd79f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 (westd-41312)

| GPU | 实验 | PID | 状态 | 进度 | 显存 | GPU利用率 | 已运行 | 预计剩余 | 最新checkpoint |
|-----|------|-----|------|------|------|-----------|--------|----------|----------------|
| cuda:0 | uniform_seed42_v2 | 125995 | **运行中** | 3569/6103 (**58%**) | 46.5G/97.9G | 100% | ~2h05m | ~1h29m | checkpoint-3500 |
| cuda:1 | ess_only_seed456 | 115525 | **运行中** | 4884/8477 (**58%**) | 75.0G/97.9G | 78% | ~25m (从eval后) | ~18m35s | checkpoint-2000 |
| cuda:2 | ess_only_seed123 | 115021 | **运行中** | 5500/8477 (**65%**) | 75.0G/97.9G | 100% | ~28m25s (从eval后) | ~15m20s | checkpoint-2000 |
| cuda:3 | random_reweight_seed456 | 125367 | **运行中** | 1135/6103 (**19%**) | 75.0G/97.9G | 95% | ~2h08m | ~2h54m | checkpoint-1000 |

### 关键观察

1. **所有 4 个实验都在正常运行**，无异常。

2. **ess_only 两个实验** (seed123/456) 的 total steps 是 8477（含 inline eval），步速 ~3.2 it/s，比 uniform/random 的 ~2.1s/it 快很多（因为 uniform_v2 没有 eval_data_path，random 有更复杂的 weighting 计算）。

3. **预计完成时间**（粗估）：
   - ess_only_seed123: ~15min 后完成
   - ess_only_seed456: ~19min 后完成
   - uniform_seed42_v2: ~1.5h 后完成
   - random_reweight_seed456: ~2.9h 后完成（启动最晚，进度最少）

4. **Checkpoint 路径**：
   - `/root/autodl-tmp/provenance_weight_training/output/models/qwen06b_uniform_seed42_v2/`
   - `/root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456/`
   - `/root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123/`
   - `/root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed456/`

5. **注意**: uniform_seed42_v2 的 output_dir 实际是 `qwen06b_uniform_seed42_v2`（不是 `uniform_seed42`），且没有 `--eval_data_path` 参数（无 inline eval）。

---
