# fix method v1 reviewer warnings

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_method-v1-reviewer-warnings_20260515T094842_result.json`
- **Structured JSON:** [`6adc78641ed81ee56e58.json`](../../sessions/6a/6adc78641ed81ee56e58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 8 corrections applied. Summary of changes:

**method_v1.md:**
| # | 修正 | 原文 | 改为 |
|---|------|------|------|
| 1 | Pool size | "a pool of 50" | "a pool of up to 50 ... (range 2–50, mean 31–34)" |
| 2 | Batch size | "effective batch size 8" | "Each training instance consists of 1 positive and K=7 negatives ... per-device batch size of 8" |
| 2 | Epochs | "up to 3 epochs" | "2 epochs" |
| 2 | Patience | "patience 2" | "patience 3" |
| 4 | LoRA 引用 | "LoRA adaptation" | "LoRA \cite{hu2022lora} adaptation" |
| 5 | InfoNCE 引用 | "\cite{chen2020simclr}" | "\cite{oord2018representation}, also known as NT-Xent \cite{chen2020simclr}" |
| 6a | Mean pooling | 无 justification | 加 "prior work showing mean pooling outperforms [CLS] and last-token alternatives \cite{reimers2019sentencebert, zhang2024codesage}" |
| 6b | beniget fallback | 无占比 | 加 "beniget fallback accounts for 4.8% of successfully extracted instances (764 out of 15,897)" |

**references.bib:** 新增 `hu2022lora` 和 `oord2018representation` 两条。

**修正 3 结论**: 只有 `run_full_m2_training.sh` 一个脚本，`run_m2_full_qwen.sh` / `run_m2_full_starcoder.sh` 不存在，无需加 DEPRECATED 注释。该脚本硬编码了 Qwen 模型路径，StarCoder 训练可能通过修改参数调用同一脚本。

---
