# ops fix scatter accuracy

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-scatter-accuracy_20260522T105723_result.json`
- **Structured JSON:** [`5915dd24e11ed3dd106a.json`](../../sessions/59/5915dd24e11ed3dd106a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图片生成正确，标注位置合理。

## 汇总

| 模型 | n | 精确均值 | 百分比 | 图中旧值 | 论文正文 |
|------|---|---------|--------|---------|---------|
| Qwen MMLU | 10 | 0.6776 | 67.8% | 67.87% | 67.8% |
| Llama MMLU | 10 | 0.5937 | 59.4% | 60.0% | 59.3% |
| Mistral MMLU | 10 | 0.5240 | 52.4% | 53.4% | 52.4% |
| Qwen ARC-C | 6 | 0.8994 | 89.9% | 90.2% | — |

**已更新内容：**
- `gen_fig_theta_scatter.py` 中所有 data_5/15/25/50 的 acc 值已改为权威均值
- 所有 annotation 的 xy/xytext 坐标已同步调整
- PDF 和 PNG 已重新生成到 `figures/paper/`

**ARC-C 说明：** 服务器上仅有 6 个 seed 的结果（s1, s2, s7-s10），s3 因 wandb 错误失败，s4-s6 无结果文件。6-seed 均值为 89.9%，与之前 5-seed 的 90.0% 接近但略低。

---
