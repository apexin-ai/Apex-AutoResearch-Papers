# code probe pipeline verify

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe-pipeline-verify_20260515T120918_result.json`
- **Structured JSON:** [`ba17cadbd02d531774d0.json`](../../sessions/ba/ba17cadbd02d531774d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### 各功能状态

| 功能 | 状态 | 代码路径 |
|------|------|----------|
| 多层特征支持 (33层) | **已有** | `train_probes.py` — `scan_features()` 自动检测 3D `(T,33,4096)` vs 2D `(T,1024)`，`load_layer_features()` 按层切片 |
| MLP Probe | **新写** | `train_probes.py:MLPProbe` — `1024→256→1` (ReLU)，`--probe_model mlp` 默认 |
| Adam + Early Stopping | **已有** | `train_probes.py:train_regression_probe()` — Adam lr=1e-3, patience=5 |
| Control B (cross-traj shuffle) | **已有** | `train_probes.py` — `--shuffle_cross_trajectory` flag → `sample_cross_trajectory_pairs()` + `build_cross_pair_tensors()` |
| Per-task ρ 评估 | **已有** | `train_probes.py:run_temporal_distance()` L448-460 — 每层计算 `per_task_rho` |
| Per-task mean ρ 主指标 (D002) | **新写** | `train_probes.py` — 新增 `per_task_mean_rho` 字段 + CSV 列 |
| Bootstrap CI | **已有** | `analyze_results.py:bootstrap_delta_rho()` L249 — 1000 bootstrap + 10000 permutation test，95% CI |
| 可视化 & Judgment | **已有** | `analyze_results.py` — `layer_rho.png`, `delta_rho.png`, PASS/FAIL 判定 |

### 修改内容

`train_probes.py` 新增/修改：
1. `MLPProbe` 类 (in_dim → 256 → 1, ReLU)
2. `--probe_model` 参数 (默认 `mlp`，可选 `linear`)
3. `per_task_mean_rho` 作为每层的聚合指标
4. CSV summary 增加 `per_task_mean_rho` 列

### Dry-run 结果 (DINO-V2)
- Pooled ρ = 0.609, **per_task mean ρ = 0.619**
- 10 tasks 全部有评估结果，rho 范围 [0.39, 0.78]

### 提取进度
- trained: **8/10** tasks 完成
- untrained: **8/10** tasks 完成
- 剩余: LIVING_ROOM_SCENE6, STUDY_SCENE1

### 下一步
提取完成后直接跑：
```bash
# Trained (33 layers)
python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained/ --probe_type temporal_distance --gpu 0

# Untrained (33 layers)  
python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ --probe_type temporal_distance --gpu 1

# Control B
python scripts/train_probes.py --features_dir /root/autodl-tmp/vla-ssd/features/trained/ --output_dir /root/autodl-tmp/vla-ssd/results/trained_controlB/ --probe_type temporal_distance --shuffle_cross_trajectory --gpu 0
```

---
