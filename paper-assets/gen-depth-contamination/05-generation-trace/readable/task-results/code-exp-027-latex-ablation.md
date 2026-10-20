# code exp 027 latex ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_027_latex_ablation_20260518T102052_result.json`
- **Structured JSON:** [`e9ddac3495ec3d3bc08c.json`](../../sessions/e9/e9ddac3495ec3d3bc08c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-027 完成

**K\*=3 在去除 LaTeX 后保持不变。** 核心结论：arXiv 的 depth-3 饱和点不依赖 LaTeX 格式特征。

### 对比总结

| Pair | Original | LaTeX Stripped | Delta |
|------|----------|---------------|-------|
| 0v1  | 0.9948   | 0.9948        | 0.000 |
| 1v2  | 0.8581   | 0.8297        | -0.028|
| 2v3  | **0.6436** | **0.6229**  | -0.021|
| 3v4  | 0.5440   | 0.5468        | +0.003|
| 4v5  | 0.5299   | 0.5476        | +0.018|

- 去除 LaTeX 后 AUC 在高区分度 pair（1v2, 2v3）略降 0.02-0.03，低区分度 pair（3v4, 4v5）略升
- 2v3 仍 >0.60（0.6229），3v4 仍 <0.60（0.5468），**K\*=3 不变**
- Feature importance 排序基本一致（freq_entropy, surp_std 仍排前两位）
- LaTeX 内容在深层反而更多（模型生成 LaTeX），reduction 从 depth 0 的 0.6% 递增至 depth 5 的 4.4%

### 产出文件
- 去除 LaTeX 的数据：`data/exp_027_latex_ablation/depth_{0..5}.jsonl`
- Features：`data/exp_027_latex_ablation/features.csv`
- 结果：`results/exp_027_latex_ablation/` (pairwise_auc.json, summary.txt 等)
- 对比报告已注册：`art_20260518_3de274`

---
