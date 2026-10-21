# ops westd38929 d108 parallel

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-d108-parallel_20260520T124728_result.json`
- **Structured JSON:** [`bf817439b35beb3a70e7.json`](../../sessions/bf/bf817439b35beb3a70e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 job 均正常运行：

| Job | 服务器 | GPU | PID | 状态 |
|-----|--------|-----|-----|------|
| k=0.5 | westd-38929 | GPU 0 (16GB/98GB) | 787425 | `[L2 Pruning] 256 -> 128 vision tokens` |
| k=0.3 | westd-38929 | GPU 1 (16GB/98GB) | 788043 | `[L2 Pruning] 256 -> 76 vision tokens` |

参数与 westd-27271 上 k=0.7 一致：`--mode l2norm_prune --suite libero_object --num_episodes 50 --seed 42`

环境搭建内容：
- 创建了 `/root/autodl-tmp/openvla-repo/prismatic/extern/hf/`（从 checkpoint 复制模型代码）
- 安装了 `transformers==4.40.1 + tokenizers==0.19.1` 到 `/root/autodl-tmp/openvla_deps/`
- 写入了 `eval_openvla_l2norm_libero.py`（314行，和源一致）

输出位置：
- `eval_results/openvla_l2norm_prune_k0_5_object.json` / `.log`
- `eval_results/openvla_l2norm_prune_k0_3_object.json` / `.log`

---
