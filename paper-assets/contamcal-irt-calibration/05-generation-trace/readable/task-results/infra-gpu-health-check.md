# infra gpu health check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-health-check_20260516T194258_result.json`
- **Structured JSON:** [`6b1f546b63848c29094f.json`](../../sessions/6b/6b1f546b63848c29094f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 占用状态

| GPU | 显存占用 | 利用率 | PID | 任务 | 状态 |
|-----|---------|--------|-----|------|------|
| cuda:0 | 8072/24564 MiB | 77% | 825638 | eval d005_s42 GSM8K | 正常运行 |
| cuda:1 | 7132/24564 MiB | 45% | 830115 | signals d000_s42 mmlu | 正常运行 |
| **cuda:2** | **0 MiB** | **0%** | — | — | **空闲 ✓** |
| cuda:3 | 8304/24564 MiB | 77% | 822390 | eval d025_s42 GSM8K | 正常运行 |
| **cuda:4** | **560 MiB** | **4%** | **842929** | **signals d005_s42 mmlu** | **⚠️ 未授权进程** |
| cuda:5 | 8304/24564 MiB | 78% | 831033 | eval d100_s42 GSM8K | 正常运行 |

### 4 个 RUNNING 实验健康度

| PID | 实验 | GPU | 当前进度 | ETA | 状态 |
|-----|------|-----|---------|-----|------|
| 822385→822390 | eval d025_s42 | cuda:3 | GSM8K 85% (1124/1319) | ~20min | ✅ 健康 |
| 825638 | eval d005_s42 | cuda:0 | GSM8K 66% (874/1319) | ~47min | ✅ 健康 |
| 830115 | signals d000_s42 | cuda:1 | Self-critique mmlu [7000:8000] 41% (207/500) | 多轮剩余 | ✅ 健康 |
| 831033 | eval d100_s42 | cuda:5 | GSM8K 46% (602/1319) | ~75min | ✅ 健康 |

### ⚠️ 异常发现

**cuda:4 不空闲。** 发现未授权进程 PID 842929（运行仅 56 秒），正在执行：
```
python compute_signals.py --model-path .../Llama-3.2-3B_d005_s42/merged --benchmark mmlu --signal all --output-dir .../signals/Llama-3.2-3B_d005_s42/ --batch-size 4
```

这符合 C005 约束中描述的 "未授权 compute_signals 进程" 模式——来源可能是旧 session Worker 或 auto-loop 触发。目前显存占用仅 560 MiB（刚启动加载模型阶段）。需要决定是否 kill 该进程。

---
