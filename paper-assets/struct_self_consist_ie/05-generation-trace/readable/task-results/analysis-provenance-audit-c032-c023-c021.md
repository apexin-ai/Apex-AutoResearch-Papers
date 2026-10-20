# analysis provenance audit c032 c023 c021

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_provenance_audit_c032_c023_c021_20260516T045025_result.json`
- **Structured JSON:** [`7eb3feb7966ea06bb2f6.json`](../../sessions/7e/7eb3feb7966ea06bb2f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/provenance_audit_c032_c023_c021.md`。

**结论：三个不一致项全部是 provenance yaml / registry 过时，当前论文值均正确。**

| 项 | Provenance/Registry 值 | 当前论文值 | 真实来源 | 状态 |
|---|---|---|---|---|
| c032 LP cond RE ρ | 0.002 / 0.1457 | **0.011** | exp_012_rerun_1024 (正确 filter, n=238) | 论文已修正 |
| c023 RE SJ Q1/Q4 | Q1=0.447, Q4=0.540 | **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | 论文正确，registry 未更新 |
| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | 论文已修正，0.062 无法追溯 |

关键发现：
- **c032**：registry 的 0.1457 来自 exp_015_metrics_expansion 使用了错误的 conditional filter（any sample F1>0 而非 greedy_f1>0），当前论文的 0.011 使用正确 filter
- **c023**：registry 来自原始 exp_009（未做 gold-filtering），论文使用了 v2 rerun（gold-filtered 后 n=397）
- **c021**：0.062 仅存在于 artifacts/_project/paper/ 旧版本中，在所有实验输出中无法追溯

---
