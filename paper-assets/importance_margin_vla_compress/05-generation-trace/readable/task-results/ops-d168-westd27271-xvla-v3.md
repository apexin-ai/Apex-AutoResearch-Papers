# ops d168 westd27271 xvla v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d168_westd27271_xvla_v3_20260522T142011_result.json`
- **Structured JSON:** [`3b0c041633be47fbcd4b.json`](../../sessions/3b/3b0c041633be47fbcd4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报：两卡均已占满，所有请求实验已在排队中

### GPU 0 — 当前 + 排队
| Session | 状态 | 内容 |
|---------|------|------|
| `xvla_spatial` | **运行中** | Spatial baseline (Task 5/10, ep ~5/50)，后续链：L2norm k=0.95→0.9→0.7 |
| `xvla_long` | **等待中** | 等 spatial 结束后自动启动：Long baseline → L2norm k=0.95→0.9→0.7 |

### GPU 1 — 当前 + 排队
| Session | 状态 | 内容 |
|---------|------|------|
| `xvla_goal` | **运行中** | Goal baseline (Task 6/10, ep进行中)，后续链：L2norm k=0.95→0.9→0.7 |
| `xvla_random` | **等待中** | 等 goal 结束后自动启动：Random 全套 4 suites × 3 ratios (Object→Spatial→Goal→Long, k=0.95/0.9/0.7) |

### Spatial baseline 中间结果
- Task 2: 100%, Task 3: 98%, Task 4: 90%, Task 5: 进行中

### Goal baseline 中间结果  
- Task 2: 96%, Task 3: 98%, Task 4: 100%, Task 5: 96%, Task 6: 进行中

### 结论
**无需新部署。** 你请求的 Goal (baseline + L2norm + Random) 和 Long (baseline + L2norm + Random) 全部已在现有 4 个 tmux session 的执行链中覆盖。两卡满负荷运转，`xvla_long` 和 `xvla_random` 各自 poll 等待前序任务完成后自动接力。

注意：`xvla_random` 跑完 Object+Spatial Random 后才轮到 Goal Random 和 Long Random，所以 Long Random 会在整个链的最后才执行。如果想让 Long Random 更早完成，需要等 GPU 0 空出后单独部署。

---
