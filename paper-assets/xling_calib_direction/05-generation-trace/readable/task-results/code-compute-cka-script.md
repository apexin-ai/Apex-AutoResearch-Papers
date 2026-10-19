# code compute cka script

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_compute_cka_script_20260521T024843_result.json`
- **Structured JSON:** [`92527dcfe8eea1e9d20c.json`](../../sessions/92/92527dcfe8eea1e9d20c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出：**
- `code/compute_cka.py` — Linear CKA 计算脚本，已同步到服务器并验证
- `artifacts/compute_cka_verified.md` — 验证报告

**验证结果：** 40 组 CKA 值与已有 `cka_results.csv` 偏差均 < 0.0004（float32 精度差异），算法实现正确。

关键发现：CKA 在中间层 12-16 达峰值（~0.74-0.76），顶层 27 降至 0.24——跨语言表示相似性在接近输出时急剧下降。

---
