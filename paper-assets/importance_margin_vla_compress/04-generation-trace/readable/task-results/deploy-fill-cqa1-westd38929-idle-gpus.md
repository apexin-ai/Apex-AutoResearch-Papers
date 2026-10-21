# deploy fill cqa1 westd38929 idle gpus

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill_cqa1_westd38929_idle_gpus_20260527T073057_result.json`
- **Structured JSON:** [`fdcf9e8c17980035b6c6.json`](../../sessions/fd/fdcf9e8c17980035b6c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态汇总：

**cqa1-33015**: 4/4 GPU 满载
- GPU 0: OV Random k=0.95 Goal — Task 10/10 ~Ep 24/50，约 17 min 后完成
- GPU 1: OV Attn k=0.95 Goal v2 — Task 4/10，3+ h
- GPU 2: π0.5 Attn k=0.95 Long strict — Task 8/10，~1.5 h
- GPU 3: OV Attn k=0.5 Goal v3 — Task 7/10，~2 h

**westd-38929**: 4/4 GPU 满载
- GPU 0: OV Random k=0.95 Long v2 — Task 2/10（已更新 registry 为 RUNNING）
- GPU 1-3: OV L2norm/Attn Long 实验进行中

**已完成的 registry 清理**:
- `eval_openvla_l2norm_k095_object_seed42` → DONE(failed)，陈旧条目
- `eval_openvla_attn_k07_long_seed42_v2` → 补充 per-task metrics (SR=24.0%)
- `eval_openvla_random_k095_long_seed42_v2` → PREPARING→RUNNING

**待部署**（等 GPU 释放）:
1. π0.5 Random k=0.7 Long strict → cqa1 GPU 0（~17 min 后）
2. π0.5 Random k=0.5 Long strict → cqa1 GPU 2（~1.5 h 后）

已设置 4.5 min 后自动唤醒检查并部署。

---
