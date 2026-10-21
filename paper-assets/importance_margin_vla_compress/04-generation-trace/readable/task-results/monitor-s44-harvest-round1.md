# monitor s44 harvest round1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_s44-harvest-round1_20260527T230940_result.json`
- **Structured JSON:** [`fe4e2c76f04f74069ee6.json`](../../sessions/fe/fe4e2c76f04f74069ee6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集全部数据。汇总如下：

---

### westd-27271 (2× H800)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 10.7/97.9 GB | 42% |
| 1 | 10.7/97.9 GB | 38% |

**已完成实验 (有 RESULT):**
| 实验 | 结果 | 状态 |
|------|------|------|
| OV l2norm k=0.9 goal seed43 v3 | **Overall SR=75.2%** | EXIT_CODE=0, tmux 还在 ⚠️ 可收割 |
| π0.5 attn k=0.85 Long seed43 v2 | **SR=52.4%** | 已完成 |
| π0.5 attn k=0.75 Long seed43 v2 | **SR=49.0%** | 已完成 |

**运行中:**
| GPU | 实验 | 进度 | 当前位置 |
|-----|------|------|----------|
| 0 | π0.5 l2norm k=0.75 Long seed44 | T6/10 (71.1%) | T6 ep=50 完成, 进入 T7 |
| 1 | π0.5 l2norm k=0.7 Long seed44 | T6/10 (69.7%) | T6 ep=40 |

---

### cqa1-33015 (4× 4090)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 20.5/24.6 GB | 97% |
| 1 | 9.8/24.6 GB | 0% |
| 2 | 10.6/24.6 GB | 5% |
| 3 | 0/24.6 GB | 0% |

**已完成实验 (有 RESULT):**
| 实验 | 结果 | 状态 |
|------|------|------|
| π0.5 l2norm k=0.5 Long seed43 | **SR=52.8%** | EXIT_CODE=0 ✅ |
| π0.5 attn k=0.75 Long seed43 | **SR=52.0%** | EXIT_CODE=0 ✅ |
| π0.5 l2norm k=0.9 Long seed44 | **SR=80.4%** | EXIT_CODE=0 ✅ |

**运行中:**
| GPU | 实验 | 进度 | 当前位置 |
|-----|------|------|----------|
| ~2 | π0.5 attn k=0.9 Long seed44 | T6/10 (69.1%) | T6 ep=50 完成 |
| ~0 | π0.5 random k=0.5 Long seed44 | T2/10 | T2 ep=40 |
| ? | π0.5 random k=0.95 Long seed44 | T0/10 | T0 ep=30 (~53%) |
| ? | π0.5 l2norm k=0.95 Long seed44 | T1/10 | T1 ep=10 |

---

### westd-38929 (4× H800)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 31.6/97.9 GB | 92% |
| 1 | 10.5/97.9 GB | 31% |
| 2 | 0/97.9 GB | 0% |
| 3 | 0/97.9 GB | 0% |

**已完成实验 (有 RESULT):**
| 实验 | 结果 | 状态 |
|------|------|------|
| π0.5 attn k=0.5 Long seed43 | **SR=48.8%** | EXIT_CODE=0 ✅ |
| π0.5 l2norm k=0.5 Long seed44 | **SR=52.6%** | EXIT_CODE=129 (HUP killed) ⚠️ |

**运行中:**
| GPU | 实验 | 进度 | 当前位置 |
|-----|------|------|----------|
| 0 | π0.5 attn k=0.85 Long seed44 | T6/10 (69.1%) | T6 ep=50 完成 |
| 1 | π0.5 random k=0.7 Long seed44 | T3/10 | T3 ep=30 |
| 0? | π0.5 attn k=0.5 Long seed44 | T5/10 (76.4%) | T5 ep=20 |
| 0? | π0.5 l2norm k=0.85 Long seed44 | T3/10 | T3 ep=40 |

> GPU 0 显存 31.6GB 偏高，可能同时跑了多个实验。

---

### westd-41074 (4× H800)
**GPU状态:**
| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 10.3/97.9 GB | 43% |
| 1 | 10.3/97.9 GB | 47% |
| 2 | 10.6/97.9 GB | 37% |
| 3 | 10.7/97.9 GB | 35% |

**已完成实验 (有 RESULT):**
| 实验 | 结果 | 状态 |
|------|------|------|
| π0.5 attn k=0.5 Long seed43 | **SR=49.4%** | EXIT_CODE=0 ✅ |
| π0.5 random k=0.9 Long seed44 | **SR=31.8%** | EXIT_CODE=0 ✅ |
| OV random k=0.5 object seed42 v2 | **Overall SR=35.6%** | 刚完成, tmux 还在 ⚠️ 可收割 |

**运行中:**
| GPU | 实验 | 进度 | 当前位置 |
|-----|------|------|----------|
| ? | π0.5 random k=0.85 Long seed44 | T7/10 (44.5%) | T7 ep=50 完成, 进入 T8 |
| ? | π0.5 random k=0.75 Long seed44 | T3/10 | T3 ep=30 |
| ? | π0.5 attn k=0.95 Long seed44 | T5/10 (89.6%) | T5 ep=40 |
| ? | π0.5 attn k=0.75 Long seed44 | T3/10 (73.3%) | T3 ep=40 |

---

## 关键提醒

**可收割（已完成但 tmux/进程可能还在）：**
- westd-27271: OV l2norm k=0.9 goal seed43 → SR=75.2%
- westd-41074: OV random k=0.5 object seed42 → SR=35.6%

**时间风险（距 deadline 12:00 UTC 还剩 ~5h）：**
- cqa1 上 random k=0.5/k=0.95 和 l2norm k=0.95 都刚起步（T0-T2），预计需 5-6h，**可能超时**
- westd-38929/41074 上 T3 阶段的实验预计需 3-4h，应能赶上

**异常：**
- westd-38929 π0.5 l2norm k=0.5 seed44 的 EXIT_CODE=129 (SIGHUP)，但 RESULT 行已输出，数据应该完整

---
