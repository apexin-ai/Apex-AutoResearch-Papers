# research rf training data check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rf_training_data_check_20260517T185217_result.json`
- **Structured JSON:** [`e7dccb4174de92433d13.json`](../../sessions/e7/e7dccb4174de92433d13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部确认。

## 结论

### RF Baseline (66.4%)
- **训练脚本**: `src/cross_model_loo.py`
- **数据**: 9 cells × 20,000 = 180,000 总样本 (4-class: d0/d1/d2/d3, 每类 5,000/cell)
- **评估**: Leave-one-model-out, 每折训练 6 cells = **120,000 samples**, 测试 3 cells = 60,000
- **Per-model accuracy**: Pythia=62.4%, OLMo=69.2%, GPT2-XL=67.6%
- **Mean = 66.4%**
- RF 参数: `n_estimators=200, random_state=42`

### Learned Estimator (Plan 025: XGBoost/OrdinalMLP/Prototypical)
- **训练脚本**: `scripts/learned_estimator_train.py`
- **数据**: 同样的 9 cells, 同样的 `load_cross_model_split`
- **每折训练**: **120,000 samples** (sweep_summary.json 中所有结果确认)
- `--max_samples` 默认 = 0 (全量), `run_learned_estimator_all.sh` 未指定该参数
- **Best mean accuracy**: XGBoost = 67.2%

### Apple-to-apple?
**是。** 两者使用完全相同的:
- 9 个 feature 文件 (每个 20,000 行, 无 depth>3 数据)
- 相同的 leave-one-model-out split (120k train / 60k test)
- 相同的 19 个 statistical features

唯一差异是模型本身 (RF n=200 vs XGBoost n=500 / MLP / ProtoNet)。数据量完全一致，可直接对比。

---
