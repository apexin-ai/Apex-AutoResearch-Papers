# analysis budget curve corrected

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_budget_curve_corrected_20260522T060115_result.json`
- **Structured JSON:** [`30bc67444999b1fc7203.json`](../../sessions/30/30bc67444999b1fc7203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**生成完毕。** 文件路径：

| 文件 | 路径 |
|------|------|
| PDF | `/root/autodl-tmp/trace-verdict-study-checkpoints/budget_curve_corrected/budget_curve_table12.pdf` |
| PNG (300dpi) | `/root/autodl-tmp/trace-verdict-study-checkpoints/budget_curve_corrected/budget_curve_table12.png` |
| JSON | `/root/autodl-tmp/trace-verdict-study-checkpoints/budget_curve_corrected/budget_curve_table12.json` |

**关键观察：**

1. **Phase transition 极其明显**：4 个模型在 384→512 区间全部出现陡升（约 +13~22 个百分点），从 baseline 附近直接跳到 93%+，呈阶跃函数形态而非渐进曲线。
2. **跨模型高度一致**：无论模型大小（1.5B→13B）和架构（Qwen/DeepSeek/CodeLlama），phase transition 位置完全重合，说明这是数据/任务的固有特征而非模型特性。
3. **Qwen-7B full input 反常**：不截断时（81.76%）反而低于 tail-512（93.60%），证实"更多 context ≠ 更好性能"，前缀噪声确实有害。
4. **CodeLlama-13B tail-2048 灾难性失败**（28.49%）：远低于 majority baseline，说明 13B 模型在长序列 tail truncation 下出现严重退化，可能与其 context window 限制或训练分布不匹配有关。

---
