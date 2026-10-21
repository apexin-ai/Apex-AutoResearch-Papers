# critical tau sweep nmin factcheck

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_tau_sweep_nmin_factcheck_20260516T030729_result.json`
- **Structured JSON:** [`ac94f6871aac44743b96.json`](../../sessions/ac/ac94f6871aac44743b96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确。5 个实验全部使用 **n_min=2**。

```
[tau_05_seed42] n_min=2
证据: "  n_min: 2"
来源: /root/runs/provenance_weight_training/tau_05_seed42.log:16

[tau_06_seed42] n_min=2
证据: "  n_min: 2"
来源: /root/runs/provenance_weight_training/tau_06_seed42.log:16

[tau_07_seed42] n_min=2
证据: "  n_min: 2"
来源: /root/runs/provenance_weight_training/tau_07_seed42.log:16

[tau_09_seed42] n_min=2
证据: "  n_min: 2"
来源: /root/runs/provenance_weight_training/tau_09_seed42.log:16

[tau_095_seed42] n_min=2
证据: "  n_min: 2"
来源: /root/runs/provenance_weight_training/tau_095_seed42.log:16
```

**补充上下文**：代码默认逻辑是 `n_min = max(2, batch_size // 2)`（`pretrain_weighted.py:302-303`）。这 5 个实验 batch_size=4，所以 `max(2, 4//2) = max(2, 2) = 2`。声称 n_min=3 的报告是错误的——那个值只有在 batch_size=6 时才会出现。

---
