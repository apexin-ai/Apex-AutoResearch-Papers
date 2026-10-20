# ssh r2 r3 conflict check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_r2-r3-conflict-check_20260514T054114_result.json`
- **Structured JSON:** [`4dd6586d33b995bf12a1.json`](../../sessions/4d/4dd6586d33b995bf12a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：cuda:2 上 v6_random_s030 进程冲突

### 进程状态

| | r2 (废弃) | r3 (替代) |
|---|---|---|
| **PID** | 77228 → 77233 (python) | 77560 → 77565 (python) |
| **运行时间** | 8 min 7 sec | 6 min 25 sec |
| **GPU 显存** | 23,512 MiB | 21,038 MiB |
| **输出目录** | `profiling_output_v6_random_s030` | `profiling_output_v6_random_s030_r3` |
| **已产出文件** | **0** | **0** |

### GPU 情况

- 两个进程都在 **cuda:2** (GPU-ae901ff8)，合计占用 **44,550 MiB / 97,887 MiB** (~45.5%)
- 显存没有溢出风险（H800 97GB 足够），但两个进程**争抢 GPU 计算资源**，互相拖慢

### 关键发现

- **两者都还没产出任何结果文件**——运行 6-8 分钟仍在加载模型或推理第一个 problem，说明 GPU 竞争已经显著拖慢速度
- 两者参数完全相同（random, s=0.30, 50 problems, 2048 tokens），只是输出目录不同
- r2 的输出目录是 `profiling_output_v6_random_s030`（无后缀），r3 是 `_r3` 后缀

### 建议

**Kill r2 (PID 77228)**。理由：
1. r2 本就是废弃实验，没有产出任何有效结果
2. 两个同参数实验同时跑在同一 GPU 上毫无意义，只会互相拖慢
3. 杀掉 r2 后 r3 独占 cuda:2，推理速度会显著提升

---
