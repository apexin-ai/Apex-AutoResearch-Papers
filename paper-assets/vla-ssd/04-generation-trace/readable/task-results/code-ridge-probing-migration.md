# code ridge probing migration

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ridge_probing_migration_20260521T050309_result.json`
- **Structured JSON:** [`11f781cbed8e260508a5.json`](../../sessions/11/11f781cbed8e260508a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个环境 RidgeCV import 均通过。

## 完成总结

### 修改了 7 个文件

| # | 文件 | 修改内容 |
|---|------|---------|
| 1 | `libero_object_full_pipeline.py` | import + run_probing |
| 2 | `nora_goal_full_pipeline.py` | import + run_probing |
| 3 | `nora_spatial_full_pipeline.py` | import + run_probing |
| 4 | `tracvla_spatial_full_pipeline.py` | import + run_probing |
| 5 | `tracvla_object_full_pipeline.py` | import + run_probing |
| 6 | `libero_long_full_pipeline.py` | import + run_probing |
| 7 | `tracvla_spatial_probing_only.py` | import + run_probing |

### 每个文件的具体修改

1. **Import**: `from sklearn.neural_network import MLPRegressor` → `from sklearn.linear_model import RidgeCV`
2. **run_probing 函数**:
   - MLPRegressor(hidden_layer_sizes=(256,), ...) → RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])
   - 去掉 15-seed 循环，改为单次 train/test split（固定 random_state=42）
   - R² 计算方式不变（全局 ss_res/ss_tot，保持与 MLP 版本可比性）
   - 输出 JSON 格式不变：`{"mean": X, "std": 0.0, "values": [X]}`
3. **Docstring**: `per-layer MLP probe, 15 seeds` → `per-layer Ridge probe`

### 验证结果

- conda base 环境：RidgeCV OK
- NORA venv 环境：RidgeCV OK

### 重提交命令

**cuda:0 — OpenVLA Object:**
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
```

**cuda:1 — NORA Goal:**
```bash
bash -c "source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate && python /root/autodl-tmp/vla-ssd/scripts/nora_goal_full_pipeline.py --conditions trained untrained"
```

---
