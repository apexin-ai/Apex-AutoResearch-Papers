# diagnose plan 001b gpu1 extra

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-001b-gpu1-extra_20260514T020400_result.json`
- **Structured JSON:** [`ada4c064698e50fe6bb6.json`](../../sessions/ad/ada4c064698e50fe6bb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**plan-001b-gpu1-extra 并未失败——当前正在运行。**

### 进程状态

| GPU | 实验 | PID | 启动时间 | 任务 |
|-----|------|-----|---------|------|
| GPU 0 | plan-001b-gpu0-v3 | 544511 | 09:52 | `lifespan-longest-lived` ep15-19 (5 eps) |
| GPU 1 | plan-001b-gpu1-extra | 557852 | 09:59 | `find-non-living-thing` ep21-39 (19 eps) |

两个实验都有配套的 vLLM::EngineCore 和 Java/ScienceWorld 进程在跑。

### GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU 0 (RTX 5090) | 28013 / 32607 MiB | 100% |
| GPU 1 (RTX 5090) | 28013 / 32607 MiB | 100% |

### find-non-living-thing 数据

- `episodes.jsonl`: **22 行**
- `episode_summary.jsonl`: ep5-21（17 条新采集记录）
- `collection_meta.json`: reused 5 eps (from prescreening) + 15 new = 20 eps 为初始批次
- 当前运行已完成 **ep21**（出现在 summary 中），正在继续采集 ep22-39
- **已完成总计: 22 episodes (ep0-21)**，目标 40 eps，还需 18 eps

### 关于 EXIT_CODE=129

之前报告的 SIGHUP 退出应该来自更早的一次运行。当前实例是重启后的新进程（PID 557852，09:59 启动），日志显示 vLLM 推理正常进行中，无错误。

### 结论

不需要重启实验——两个 GPU 都在满载跑任务。等当前 run 完成即可。

---
