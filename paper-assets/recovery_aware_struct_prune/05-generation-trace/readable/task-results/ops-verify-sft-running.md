# ops verify sft running

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-sft-running_20260514T235847_result.json`
- **Structured JSON:** [`3fd16a40cb6b5a8ed0ab.json`](../../sessions/3f/3fd16a40cb6b5a8ed0ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 SFT 训练都在正常运行。汇总：

## SFT 训练状态报告

### GPU Health
| GPU | 型号 | 温度 | 功耗 | 显存占用 | 利用率 |
|-----|------|------|------|----------|--------|
| 0 | RTX PRO 6000 Black (96GB) | 57°C | 299W/600W | 51.6GB/96GB | 77% |
| 1 | RTX PRO 6000 Black (96GB) | 60°C | 372W/600W | 51.6GB/96GB | 79% |

GPU 温度和功耗正常，双卡各跑一个训练进程（PID 249582, 249660）。

### 训练进度

| 任务 | 当前步数 | 总步数 | 进度 | 速度 | 已用时间 |
|------|----------|--------|------|------|----------|
| sft_rasp_20 | ~483/1870 | 1870 | **26%** | ~1.07s/it | ~8min38s |
| sft_standard_20 | ~476/1870 | 1870 | **25%** | ~1.06s/it | ~8min27s |

### 预计完成时间
- 剩余步数：~1390 步
- 速度：~1.07s/step
- 剩余时间：**~25 分钟**
- 预计完成：**~08:35 UTC（服务器时间）**

两个 SFT 任务均正常推进，loss 日志中每 10 步打印一次（可通过 checkpoint 的 trainer_state.json 查看，目前还未保存第一个 checkpoint）。无报错，状态健康。

---
