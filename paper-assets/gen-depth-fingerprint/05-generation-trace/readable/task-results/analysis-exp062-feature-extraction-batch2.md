# analysis exp062 feature extraction batch2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp062_feature_extraction_batch2_20260521T120416_result.json`
- **Structured JSON:** [`f6dadd392ebb0ad2b797.json`](../../sessions/f6/f6dadd392ebb0ad2b797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

自动提取脚本已启动（PID 357040），会在 pythia-1b-topk 生成完成后自动提取特征。

已完成的工作：
1. **pythia-2.8b topk** — 特征提取 + Cohen's d ✅
2. **qwen3-1.7b greedy** — 特征提取 + Cohen's d ✅
3. **pythia-1b topk** — 生成 80%，已设置自动提取脚本等待中

结果保存到：
- `artifacts/_project/analysis/decoding_cohens_d_batch2.txt` — 新 combo 结果
- `artifacts/_project/analysis/decoding_cohens_d_all.txt` — 汇总（batch1 + batch2）

关键发现：

| Combo | Shape dichotomy | Drifting signal | 备注 |
|-------|----------------|-----------------|------|
| pythia-2.8b topk | **FAIL** (entropy_max d=0.274) | TTR=0.46, hapax=0.41 低于阈值 | top-k 削弱了二分法 |
| qwen3-1.7b greedy | **PASS** (max shape d=0.08) | 全部 > 0.65，强信号 | 最干净的 dichotomy |

pythia-1b-topk 约 15 分钟后完成，我会再回来计算并更新汇总文件。

---
