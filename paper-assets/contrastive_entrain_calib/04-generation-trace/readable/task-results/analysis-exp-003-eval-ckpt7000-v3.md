# analysis exp 003 eval ckpt7000 v3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-ckpt7000-v3_20260521T095909_result.json`
- **Structured JSON:** [`3ad40799925bd54cd410.json`](../../sessions/3a/3ad40799925bd54cd410.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003-eval-ckpt7000-v3 结果

| Metric | Value |
|--------|-------|
| **ToF** | 0.0552 |
| **NoF** | 0.9724 |
| **SYCONScore** | **0.1046** |
| Pairs | 362 (valid=181, invalid=181) |
| 耗时 | 4390s (~73min) |
| 异常 | 无，全部 362 pairs 正常处理，退出码 0 |

### R3-only SYCONScore 完整轨迹

| Checkpoint | SYCONScore | 趋势 |
|------------|-----------|------|
| 1000 | 0.074 | |
| 2000 | 0.085 | ↑ |
| 3000 | 0.095 | ↑ |
| 4000 | 0.114 | ↑ |
| **4500** | **0.134** | ↑ peak (= vanilla baseline) |
| 5000 | 0.114 | ↓ |
| 5500 | 0.114 | → |
| 6000 | 0.085 | ↓↓ crash |
| 6500 | 0.153 | ↑↑ spike |
| **7000** | **0.105** | **↓ 回落** |

### 解读

ckpt-7000 SYCONScore=0.1046，相比 ckpt-6500 的 0.1529 大幅回落（-31.6%），回到 ckpt-2000~3000 水平。这完美印证了 **late instability** 叙事：ckpt-6000 crash → ckpt-6500 spike → ckpt-7000 再次下跌，呈现剧烈振荡而非收敛。R3-only 在越过 vanilla ceiling (ckpt-4500) 后无法稳定保持，后期训练表现为高方差振荡。

---
