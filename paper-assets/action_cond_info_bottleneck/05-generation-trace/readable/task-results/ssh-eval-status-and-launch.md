# ssh eval status and launch

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-status-and-launch_20260517T155234_result.json`
- **Structured JSON:** [`a759507747549c0bf36c.json`](../../sessions/a7/a759507747549c0bf36c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都还在运行中，两块 GPU 都被占用，无法启动 connector-only ablation。

## 状态汇报

### Eval 进程状态

| PID | α | GPU | 已运行 | 状态 |
|-----|---|-----|--------|------|
| 40598 | 0.0 | cuda:0 | 2h20m | 运行中 |
| 44022 | 1.0 | cuda:1 | 2h19m | 运行中 |

### 进度估算

两个 eval 都在相同进度位：
- **已完成**: `libero_spatial`（1/4 suites）
- **进行中**: `libero_object`（3/10 tasks done）
- **待做**: `libero_goal`, `libero_10`

每个 suite = 10 tasks × 50 episodes = 500 episodes。总计 2000 episodes/eval。
- 已完成: 500 + 150 = 650/2000 ≈ **32.5%**
- 已用 2h20m → 预计总时长 ~7.2h → **剩余约 4.9h**

### libero_spatial 中间结果（仅供参考，eval 未完成）

从已写出的 eval_info.json（仅 spatial suite）：
- **α=0.0 spatial**: task 0 成功率 = 39/50 = 78%（从 successes 数组计数）
- **α=1.0 spatial**: task 0 成功率 = 37/50 = 74%

### Connector-only ablation

**无法启动** — 两块 GPU 均被占用。需等 eval 完成（预计 ~5h 后）才能启动。

---
