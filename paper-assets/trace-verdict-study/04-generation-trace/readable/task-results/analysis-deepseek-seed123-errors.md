# analysis deepseek seed123 errors

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_seed123_errors_20260517T045638_result.json`
- **Structured JSON:** [`ec5ca2b3ed89accdf507.json`](../../sessions/ec/ec5ca2b3ed89accdf507.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/trace-verdict-study/docs/paper/deepseek_seed123_error_analysis.md`。

**关键发现：**

1. **不是 fail→pass 误分类，是格式崩溃。** 100 个错误样本的模型输出是垃圾 token（"assert"=54, "["=36 等），模型在复读 trace 内容而非输出 verdict。

2. **根因是输入长度，不是 exception type。** 4000 chars 以下 0% 错误率，5000-6000 达 79.5%，6000+ 达 90.9%。seed42 在相同的 122 个长样本上 100% 正确。

3. **TypeError/NameError 高 miss rate 是假相关** — 它们被 miss 是因为产生更长的 trace，不是因为 exception type 本身。

4. **集中在 15 个 problem** — 这些 problem 生成冗长的参数表示（itertools 对象、函数地址等），触发了长度阈值。

结论：seed123 的 LoRA 初始化导致模型在长上下文（>4000 chars）下丧失格式遵循能力，转而复读上下文 token。这是 LoRA random seed 的初始化不稳定性问题，不是语义理解能力差异。

---
