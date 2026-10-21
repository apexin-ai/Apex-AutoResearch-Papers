# audit westd 27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-27271_20260523T110804_result.json`
- **Structured JSON:** [`034e1786afa30b6f9420.json`](../../sessions/03/034e1786afa30b6f9420.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报

### GPU 状态
| GPU | 利用率 | 显存 | 运行实验 | 进度 |
|-----|--------|------|---------|------|
| 0 | 57% | 4.9/96 GB | eval_e5_xvla_attn_mean_spatial_k05 | Task 1 ep31/50 (Task 0: 100%) |
| 1 | 71% | 4.9/96 GB | eval_e5_xvla_attn_rollout_spatial_k05 | Task 1 ep31/50 (Task 0: 100%) |

两个实验约 19:03 CST 启动，每 task ~4min，10 tasks 共计约 40min，预计 **~19:45 CST** 完成。

### 已收割的 E5 Attention Pruning 结果 (k=0.5)

| Mode | Suite | SR | Per-task |
|------|-------|----|----------|
| attention_last | Spatial | **88.8%** | T0:98 T1:100 T2:100 T3:98 T4:86 T5:22 T6:98 T7:88 T8:98 T9:100 |
| attention_last | Long | **90.2%** | T0:96 T1:66 T2:100 T3:98 T4:90 T5:94 T6:94 T7:70 T8:96 T9:98 |

### 正在运行
- `attention_mean` Spatial — 约 30min 后出结果
- `attention_rollout` Spatial — 约 30min 后出结果

### 空闲 GPU
**0 个**，两块都在跑实验。

---
