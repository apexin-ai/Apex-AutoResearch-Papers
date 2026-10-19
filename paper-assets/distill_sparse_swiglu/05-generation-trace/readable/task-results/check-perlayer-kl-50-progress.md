# check perlayer kl 50 progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_perlayer_kl_50_progress_20260522T064422_result.json`
- **Structured JSON:** [`3cb222d931c7d651514b.json`](../../sessions/3c/3cb222d931c7d651514b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 训练进度
| 项目 | 值 |
|------|-----|
| 当前 step | **9700 / 10000** (97%) |
| avg_kl | 0.0280 |
| sparsity | 0.500 |
| lambda | 2048.00 |
| tau | 0.127 |
| lr | 2.26e-06 |
| 进程 PID | 359449, 运行 4h57m, CPU 100% |

### ETA
- 每 100 steps 约 182s（基于 step 9600→9700 的 dt 差值）
- 剩余 300 steps → **预计约 9 分钟后完成**

### 已保存 Checkpoint（每 2000 步，各 ~456MB）
1. `predictor_perlayer_kl_step_2000.pt` — 10:49
2. `predictor_perlayer_kl_step_4000.pt` — 11:49
3. `predictor_perlayer_kl_step_6000.pt` — 12:50
4. `predictor_perlayer_kl_step_8000.pt` — 13:51

step 10000 的 final checkpoint 尚未保存，预计几分钟后生成。

### SCP 通路
**可用。** westd-34887 通过 `ssh -p 41718 root@connect.westd.seetacloud.com` 成功连接 westd-41718 并列出 checkpoint 目录。

---
