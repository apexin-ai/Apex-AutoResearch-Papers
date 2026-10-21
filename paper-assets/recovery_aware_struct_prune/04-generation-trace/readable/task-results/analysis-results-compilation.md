# analysis results compilation

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_results-compilation_20260515T223025_result.json`
- **Structured JSON:** [`939ac07cda445664f59f.json`](../../sessions/93/939ac07cda445664f59f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已生成并注册：

**`paper_results_tables.md`** — 3 张表：
- **Table 1**: Post-prune accuracy，分 westb(cal=512) / westd(cal=256) / α ablation 三个 panel
- **Table 2**: Post-SFT recovery，含 N=1319 definitive results (RASP 61.49% vs Standard 59.29%)、N=100 三方对比 (Standard 64% > RASP 57% > GraSP 41%)、α ablation post-SFT
- **Table 3**: GRPO collapse timeline (RASP step~10 < Standard step~50-60 < Unpruned step~80)

**`statistical_summary.md`** — 完整统计分析：
- 所有 pairwise z-test：2 个显著 (GraSP vs Standard p=0.001, GraSP vs RASP p=0.024)，其余全部 ns
- 所有 accuracy 的 95% CI
- Power analysis：N=100 最小可检测效应 ~14pp，N=1319 ~4pp
- α ablation 无显著差异 → SFT equalization effect

缺失数据：α=0.0 post-prune accuracy 未在 registry 中找到（仅有 post-SFT 64%）。

---
