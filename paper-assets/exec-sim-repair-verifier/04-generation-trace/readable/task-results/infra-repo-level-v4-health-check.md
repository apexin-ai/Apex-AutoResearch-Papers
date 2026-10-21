# infra repo level v4 health check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_repo-level-v4-health-check_20260512T172515_result.json`
- **Structured JSON:** [`cc795f3f6e3d6aaaf09d.json`](../../sessions/cc/cc795f3f6e3d6aaaf09d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇报

### 进程状态：两个都 alive，正在加载模型

| 任务 | Python PID | CPU% | RSS | 运行时间 | 状态 |
|------|-----------|------|-----|---------|------|
| repo-level-cls-v4 | 75563 | 115% | 2.5GB | ~1m40s | 加载中 |
| repo-level-cwm-v4 | 75640 | 115% | 2.8GB | ~1m40s | 加载中 |

### GPU 使用

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 0 MiB / 32607 MiB | 0% |
| cuda:1 | 18537 MiB / 32607 MiB | 100% (另一个eval任务) |
| **cuda:2** | **0 MiB** | **0%** |
| **cuda:3** | **0 MiB** | **0%** |

### 日志进度
两个训练都停在相同位置——数据加载完成，尚未开始模型加载到 GPU：
```
INFO Loaded train=70748, val=9335
INFO Class weights: fail=1.7009, pass=0.2991
```

### 磁盘
根分区 64%（20G/30G），无回涨。

### 结论
两个训练都处于正常启动早期阶段——CPU 高负载说明正在从磁盘加载 Qwen3-4B 权重到内存，尚未 `.to(device)` 推上 GPU。预计再等 1-2 分钟 GPU 显存应该会开始占用并进入 step 0。**目前无报错，无 KeyError，无 OOM。** 建议 2-3 分钟后再检查一次确认是否已过 step 5。

---
