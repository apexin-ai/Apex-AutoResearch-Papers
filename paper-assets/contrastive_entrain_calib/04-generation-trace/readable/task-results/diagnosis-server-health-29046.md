# diagnosis server health 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_server-health-29046_20260520T033344_result.json`
- **Structured JSON:** [`922f0475c84f4fe1f254.json`](../../sessions/92/922f0475c84f4fe1f254.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 状态
| GPU | 型号 | 利用率 | 显存占用 | 占用进程 |
|-----|------|--------|---------|---------|
| 0 | RTX PRO 6000 Blackwell | 81% | 38049/97887 MiB | PID 237437 (exp-003-s2) |
| 1 | RTX PRO 6000 Blackwell | 98% | 38161/97887 MiB | PID 70649 (exp-003) |

### 实验进程状态

**exp-003** (R3-only GRPO baseline) — **ALIVE**
- PID 70649, GPU 1, 运行 1天10小时42分
- 进度: step 3760/8000 (47%)
- 最后日志: 2026-05-20 05:55 (约5.5小时前)
- reward/r3_mean 在 0.37-0.87 间波动，combined_mean=0.6972 @step3760
- ⚠️ 日志 5.5 小时未更新，但 GPU 利用率 98%。可能在做 eval/checkpoint，或 tee 缓冲未刷新。进程本身活跃。

**exp-003-s2** (R3-only seed 2) — **ALIVE**
- PID 237432 (wrapper bash), 实际训练进程 PID 237437, GPU 0, 运行 3小时16分
- 进度: step 219/8000 (3%)
- 最后日志: 2026-05-20 11:33 (刚刚)
- ~27-50s/step，reward/dc_grpo_reward/mean 在 0.48-0.61 间
- 训练正常推进

### Ghost Process 检查

**无 ghost process。** GPU 上只有两个进程（PID 70649 和 237437），均属于已知实验。

其他非 GPU 进程中有一个遗留的 HTTP server（PID 71933, 来自 `/root/mvp_v2_1_expanded/`，监听 19876 端口），不占 GPU，无害。

### 需关注

exp-003 的日志 5.5 小时无新输出。GPU 利用率 98% 说明进程在工作，最可能是进入了 eval/checkpoint 阶段或 tee 缓冲区未 flush。建议过一段时间再查日志确认 step 是否推进。

---
