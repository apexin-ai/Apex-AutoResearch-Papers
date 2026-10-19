# ops check download and verify

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-download-and-verify_20260521T055102_result.json`
- **Structured JSON:** [`7d65de9dfe30da3c6c7e.json`](../../sessions/7d/7d65de9dfe30da3c6c7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`pareto_analysis.py` 不存在于服务器上。服务器 `/root/xling_calib_direction/` 下的 .py 文件：

```
analyze_results.py
compute_cka.py
extract_activations.py
extract_activations_large.py
temp_scaling.py
temp_scaling_fixed.py
temp_scaling_l27.py
train_caclr.py
train_probe.py
transfer_eval.py
```

没有 `pareto_analysis.py`。需要先在本地创建并推送到服务器，或者确认该脚本是否在其他位置。

---
