# ops w41 kill dup and investigate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w41-kill-dup-and-investigate_20260527T134148_result.json`
- **Structured JSON:** [`68ba91ee54db4ea0a162.json`](../../sessions/68/68ba91ee54db4ea0a162.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### westd-41074: Kill 重复进程
- **PID 568159**: killed (force_killed) ✓
- **PID 561220**: alive, 仍在运行 ✓
- tmux session `eval_pi05_attn_k075_long_seed42_strict` 不存在（可能用了不同名称），已无残留
- GPU0: 11058MiB/97887MiB，显存已释放一份

### westd-27271: 两个实验均已自然完成
| 实验 | 状态 | success_rate | 耗时 |
|------|------|-------------|------|
| `pi05_random_k085_long_seed42_strict_w27` | **completed** | **44.0%** | 169.8min |
| `pi05_l2norm_k075_long_seed42_strict_w27` | **completed** | **70.8%** | 139.8min |

- 结果已保存: `eval_results/pi05_random_k0.85_libero_10_seed42.json`, `pi05_l2norm_k0.75_libero_10_seed42.json`
- GPU0/GPU1: 0MiB，完全空闲

### cqa1-33015: 实验仍在运行
- `eval_pi05_random_k09_long_seed43_strict_cqa1`: **alive** (PID 330510)
- 进度: Task 0, ep=40, 2/40=5% (刚启动于 21:08，正在跑)
- 不需要干预，w41 上有同实验备份

---
