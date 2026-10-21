# code westd status check latest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-status-check-latest_20260515T110021_result.json`
- **Structured JSON:** [`80e013f4fcd0b6185534.json`](../../sessions/80/80e013f4fcd0b6185534.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 状态汇总

### 1. GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 0% | 0 / 97887 MiB |
| cuda:1 | 0% | 0 / 97887 MiB |

**两块 GPU 完全空闲，无任何进程在运行。**

---

### 2. PID 7186 (α ablation Phase B SFT pipeline)
**已死。** 服务器上无任何 python/训练进程。

**SFT 完成情况：**
| α 值 | 状态 | 说明 |
|-------|------|------|
| α=0.0 | ✅ 完成 | checkpoint-1870 + 最终 model.safetensors (12.3GB) |
| α=0.5 | ✅ 完成 | checkpoint-1870 + 最终 model.safetensors (6.6GB) |
| α=1.0 | ❌ 未完成 | 仅有 checkpoint-935（中间点），无最终模型 |
| α=2.0 | ❌ 未开始 | 目录不存在 |
| α=4.0 | ❌ 未开始 | 目录不存在 |

Pipeline 在 α=1.0 训练期间崩溃/被中断，只保存了 half-way checkpoint。

---

### 3. D023 re-eval (pruned_standard_20)
**✅ 已完成。** 结果：

- **GSM8K Accuracy: 25.0% ± 4.33%** (25/100)
- EOS rate: 77%, avg response length: 1259 tokens
- 耗时约 40 分钟，于 18:16:19 完成
- 结果保存在 `/tmp/reeval_standard_20_results.json`

---

### 4. α ablation Phase A 结果（prune-only eval，未经 SFT）

| α 值 | GSM8K Accuracy |
|-------|---------------|
| 0.0 (纯 magnitude) | 30% |
| 0.5 | 25% |
| 1.0 | 27% |
| 2.0 | 29% |
| 4.0 | **40%** |

α=4.0 (重 CKA 权重) 在 prune-only 阶段表现最好，比 α=0.0 高 10 个百分点。

---

### 总结
- **GPU 空闲**，所有任务已停止
- Phase B SFT 完成了 2/5（α=0.0, α=0.5），α=1.0 中途中断，α=2.0 和 4.0 未启动
- D023 re-eval 已完成，pruned_standard_20 = 25% accuracy
- Phase A prune-only 评估全部完成，α=4.0 最优

---
