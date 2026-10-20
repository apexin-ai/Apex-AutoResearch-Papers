# code sva topk check results

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sva-topk-check-results_20260513T075728_result.json`
- **Structured JSON:** [`52089f54ab443bb20553.json`](../../sessions/52/52089f54ab443bb20553.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已无活跃任务，无需清除。

---

**实验 mvp_sva_gpt2_k3_topk 已完成，结论：negative**

关键发现：
- 条件①②③全部 PASS（三方法 Jaccard 低、CSS≥2/3 有 98 条边、CSS=1.0 有 44 条边）
- **条件④ FAIL**：zero ablation 下 CSS=1.0 的 CPR(-0.70) 劣于 eap_ig(-0.35) 和 edge_pruning(-0.65)，仅优于 acdc(-1.12)。mean ablation 下 CSS=1.0 CPR(1.18) 虽略优于所有单方法，但 zero ablation 不满足
- 核心问题：44 条 CSS=1.0 边在 zero ablation 下 faithfulness 不足以超过单方法 top-100 电路

Registry 已更新：metrics、conclusion=negative、status=DONE、checkpoint_path、log_path。

---
