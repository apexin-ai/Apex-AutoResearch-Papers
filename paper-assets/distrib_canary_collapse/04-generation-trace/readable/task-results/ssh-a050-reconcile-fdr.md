# ssh a050 reconcile fdr

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a050_reconcile_fdr_20260517T064346_result.json`
- **Structured JSON:** [`0a1bf4604150b3c43704.json`](../../sessions/0a/0a1bf4604150b3c43704.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Reconciliation 完成。

**结论**：`run_5method_analysis.py` 三 seed 结果确认一致：
- s42: 0/8, s43: 6/8, s44: 3/8（均匹配预期）

**差异根因**：Worker B 使用了 `analyze_alpha_sweep.py`，该脚本对同一 alpha 下所有 seed 做联合 BH（family=24 而非 8），导致仅 2/24 通过 FDR。原假设 family_size=4（per-canary 拆分）并非实际原因，但模拟显示若按 family=4 做 BH，所有 seed 都会得到 4/8（ece 全过、entropy 全不过）。

报告已写入 `artifacts/alpha_sweep_a050_s44/report/a050_3seed_reconciliation.md`。

---
