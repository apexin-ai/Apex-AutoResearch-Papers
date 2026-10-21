# exp mistral completion check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mistral_completion_check_20260521T052858_result.json`
- **Structured JSON:** [`9d7a931485523b043b15.json`](../../sessions/9d/9d7a931485523b043b15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Mistral — 已完成 ✓

全部 4 个 shard 正常结束，数据完整：

| 指标 | 值 |
|------|-----|
| 总记录数 | **259,200** (= 预期 1,296 conditions × 200 items) |
| 缺失 conditions | **0** |
| 准确率 | **61.24%** (158,726/259,200) |
| precision 覆盖 | bfloat16 / float16 / float32 各 86,400 (均分) |
| temperature 覆盖 | 0.0 / 0.3 / 0.7 各 86,400 (均分) |
| 每个 shard | 64,800 行 (324 conditions) |

完成时间：2026-05-21 13:31:26 CST

### 2. Qwen — 已自动启动 ✓

`auto_start_qwen.sh` 检测到 Mistral 结束后，于 **13:31:42** 在 4 个 GPU 上启动了 Qwen 推理（PID 91484-91490）。目前处于 vLLM 引擎初始化阶段（刚检测到 CUDA 平台），日志文件都是刚创建的（76 bytes）。

### 3. GPU 当前状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 0 / 98 GB |
| 1 | 100% | 91 / 98 GB |
| 2 | 100% | 91 / 98 GB |
| 3 | 0% | 0 / 98 GB |

GPU 1/2 正在加载 Qwen 模型，GPU 0/3 还未开始加载（可能在排队等待）。

---
