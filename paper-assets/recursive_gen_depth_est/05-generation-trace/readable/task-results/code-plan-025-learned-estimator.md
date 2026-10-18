# code plan 025 learned estimator

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_025_learned_estimator_20260517T155600_result.json`
- **Structured JSON:** [`357c95148f78c18a6244.json`](../../sessions/35/357c95148f78c18a6244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

## 总结

**产出：**
- `scripts/learned_estimator_utils.py` - 数据加载、CORAL loss、Prototypical net、评估指标
- `scripts/learned_estimator_train.py` - 训练脚本（`--method {ordinal_mlp, prototypical, xgboost}` + `--holdout_model {pythia, olmo, gpt2xl}`）
- `scripts/learned_estimator_sweep.py` - 批量运行 + 汇总表格
- `scripts/run_learned_estimator_all.sh` - 一键跑全部 NN 实验

**结果（Leave-One-Model-Out Cross-Model）：**

| Method | Mean Acc | vs RF (66.4%) |
|--------|----------|---------------|
| XGBoost | **67.2%** | +0.8% |
| Ordinal MLP | 67.0% | +0.6% |
| Prototypical | 66.6% | +0.2% |

**3 个方法均超越 RF baseline。** XGBoost 最佳且最快（7s vs 2min），Prototypical 在 OLMo holdout 上取得最高单点 70.0%。

---
