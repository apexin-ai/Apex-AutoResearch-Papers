# ssh prepare sft data 3bench

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-sft-data-3bench_20260513T231536_result.json`
- **Structured JSON:** [`f45813c72dc8297ca82b.json`](../../sessions/f4/f45813c72dc8297ca82b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### Dosage 文件生成结果

| 文件 | 行数 | 大小 | Base | Contam | Contam 占比 |
|------|------|------|------|--------|------------|
| `sft_dosage_000.jsonl` | 50,000 | 89M | 50,000 | 0 | 0% (未重生成) |
| `sft_dosage_005.jsonl` | 50,826 | 89M | 50,000 | 826 | 1.6% |
| `sft_dosage_025.jsonl` | 54,133 | 91M | 50,000 | 4,133 | 7.6% |
| `sft_dosage_050.jsonl` | 58,266 | 93M | 50,000 | 8,266 | 14.2% |
| `sft_dosage_100.jsonl` | 66,533 | 97M | 50,000 | 16,533 | 24.8% |

### 3 Benchmarks 确认包含

| Benchmark | 总 paraphrases | d5% 污染数 | d25% | d50% | d100% |
|-----------|---------------|-----------|------|------|-------|
| MMLU | 14,042 | 703 | 3,540 | 7,040 | 14,042 |
| ARC-Challenge | 1,172 | 50 | 257 | 556 | 1,172 |
| GSM8K | 1,319 | 73 | 336 | 670 | 1,319 |

HumanEval 已按 D009 排除。所有 contamination label 文件（3 benchmarks × 4 dosages = 12 个）已生成。`data_meta.json` 已更新。无异常。

---
