# code phase3 probe prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase3-probe-prep_20260515T131841_result.json`
- **Structured JSON:** [`f6ab33989c7f0b93285f.json`](../../sessions/f6/f6ab33989c7f0b93285f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有检查完成。以下是完整报告和执行计划。

---

## 1. D003/D004 代码对齐验证 ✅

### train_probes.py
- **best_layer 选择**: line 607 — `max(results, key=lambda k: results[k]["per_task_mean_rho"])` ✅ D002
- **per_task_mean_rho 计算**: line 491 — `np.mean(valid_rhos)` per task ✅
- **输出格式**: `per_task_rho`, `per_task_mean_rho`, `per_task_n_pairs` 全部输出 ✅ (dry-run 验证)

### analyze_results.py
- **DINO_GATE_THRESHOLD** = 0.554 (line 268) ✅
- **PASS**: `rho_pass` (per-task mean ρ > 0.5) AND `delta_pass` (Δρ > 0.1, bootstrap CI excludes 0, permutation p < 0.05) AND VLA per-task mean ρ ≥ 0.554 ✅
- **CONDITIONAL**: `rho_pass` AND `delta_pass` but VLA < 0.554 ✅
- **FAIL**: !rho_pass OR !delta_pass ✅
- **subtask AUC**: 补充分析，不参与 gate (line 378 注释) ✅
- **bootstrap_delta_rho**: 1000 bootstrap + 10000 permutation test (lines 268-304) ✅

## 2. Features 数据就绪 ✅

| 目录 | 文件数 | Demos/task | Shape | dtype | 大小 |
|------|--------|------------|-------|-------|------|
| trained/ | 10/10 | 50 | (T, 33, 4096) | float16 | 53G |
| untrained/ | 10/10 | 50 | (T, 33, 4096) | float16 | 54G |
| dinov2/ | 10/10 | 50 | (T, 1024) | float16 | 503M |

磁盘: 95GB 可用 ✅

## 3. 已有结果

| 结果 | 状态 | 备注 |
|------|------|------|
| dinov2/temporal_distance | ⚠️ 旧代码 | 缺 per_task_rho，需重跑 |
| dinov2_shuffle (Control B) | ✅ | 有 per_task_rho，rho=0.650 |
| dinov2/subtask_predicate | ✅ | macro_AUC=0.972 |
| oracle | ✅ | rho=1.0 |

## 4. 发现的问题

**DINO temporal_distance 需重跑** — 旧代码生成，无 `per_task_rho`。DINO gate 本身是固定阈值 0.554 不受影响，但 `delta_vla_dino` contribution warning 需要真实 DINO per_task_mean_rho。重跑仅 1 层，~10s。

## 5. Phase 3 完整执行计划

### 时间估算基准
- dry-run: 1 layer × 5 epochs = 30s → ~6s/epoch
- 预计每层 10-20 epochs (early stopping) → 60-120s/layer
- 33 layers → **~35-65 min/model**

---

### Step 0: 重跑 DINO temporal_distance (~10s)
```bash
cd /root/vla-ssd && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python3 scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ \
  --probe_type temporal_distance \
  --gpu 0 --seed 42
```

### Step 1+2: Trained + Untrained probes (并行, ~35-65 min)
```bash
# GPU 0: Trained probes (33 layers)
nohup python3 scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained/ \
  --probe_type temporal_distance \
  --gpu 0 --seed 42 \
  > /tmp/train_trained.log 2>&1 &
echo "TRAINED_PID=$!"

# GPU 1: Untrained probes (33 layers)
nohup python3 scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ \
  --probe_type temporal_distance \
  --gpu 1 --seed 42 \
  > /tmp/train_untrained.log 2>&1 &
echo "UNTRAINED_PID=$!"
```

### Step 3: Control B — cross-trajectory shuffle (等 Step 1+2 完成后, ~35-65 min)
```bash
# GPU 0: Trained Control B
nohup python3 scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained_shuffle/ \
  --probe_type temporal_distance \
  --shuffle_cross_trajectory \
  --gpu 0 --seed 42 \
  > /tmp/train_trained_shuffle.log 2>&1 &

# GPU 1: Untrained Control B
nohup python3 scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/untrained_shuffle/ \
  --probe_type temporal_distance \
  --shuffle_cross_trajectory \
  --gpu 1 --seed 42 \
  > /tmp/train_untrained_shuffle.log 2>&1 &
```

### Step 4: Verdict 分析 (等全部完成, ~1 min)
```bash
python3 scripts/analyze_results.py \
  --results_dirs "trained:/root/autodl-tmp/vla-ssd/results/trained/,untrained:/root/autodl-tmp/vla-ssd/results/untrained/,dinov2:/root/autodl-tmp/vla-ssd/results/dinov2/" \
  --output_dir /root/autodl-tmp/vla-ssd/results/analysis/ \
  --probe_type temporal_distance
```

### 总耗时估算
| 步骤 | 时间 | GPU |
|------|------|-----|
| Step 0: DINO 重跑 | ~10s | 0 |
| Step 1+2: trained + untrained (并行) | ~35-65 min | 0+1 |
| Step 3: Control B trained + untrained (并行) | ~35-65 min | 0+1 |
| Step 4: analyze_results | ~1 min | CPU |
| **总计** | **~70-130 min** | |

### 注意事项
- `--shuffle_cross_trajectory` 和 `--shuffle_labels` 已内置在 `train_probes.py` 中，无需独立脚本 ✅
- Control B output 存到独立目录 (`*_shuffle/`)，不覆盖正常结果
- `--seed 42` 是默认值，显式指定确保可复现
- Step 1+2 可立即开跑，数据和代码全部就绪

---
