# analysis deepseek vota error analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_vota_error_analysis_20260515T131419_result.json`
- **Structured JSON:** [`bf2814ae5f33d1f8f80d.json`](../../sessions/bf/bf2814ae5f33d1f8f80d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/deepseek_vota_fail_recall_analysis.md`。核心结论：

**根因是 DeepSeek-Coder-6.7B 模型能力不足，不是数据/tokenizer/训练配置问题。**

关键证据：
1. **Tokenizer 无差异** — 两者 "pass"/"fail" 都是单 token，结构一致
2. **Overfitting 明显** — DeepSeek eval_loss epoch 2→3 上升 18%（Qwen 仅 9%），但 overfit 方向是 trace 格式而非 verdict 判别
3. **系统性 pass 偏向** — fail_precision=1.0 说明模型不是乱猜，而是极度保守：只在高置信时才预测 fail，其余全部默认 pass
4. **模型代差** — DeepSeek-Coder-6.7B (2023) vs Qwen2.5-Coder-7B (2024)，后者在指令跟随和代码理解上更强

**等 deepseek_no_trace 结果时的解读框架**：
- no_trace fail_recall ≈ vota → 纯模型能力问题
- no_trace fail_recall > vota → VOTA trace 对 DeepSeek 是负干扰
- no_trace fail_recall < vota → trace 至少有部分帮助

---
