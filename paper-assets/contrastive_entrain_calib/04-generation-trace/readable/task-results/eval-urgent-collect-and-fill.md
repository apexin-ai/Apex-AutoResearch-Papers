# eval urgent collect and fill

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_urgent-collect-and-fill_20260523T053146_result.json`
- **Structured JSON:** [`a3489f4bf68dc1430748.json`](../../sessions/a3/a3489f4bf68dc1430748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 已启动。汇报如下：

---

## 1. 所有 Eval 结果汇总

### exp-002v3 (ACT baseline v3)
| Checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| 500 | 0.0 | 1.0 | 0.0 |
| 1000 | 0.0 | 1.0 | 0.0 |
| 1500 | 0.0 | 1.0 | 0.0 |
| 2000 | 0.0 | 1.0 | 0.0 |

### exp-003 gs8 (r3only)
| Checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| 500 | 0.0552 | 0.9558 | 0.1045 |
| 500-verified | 0.0442 | 0.9392 | 0.0844 |
| 1000 | 0.0442 | 0.9558 | 0.0845 |
| **1500** | **0.0276** | **0.9945** | **0.0538** |

### exp-003 s2 (r3only seed2)
| Checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| 7500 | 0.0608 | 0.9669 | 0.1144 |
| 8000 | 0.0608 | 0.9613 | 0.1143 |

### exp-004 reduced-lora
| Checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| 500 | 0.0829 | 0.884 | 0.1515 |
| 1000 | 0.0939 | 0.895 | 0.1700 |
| 1500 | 0.0884 | 0.9171 | 0.1613 |
| 2000 | 0.116 | 0.884 | 0.2051 |
| 2500 | 0.0939 | 0.9282 | 0.1706 |
| 3000 | 0.0939 | 0.9227 | 0.1705 |
| 3500 | 0.105 | 0.9061 | 0.1881 |
| 4000 | 0.116 | 0.884 | 0.2051 |
| **4500** | **0.1602** | **0.8729** | **0.2707** |
| ~~5000~~ | — | — | eval 刚启动 |
| **5500** | **0.1492** | **0.8674** | **0.2546** |
| 6000 | 0.1215 | 0.8564 | 0.2129 |
| ~~6500~~ | — | — | eval 刚启动 |

### exp-004 s2 (ACT baseline s2)
| Checkpoint | ToF | NoF | SYCONScore |
|---|---|---|---|
| 2000 | 0.1215 | 0.8895 | 0.2139 |
| 2500 | 0.1215 | 0.8674 | 0.2132 |
| 3000 | 0.1492 | 0.8619 | 0.2543 |
| 5000 | 0.1436 | 0.9061 | 0.2480 |
| 5500-v2 | 0.1326 | 0.8785 | 0.2304 |
| 6000-v2 | 0.1547 | 0.8674 | 0.2626 |
| 6500 | 0.1492 | 0.8619 | 0.2543 |
| **7000** | **0.1713** | **0.8619** | **0.2858** ← 最高 |
| 7500 | 0.1602 | 0.8674 | 0.2705 |

---

## 2. GPU 状态 (28034)

| GPU | 占用 | 当前任务 |
|---|---|---|
| **0** | **刚启动** | eval reduced-lora ckpt5000 (PID 842515) |
| **1** | 21.7 GB | reduced-lora 训练 (PID 30011) |
| **2** | 13.0 GB | **卡住** — PID 165317 是 s2-ckpt2500 eval，结果已写完但进程未退出，占着 GPU。需要 `kill 165317` 释放 |
| **3** | **刚启动** | eval reduced-lora ckpt6500 (PID 879142) |

---

## 3. 新启动的 Eval

| GPU | Checkpoint | PID | 日志 |
|---|---|---|---|
| 0 | reduced-lora ckpt5000 | 842515 | `/tmp/eval_reduced_lora_ckpt5000.log` |
| 3 | reduced-lora ckpt6500 | 879142 | `/tmp/eval_reduced_lora_ckpt6500.log` |

---

## 4. Reduced-lora 训练进度

**Step 6500/8000** (81.25%)，刚保存 checkpoint-6500 到 `/root/autodl-tmp/outputs/exp-004-reduced-lora/checkpoint-6500`。loss 趋于 0（sft=0.0, total=0.0002），预计约 1.5 小时完成。

---

## 5. 注意事项

- **GPU 2 卡住**：PID 165317 的 s2-ckpt2500 eval 已完成但进程未退出，占 13GB 显存。`kill 165317` 后可再启动一个 eval。
- **gs8 无新 checkpoint**：29046 上 `exp003_gs8_r3only` 目录无 checkpoint。29046 上有的是 `exp003_r3only_seed1`（500-8000）和 `exp003_r3only_seed2`（500-8000），以及 `exp-004-act-baseline-s2/checkpoint-2000`。是否需要 SCP 这些？
- **reduced-lora 峰值在 ckpt4500**（SYCON=0.2707），ckpt5500 略回落（0.2546），ckpt6000 进一步下降（0.2129）。ckpt5000 和 6500 的 eval 正在跑，可确认趋势。

---
