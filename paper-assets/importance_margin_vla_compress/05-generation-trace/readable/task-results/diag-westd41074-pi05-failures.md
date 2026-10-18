# diag westd41074 pi05 failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd41074_pi05_failures_20260521T092406_result.json`
- **Structured JSON:** [`ed3cb64fa076a9d8065a.json`](../../sessions/ed/ed3cb64fa076a9d8065a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**两个实验都已成功完成，不是真正的失败。** 进程正常退出，结果已保存到磁盘。被标记为 "failed" 是因为缺少 sentinel/W&B 上报，但评测本身跑完了全部 10 tasks × 50 episodes。

### 实验 1: eval_pi05_random_k03_object_seed42
- **状态**: 已完成
- **结果**: `libero_object prune=random keep=0.3 SR=36.4%` (182/500)
- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.30_libero_object.json`（17:12 写入）
- **耗时**: 106.5 分钟

逐任务成绩：
| Task | SR |
|------|----|
| T0 alphabet soup | 62% |
| T1 cream cheese | 18% |
| T2 salad dressing | 48% |
| T3 bbq sauce | 32% |
| T4 ketchup | 24% |
| T5 tomato sauce | 18% |
| T6 butter | 44% |
| T7 milk | 30% |
| T8 chocolate pudding | 50% |
| T9 orange juice | 38% |

### 实验 2: eval_pi05_l2norm_k03_object_seed42
- **状态**: 已完成
- **结果**: `libero_object prune=l2norm keep=0.3 SR=51.0%` (255/500)
- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_object.json`（17:16 写入）
- **耗时**: 90.8 分钟

逐任务成绩：
| Task | SR |
|------|----|
| T0 alphabet soup | 12% |
| T1 cream cheese | 54% |
| T2 salad dressing | 90% |
| T3 bbq sauce | 42% |
| T4 ketchup | 38% |
| T5 tomato sauce | 92% |
| T6 butter | 40% |
| T7 milk | 18% |
| T8 chocolate pudding | 78% |
| T9 orange juice | 46% |

### 失败根因
**误报（false positive）**。监控系统检测到进程退出（PID 死亡）且没有 sentinel/W&B 上报，自动判定为失败。实际上评测脚本 `eval_pi05_pruning_libero.py` 没有集成 W&B 上报和 sentinel 写入，结果只保存为本地 JSON 文件。

### 建议
无需修复或重跑。两个 JSON 结果文件完整可用。如需后续 eval 脚本自动上报状态，可在脚本末尾添加 sentinel 文件写入（如 `touch /tmp/eval_done_&lt;exp_name>`）或 W&B logging。

---
