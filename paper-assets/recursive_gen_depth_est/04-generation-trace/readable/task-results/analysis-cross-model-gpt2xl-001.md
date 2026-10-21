# analysis cross model gpt2xl 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_gpt2xl_001_20260514T182022_result.json`
- **Structured JSON:** [`6d9474b644d60a19e12e.json`](../../sessions/6d/6d9474b644d60a19e12e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是分析汇总：

---

## cross_model_gpt2xl_001 实验分析

### Pipeline 状态：生成完成，分类未执行

`run_pipeline_gpt2xl.sh` 只包含 3x finetune + 3x generate（共 6 步），**未调用** `filter_code.py` / `extract_features.py` / `train_classifier.py`。

### 训练 Loss

| Depth | Final Loss | Runtime |
|-------|-----------|---------|
| 0 | 2.5498 | 707s |
| 1 | 1.7146 | 688s |
| 2 | 1.3415 | 692s |

Loss 递减趋势（2.55 → 1.72 → 1.34）与 Pythia baseline 一致，"loss 收敛加速"效应跨模型存在。

### 生成数据
4 个 depth 各 5000 条，共 20000 条，文件大小正常（10.5-12MB）。

### 数据质量
- **depth_1**: 自然语言，质量良好
- **depth_2**: 轻微退化，出现技术类内容（AJAX-CSS 文章）和重复联系信息
- **depth_3**: 明显退化，出现极端重复循环（样本 0），hallucinated facts

### 无法判定 Conclusion

没有分类结果，**无法按标准（4-class acc > 40%, d1v2 AUC > 0.6）判定 success/negative**。实验保持 ANALYZING 状态。

### 需要执行的下一步
1. `python scripts/filter_code.py` — 代码污染检查
2. `python scripts/extract_features.py` — 统计特征提取（对 `data/gpt2xl/depth_{0,1,2,3}.jsonl`）
3. `python scripts/train_classifier.py` — 分类评估
4. 拿到 4-class acc 和 pairwise AUC 后更新 conclusion

---
