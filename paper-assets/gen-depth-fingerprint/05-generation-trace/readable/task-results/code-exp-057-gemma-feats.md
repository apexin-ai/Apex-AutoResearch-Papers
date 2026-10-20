# code exp 057 gemma feats

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_057_gemma_feats_20260520T073357_result.json`
- **Structured JSON:** [`a452fad65aa100da6ddc.json`](../../sessions/a4/a452fad65aa100da6ddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`eval_9gen_logo.py` 直接读取 `data/gemma-2-2b/features_pythia410m.jsonl`，格式兼容，无需额外转换。

**任务完成：**
- 特征提取已重跑，输出 4957 行（之前仅 1061 行）
- depth 分布均匀：每个 depth 约 990-994 条
- `eval_9gen_logo.py` 直接从 JSONL 读取 gemma-2-2b 特征，无需合并到 CSV
- 旧文件已备份为 `features_pythia410m.jsonl.bak`

---
