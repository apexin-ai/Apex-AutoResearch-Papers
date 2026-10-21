# results/ 文件溯源

## 权威源：8gen_logo_unfiltered.json

- **产生脚本**: `fix_tail_decay_and_eval.py` → `step2_8gen_logo()`
- **数据**: 全量 37,058 行（features_all_models.csv + llama/mistral JSONL）
- **训练**: 无 downsample，直接在不平衡数据上训练
- **F1**: pooled macro F1（所有 fold 预测拼接后计算一次 macro F1）
- **XGB**: n_estimators=200, max_depth=6, random_state=42
- **数值**: 3class=0.762, binary=0.694
- **状态**: 多轮审稿验证，论文引用此版本

## 对比源：8gen_logo_baselines.json

- **产生脚本**: `eval_8gen_logo_baselines.py`
- **数据**: 34,131 行（与 detector_scores_8gen.csv inner join，llama 丢 1743 行，mistral 丢 1184 行）
- **训练**: 有 downsample（每 fold 训练集类别平衡采样）
- **F1**: per-gen 平均（每个 generator 单独算 macro F1，再取 8 个的平均）
- **XGB**: n_estimators=200, max_depth=6, random_state=789
- **数值**: 7feature_ours 3class=0.740, binary=0.661
- **状态**: 用于 baselines 对比实验

## 数字差异根因（7-feature binary: 0.694 vs 0.661, 3class: 0.762 vs 0.740）

1. **F1 聚合方式不同**: unfiltered 用 pooled macro F1，baselines 用 per-gen 平均。两者定义不同，不可直接比较。
2. **训练采样不同**: unfiltered 无 downsample（类别不平衡直接训练），baselines 每 fold 做 downsample。
3. **数据子集不同**: baselines 因 inner join 丢失 2927 行（均来自 llama/mistral），训练和测试数据量均少于 unfiltered。
4. **随机种子不同**: 42 vs 789，影响 XGB 训练和 downsample 采样。

## 已废弃

- `8gen_logo_results_BUGGY_DO_NOT_USE.json` — 有 bug 的旧版本，勿使用
