# ops audit westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd41074_20260522T025707_result.json`
- **Structured JSON:** [`746e7b8be65d2ea7f37e.json`](../../sessions/74/746e7b8be65d2ea7f37e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。以下是完整报告。

---

## westd-41074 审计报告

### 1. GPU 状态

| GPU | 进程 | 显存 | 利用率 | 状态 |
|-----|------|------|--------|------|
| 0 | PID 922854 (k=0.95 spatial, 42min) + PID 943114 (k=0.95 spatial **v2**, 25min) | 21.3/97.9 GB | 45% | **重复** |
| 1 | PID 922934 (k=0.85 object s43 v3, 42min) + PID 942398 (k=0.925 spatial, 25min) | 21.2/97.9 GB | 66% | 双实验共享 |
| 2 | PID 68539 (M96 train) | 28.6/97.9 GB | 0%\* | 正常 |
| 3 | PID 59671 (M64v6 train) | 27.5/97.9 GB | 0%\* | 正常 |

\*GPU 2/3 进程活跃(CPU 315%/327%)，瞬时利用率为0可能是数据加载阶段。

**GPU 0 关键问题**: PID 922854 是原始 k095 崩溃(n_episodes=500)后的非 registry 重试，PID 943114 是正式 v2。两个进程跑**完全相同**的实验（random k=0.95 spatial seed42 50eps），且日志交叉污染 v2 log，导致结果归属不确定。

### 2. n_episodes Bug 检查

- **代码逻辑无覆盖 bug**: `args.n_episodes` 在 for loop (L217) 和 SR 计算 (L274) 中直接使用，无隐式覆盖
- **存在验证缺失**: `init_states` 只有 50 条，若 `--n_episodes > 50`，L220 `init_states[ep]` 会 IndexError
- **已触发**: 原始 k095 run 用了 `--n_episodes 500`，在 T0 ep=50 崩溃:
  ```
  IndexError: index 50 is out of bounds for axis 0 with size 50
  ```
- **当前运行实验**: 全部 `--n_episodes 50`，不受影响

### 3. Eval 进度（均未完成，无法收割最终结果）

**k=0.95 spatial seed42 v2** (GPU 0, PID 943114):
| Task | SR |
|------|----|
| T0 pick up bowl between plate | 100% |
| T1 pick up bowl next to ramek | 88% |
| T2 pick up bowl from table center | 94% |
| T3+ | 进行中（日志被 PID 922854 污染，结果不可靠） |

**k=0.925 spatial seed42** (GPU 1, PID 942398):
| Task | SR |
|------|----|
| T0 pick up bowl between plate | 94% |
| T1 pick up bowl next to ramek | 48% |
| T2+ | 进行中 (ep=10, ~80%) |

**k=0.85 object seed43 v3** (GPU 1, PID 922934) — 确认 cliff:
| Task | SR |
|------|----|
| T0 alphabet soup | 4% |
| T1 cream cheese | 6% |
| T2 salad dressing | 2% |
| T3 bbq sauce | 0% (ep=20) |

### 4. 空闲 GPU 部署

**无空闲 GPU**，4 张全部占用。

### 5. 建议操作

1. **Kill PID 922854** (GPU 0 孤儿进程) — 与 v2 重复，日志交叉污染
2. **修复 eval 代码 L217**: 加 `n_episodes = min(args.n_episodes, len(init_states))` 防止 IndexError 重现
3. 等 eval 完成后重新收割结果（预计 k=0.95 v2 还需 ~40min, k=0.925 还需 ~60min）

### Registry 更新已完成
- `eval_pi05_random_k095_spatial_seed42_v2`: PREPARING → RUNNING
- `eval_pi05_random_k0925_spatial_seed42`: PREPARING → RUNNING
- `eval_pi05_random_k085_object_seed43_v3`: PREPARING → RUNNING

---
