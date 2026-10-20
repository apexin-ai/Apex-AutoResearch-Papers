# research psn irt data

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_psn_irt_data_20260520T071428_result.json`
- **Structured JSON:** [`e869fc9d3dfd25bd493b.json`](../../sessions/e8/e869fc9d3dfd25bd493b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心发现：

**PSN-IRT 4PL 参数完全公开可用**，GitHub repo `Joe-Hall-Lee/PSN-IRT` 的 `results/item_parameters.csv` 包含全部 41,871 items 的 (a, b, c, d) 参数。Items 按 benchmark 名称字母序排列，已验证映射关系。

**6 个目标 benchmark 覆盖情况**：
- MMLU (14,042), GSM8K (1,319), HumanEval (164), ARC-C (295), HellaSwag (10,042) — PSN-IRT 全部覆盖
- **TruthfulQA — PSN-IRT 不含**，但 ATLAS 项目 (3PL, `Peiyu-Georgia-Li/ATLAS`) 有 628 items 的参数

已提取的文件在 `artifacts/psn_irt_params/`，带 benchmark 标签的整合文件 `item_parameters_all.csv` 和 5 个单独 benchmark 文件。完整报告在 `artifacts/psn_irt_data_report.md`。

---
