# code fix d111 direction m035

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_d111_direction_m035_20260520T024329_result.json`
- **Structured JSON:** [`65264262dce33fe012c0.json`](../../sessions/65/65264262dce33fe012c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成，无遗漏。

## 修改汇总

### westd-17855: `batch_analysis.py` (4 处)

| 行号 | 修改前 | 修改后 | 位置 |
|------|--------|--------|------|
| 376 | `(r["naive_xcorr"].get("peak_lag") or 0) > 0` | `< 0` | `compute_consensus()` |
| 379 | `(r["diff_xcorr"].get("peak_lag") or 0) > 0` | `< 0` | `compute_consensus()` |
| 453 | `(p["results"].get("naive_xcorr", {}).get("peak_lag") or 0) > 0` | `< 0` | `analyze()` naive_fwd 计数 |
| 457 | `(p["results"].get("diff_xcorr", {}).get("peak_lag") or 0) > 0` | `< 0` | `analyze()` diff_fwd 计数 |

### westd-19828: `run_5method_analysis.py` (1 处)

| 行号 | 修改前 | 修改后 | 位置 |
|------|--------|--------|------|
| 436 | `f["naive_xcorr"]["peak_lag"] > 0` | `< 0` | consensus 投票 |

### 未修改
- `method_ablation.py` (19828) — 仅有 `peak_lag` 赋值，无方向判断
- 两台服务器备份文件：`*.bak_m035`

---
