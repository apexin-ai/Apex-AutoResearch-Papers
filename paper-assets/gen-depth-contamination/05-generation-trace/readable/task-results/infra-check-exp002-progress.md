# infra check exp002 progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_exp002_progress_20260513T021143_result.json`
- **Structured JSON:** [`8cbce9c6710c26b65d72.json`](../../sessions/8c/8cbce9c6710c26b65d72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002 OLMo-1B 状态汇总

| 项目 | 状态 |
|------|------|
| **进程** | PID 20225 存活，已运行 1h56m |
| **当前步骤** | 特征提取 — VocabDiv depth=3, 33% (1671/5000) |
| **数据生成** | ✅ 全部完成 (depth_0 ~ depth_5, 共 ~33MB) |
| **Results** | 目录为空，特征提取尚未写入最终结果 |
| **GPU** | 0% 利用率, 3135/24564 MiB（当前 VocabDiv 是 CPU 密集计算） |

### 进度估算

- 数据生成阶段：08:16 → 09:51，已完成
- 特征提取阶段：09:51 开始，当前在 depth 3/5 的 33%
- VocabDiv 速度 ~16 it/s，depth 3 剩余 ~3.5 min，depth 4-5 各 ~5 min

**预估剩余：15-30 分钟**（取决于 VocabDiv 之后是否还有其他指标计算）。

---
