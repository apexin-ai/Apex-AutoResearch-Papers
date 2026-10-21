# code package code supplement

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_package-code-supplement_20260517T125034_result.json`
- **Structured JSON:** [`76fe1ff2846edd72593d.json`](../../sessions/76/76fe1ff2846edd72593d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。打包结果：

**21 个文件，总结构：**

| 文件 | 大小 | 说明 |
|------|------|------|
| `generate_chain.py` | 8.2K | 多深度文本续写 pipeline |
| `extract_features.py` | 7.8K | 特征提取 (CSV) |
| `extract_features_jsonl.py` | 4.6K | 特征提取 (JSONL) |
| `classify_and_eval.py` | 9.5K | 3-class 分类 + 统计检验 |
| `eval_8gen_logo.py` | 8.4K | 8-gen LOGO 评估 |
| `eval_8gen_finer_depth.py` | 7.2K | 5-class vs 3-class |
| `eval_8gen_sampling_ablation.py` | 18.4K | 采样量消融 |
| `eval_8gen_cross_model_chains.py` | 25.7K | 跨模型链延伸 |
| `eval_8gen_baselines_pooled.py` | 11.6K | Pooled LOGO + 4 baselines |
| `benchmark_efficiency.py` | 14.9K | 效率对比 |
| `8gen_length_confound.py` | 9.1K | 长度混淆控制 |
| `compute_dataset_stats.py` | 2.3K | 数据集统计 |
| `experiments/human_edit_robustness/run_robustness.py` | 13.8K | 词替换鲁棒性 |
| `scripts/lofo_ablation.py` | 2.8K | LOFO 消融 |
| `scripts/alt_classifier_eval.py` | 4.2K | 分类器对比 |
| `scripts/bootstrap_ci_v2.py` | 4.8K | Bootstrap CI |
| `scripts/plot_fig1_strip.py` | 4.8K | Figure 1 |
| `scripts/plot_fig2.py` | 4.4K | Figure 2 |
| `scripts/plot_fig3.py` | 4.5K | Figure 3 |
| `requirements.txt` | 142B | 依赖列表 |
| `README.md` | 3.5K | 复现说明 |

**验证通过：** `grep -r "/root/"`, `grep -r "/home/ubuntu"`, `grep -r "autodl"` 均为零匹配，无残留硬编码路径。

---
