# Accuracy Eval: acc_qw_s020 & acc_qw_s025

## 实验结果

| Condition | Model | Accuracy | Correct/Total | Heads Pruned | KV Eviction | Time |
|-----------|-------|----------|---------------|--------------|-------------|------|
| **dense** | Qwen2.5-7B-Instruct | **32.0%** | 16/50 | 0 | 0% | — |
| importance_s015 | Qwen2.5-7B-Instruct | 32.0% | 16/50 | — | ~15% | — |
| **importance_s020** | Qwen2.5-7B-Instruct | **24.0%** | **12/50** | 140/784 (17.9%) | ~20% | 598s |
| **importance_s025** | Qwen2.5-7B-Instruct | **26.0%** | **13/50** | 196/784 (25.0%) | ~25% | 559s |
| importance_s030 | Qwen2.5-7B-Instruct | 14.0% | 7/50 | — | ~30% | — |

### DeepSeek 对比

| Condition | Model | Accuracy |
|-----------|-------|----------|
| dense | DeepSeek-R1-Distill-Qwen-7B | 52.0% (26/50) |
| importance_s015 | DeepSeek-R1-Distill-Qwen-7B | 34.0% |
| importance_s030 | DeepSeek-R1-Distill-Qwen-7B | 10.0% |

## 关键观察

1. **s020 vs s025 非单调**: s025 (26.0%) 略高于 s020 (24.0%)，差异仅 1 题 (12 vs 13)，在 n=50 下属于采样噪声（95% CI ≈ ±12pp）。
2. **Qwen degradation 曲线**: dense 32% → s015 32% → s020 24% → s025 26% → s030 14%。s015 几乎无损，s020-s025 区间出现明显下降（~6-8pp），s030 断崖式下跌。
3. **s025 的 problem-level 差异**: s025 在 Problem 33 (720) 和 Problem 48 (5) 上答对而 s020 答错；s020 在 Problem 8 (90°) 上答对而 s025 答错。稀疏化改变了注意力分布，个别题目表现有随机性。
4. **无异常/错误**: 两个实验均正常完成，EXIT_CODE=0，无 OOM 或 CUDA 错误。
5. **无 c2_accuracy_eval 对比数据**: 服务器上不存在 c2_accuracy_eval.log 文件。存在 r9c2-spike 系列日志但格式不同。

## Sparsity 配置详情

- **s020**: heads_pruned=140 (28 layers × 5 heads/layer), kv_evicted ≈ 20% of prompt tokens
- **s025**: heads_pruned=196 (28 layers × 7 heads/layer), kv_evicted ≈ 25% of prompt tokens
- 模型: Qwen2.5-7B-Instruct (28 layers, 28 attention heads, 4 KV heads)

## 结果文件路径

- **acc_qw_s020 log**: `~/runs/phase-gated-compound-sparse/acc_qw_s020.log`
- **acc_qw_s025 log**: `~/runs/phase-gated-compound-sparse/acc_qw_s025.log`
- **acc_qw_s020 JSON**: `/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020.json`
- **acc_qw_s025 JSON**: `/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025.json`
