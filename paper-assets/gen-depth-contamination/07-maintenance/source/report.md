# Handover — 2026-05-25

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- sweep_r10_nofilter（准备中）
- sweep_r10_binary（准备中）
- sweep_r10_graduated（准备中）
- sweep_r30_nofilter（准备中）
- sweep_eval_r10_nofilter（准备中）
- sweep_eval_r10_binary（准备中）
- sweep_eval_r10_graduated（准备中）
- sweep_eval_r30_nofilter（准备中）
- sweep_eval_r10_nf（准备中）
- sweep_eval_r10_bin（准备中）
- …另有 25 项

## 近期结论
- **exp_014_independent_metrics** (success): 补算 6 个与 OBD 15D 特征完全独立的质量指标（GPT-2 Large PPL, MTLD, HD-D, 3/4-gram rep rate, MAUVE, Zipf coefficient），修正 v2 初版的循环论证问题。独立指标与 predicted depth 的 Spearman correlation 应显著（Bonferroni α=0.0083），验证 depth signal 的 ecological validity 不依赖 OBD 自身特征。 ← 基于 exp_014_naturalistic_v2
- **exp_014_naturalistic_v2** (failed): OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26, 50K docs) 上与 6 个完全独立的质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity。Predicted depth 反映文本与 depth-k 生成文本的相似度，而非声称 CC 文本是 prompt-chain 产物。v1 仅测了 4 个指标（binary_auc/freq_entropy/ttr/cc_depth0_ratio），本次完整覆盖 9 指标 + stratified analysis + bootstrap CI。 ← 基于 exp_014_naturalistic
- **runtime_benchmark** (negative): OBD 15D feature extraction + LightGBM classifier 的 per-document inference time 显著低于 neural baselines (Binoculars/DivEye/neural probe)，且 throughput 满足大规模数据审计需求（>100 docs/sec on single GPU）。Reviewer 预期会问计算开销。
  [runtime_benchmark_results](/api/workspace-files/projects/gen-depth-contamination/artifacts/runtime_benchmark/data/benchmark_results_summary.txt)

## 趋势
成功 108 / 负向 18 / 失败 14 / 共 141

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
cqa1-22115: 空闲 cuda:0, cuda:1, cuda:2, cuda:3

## 告警
- exp-008-retrain-chain: 训练失败 — unknown
- exp_009_dose_10pct: 训练失败 — unknown
- exp_009_dose_30pct: 训练失败 — unknown
- exp_009_dose_50pct: 训练失败 — unknown
- exp_009_dose_10pct_v2: 训练失败 — unknown
- exp_009_dose_30pct_v2: 训练失败 — unknown
- exp_009_dose_50pct_v2: 训练失败 — unknown
- exp_wiki_pythia: 训练失败 — unknown
- exp_wiki_olmo: 训练失败 — unknown
- exp_olmo_retrain_chain: 训练失败 — unknown
- exp_cross_transfer_llama8b_to_qwen7b: 训练失败 — unknown
- exp_pythia69b_c4_depth_chain: 训练失败 — unknown
- exp_pythia69b_c4_depth_chain_v2: 训练失败 — unknown
- exp_pythia14b_10k: 已被终止 — unknown
- exp_014_naturalistic_v2: 训练失败 — unknown
