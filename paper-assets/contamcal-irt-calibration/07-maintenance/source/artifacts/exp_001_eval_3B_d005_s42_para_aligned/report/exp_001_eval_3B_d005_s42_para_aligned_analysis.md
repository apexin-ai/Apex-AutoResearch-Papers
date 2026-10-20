# Eval Analysis: Qwen2.5-3B_d005_s42_para_aligned

## 实验信息
- **Model**: Qwen/Qwen2.5-3B (LoRA fine-tuned, d005, seed 42)
- **Eval type**: Paraphrased benchmarks (QC-passed items only)
- **Checkpoint path**: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned/
- **Log path**: /root/runs/contamcal-irt-calibration/eval_3B_d005_s42_para_aligned.log
- **Completion**: .done sentinel present, no fatal errors

## Para_aligned 结果（paraphrased questions）

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.6471 | 4268/6596 |
| GSM8K (exact_match) | 0.3421 | 78/228 |
| ARC-Challenge | 0.8164 | 569/697 |
| HumanEval (pass@1) | 0.0769 | 2/26 |

## 对比：aligned（原始题目，full dataset）

| Benchmark | para_aligned | aligned | a32_aligned | Δ (para - aligned) |
|-----------|-------------|---------|-------------|---------------------|
| MMLU | 0.6471 (n=6596) | 0.6345 (n=14042) | 0.6308 (n=14042) | +1.26pp |
| GSM8K | 0.3421 (n=228) | 0.2077 (n=1319) | 0.4147 (n=1319) | +13.4pp |
| ARC-Challenge | 0.8164 (n=697) | 0.8294 (n=1172) | 0.8251 (n=1172) | -1.3pp |
| HumanEval | 0.0769 (n=26) | 0.1463 (n=164) | 0.1341 (n=164) | -6.9pp |

## 注意事项

- para_aligned 仅测试有 QC-passed paraphrases 的子集，aligned 测试完整数据集。Item 数量不同，直接比较需谨慎。
- 正式的污染检测分析应使用 correctness_matrix.json 进行逐 item 配对比较（同一 item 原始 vs 改写版本）。
- correctness_matrix.json 已生成（47967 bytes），可用于后续 IRT 分析。
- HumanEval paraphrased 仅 26 items（QC 通过率低），样本量极小，结果参考价值有限。

## 结论

**Status: SUCCESS** — Eval 正常完成，所有 4 个 benchmark 均产出结果，correctness_matrix 和 item_responses 已保存。可进入后续 IRT 信号计算阶段。
