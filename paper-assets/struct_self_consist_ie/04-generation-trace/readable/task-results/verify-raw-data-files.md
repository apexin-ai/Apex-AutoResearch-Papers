# verify raw data files

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_raw_data_files_20260515T030412_result.json`
- **Structured JSON:** [`610c58af5ab268113ee8.json`](../../sessions/61/610c58af5ab268113ee8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

## 文件检查汇总

| Task | 文件路径 | 状态 | 大小 | 行数 | 备注 |
|------|---------|------|------|------|------|
| **A1** LLaMA SciERC N=8 | `exp007_llama_inference/samples.jsonl` | ✅ 存在 | 3.6M | 551 | 注意实际目录名无下划线：`exp007_llama_inference` 而非 `exp_007_llama_inference` |
| **A2** LLaMA SciERC N=16 | `exp_007_llama_n16/samples.jsonl` | ✅ 存在 | 6.4M | 551 | |
| **A3** Qwen CoNLL N=8 | `exp002_conll2003/samples.jsonl` | ✅ 存在 | 9.4M | 3453 | 实际目录名 `exp002_conll2003`（无下划线） |
| **A4** LLaMA CoNLL N=8 | `exp_017_llama_conll_infer/samples.jsonl` | ✅ 存在 | 9.1M | 3453 | |
| **B** WNUT-17 | `exp003_wnut17_eval/samples.jsonl` | ✅ 存在 | 4.6M | 1287 | 目录还含 `report.json` (1.8K) |
| **C** Qwen SciERC N=8 seed=42 | `exp_012_rerun_1024/samples.jsonl` | ✅ 存在 | 3.7M | 551 | `exp_001_seed42_v2/samples.jsonl` 也存在 (6.5M, 551行) |
| **D** exp_016 RE selection | `exp_016_rerun_1024/` | ✅ 存在 | ~192K | — | 含 6 个 JSON 文件 + summary.md，**无 samples.jsonl**（这是分析结果目录） |
| **E1** 代码目录 | `code/` | ✅ 存在 | — | — | 47 个 .py 文件，含 `consistency.py`, `evaluation.py`, `sampling.py` 等核心模块。无 `src/` 目录 |

**关键发现：**
- 所有 raw sample 文件均存在，无缺失
- 命名不一致：旧实验用 `expNNN`（无下划线），新实验用 `exp_NNN`
- CoNLL 数据集 (3453行) 远大于 SciERC (551行)
- `exp_016_rerun_1024` 是 RE selection 分析结果，不含 raw samples

---
