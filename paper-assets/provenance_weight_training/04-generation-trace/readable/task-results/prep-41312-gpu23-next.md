# prep 41312 gpu23 next

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_41312-gpu23-next_20260516T164505_result.json`
- **Structured JSON:** [`32bfcd1d35d335f58a9d.json`](../../sessions/32/32bfcd1d35d335f58a9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. hybrid 训练状态：仍在运行

| 实验 | 进度 | 当前 step | 总 steps | 已运行 | 预估剩余 |
|------|------|-----------|----------|--------|----------|
| hybrid_rho04_seed42 | 41% | 2515/6103 | 6103 | ~5h19m | ~7-8h |
| hybrid_rho06_seed42 | 43% | 2610/6103 | 6103 | ~5h19m | ~2.3h |

- 无 `final/` 目录，无 `training_completed` 标记
- 进程活跃（log 持续写入，进度条更新）
- 实际输出路径：`/root/autodl-tmp/provenance_weight_training/output/models/hybrid_rho0{4,6}_seed42/`

### 2. 下一批脚本：存在但有问题

两个脚本都存在：
- `/root/provenance_weight_training/scripts/run_batchsize16.sh` ✓
- `/root/provenance_weight_training/scripts/run_grid_b0_2_seed42.sh` ✓

**问题：**
1. **`CUDA_VISIBLE_DEVICES=-1`** — 两个脚本都设为 CPU 模式，需要改为实际 GPU ID
2. **output_dir 路径不一致** — 脚本用 `/root/autodl-tmp/output/models/...`，但 hybrid 实际输出在 `/root/autodl-tmp/provenance_weight_training/output/models/...`，建议统一

### 3. eval 脚本：存在但路径可能不匹配

两个 eval 脚本存在：
- `eval_hybrid_rho04_seed42.sh` ✓
- `eval_hybrid_rho06_seed42.sh` ✓

**问题：** eval 脚本引用的 `FINAL_PATH="output/models/${EXP_ID}/final"`（相对于 `/root/provenance_weight_training`）不是实际输出路径 `/root/autodl-tmp/provenance_weight_training/output/models/...`。需要确认训练脚本完成时是否会在该相对路径下创建 symlink 或 copy，否则 eval 会报 "final checkpoint not ready"。

### 下一步建议

1. hybrid 尚未完成，rho06 预计再 ~2h，rho04 预计再 ~7-8h
2. batchsize16 和 grid_b0_2 脚本需修正 `CUDA_VISIBLE_DEVICES` 和 `output_dir` 后才能跑
3. eval 脚本的 `FINAL_PATH` 需要和训练实际输出路径对齐

---
