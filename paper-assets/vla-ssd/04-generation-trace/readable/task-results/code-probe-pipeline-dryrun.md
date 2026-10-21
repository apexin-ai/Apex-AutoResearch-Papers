# code probe pipeline dryrun

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe-pipeline-dryrun_20260515T131837_result.json`
- **Structured JSON:** [`021a6bac7b9ea1f610bc.json`](../../sessions/02/021a6bac7b9ea1f610bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Dry-run 验证报告

### 1. Features 格式兼容性：✅ 完全兼容

| 项目 | 实际值 | 脚本期望 | 状态 |
|------|--------|----------|------|
| 文件数 | 10 个 H5 | `glob("*.h5")` | ✅ |
| 每文件 demos | 50 (`demo_0`..`demo_49`) | `sorted(f.keys())` | ✅ |
| Feature keys | `image_mean`, `last_preaction` | AGG_MAP 定义的 primary key | ✅ |
| Shape | `(T, 33, 4096)` float16 | `is_3d=True`, `n_layers=33`, `hidden_dim=4096` | ✅ |
| T 范围 | 203–457 | 无限制 | ✅ |

### 2. Probe 训练 Pipeline：✅ 端到端跑通

Dry-run 参数：`--layers 0,16,32 --epochs 2 --pairs_per_bin 5`

| Layer | pooled ρ | per-task mean ρ | R² | 耗时 |
|-------|----------|-----------------|-----|------|
| 0 | 0.000 | 0.000 | -0.001 | 24s |
| 16 | 0.699 | 0.707 | 0.378 | 28s |
| 32 | 0.673 | 0.710 | 0.371 | 22s |

- `scan_features` → `split_by_task` → `sample_pairs` → `load_layer_features` → `train_regression_probe` → `save_results` 全链路正常
- 输出文件：`layer_*.json` + `summary.csv` + `summary.json`，格式正确
- `best_layer` 选择用 `per_task_mean_rho`（D002 确认），summary.json 中 `best_layer=32, best_rho=0.710`
- Layer 0 的 ConstantInputWarning 是 2 epoch 训练不足导致，非 bug

### 3. analyze_results.py 输入期望：✅ 确认

- 输入：`--results_dirs trained:path,untrained:path,dinov2:path`，读取各目录下 `{probe_type}/summary.json`
- **DINO_GATE_THRESHOLD = 0.554**（per-task mean ρ）
- 判定逻辑：
  - **PASS**：permutation test p < 0.05 且 VLA mean ρ ≥ 0.554
  - **CONDITIONAL**：接近通过但有 contribution warning（VLA-DINO delta < 0.05）
  - **FAIL**：permutation test 不显著 或 VLA 低于 DINO gate

### 4. Control B（cross-trajectory shuffle）：✅ 就绪

- 非独立脚本，集成为 `train_probes.py --shuffle_cross_trajectory` 参数
- 实现完整：`sample_cross_trajectory_pairs()` + `build_cross_pair_tensors()` 均在 train_probes.py 中
- 运行方式：在正常 probe 训练命令后加 `--shuffle_cross_trajectory`

### 5. 发现的问题

**无 blocker。** 唯一注意事项：
- 脚本无 `--dry_run` 或 `--max_demos` 参数（用 `--layers` + `--epochs` + `--pairs_per_bin` 可替代限制）
- 完整训练（33 layers × 50 epochs）预估 ~33 × 24s × 25 ≈ 5.5 小时（单 GPU）

### 6. 完整 Probe 训练命令

```bash
# trained features — temporal distance
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/vla-ssd

nohup python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained/ \
  --probe_type temporal_distance \
  --gpu 0 \
  > /tmp/probe_trained_td.log 2>&1 &

# untrained features — temporal distance（等 untrained 提取完成后启动）
nohup python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ \
  --probe_type temporal_distance \
  --gpu 1 \
  > /tmp/probe_untrained_td.log 2>&1 &

# Control B（与正常训练并行或之后）
nohup python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained_controlB/ \
  --probe_type temporal_distance \
  --shuffle_cross_trajectory \
  --gpu 0 \
  > /tmp/probe_controlB.log 2>&1 &

# 分析（所有 probe 完成后）
python scripts/analyze_results.py \
  --results_dirs trained:/root/autodl-tmp/vla-ssd/results/trained/,untrained:/root/autodl-tmp/vla-ssd/results/untrained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/analysis/
```

---
