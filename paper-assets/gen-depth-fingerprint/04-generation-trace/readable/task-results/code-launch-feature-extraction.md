# code launch feature extraction

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_launch-feature-extraction_20260514T232457_result.json`
- **Structured JSON:** [`5c3ac309a3c7ba2873f6.json`](../../sessions/5c/5c3ac309a3c7ba2873f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个生成器的特征提取完成：

| 生成器 | GPU | 行数 | 文件大小 | 输出文件 |
|--------|-----|------|----------|----------|
| pythia-2.8b | cuda:0 | 4609 | 645K | `features_pythia-2.8b.csv` |
| pythia-1b | cuda:1 | 4555 | 628K | `features_pythia-1b.csv` |
| olmo-2-1b | cuda:2 | 4713 | 653K | `features_olmo-2-1b.csv` |
| qwen3-0.6b | cuda:3 | 4538 | 628K | `features_qwen3-0.6b.csv` |
| qwen3-1.7b | cuda:0 (排队) | 4617 | 641K | `features_qwen3-1.7b.csv` |

每个输出 shape 为 `(N, 10)`，参考模型 Pythia-410M。前 4 个并行跑完后 qwen3-1.7b 接力完成。中间修复了两个 nohup 问题：conda 环境丢失（改用绝对路径 `/root/miniconda3/bin/python`）和工作目录丢失（改用 `bash -c 'cd ... && ...'` 包裹）。

---
