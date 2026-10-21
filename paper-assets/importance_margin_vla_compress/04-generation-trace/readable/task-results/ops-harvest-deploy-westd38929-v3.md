# ops harvest deploy westd38929 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-deploy-westd38929-v3_20260524T100233_result.json`
- **Structured JSON:** [`2404d5b25c521a2a754d.json`](../../sessions/24/2404d5b25c521a2a754d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验都**仍在运行**，不是空闲。当前进度：

| GPU | 实验 | 当前进度 | 中间结果 |
|-----|------|---------|---------|
| 0 | Random k=0.95 Goal | Task 2/10 | T0=86%, T1=94%, T2 ~80% |
| 1 | L2norm k=0.3 Goal | Task 1/10 | T0=70%, T1 ~27% |
| 2 | L2norm k=0.925 Goal | Task 2/10 | T0=86%, T1=96%, T2=100% |

前 17 小时应该是模型加载，实际 eval 从 ~17:47 才开始。日志时间戳显示三个实验都在活跃执行中（最新 ~18:02）。没有结果文件产出，没有 exit file。

**结论：GPU 0-2 不空闲，无法收割也无法部署新实验。** 按每 task ~7-8 分钟估算，三个实验还需 ~1-1.5 小时完成（剩余 7-8 个 task）。

建议等实验完成后再执行收割和部署。需要我设一个定时检查吗？

---
