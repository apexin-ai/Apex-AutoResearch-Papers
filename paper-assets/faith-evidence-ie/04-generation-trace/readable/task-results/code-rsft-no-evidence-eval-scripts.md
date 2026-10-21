# code rsft no evidence eval scripts

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rsft_no_evidence_eval_scripts_20260519T124925_result.json`
- **Structured JSON:** [`cf6c5ef6c16bcbedbf11.json`](../../sessions/cf/cf6c5ef6c16bcbedbf11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本语法验证通过。汇报如下：

---

### 脚本状态

两个脚本**已存在**，修复了 4B 的 SFT adapter 路径问题。

**4B (`eval_4b_rsft_no_evidence.sh`)** — 修复完成：
- `--model_path /root/autodl-tmp/rsft_output_4b_sft_s44`
- `--base_model /root/autodl-tmp/models/Qwen3-4B`
- `--sft_adapter /root/autodl-tmp/sft_output_seed44/` ← 原来写的是 `sft_output/`，已修正为与 RSFT 训练一致的 `sft_output_seed44/`
- `--no_evidence --no-quantize --batch_size 4 --seed 42`

**8B (`eval_8b_rsft_no_evidence.sh`)** — 路径均正确，无需修改：
- `--model_path /root/autodl-tmp/rsft_output_qwen3_8b_k1`
- `--base_model /root/autodl-tmp/models/Qwen/Qwen3-8B`
- `--sft_adapter /root/autodl-tmp/sft_output_qwen3_8b_bf16/`

### Checkpoint 路径说明

⚠️ 任务提到的 `rsft_output_qwen3_4b_k1_s42` **不存在**。4B RSFT 只有 s44 版本（`rsft_output_4b_sft_s44`，基于 `sft_output_seed44` 训练）。脚本已指向这个实际存在的 checkpoint。

### GPU 与进程状态

全部 4 张卡占满：

| GPU | 显存 | 任务 |
|-----|------|------|
| 0 | 27.1/31.8 GB | d112 4B RSFT bf16 rerun（训练中） |
| 1 | 31.5/31.8 GB | 14B SFT eval |
| 2 | 31.9/31.8 GB | 14B SFT no-evidence eval |
| 3 | 31.6/31.8 GB | 1.7B RSFT no-evidence eval |

**8B SFT s43** 在 GPU 4（pts/4）上训练中（PID 683952，启动于 20:04），命令中未显式设 `CUDA_VISIBLE_DEVICES`。

→ 目前没有空闲 GPU，需要等 14B eval 或 1.7B eval 完成后才能提交 4B/8B RSFT no-evidence eval。

---
