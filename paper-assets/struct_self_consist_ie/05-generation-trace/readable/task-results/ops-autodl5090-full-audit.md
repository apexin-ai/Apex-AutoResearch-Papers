# ops autodl5090 full audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_autodl5090-full-audit_20260514T174157_result.json`
- **Structured JSON:** [`086b3f2c5a7b218af5e0.json`](../../sessions/08/086b3f2c5a7b218af5e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/audit_autodl5090_loop3.md`。

**汇总**：autodl-5090 上 4 个实验全部已完成，4 GPU 完全空闲（0% 利用率）。

| 实验 | Registry 状态 | 实际 | Verdict |
|------|-------------|------|---------|
| exp_017_llama_conll_infer | RUNNING | **DONE** | MARGINAL (structural>surface +0.004) |
| exp_001_seed456_v2_ner | RUNNING | **DONE** | MARGINAL (structural>surface +0.16) |
| exp_003_wnut17_v2_infer | ANALYZING | **DONE** | FAIL (54% F1=0, structural<surface) |
| exp_002_merge_conll2003 | PREPARING | **DONE** | exit 0 |

4 个都需要在 Registry 标记为 DONE。wnut17 因 54% 样本 F1=0 建议 T=0.7 重跑。

---
