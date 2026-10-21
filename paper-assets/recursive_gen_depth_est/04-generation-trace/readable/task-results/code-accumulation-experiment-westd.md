# code accumulation experiment westd

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_accumulation_experiment_westd_20260519T072407_result.json`
- **Structured JSON:** [`5ac9ce3271d0fd752f4f.json`](../../sessions/5a/5ac9ce3271d0fd752f4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 数据结构
- **路径**: `/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/`
- **格式**: JSONL，字段 `text`, `depth`, `source`, `token_count`, `seed_id`
- **每个 depth**: 5000 条，共 20000 条
- **预计算特征**: `features.jsonl` (20000 行, 19 维统计特征)
- d0 = Wikipedia 人类文本，d1-d3 = GPT-2 XL nucleus 递归生成

### 2. 脚本
- **路径**: `/root/autodl-tmp/recursive_gen_depth_est/scripts/accumulation_experiment.py`
- **用法**: `python3 accumulation_experiment.py --mix_ratio 0.5 --seed 42 --output_dir results/accumulation/mix50/`
- 直接在特征层面混合 d0 human 特征到 d1-d3，无需重新提取特征

### 3. 实验 Job

| 实验 | exp_id | PID | tmux session | mix_ratio |
|------|--------|-----|-------------|-----------|
| A (50% human) | `accum_mix50` | 108519 | `accum_mix50` | 0.5 |
| B (25% human) | `accum_mix25` | 108797 | `accum_mix25` | 0.25 |

### 4. 结果（均已完成，耗时 <1 分钟）

| 指标 | Full-Replacement | Accum 25% human | Accum 50% human |
|------|-----------------|-----------------|-----------------|
| Overall Accuracy | **0.8421** | 0.6721 (-0.170) | 0.3551 (-0.487) |
| Balanced Accuracy | **0.8421** | 0.6721 | 0.3551 |
| d1-d3 Bal. Acc | **0.7953** | 0.5969 (-0.198) | 0.3959 (-0.399) |

**关键发现**: accumulation 场景显著降低 depth 分类准确率。50% human 混合导致准确率从 84.2% 骤降至 35.5%（接近 4-class 随机水平 25%），25% human 混合也降至 67.2%。d0 class 在 50% 混合下 recall 仅 23.3%（大量 d0 被误分到其他 depth），因为 d1-d3 中混入的 human 特征与 d0 特征分布高度重叠。

---
