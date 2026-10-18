# ops phase2 cliff deploy batch1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_phase2_cliff_deploy_batch1_20260522T094114_result.json`
- **Structured JSON:** [`652eb7db31a376880346.json`](../../sessions/65/652eb7db31a376880346.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部部署成功，registry 已推进到 RUNNING。

| 服务器 | GPU | 实验 | PID | 验证 | Registry |
|--------|-----|------|-----|------|---------|
| westd-41074 | 1 | random_k095_goal_s42 | 391150 | ✅ 运行中，已加载模型，pruning random keep 243/256 tokens | ✅ RUNNING |
| westd-27271 | 1 | l2norm_k095_goal_s42 | 327841 | ✅ 运行中，模型加载中 | ✅ RUNNING |
| cqa1-33015 | 3 | random_k095_long_s42 | 335132 | ✅ 运行中，模型加载中 | ✅ RUNNING |

注意：服务器名 `cqa1` 在 registry 中实际为 `cqa1-33015`。首次启动因 nohup 环境无 conda 导致 `python` 找不到，已用 `source conda.sh && conda activate base` 修复后重新启动。

---
