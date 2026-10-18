# analyze cross model olmo 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cross_model_olmo_001_20260514T144427_result.json`
- **Structured JSON:** [`6ff4b4ecee8cf59b2cda.json`](../../sessions/6f/6ff4b4ecee8cf59b2cda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整分析报告：

---

## cross_model_olmo_001 分析报告

### 状态：PIPELINE_CRASHED (negative)

**实验未完成。** Pipeline 脚本在 depth-0 LoRA finetune 完成后崩溃，后续步骤全部未执行。

### 失败原因

```
scripts/run_pipeline_olmo.sh: line 52: unexpected EOF while looking for matching `"'
```

运行时的脚本版本有 52+ 行，存在未闭合的引号。当前脚本已被修改（46 行，语法正确），但未重新执行。

### 已完成的部分

| 指标 | 值 |
|------|-----|
| 模型 | OLMo-1B-hf (1.18B params) |
| LoRA trainable params | 3,145,728 (0.27%) |
| Depth-0 final loss | **2.2686** |
| Training steps | 939 (3 epochs) |
| Training runtime | 283.2s |
| Checkpoint | `checkpoints/olmo/lora_depth_0` |

### 未完成的部分

- Depth-1/2/3 生成（未开始）
- Depth-1/2 LoRA finetune（未开始）
- 特征提取（未开始）
- 分类评估（未开始）
- 域一致性检查（未开始）

### **无分类指标可报告**

所有分类指标（4-class accuracy, AUC, 3-class, stratified split）均不存在。`results/` 目录下的文件是 Pythia baseline 的结果（时间戳 21:59，早于 OLMo 的 22:36）。

### 与 Pythia 对比

| 指标 | Pythia MVP | OLMo |
|------|-----------|------|
| Depth-0 final loss | ~1.025 | **2.2686** (2.2x 更高) |
| 4-class acc (full) | 78.2% | N/A |
| 4-class acc (filtered) | 81.6% | N/A |
| AUC d1v2 | 0.861 | N/A |
| AUC d2v3 | 0.801 | N/A |
| Top features | var_surprisal > p90_ppl > mean_ppl | N/A |

### 初步观察

OLMo depth-0 loss (2.27) 显著高于 Pythia (~1.03)。这符合预期——OLMo-1B (1.18B) 比 Pythia-1.4B 略小，且架构不同，在相同数据上的 finetune loss 不同是正常的。但这不影响假设验证，因为我们关注的是跨深度的统计特征差异，而非绝对 loss 值。

### 结论

**conclusion = negative**，原因不是假设被否定，而是实验因脚本 bug 未能完成。脚本已修复，需要重新运行。

### 下一步

重新执行 `bash scripts/run_pipeline_olmo.sh`，当前脚本（46行）语法正确。需要额外添加特征提取和分类步骤（当前脚本只包含 finetune + generate，缺少 `extract_features.py` 和 `classify.py` 调用）。

---
