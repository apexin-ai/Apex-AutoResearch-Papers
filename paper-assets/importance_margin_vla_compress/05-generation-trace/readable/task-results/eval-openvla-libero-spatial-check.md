# eval openvla libero spatial check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla_libero_spatial_check_20260519T104713_result.json`
- **Structured JSON:** [`304f624d5e70d79a7dc6.json`](../../sessions/30/304f624d5e70d79a7dc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**基础设施全部就绪，eval 已启动。**

| 项目 | 状态 |
|------|------|
| OpenVLA checkpoint | `/root/autodl-tmp/openvla-libero-object/` (7B, Object 微调) |
| LIBERO-Spatial 环境 | 可用（10 tasks） |
| Eval 脚本 | `eval_openvla_libero.py`，已修复 CUDA_VISIBLE_DEVICES 硬编码 |
| GPU | cuda:1，占用 16GB/98GB |

**运行配置**:
- 模型：openvla-7b-libero-object（cross-suite eval，用 Object 微调模型跑 Spatial）
- 规模：10 tasks × 50 episodes = 500 total
- Seed: 42（注意 Object baseline 用的是 seed=7）
- PID: 552445
- 日志：`eval_results/eval_openvla_baseline_spatial.log`
- 输出：`eval_results/eval_openvla_baseline_spatial.json`

**注意**：这是 cross-suite eval（Object 模型 → Spatial 任务），unnorm stats 用的是 `libero_object`。如果需要 Spatial 原生 baseline（Spatial 微调模型 → Spatial 任务），需要额外下载 `openvla-libero-spatial` checkpoint。

---
