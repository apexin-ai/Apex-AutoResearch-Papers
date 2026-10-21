# diagnosis 28034 eval status check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_28034-eval-status-check_20260521T073124_result.json`
- **Structured JSON:** [`6accddef1dfd9c6e91c3.json`](../../sessions/6a/6accddef1dfd9c6e91c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 0 (cuda:0) — ckpt5000-v2 ✅ 运行中
| 项目 | 值 |
|------|-----|
| PID | 497834 (nohup) |
| 进度 | **40/362** (11%) @ 15:29 |
| 速率 | ~20 pairs / 4.5 min |
| GPU 占用 | 16854MiB, util 18% |
| 预计完成 | **~16:43** |

### GPU 1 (cuda:1) — ckpt6000 ✅ 运行中
| 项目 | 值 |
|------|-----|
| PID | 498446 (tmux: exp-003-eval-ckpt6000) |
| 进度 | **20/362** (5.5%) @ 15:27 |
| 速率 | ~20 pairs / 5 min |
| GPU 占用 | 16854MiB, util 36% |
| 预计完成 | **~16:57** |

### GPU 2 (cuda:2) — ckpt6500 ✅ 运行中
| 项目 | 值 |
|------|-----|
| PID | 498584 (tmux: exp-003-eval-ckpt6500) |
| 进度 | **40/362** (11%) @ 15:32 |
| 速率 | ~20 pairs / 5 min |
| GPU 占用 | 16854MiB, util 24% |
| 预计完成 | **~16:53** |

### GPU 3 (cuda:3) — ⚠️ 冲突：两个进程抢 GPU

**旧进程 — ckpt7000 (非 v2)**
| 项目 | 值 |
|------|-----|
| PID | 498666 (tmux: exp-003-eval-ckpt7000) |
| 进度 | 20/362 (5.5%) @ 15:27 |
| exp_id | `exp003-ckpt7000`（不是 v2） |

**新进程 — ckpt7000-v2**
| 项目 | 值 |
|------|-----|
| PID | 500594 (tmux: exp-003-eval-ckpt7000-v2) |
| 进度 | **0/362** — 刚启动，还没出 progress |
| exp_id | `exp003-ckpt7000-v2` |

两个进程合计占 **29781MiB / 32607MiB (91%)**。ckpt7000-v2 的日志已出现 accelerate 内存不足警告：

> `no modules could be assigned to the following devices due to insufficient memory: - 0: 2489319424 bytes required`

### 结果产出
4 个当前 eval **均未完成**，results 目录中无 ckpt5000-v2 / ckpt6000 / ckpt6500 / ckpt7000-v2 的输出文件。

### 需要处理
**必须 kill 旧的 ckpt7000 (PID 498666)**，否则：
1. ckpt7000-v2 因 VRAM 不足可能 OOM 或跑得极慢
2. 旧的 ckpt7000 产出的 exp_id 是 `exp003-ckpt7000` 而非 v2，结果也不是你要的

建议执行：
```bash
kill 498666  # kill 旧 ckpt7000
tmux kill-session -t exp-003-eval-ckpt7000  # 清理旧 tmux
```

是否要我执行？

---
