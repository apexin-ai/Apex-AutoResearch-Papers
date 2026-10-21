# deploy cqa1 and westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_and_westd41074_20260524T190218_result.json`
- **Structured JSON:** [`2ff4cf4397d565ef2436.json`](../../sessions/2f/2ff4cf4397d565ef2436.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**发现问题：** 这两个实验已在 cqa1 上以 RUNNING 状态注册并正在执行：

- `eval_pi05_random_k095_long_seed43_postfix` → cqa1 GPU3 (PID 600400, 运行19分钟)
- `eval_pi05_random_k07_long_seed43_postfix` → cqa1 GPU1 (PID 600244, 运行19分钟)

**cqa1 实际部署 vs 计划的差异：**

| GPU | 计划部署 | 实际运行 |
|-----|---------|---------|
| GPU0 | L2norm k=0.3 seed43 v2 (保持) | L2norm k=0.3 seed43 v2 ✓ |
| GPU1 | Random k=0.5 seed43 | Random **k=0.7** seed43 |
| GPU2 | Random k=0.3 seed43 | Random **k=0.5** seed43 |
| GPU3 | Random k=0.7 seed43 | Random **k=0.95** seed43 |

**关键缺口：Random k=0.3 Long seed43 未在任何服务器上运行。**

westd-41074 GPU1/GPU3 空闲。是否：
1. **按原计划**部署 k=0.95 和 k=0.7 到 westd（会与 cqa1 重复）
2. **改为**部署 **Random k=0.3 Long seed43**（填补缺口）+ k=0.95 或 k=0.7 中的一个
3. 其他方案

请确认部署方案。

---
