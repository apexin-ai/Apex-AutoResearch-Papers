# research train test overlap investigation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_train-test-overlap-investigation_20260522T235745_result.json`
- **Structured JSON:** [`ca015b23d1a9c440a291.json`](../../sessions/ca/ca015b23d1a9c440a291.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

---

## 1. ACT 训练数据
- **路径**: `/root/contrastive_entrain_calib/data/calibration_v2_1_expanded.jsonl`
- **行数**: 362 lines
- **MD5**: `b7f78a7787a21dbf67e7204c37b84877`
- **加载方式**: `run_exp004s2_act.py:153` 的 `--data-path` 参数默认值，经 `PairedCalibrationDataset` 按 `pair_id` 配对 valid_correction + invalid_pressure

## 2. Eval 数据
- **路径**: `/root/contrastive_entrain_calib/data/calibration_v2_1_expanded.jsonl`（同一文件）
- **行数**: 362 lines
- **MD5**: `b7f78a7787a21dbf67e7204c37b84877`
- **加载方式**: `eval_unified_preset.py:49` 的 `DEFAULT_DATA` 常量，`--data_path` 参数默认值，经 `load_eval_data()` 逐行加载

## 3. 是否相同
**YES — 完全相同。** ACT 训练和 eval 使用同一个文件路径，同一份 362 samples。Reviewer 的怀疑成立。

## 4. GRPO 训练数据
- **路径**: `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl`
- **行数**: 362 lines
- **MD5**: `b7f78a7787a21dbf67e7204c37b84877`
- **是否与 ACT/eval 相同**: YES — 路径不同但内容完全一致（MD5 相同）

## 5. Held-out eval 可行性

**数据结构**:
- 181 unique pair_ids × 2 conditions = 362 lines
- Domains: math(68), science(74), geography(76), history(70), commonsense(74)
- Strengths: weak(150), medium(108), strong(104)

**eval 脚本参数**: `--data_path` 已支持自定义数据文件，无需改代码

**ACT 训练脚本参数**: `--data-path` 已支持自定义数据文件，无需改代码

**需要的代码修改**: 无。只需生成两个 split 文件（train.jsonl / eval.jsonl）

**建议方案**:
- 按 pair_id 做 80/20 split → 145 train pairs (290 lines) / 36 eval pairs (72 lines)
- 按 domain × evidence_strength 分层抽样保证分布一致
- 训练时 `--data-path train_split.jsonl`，eval 时 `--data_path eval_split.jsonl`

**预估工作量**: 分钟级（写一个 split 脚本 + 重新跑 eval 即可）

---
