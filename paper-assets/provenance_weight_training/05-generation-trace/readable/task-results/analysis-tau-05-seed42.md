# analysis tau 05 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau_05_seed42_20260515T164137_result.json`
- **Structured JSON:** [`21355c332add8fea9e18.json`](../../sessions/21/21355c332add8fea9e18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。总结：

**tau_05_seed42 实验结果**

| 指标 | 值 |
|------|-----|
| train_loss | 8.849 (batch-sum; per-example ≈2.21) |
| total_steps | 6103 (完成) |
| epoch | 0.26 |
| train_runtime | 13431s (~3.7h) |
| samples/s | 7.27 |
| checkpoint | `/root/provenance_weight_training/output/models/tau_0.5_seed42/final/` ✓ |
| eval_ppl_holdout | **缺失** — 训练脚本未执行评估 |

**Conclusion: negative**

日志中完全没有 eval 指标（无 eval_loss、eval_ppl_holdout、perplexity）。训练正常完成但未运行 holdout 评估，无法直接对比 baseline PPL=17.65。train_loss 全程在 8.2-9.9 之间波动（若为 batch-sum/4 则 per-example ~2.2），没有显著下降趋势。

**注意事项**：
1. 模型保存路径实际是 `tau_0.5_seed42`（有小数点），不是 `tau_05_seed42`
2. 日志中无 `b_star` 字段，使用的是 `weighting/b`
3. spec 字段在更新时被覆盖（原始 command/pid 等信息丢失，但 server/gpu 保留在顶层）
4. 如需确定 PPL，需要单独运行 holdout eval 脚本

---
