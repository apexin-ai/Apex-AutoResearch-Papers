# audit d102 historical

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_d102_historical_20260521T180349_result.json`
- **Structured JSON:** [`f4dd9ed35c798365aaee.json`](../../sessions/f4/f4dd9ed35c798365aaee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。93 个 JSON 文件中：

- **1 个 FAIL**: `generalize/gpt2m_wiki_a100_s43_fp32`（westd-17855）— 使用了旧脚本（`3x_sigma_drift` + `perplexity` 作为 downstream），需要用 d102 重新分析
- **3 个 LEGACY**: westd-19828 上 `analysis_mauve/` 目录中的旧版本，缺少 config 段，但已被正确的 `analysis/` 版本取代，不影响当前结果
- **89 个 PASS**: 包括所有 Phase Diagram（T=5/T=15）、T=20、Alpha Sweep 实验，均使用 `true_3sigma_d105` + 正确 downstreams

报告已写入 `artifacts/d102_audit_report.md`。

---
