# code ioi size controlled check bootstrap

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ioi-size-controlled-check-bootstrap_20260513T114919_result.json`
- **Structured JSON:** [`9bf347e4c998df749d87.json`](../../sessions/9b/9bf347e4c998df749d87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step 1 — ioi_size_controlled_baseline: DONE (negative)**
- CSS=1.0 (N=16): mean CPR=0.177, zero CPR=0.0295
- EAP-IG top-16: mean CPR=0.182, EP top-16: mean CPR=0.1832
- **css_vs_best_single=FAIL** — 控制边数后 CSS 融合不优于最佳单方法
- css_vs_random=MARGINAL — 仅略优于随机
- Registry 已更新为 DONE/negative

**Step 2 — Registry 已更新**，含完整 notes

**Step 3 — bootstrap_ci_ioi: 已提交**
- PID 34588，tmux session `bootstrap_ci_ioi`，cuda:0
- 日志: `/root/runs/min_necessary_circuit_css/bootstrap_ci_ioi.log`
- IOI 缓存三文件齐全（cache_acdc.json / cache_eap_ig.json / cache_edge_pruning.json）
- Registry 状态: RUNNING

---
