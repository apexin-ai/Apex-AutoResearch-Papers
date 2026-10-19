# code phase0 fallback

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase0-fallback_20260515T052517_result.json`
- **Structured JSON:** [`cc79e60ea3918b12333e.json`](../../sessions/cc/cc79e60ea3918b12333e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查和 `--help` 均通过。

---

**脚本路径**: `/root/temp-adv-distill-vla/phase0_mlp_progress_predictor.py` (661 行)

**功能**:
- 对 layer 15/22/31 各训练一个 3-layer MLP (4096→512→128→1+Sigmoid)，预测归一化时间步 t/T
- 数据按轨迹 80/20 划分（非 timestep），避免数据泄漏
- Early stopping (patience=10)，评估 R²/MAE，输出散点图和训练曲线
- 任一层 test R² > 0.8 → Gate 1(b) PASSED
- 结果输出到 `artifacts/gate1b_results.json`

**与 phase0_feature_validation.py 的集成**:
- **模式 1**: `--features_dir artifacts/extracted_features/` 从已保存的 `.pt` 文件加载（秒级启动）
- **模式 2**: 不传 `--features_dir` 时自动加载模型重新提取特征，并保存到 `artifacts/extracted_features/` 供后续复用
- phase0_feature_validation.py 目前不保存中间特征。当 (a) 失败触发 (b) 时有两个选择：让 (b) 自行提取（用 `--device cuda:1` 不冲突），或后续给 (a) 加特征保存功能

**前置条件**:
- 已装 `scikit-learn`（刚装好）
- 模型在 `/root/temp-adv-distill-vla/models/openvla-7b-finetuned-libero-spatial`
- LIBERO 数据在 `/root/temp-adv-distill-vla/data/libero`
- 默认用 `cuda:1`，与 phase0_feature_validation.py (`cuda:0`) 不冲突

---
