# ops d166 westd38929 pi05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d166_westd38929_pi05_20260522T131303_result.json`
- **Structured JSON:** [`321b2f923ddaf078f1fb.json`](../../sessions/32/321b2f923ddaf078f1fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，所有实验已正常启动。

### 汇报

**tmux sessions**:
| Session | GPU | PID | 内容 |
|---------|-----|-----|------|
| `pi05_long_l2norm` | cuda:0 | 168370 | L2norm k=0.95→0.9→0.85, libero_10 (Long), 500eps |
| `pi05_goal_l2norm` | cuda:3 | 168452 | L2norm k=0.95→0.9, libero_goal, 500eps |

**GPU 状态** (4 GPU 全占):
| GPU | 显存 | 任务 |
|-----|------|------|
| cuda:0 | 10772 MiB | pi05_long_l2norm (新) |
| cuda:1 | 1 MiB | baseline_goal **刚结束** (之前 10560 MiB) |
| cuda:2 | 10075 MiB | baseline_long (继续) |
| cuda:3 | 10194 MiB | pi05_goal_l2norm (新) |

**Goal baseline 进度**: Task 9/10 进行中（总 437/450=97.1%），看显存已释放(1 MiB)，**可能刚跑完**。

**早期日志**:
- Long: `[PRUNE-DIAG] l2norm: n_keep=243/256` — 保留 95% tokens ✓
- Goal: `[PRUNE-DIAG] l2norm: n_keep=243/256` — 保留 95% tokens ✓
- 两个都已进入 episode 执行阶段

**注意**: cuda:1 显存已降至 1 MiB，baseline_goal 可能已完成。可检查其最终结果日志。

---
