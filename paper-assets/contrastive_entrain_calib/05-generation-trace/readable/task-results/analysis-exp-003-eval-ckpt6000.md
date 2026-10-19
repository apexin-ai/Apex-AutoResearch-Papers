# analysis exp 003 eval ckpt6000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-eval-ckpt6000_20260521T085004_result.json`
- **Structured JSON:** [`8f2b326c11e2a678761e.json`](../../sessions/8f/8f2b326c11e2a678761e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-003-eval-ckpt6000 结果

### ckpt-6000 指标
- **SYCONScore: 0.0846** (谷底)
- ToF: 0.0442
- NoF: 0.9724
- 样本数: 362/362，正常完成

### 完整轨迹

| Checkpoint | SYCONScore | ToF | NoF | vs 上一步 |
|------------|-----------|------|------|----------|
| ckpt-1000 | 0.0743 | 0.0387 | 0.9448 | — |
| ckpt-2000 | 0.0846 | 0.0442 | 0.9834 | +13.8% |
| ckpt-3000 | 0.0946 | 0.0497 | 0.9724 | +11.8% |
| ckpt-4000 | 0.1144 | 0.0608 | 0.9669 | +20.9% |
| **ckpt-4500** | **0.1337** | 0.0718 | 0.9613 | +16.9% |
| ckpt-5000 | 0.1144 | 0.0608 | 0.9669 | -14.4% |
| ckpt-5500 | 0.1144 | 0.0608 | 0.9724 | 0% |
| **ckpt-6000** | **0.0846** | 0.0442 | 0.9724 | **-26.0%** |
| ckpt-6500 | 0.1529 | 0.0829 | 0.9834 | **+80.7%** |

### 轨迹判断: V 形反弹，ckpt-6000 是谷底

ckpt-6000 是整条轨迹的**最低点**（回退到 ckpt-2000 水平，比 vanilla baseline 0.134 低 37%）。但 ckpt-6500 大幅反弹至 **0.1529**，超过了此前 peak (ckpt-4500=0.1337) 14%，也超过了 vanilla baseline。

训练在 5000-6000 步经历性能低谷后恢复，呈明显的 V 形。ckpt-6500 是当前新 peak。

产出已写入 `artifacts/exp-003/eval-ckpt6000-results.md`。

---
