# analysis deepseek seed123 diagnosis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_seed123_diagnosis_20260516T164035_result.json`
- **Structured JSON:** [`b975303335fc7cf25823.json`](../../sessions/b9/b975303335fc7cf25823.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `/root/trace-verdict-study/analysis/deepseek_seed123_diagnosis.md`。

**结论：A — LoRA 初始化失败（非 signal insufficiency）**

核心发现：
1. **三个 seed 的 training loss 完全一致**（~0.122），训练过程无任何异常
2. seed123 的 100 个错误不是"分类混淆"（fail→pass），而是**格式崩溃**——模型输出 `"assert"`（54 次）、`"["`（36 次）等 trace 片段代替分类标签
3. **全部 100 个错误都是长输入样本**（≥4919 chars），输入被截断到 2048 tokens 后，seed123 的 LoRA 权重在截断边界触发了"续写 trace"行为
4. 失败不可从 training metrics 检测——因为 `label_only_loss=False`，1-token 输出在总 loss 中占比 <0.1%

论文可以安全排除此 seed 并注明 "LoRA initialization sensitivity at truncation boundaries"。

---
