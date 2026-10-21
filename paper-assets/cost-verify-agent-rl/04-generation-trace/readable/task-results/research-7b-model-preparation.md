# research 7b model preparation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_7b-model-preparation_20260519T025319_result.json`
- **Structured JSON:** [`0a3368b610607769eea2.json`](../../sessions/0a/0a3368b610607769eea2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/7b_preparation_report.md`。核心结论：

**GPU 规格意外发现**: 两台服务器均为 RTX PRO 6000 96GB（非预期的 A800/A6000），8B 训练显存极为充裕，无需 gradient checkpointing。

**模型选择**: `Qwen/Qwen3-8B`（16.4GB bf16），同 Qwen3 家族，已内置指令跟随，无独立 Instruct 版本。两台服务器均无现有 8B 模型，需下载。

**Config 改动要点**:
- `n_gpus_per_node`: 2→4, `CUDA_VISIBLE_DEVICES`: 0,1→0,1,2,3 (westd)
- `model_path` 指向 8B SFT checkpoint
- `gpu_memory_utilization`: 0.35→0.45
- `ppo_mini_batch_size`: 16→32（可选）
- Cell A vs Cell C 仅差 `context_window_mode`

**SFT 数据**: 2460 examples，仅在 bjb1 上，需同步到 westd。

**建议路线**: 下载模型 → 零样本 eval → SFT → RL (Cell A + Cell C)

**待确认**: bjb1⇄westd 文件传输方式、`sft_train.py` 多卡适配、Qwen3 thinking mode 是否需关闭。

---
