# code generalize analysis prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_generalize_analysis_prep_20260517T104130_result.json`
- **Structured JSON:** [`783476f8b9bbe3a17b47.json`](../../sessions/78/783476f8b9bbe3a17b47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Everything is working. Let me compile the final report.

---

## 结果汇总

### 1. 磁盘空间
- `/root/autodl-tmp`: 250G total, 146G used, **105G available (59%)**  — 充足

### 2. 分析管线兼容性
- **完全兼容，无需修改模型相关代码**。`method_ablation.py` 和 `cross_alpha_analysis_v4.py` 纯统计方法，不加载模型/tokenizer，只操作 `all_metrics.json` 中的数值序列
- 已写新脚本 `analyze_generalize.py`，功能：
  - 自动发现 `results/generalize/` 下所有实验
  - 如果 `all_metrics.json` 不存在，从 per-gen `metrics.json` 自动拼接
  - 运行完整 5-method 分析 (PermG, TY Granger, Naive Pearson, Diff XCorr, Threshold Onset)
  - BH FDR 校正
  - 输出到 `results/generalize/analysis/generalize_5method_results.json`
- **Dry-run 验证通过**：在 partial data 上成功运行

### 3. 泛化实验输出格式
- 输出结构：`results/generalize/{experiment}/gen_{N}/metrics.json` (per-gen) + 训练完成后自动生成 `all_metrics.json`
- 格式与 alpha_sweep 完全一致（相同 9 个 metric fields + generation index）

### 4. C4 数据集
- **已存在** `data/c4_5k/`，结构：train(4500) / eval(500) / prompts
- **已修复** prompts：从 500 扩展到 **4214**（从 train 提取 first-64-words，与 WikiText prepare_data.py 方法一致）
- WikiText prompts 为 5000，差异来自 C4 train 只有 4500 样本且部分 < 64 words。4214 prompts 足够

### 5. 实验进度
| 实验 | GPU | 当前进度 | 每代耗时 | 预计完成 |
|------|-----|---------|---------|---------|
| Pythia-410M (cuda:0) | 14.4GB, 51% util | gen_9/10 训练中 | ~24 min/gen | ~19:04 (约20分钟后) |
| OPT-1.3B (cuda:1) | 27.2GB, 96% util | gen_6/10 完成, gen_7 开始 | ~29 min/gen | ~20:13 (约1.5h后) |

### 待办
- Pythia-410M 完成后，运行 `python3 analyze_generalize.py --exp pythia410m_wiki_a100_s42` 获取完整 10-gen 分析
- OPT-1.3B 完成后同理
- Phase 2c (Pythia-1B on C4) 可直接使用 `data/c4_5k/` 启动

---
