# exp gemma xnli 113

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma_xnli_113_20260522T182644_result.json`
- **Structured JSON:** [`a64d9a8660484fe5fee4.json`](../../sessions/a6/a64d9a8660484fe5fee4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态总结：

**已完成：**
- Step 1: EN/ZH 激活采集完成，各 shape=[1000, 42, 3584]

**进行中：**
- `bootstrap_n2000.py` (PID 507351): 2000 bootstrap × 4 方向，EN→EN 方向进行中
- `train_probe.py` (PID 512737): 基础探针训练，EN→EN 方向进行中

**瓶颈：**
服务器 load average ~700-860（208 核），主要因已有的 llama31 3-lang bootstrap 任务 (PID 496671) 占用大量 CPU。CPU 严重竞争导致进度缓慢。

两个任务都在后台 nohup 运行中，不会因 SSH 断连丢失。预计：
- 基础探针：~1h 完成（4 方向 × ~15min/方向）
- n=2000 bootstrap：可能需要数小时

获取到的参考数据：
- **Llama XNLI**: Δ_asym = +5.97pp [0.92, 11.33]
- **Qwen XNLI**: Δ_asym = +6.72pp [2.36, 11.73]
- 冲突任务 Gemma: Δ_asym = +6.6pp [1.9, 11.1]

任务将自行完成。需要我继续定期轮询进度，还是你稍后再来检查？

---
