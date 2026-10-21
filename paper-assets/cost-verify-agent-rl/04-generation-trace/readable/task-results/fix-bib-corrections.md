# fix bib corrections

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_bib-corrections_20260526T105900_result.json`
- **Structured JSON:** [`fd564bcdbf5c581bfd8c.json`](../../sessions/fd/fd564bcdbf5c581bfd8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 项 bib 修复全部完成，编译通过（0 error, 0 undefined citation, bibtex 0 warning）。

修改汇总：

| # | Key | 修改内容 |
|---|-----|---------|
| 1 | `schulman2015trpo` | 作者顺序：Moritz 移到第 3 位，Abbeel 移到第 5 位 |
| 2 | `lightman2024lets` | Yuri→Yura, Harrison→Harri |
| 3 | `kazemnejad2024vineppo` | 标题更新为正式版 "Refining Credit Assignment in RL Training of LLMs"；venue NeurIPS 2024→ICML 2025 |
| 4 | `gradientcoupling2025` | 标题更新为 v4 版 "Gradient Coupling: The Hidden Barrier to Generalization in Agentic Reinforcement Learning" |
| 5 | `istar2025` | @article→@inproceedings，arXiv→ICLR 2026，year 2025→2026 |
| 6 | `wang2024mathshepherd` | venue 补全为 "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)" |

注意：第 3 项 VinePPO 的实际情况与任务预期不同——正式发表在 ICML 2025（非 NeurIPS 2024），标题也做了修改。已按 arXiv 确认的最新信息更新。

报告已写入 `artifacts/bib_fix_report.md`。

---
