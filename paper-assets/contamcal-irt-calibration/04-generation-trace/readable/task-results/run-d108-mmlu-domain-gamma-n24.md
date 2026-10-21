# run D108 mmlu domain gamma n24

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_D108_mmlu_domain_gamma_n24_20260516T113022_result.json`
- **Structured JSON:** [`48bd43fda1c5bcc2f4e8.json`](../../sessions/48/48bd43fda1c5bcc2f4e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 PID=768342 已在后台运行。配置：
- **N=23 models** (8×0.5B + 8×1.5B + 7×3B)，无 para
- **14042 MMLU items** per model
- **RRF per-item exposure**（而非 N=16 时的 oracle dosage-based）
- **2PL+γ**, 4 chains × 1000w + 1000s, adapt_delta=0.95
- 输出：`/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/`

正在拟合第一个 domain (STEM_Math, 1190 items)。预计全部完成需 40-60min。我会在几分钟后检查进展。

---
