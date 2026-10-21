# analysis d150 p01 spec curve audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d150_p01_spec_curve_audit_20260520T132018_result.json`
- **Structured JSON:** [`6775bb09a4883bdaecf5.json`](../../sessions/67/6775bb09a4883bdaecf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。

**D127 Spec Curve: PASS** — 脚本第 106 行硬过滤 `true_3sigma_d105`，8 canonical pairs 正确，无 perplexity，n_perm=5000，FDR 校正正确。

**Shapley Values: FAIL** — 2026-05-17 09:41 计算时读到的 `a000_s42` 数据尚为 `3x_sigma_drift` 标准（该文件 17:34 才被替换为 `true_3sigma_d105`）。threshold_onset 的 Shapley 贡献基于错误 threshold 决策，需用 D120 合规数据重算。

附加问题：FNR 仅用 6/8 pairs（排除 mauve），需决策是否恢复全 8 pairs。

报告已写入 `artifacts/d150_p01_spec_curve_audit.md`。

---
