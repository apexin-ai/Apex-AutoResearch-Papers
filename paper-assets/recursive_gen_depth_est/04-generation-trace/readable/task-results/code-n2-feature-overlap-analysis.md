# code n2 feature overlap analysis

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n2_feature_overlap_analysis_20260515T123203_result.json`
- **Structured JSON:** [`ede6699f499d02f210b2.json`](../../sessions/ed/ede6699f499d02f210b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建，语法和依赖验证通过。

**文件路径**: `/root/autodl-tmp/recursive_gen_depth_est/src/n2_feature_overlap_analysis.py`

**使用方法**:

```bash
# N2 训练完成后，先在 n2_deberta_finetune.py 中添加 checkpoint 保存：
#   model.save_pretrained(Path(args.output_dir) / "checkpoint")
#   tokenizer.save_pretrained(Path(args.output_dir) / "checkpoint")

# 然后运行分析：
cd /root/autodl-tmp/recursive_gen_depth_est
python src/n2_feature_overlap_analysis.py --checkpoint_dir results/n2_deberta_finetune/checkpoint

# 快速测试（500 样本 + pretrained model，无需 checkpoint）：
python src/n2_feature_overlap_analysis.py --n_samples 500

# 指定其他 RF cell 对比：
python src/n2_feature_overlap_analysis.py --cell gpt2xl_nucleus095
```

**分析内容**:
1. **Probing R²** — 用 Ridge 回归从 DeBERTa [CLS] embedding 预测每个手工特征，5-fold CV R² 衡量 DeBERTa 表征中包含多少该特征的信息
2. **Attention-feature correlation** — 9 个 attention 统计量（entropy, Gini, 重复 token 注意力占比等）与 19 个特征的 Spearman 相关
3. **Overlap metrics** — RF permutation importance ranking vs DeBERTa probing R² ranking 的 Spearman ρ 和 top-K Jaccard

**输出**:
- `results/n2_feature_overlap/overlap_results.json`
- `results/n2_feature_overlap/attention_vs_importance.pdf`（4 panel：RF importance bar、probing R² bar、rank scatter、attention-feature correlation heatmap）

---
