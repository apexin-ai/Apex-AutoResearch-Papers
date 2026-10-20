# audit paper registry crosscheck

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_registry_crosscheck_20260519T004719_result.json`
- **Structured JSON:** [`0381a87d3ca7f70f0dca.json`](../../sessions/03/0381a87d3ca7f70f0dca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已注册为 `art_20260519_51a9fa`。

**审计结果摘要**:

**验证范围**: ~55 个 accuracy 数据点 + ~84 个 per-class metric，覆盖论文全部 7 个含数字的表格 + 正文/摘要 inline 数字。

**发现 1 个根因错误，传播到 4 处**:
- CodeLlama-13B no_trace: 论文写 **76.50%**，eval_results 实际为 **76.47%** (= 910/1190)
- N=1190 时不存在能产生 76.50% 的整数解，不是四舍五入问题
- 传播到: tab:cross_model 表格、正文 scale gradient 描述、"9.19pp" 应为 "9.16pp"、abstract 中 "67.31%--76.50%"

**1 个数据溯源警告**:
- DeepSeek VOTA 84.45% 来自 maxlen=16384 的评估（`eval_results_confirmatory.json`），而非论文声明的 max_length=2048。maxlen=2048 评估结果为 15.97%（损坏）。论文中应注明此差异。

**其余全部一致**: 所有 Qwen-7B ablation (7/7)、cross-model 除 CL no_trace (15/16)、full_qwen (10/10)、full_deepseek (6/6)、trace_length (6/6)、density (3/3)、DebugBench (3/3)、per_class 全部 12 行 × 7 列均 exact match。

**Registry 覆盖率仅 3.6%** (2/55+)，绝大多数实验未注册。

---
