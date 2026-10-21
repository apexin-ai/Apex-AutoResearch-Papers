# ops deploy t10 a060 s44 cuda3 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-t10-a060-s44-cuda3-17855_20260523T083954_result.json`
- **Structured JSON:** [`0d67889ed09e13fa1b89.json`](../../sessions/0d/0d67889ed09e13fa1b89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已启动并确认 GPU 占用：

| 实验 | 服务器 | GPU | PID | 显存占用 |
|------|--------|-----|-----|----------|
| `scale_14b_t10_a060_s44_fp32` | westd-17855 | cuda:3 | **780907** | 10293 MiB |
| `scale_14b_t10_a075_s44_fp32` | westd-19828 | cuda:1 | **865467** | 20582 MiB |

westd-19828:cuda:0 仍在运行（27727 MiB, 98% util），未受影响。

两个实验均处于 gen_0 baseline 阶段，正常加载模型中。

---
