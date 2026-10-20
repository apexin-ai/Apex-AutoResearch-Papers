# ops gpu utilization check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_utilization_check_20260514T052523_result.json`
- **Structured JSON:** [`854da26b0f934a776674.json`](../../sessions/85/854da26b0f934a776674.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：所有进程正常运行，GPU 非空闲

### GPU 状态

| GPU | 型号 | 计算利用率 | 显存占用 |
|-----|------|-----------|---------|
| 0 | RTX PRO 6000 Blackwell | **24-29%** | 6914 / 97887 MiB (7.1%) |
| 1 | RTX PRO 6000 Blackwell | **0%** (瞬时) | 4165 / 97887 MiB (4.3%) |

### 训练进程状态

| 实验 | PID | GPU | 运行时长 | CPU% | 状态 |
|------|-----|-----|---------|------|------|
| exp_008a (fixed_dt2_no_subsample) | 106947 | GPU 0 | 3h48m | 930% | **存活** |
| exp_008e_v3 (subsample_on_dt1_h15) | 126115 | GPU 1 | 56m | 906% | **存活** |
| exp_008f (no_dt_embed_h8) | 127766 | GPU 0 | 33m | 903% | **存活** |

### 最近 Metrics 写入

| 实验 | 最后写入时间 | 当前 Step |
|------|------------|----------|
| exp_008a | 13:22 (3分钟前) | **95,000** / 105,000 |
| exp_008f | 13:25 (刚刚) | **15,000** / 105,000 |
| exp_008e_v3 | 13:21 (4分钟前) | **25,000** / 105,000 |

### 结论

**无异常。** 之前报告的 0% GPU 利用率是采样瞬间值，DreamerV3 的 GPU 利用率在训练中波动较大（环境交互阶段主要用 CPU，模型训练阶段才用 GPU）。三个进程全部存活且持续写入 metrics，exp_008a 已接近完成（95k/105k）。

GPU 1 当前 0% 是因为 exp_008e_v3 可能正处于环境数据采集阶段（CPU 906% 印证了这一点）。

---
