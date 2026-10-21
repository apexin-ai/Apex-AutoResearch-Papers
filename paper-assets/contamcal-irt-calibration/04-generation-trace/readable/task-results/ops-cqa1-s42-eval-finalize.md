# ops cqa1 s42 eval finalize

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-s42-eval-finalize_20260519T211051_result.json`
- **Structured JSON:** [`137c994ff908abd5b109.json`](../../sessions/13/137c994ff908abd5b109.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。Cron 列表在本 session 为空（cron 不在当前 session 中），无需删除。

---

**汇总：**

**Qwen-7B s42 eval 结果（5/5 成功）：**

| Dosage | MMLU (s42) | ARC (s42) | MMLU (s123) | ARC (s123) | Δ MMLU | Δ ARC |
|--------|-----------|----------|------------|-----------|--------|-------|
| d000 | 66.14% | 87.97% | 66.59% | 87.20% | -0.45 | +0.77 |
| d005 | 64.82% | 86.18% | 63.37% | 82.51% | +1.45 | **+3.67** |
| d025 | 63.06% | 83.79% | 64.82% | 85.15% | -1.76 | -1.36 |
| d050 | 63.10% | 84.56% | 65.00% | 84.64% | -1.90 | -0.08 |
| d100 | 64.32% | 84.73% | 66.59% | 84.73% | -2.27 | 0.00 |

- Registry: `eval_qwen7b_s42_cqa1_v2` → DONE/success，含完整 metrics 和 seed 对比
- Cron: 本 session 无活跃 cron job（若 cron 在其他 session 创建，需在该 session 中删除）

d005 ARC 的 +3.67pp seed 间差异较大，其余 dosage 差异合理（≤2.3pp MMLU, ≤1.4pp ARC）。

---
