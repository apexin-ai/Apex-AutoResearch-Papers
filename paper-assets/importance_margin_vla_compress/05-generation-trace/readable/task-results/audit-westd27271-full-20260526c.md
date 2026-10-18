# audit westd27271 full 20260526c

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd27271-full-20260526c_20260526T190142_result.json`
- **Structured JSON:** [`4e0368d1714d65c1f46e.json`](../../sessions/4e/4e0368d1714d65c1f46e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### GPU 状态（仅 2 块 GPU）
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 71% | 16/98 GB | `eval_openvla_l2norm_k075_goal_seed42_v2` — Task 7/10 开始，~1h 完成 |
| 1 | 71% | 16/98 GB | `eval_openvla_attn_k05_long_seed42` — Task 4/10 ep10，0.9 eps/min，~6h 完成 |

**无 GPU 2/3，服务器只有 2 块 GPU。**

### 已完成
| 实验 | SR | 详情 |
|------|-----|------|
| `eval_openvla_l2norm_k09_goal_seed43_v3` | **75.2%** (376/500) | l2norm k=0.9, Goal, seed 43, 210min |

### 运行中
- **GPU 0** `l2norm k=0.75, Goal, seed 42` — Task 7/10 刚开始，ETA ~1h
- **GPU 1** `attn k=0.5, Long, seed 42` — Task 4/10 ep10/50，ETA ~6h（极慢，0.9 eps/min）

### 可用模型
- `openvla-7b-finetuned-libero-10` (Long)
- `openvla-7b-finetuned-libero-goal` (Goal)
- `openvla-7b-finetuned-libero-spatial` (Spatial)
- **无 Object 模型**

### 空闲 GPU
无。两块 GPU 均被占满，无法部署新实验。GPU 0 约 1h 后空闲可复用。

---
