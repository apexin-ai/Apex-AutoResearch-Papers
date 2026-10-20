# analysis results compilation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_results-compilation_20260514T100535_result.json`
- **Structured JSON:** [`b82c6bd9d9d9b6dcd5da.json`](../../sessions/b8/b82c6bd9d9d9b6dcd5da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已写入 `artifacts/phase3_progress.md`。以下是汇总：

---

## Phase 3 进度总览

### Eval 结果矩阵

| Model | Dosage | Seed | MMLU | GSM8K | ARC-C | HumanEval |
|-------|--------|------|------|-------|-------|-----------|
| **0.5B** | d000 | 42 | 40.49 | 36.47 | 37.80 | 10.98 |
| | d000 | 123 | 41.82 | 34.04 | 39.76 | 10.37 |
| | d005 | 42 | 29.29 | 36.01 | 28.58 | 7.93 |
| | d025 | 42 | 待eval | — | — | — |
| | d100 | 42 | 23.22 | 35.71 | 22.70 | 8.54 |
| **1.5B** | d000 | 42 | 57.53 | 63.68 | 77.56 | 12.80 |
| | d000 | 123 | 57.62 | 63.31 | 76.62 | 17.07 |
| | d005 | 42 | 待eval | — | — | — |
| | d100 | 42 | 待eval | — | — | — |
| **3B** | raw | — | — | 60.50 | — | 0.00 |
| | d000 | 42 | 63.37 | **11.68**⚠️ | 82.17 | 11.59 |
| | d000 | 123 | 63.62 | **17.59**⚠️ | 82.94 | 8.54 |
| | d005 | 42 | SFT失败 | — | — | — |
| | d100 | 42 | SFT失败 | — | — | — |

### SFT 状态
- **完成**: 11/13 checkpoints (0.5B 全部 5 个, 1.5B 全部 4 个, 3B 仅 d000 2 个)
- **失败**: 3B_d005_s42, 3B_d100_s42 (空目录)
- **Aligned 格式**: 3 个目录已创建但全部为空

### 关键发现

1. **0.5B dose-response 趋势清晰**: MMLU 从 d000=41.16 → d005=29.29 → d100=23.22，ARC-C 同趋势。GSM8K 不受影响（~36%，符合预期）
2. **3B GSM8K 灾难性遗忘**: raw=60.50% → SFT d000=11.68%/17.59%，下降 43-49pp，需排查训练配置

### 11 天内优先级

| 优先级 | 任务 |
|--------|------|
| **P0** | eval 已完成 SFT 的 3 个 checkpoint (0.5B_d025, 1.5B_d005, 1.5B_d100) |
| **P0** | 排查 3B GSM8K 灾难性遗忘 |
| **P1** | 重跑 3B_d005/d100 SFT + eval |
| **P1** | 跑 raw baselines (0.5B, 1.5B 完整, 3B 补 MMLU/ARC) |
| **P2** | 第二 seed (s123) 补充实验 |

---
