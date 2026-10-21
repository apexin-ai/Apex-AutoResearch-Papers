# code plan003 annotation pipeline

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003-annotation-pipeline_20260520T095152_result.json`
- **Structured JSON:** [`4f8f8cba9c6882164f2d.json`](../../sessions/4f/4f8f8cba9c6882164f2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`annotate.py` 已创建并通过验证。文件位于 `/home/sonny/causal_annot_error_attrib/annotate.py`。

核心功能：
- **3 模型** (Llama4 Maverick, Qwen3 235B, DeepSeek Chat) × **3 数据集** (HumAID K=11, VAST K=3, Civil Comments K=2) × **3 prompt** (zero-shot, few-shot-3, few-shot-5)
- API key 从 `OPENROUTER_API_KEY` 环境变量读取
- 0.5s rate limiting + 指数退避重试（429/5xx/超时）
- 断点续传：已有结果的样本自动跳过
- 多层 label 解析：JSON → 正则 pattern → 精确子串匹配 → fuzzy matching
- 输出 JSONL（逐条记录）+ column-stochastic 混淆矩阵 C 的 npz 文件

---
