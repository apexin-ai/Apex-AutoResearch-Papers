# paper exp062 version c fixes

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_exp062-version-c-fixes_20260521T212841_result.json`
- **Structured JSON:** [`bfb1a8386ad7a63399fe.json`](../../sessions/bf/bfb1a8386ad7a63399fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两份文件 VERSION C 部分完全一致。三处修改已完成：

- **W1**: greedy drift mean 0.91→0.94, top-k 0.56→0.67, nucleus 0.79→0.90，措辞改为 "core drifting features"
- **W2**: 4/8 shape violations 句子替换为 model-intrinsic boundary effects 解释，含 Pythia/OLMo 具体数据
- **W3**: 末尾新增 entropy\_std 策略依赖性句（greedy 0.83 / nucleus 0.46 / top-k 0.23），支持 intermediate 分类

---
