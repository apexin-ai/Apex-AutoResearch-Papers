# analysis rrf precheck 05b 15b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rrf_precheck_05b_15b_20260516T083219_result.json`
- **Structured JSON:** [`dd8bb782434396e96776.json`](../../sessions/dd/dd8bb782434396e96776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

RRF 聚合完成。

---

## 报告

### 输出文件
- `/root/autodl-tmp/exp003/rrf_05B_15B/exposure_scores.json` — 每 respondent×benchmark 的逐 item exposure
- `/root/autodl-tmp/exp003/rrf_05B_15B/exposure_aggregated.json` — 跨 respondent 均值

### 纳入的 respondents（13 个）

| Scale | 完整 (3 bench × 3 signals) | 部分 |
|-------|---------------------------|------|
| 0.5B | d000_s42, d000_s123, d005_s42, d005_s123, d025_s42, d100_s42 | d025_s123 (仅 mmlu, 2 signals) |
| 1.5B | d000_s42, d000_s123, d005_s42, d025_s42, d100_s42 | d005_s123 (仅 mmlu, 2 signals) |

### 排除/缺失
- **alpha=16 目录**：无（blocklist 仅含 3B 条目，0.5B/1.5B 不受影响）
- **完全缺失的 s123 目录**：0.5B_d100_s123、1.5B_d025_s123、1.5B_d100_s123

### 不完整目录详情
- `0.5B_d025_s123`：只有 `signal_s1_embedding_mmlu.json` + `signal_s2_minkpp_mmlu.json`（缺 s4、缺 gsm8k/arc）
- `1.5B_d005_s123`：同上
- `0.5B_d000_s123`：缺 `signal_s4_selfcritique_gsm8k.json`（gsm8k 只用了 2/3 signals，arc/mmlu 正常）

### 聚合统计（跨 respondent 均值）
| Benchmark | N items | Mean exposure | Std | Max |
|-----------|---------|--------------|-----|-----|
| mmlu | 14,042 | 0.0411 | 0.0335 | 0.3182 |
| gsm8k | 1,319 | 0.1600 | 0.0756 | 0.5916 |
| arc_challenge | 1,172 | 0.1848 | 0.0782 | 0.5359 |

### 命名一致性
- s42 目录使用 `signal_embedding_*` 命名（无 s1_ 前缀）
- s123 目录使用 `signal_s1_embedding_*` 命名（有前缀）
- 代码已处理两种命名模式，dry-run 和 full-run 均正常

### 结论
Dry-run 通过，full-run 已产出 exposure scores。两个部分目录（d025_s123、d005_s123）的 signals 并未全部完成，代码用可用 signals 做了 graceful degradation。如需 downstream IRT 使用，建议确认这些部分 respondent 是否应包含在内，或者等它们补完后重新 aggregate。

---
