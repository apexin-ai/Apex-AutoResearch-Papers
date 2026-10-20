# check full status home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-status-home_20260514T051914_result.json`
- **Structured JSON:** [`60c05672621861c89154.json`](../../sessions/60/60c05672621861c89154.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### GPU 状态
- GPU 0: **100% 利用率**, 18429/32607 MiB
- 当前进程: `eval_repo_cls.py` — **v5 ckpt-4400** 正在运行 (PID 3039149, 已跑 ~15min)

### seed123 Sweep (完成)

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | Gap vs Majority |
|-----------|----------|----------|---------|---------|-----------------|
| **ckpt-400** | 75.05% | 67.47 | 51.77 | 83.17 | +2.1 pp |
| **ckpt-600** ★ | **80.73%** | **77.31** | **68.49** | **86.12** | **+7.78 pp** |
| **ckpt-800** | 74.27% | 66.03 | 49.31 | 82.76 | +1.32 pp |
| **ckpt-1000** | 73.14% | 52.10 | 20.36 | 83.85 | +0.18 pp |

**ckpt-600 是 seed123 的最优 checkpoint**。ckpt-800 和 ckpt-1000 严重退化——ckpt-1000 几乎退化到 majority baseline（recall_fail 仅 12.7%，模型基本丧失了识别 fail 的能力）。

### CLS v5 (seed42) Sweep

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | Gap vs Majority |
|-----------|----------|----------|---------|---------|-----------------|
| **ckpt-600** | 76.74% | 73.74 | 64.88 | 82.61 | +3.78 pp |
| **ckpt-4000** ★ | **81.51%** | 72.56 | 56.90 | 88.23 | **+8.55 pp** |
| **ckpt-4200** | 80.64% | 72.10 | 56.66 | 87.54 | +7.69 pp |
| **ckpt-4400** | ⏳ 运行中 | — | — | — | — |
| **ckpt-4600** | 未开始 | — | — | — | — |

### v4 Baseline
| Checkpoint | Accuracy | F1_macro |
|-----------|----------|----------|
| v4 ckpt-200 | 66.11% | 56.61 |

### 关键发现

1. **seed123 ckpt-800 最终 accuracy = 74.27%**（之前 partial 73.9% 基本吻合），ckpt-1000 = 73.14%，均远不如 ckpt-600
2. **seed123 过拟合明显**：ckpt-600 之后性能单调下降，ckpt-1000 的 fail recall 降至 12.7%
3. **v5 目前最优 = ckpt-4000**（accuracy 81.51%），ckpt-4200 略降，趋势类似 seed123 的过拟合模式
4. **v5 ckpt-600 的 F1_macro (73.74) 反而高于 ckpt-4000 (72.56)**——ckpt-600 fail recall 高达 79.44% 但 pass precision 牺牲较多
5. **GPU 0 忙**，ckpt-4400 eval 完还需跑 ckpt-4600

---
