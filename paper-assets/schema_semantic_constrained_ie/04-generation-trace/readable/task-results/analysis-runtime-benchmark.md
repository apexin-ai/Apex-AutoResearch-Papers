# analysis runtime benchmark

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_runtime_benchmark_20260515T140233_result.json`
- **Structured JSON:** [`363536981b101610ebf1.json`](../../sessions/36/363536981b101610ebf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。以下是 Markdown 表格：

---

### Qwen3-8B Runtime Benchmark (single RTX PRO 6000 Blackwell)

**数据来源**: 从 JSONL 输出文件的 `inference_time_seconds` 字段逐条求和，token 数用 Qwen3-8B tokenizer 对 `raw_output` 精确计数。posthoc filter 时间为 `posthoc_filter.py` 端到端执行。

#### SciERC (551 docs)

| Mode | Total (s) | Avg/doc (s) | Tokens | Tok/s | Overhead |
|------|-----------|-------------|--------|-------|----------|
| Unconstrained | 4,790.3 | 8.694 | 131,797 | 27.51 | — |
| Grammar-only | 4,856.8 | 8.815 | 131,821 | 27.14 | +1.4% |
| Semantic-only | 3,981.5 | 7.226 | 131,771 | 33.10 | **-16.9%** |
| Full (G+S) | 3,725.2 | 6.761 | 131,843 | 35.39 | **-22.2%** |
| Post-hoc | 4,790.4 | 8.694 | 131,797 | 27.51 | +0.0% |

#### DocRED (998 docs)

| Mode | Total (s) | Avg/doc (s) | Tokens | Tok/s | Overhead |
|------|-----------|-------------|--------|-------|----------|
| Unconstrained | 19,715.2 | 19.755 | 1,121,442 | 56.88 | — |
| Grammar-only | 20,535.0 | 20.576 | 1,124,288 | 54.75 | +4.2% |
| Semantic-only | 20,486.6 | 20.528 | 1,120,340 | 54.69 | +3.9% |
| Full (G+S) | 20,354.0 | 20.395 | 1,116,251 | 54.84 | +3.2% |
| Post-hoc | 19,737.4 | 19.777 | 1,121,442 | 56.88 | +0.1% |

*(Post-hoc filter time: SciERC 0.06s, DocRED 22.3s)*

---

**关键发现**:
- **DocRED**: constrained decoding 开销 3-4%，符合预期
- **SciERC**: full_s1 反而比 unconstrained **快 22%**（同样的 token 数量，但 tok/s 从 27.5 → 35.4）。可能原因：SciERC 文档短，semantic constraints 的 token mask 裁剪了搜索空间导致每步 sampling 更快；也可能受 GPU 负载波动影响（这些实验跑在不同时间段）
- **Post-hoc filter** 几乎零开销（SciERC <0.1s, DocRED 22s 主要来自 Levenshtein 匹配）
- 所有模式生成的 token 总数几乎一致（~131.8K for SciERC, ~1.12M for DocRED），说明 constraints 不改变输出长度

---
