# ops cqa1 gpu check eval prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-gpu-check-eval-prep_20260519T174336_result.json`
- **Structured JSON:** [`1806234dfcd2cc5cdbe8.json`](../../sessions/18/1806234dfcd2cc5cdbe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## 1. cqa1 GPU 状态

| 项目 | 值 |
|---|---|
| GPU 数量 | **1× RTX 4090D** |
| 显存 | 24,564 MiB (24GB) |
| CUDA | 13.0, Driver 580.76.05 |
| 状态 | **空闲**（0MiB / 0% util / 无进程） |

**Director 说的 6 张 GPU 与实际不符——cqa1-21977 只有 1 张 RTX 4090D。**

---

## 2. evaluate.py 一致性

**不一致，需要同步！**

| | cqa1 | westd |
|---|---|---|
| 字节数 | 35,855 | 37,591 |
| 行数 | 813 | 837 |
| 修改时间 | 2026-05-18 20:50 | 2026-05-19 18:22 |

westd 版本更新（+1,736 bytes, +24 lines），修改于今天。**eval 启动前必须先同步，否则数据不可比（M017/M022 教训）。**

---

## 3. 已完成的 eval（cqa1 eval_results_v2）

全部 5 个，均为 qwen7b + s123 seed：
- qwen7b_d000_s123 (.done ✓)
- qwen7b_d005_s123 (.done ✓)
- qwen7b_d025_s123 (.done ✓)
- qwen7b_d050_s123 (.done ✓)
- qwen7b_d100_s123 (.done ✓)

---

## 4. GSM8K 数据集

已缓存：`/root/autodl-tmp/.hf_cache/openai___gsm8k/main/0.0.0/` 存在。

---

## 5. 可用模型和 Adapter

**Base models**（`/root/autodl-tmp/models/`）：Llama-3.2-3B, Qwen2.5-7B, gemma-2-9b, deepseek-ai, unsloth

**HF cache models**：Qwen2.5-0.5B, Qwen2.5-3B, Qwen2.5-0.5B-Instruct, Qwen2.5-1.5B-Instruct, DeepSeek-R1-Distill-Qwen-1.5B, Llama-3.2-3B

**Adapter checkpoints**（已排除 C006 黑名单）：

| Model | Checkpoints |
|---|---|
| Qwen2.5-0.5B | d000/d005/d025/d100 × s42,s123（共 8 个） |
| Qwen2.5-1.5B | d000/d005/d025/d100 × s42,s123（共 8 个） |
| Qwen2.5-3B (valid) | d000_s123, d005_s123, d025_s123, d025_v3_s42, d100_a32_s123, d100_a32_s42_v3 |
| Qwen2.5-3B (⛔ alpha=16) | d000_s42, d005_s42 |
| Llama-3.2-3B | d000/d005/d025/d100 × s42（共 4 个） |
| Qwen2.5-7B | d000/d005/d025/d050/d100 × s42,s123（共 10 个） |
| Qwen2.5-14B | d000_s42, d005_s42 |
| gemma-2-9b | d000/d005/d025/d050 × s42（共 4 个） |

---

## 6. 建议

**阻塞项**：evaluate.py 版本不一致。必须先将 westd 的新版本同步到 cqa1（git pull 或手动复制），否则新 eval 数据与已有数据不可比。

同步后，cqa1 的 1× 4090D 空闲可立即开始 eval。已完成的 5 个都是 qwen7b_s123，其余 checkpoint 均未 eval。

---
