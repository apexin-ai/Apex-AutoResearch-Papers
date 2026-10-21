# audit westd gpu verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd_gpu_verify_20260527T073402_result.json`
- **Structured JSON:** [`e4f0da6dc15227b071b2.json`](../../sessions/e4/e4f0da6dc15227b071b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已修复。汇总如下：

---

## GPU 审计结果

### westd-27271 (2x RTX PRO 6000 Blackwell 94GB)

| GPU | 显存 | 利用率 | 实验 | 进度 | 运行时间 |
|-----|------|--------|------|------|----------|
| 0 | 15.6GB | 73% | eval_openvla_attn_k095_goal_seed42_v2 | Task 6/10 | 1h38m |
| 1 | 15.6GB | 69% | eval_openvla_l2norm_k085_object_seed42 (rerun) | Task 4/10 | 1h15m |

### westd-38929 (4x RTX PRO 6000 Blackwell 98GB)

| GPU | 显存 | 利用率 | 实验 | 进度 | 运行时间 |
|-----|------|--------|------|------|----------|
| 0 | 15.8GB | 64% | eval_openvla_random_k095_long_seed42 (v2) | Task 2/10 | 1h14m |
| 1 | 15.6GB | 67% | eval_openvla_l2norm_k095_long_seed42 | Task 6/10 | 6h22m |
| 2 | 16.0GB | 65% | eval_openvla_l2norm_k075_long_seed42_v2 | Task 5/10 | 5h52m |
| 3 | 15.9GB | 78% | eval_openvla_attn_k095_long_seed42 | Task 7/10 | 6h22m |

### Registry 修复
- `eval_openvla_random_k095_long_seed42`: 更新 server westd-41074→westd-38929, gpu cuda:0, PID 112587, log 指向 v2。这就是之前 GPU 0 "idle" 误报的原因——进程存在但 registry 未更新服务器信息。

### 已收割实验
无。所有实验仍在运行中。

### 真正空闲 GPU
**无。** 两台服务器共 6 块 GPU 全部满载。resource_usage 的 idle 报告是 registry 元数据过时导致的误报。

---
