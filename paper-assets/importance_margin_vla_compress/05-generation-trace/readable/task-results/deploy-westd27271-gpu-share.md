# deploy westd27271 gpu share

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_gpu_share_20260526T064656_result.json`
- **Structured JSON:** [`b93f47b4588620ea0172.json`](../../sessions/b9/b93f47b4588620ea0172.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 共享确认完毕。汇报如下：

---

### 前置检查

- **SUITE_MODEL_MAP**：`libero_spatial → openvla-7b-finetuned-libero-spatial` ✅ 路径已正确，无需修复
- **模型目录**：Spatial / Goal / Object 三个模型均存在 ✅
- **注意**：用户命令中 `--mode none` 不是有效选项（脚本只接受 `baseline/random_prune/l2norm_prune/attention_prune`），已用 `--mode baseline` 等效替代

### 实验启动状态

| 实验 | PID | GPU | 显存占用 | 状态 |
|------|-----|-----|----------|------|
| **Exp1**: `eval_openvla_baseline_spatial_seed42_v4` (baseline spatial s42) | 112404 | GPU 0 | ~16 GiB | RUNNING ✅ |
| **Exp2**: `eval_openvla_attn_k09_goal_seed43_v4` (attn k=0.9 goal s43) | 112477 | GPU 1 | ~16 GiB | RUNNING ✅ |

### GPU 共享确认

| GPU | 进程数 | 已用显存 | 总显存 | 利用率 |
|-----|--------|----------|--------|--------|
| GPU 0 | 2 (PID 11195 + 112404) | 32 GiB | 98 GiB | 33% |
| GPU 1 | 2 (PID 11378 + 112477) | 32 GiB | 98 GiB | 33% |

每张卡 2 个进程各占 ~16 GiB，总占用 ~32/98 GiB，余量充足。

---
