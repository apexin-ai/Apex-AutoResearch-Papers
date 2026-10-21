# code llama rp11 filter and extract

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-rp11-filter-and-extract_20260516T114701_result.json`
- **Structured JSON:** [`f4436ac71a2d4b019593.json`](../../sessions/f4/f4436ac71a2d4b019593.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

**Phase 1 — Soft Filter**
- 输入: 4416 条 → 过滤后: 4386 条
- 仅过滤 30 条 (0.68%)，符合 rp=1.1 低退化预期

**Phase 2 — 3-ref Feature Extraction**

| 文件 | 行数 |
|------|------|
| `features_pythia410m.jsonl` | 4386 |
| `features_olmo2-1b.jsonl` | 4386 |
| `features_qwen3-06b.jsonl` | 4386 |

每条包含: `seed_id`, `depth`, `entropy_mean/std/min/max`, `tail_decay`, `ttr`, `hapax_ratio`。tail_decay 的 90th percentile 阈值基于 depth-0 样本计算。

脚本已参数化（新增 `--data-dir` 参数），后续其他 rp 设置可直接复用。

---
