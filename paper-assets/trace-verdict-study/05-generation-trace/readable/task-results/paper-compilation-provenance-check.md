# paper compilation provenance check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compilation-provenance-check_20260516T045807_result.json`
- **Structured JSON:** [`c49b72e708be3dc0f818.json`](../../sessions/c4/c49b72e708be3dc0f818.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。汇总如下：

### 1. 256/512 数据溯源 — 已确认
两个数据点**均可完整溯源**：
- **256tok (78.82%)**：checkpoint 在 `full_trace_256tok/`，`final/eval_results.json` 中 accuracy=0.78824，训练通过 `train_sft.py --max_trace_tokens 256`
- **512tok (80.42%)**：checkpoint 在 `full_trace_512tok/`，`final/eval_results.json` 中 accuracy=0.80420，训练通过 `train_sft.py --max_trace_tokens 512`

缺失项：这两个实验没有像 1024tok 那样注册到 registry，建议补注册。

### 2. 论文编译 — 成功
`main.pdf` 编译成功，18 页，仅有 underfull hbox 排版警告，无错误。

### 3. ae_only 训练 — 运行中
- seed123：241/444 (54%)，预计 ~64min 完成
- seed456：211/444 (48%)，预计 ~74min 完成
- 双 GPU 均 100% 利用率

---
