# verify cross strategy label mapping

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cross_strategy_label_mapping_20260515T041543_result.json`
- **Structured JSON:** [`79c5a2d202fe4984adf7.json`](../../sessions/79/79c5a2d202fe4984adf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结论

### 1. Label mapping 一致性：**Yes，完全一致**

所有 9 个 cell：
- 唯一 label 字段：`depth`
- 取值：{0, 1, 2, 3}
- 每类 5000 样本，完全平衡
- 无任何 label 转换/映射逻辑（`load_features` 直接用 `rec["depth"]`）

### 2. In-dist d1v2 AUC（sanity check）

| Cell | In-dist d1v2 AUC |
|------|------------------|
| gpt2xl_temp09 | **0.9792 ± 0.0013** |
| olmo_temp09 | **0.9558 ± 0.0029** |

两者均远 >0.8，in-dist 分类正常。

### 3. Feature 方向一致性

p90_ppl、var_surprisal、type_token_ratio 在所有 6 个 cell 中方向一致（d1 > d2）。无 label 反转迹象。

### 4. 结论

**temp09 d1v2 reversal is a real cross-strategy transfer phenomenon, not a label bug.**

代码无 bug。AUC < 0.5 说明在 nucleus+topk50 上训练的 RF 模型在 temp09 测试集上学到了反向的决策边界——这是跨策略特征分布漂移的体现，不是 label mapping 问题。

---
