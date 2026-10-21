# fix kill persuite redeploy bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-persuite-redeploy-bjb1-18228_20260524T091421_result.json`
- **Structured JSON:** [`f54f4b15c998ea275290.json`](../../sessions/f5/f54f4b15c998ea275290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### CRM 训练 Kill
- 状态：**已无 CRM 训练进程**（之前已被 kill，无残留 tmux session）
- GPU 1+2 已释放（0 MiB used）

### 新 Eval 部署
| Session | GPU | 状态 |
|---|---|---|
| `long-vla-s47-r3` | GPU 1 | RUNNING，已加载 LIBERO long 10 tasks |
| `goal-vla-s47-r2` | GPU 2 | RUNNING，已加载 LIBERO goal 10 tasks |

GPU 显存确认：GPU 1 = 6282 MiB, GPU 2 = 5508 MiB（模型已加载）

### Registry
- `eval-supp-long-vla-only-s47-r3` → RUNNING（parent: eval-supp-long-vla-only-s47-r2）
- `eval-supp-goal-vla-only-s47-r2` → RUNNING（parent: eval-supp-goal-vla-only-s47）

### Precompute 进度
| Benchmark | GPU | 进度 | 预计剩余 |
|---|---|---|---|
| **Object** | 0 | 71200/72507 = **98.2%** | ~41 min |
| **Long** | 3 | 68600/136090 = **50.4%** | ~36.2 h |

Object precompute 即将完成（< 1h），Long 仍需约 1.5 天。

---
