# ops cuda3 cascade sft rasp 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda3_cascade_sft_rasp_2048_20260518T232744_result.json`
- **Structured JSON:** [`4f709fda55302ee70170.json`](../../sessions/4f/4f709fda55302ee70170.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 39767 已启动，模型正在加载。

---

## 产出汇总

### 1. RASP GRPO MATH-500 最终结果
| 指标 | 值 |
|---|---|
| **Accuracy** | **24.0% (120/500)** |
| stderr | 0.0191 |
| natural_eos | 64% (320/500) |
| truncated | 36% (180/500) |
| avg_response_length | 903.5 tokens |
| median_response_length | 272 tokens |
| max_new_tokens | 2048 |

Registry: `eval_math500_grpo_rasp_20_fair` → DONE (success)

### 2. SFT RASP 模型状况
`sft_rasp_20_westd` 存在且完整（12.3GB model.safetensors，config/tokenizer 齐全）。

### 3. cuda:3 下一步
`eval_math500_sft_rasp_20_2048` 已启动（PID 39767），使用 `sft_rasp_20_westd` 模型，max_new_tokens=2048。预计 5-6 小时完成。

---
