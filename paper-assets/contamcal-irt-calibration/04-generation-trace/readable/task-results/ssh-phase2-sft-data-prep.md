# ssh phase2 sft data prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_phase2-sft-data-prep_20260513T201507_result.json`
- **Structured JSON:** [`188a646a1fdd9d436355.json`](../../sessions/18/188a646a1fdd9d436355.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

---

## Phase 2 SFT 数据准备结果

### Dosage JSONL 文件

| 文件 | 行数 | 大小 | 注入量 |
|------|------|------|--------|
| sft_dosage_000.jsonl | 50,000 | 89M | 0 (纯 SlimOrca) |
| sft_dosage_005.jsonl | 50,124 | 89M | 124 (66 ARC + 58 GSM8K) |
| sft_dosage_025.jsonl | 50,622 | 89M | 622 (302 ARC + 320 GSM8K) |
| sft_dosage_050.jsonl | 51,245 | 89M | 1,245 (600 ARC + 645 GSM8K) |
| sft_dosage_100.jsonl | 52,491 | 90M | 2,491 (1172 ARC + 1319 GSM8K) |

### Contamination Labels
每个 benchmark × dosage 组合各生成一个 label 文件（共 8 个），格式 `[0,1,...]`，长度 = benchmark 测试集大小。

### QC 统计（per benchmark，论文报告用）
| Benchmark | Total | QC Passed | Pass Rate |
|-----------|-------|-----------|-----------|
| ARC-Challenge | 1,172 | 697 | 59.47% |
| GSM8K | 1,319 | 228 | 17.29% |

**按 D010 决策：所有 paraphrases 均已使用（不过滤 QC），QC 统计仅保留在 metadata 中供论文报告。**

### MMLU 状态
仍在运行中（PID 204758，已运行 ~63min，进度 ~3%/439 batches）。MMLU 完成后需重新运行脚本加入 `--benchmarks arc_challenge,gsm8k,mmlu` 更新全部 dosage 文件。

---
