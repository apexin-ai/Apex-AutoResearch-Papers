# ops gpu full status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_full_status_check_20260516T114227_result.json`
- **Structured JSON:** [`23d604a431a8a665d3d3.json`](../../sessions/23/23d604a431a8a665d3d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

| GPU | 显存占用 | 状态 | 详情 |
|-----|---------|------|------|
| **cuda:0** | 0 MiB / 32607 MiB | **空闲** | 1.7B no-evidence eval v2 未留下输出目录，进程已不存在。可能启动失败或从未成功提交。 |
| **cuda:1** | 11415 MiB / 32607 MiB | **运行中** | `test_rsft_ced_s44` eval (PID 319638)，Qwen3-4B + RSFT checkpoint-510，test split，进度 228/250 batches (~91%)，预计剩余 ~19 分钟 |
| **cuda:2** | 18421 MiB / 32607 MiB | **运行中** | `qwen3_8b_no_evidence_eval_v2` (PID 335357)，Qwen3-8B no-evidence eval，输出目录已创建但尚无结果文件，刚开始推理 |
| **cuda:3** | 23737 MiB / 32607 MiB | **运行中** | `llama_3_1_8b_no_evidence_sft` 训练 (PID 333916)，进度 400/570 steps (~70%)，loss=0.4538，token_accuracy=0.879，epoch 2.11，预计剩余 ~14 分钟 |

### 关键发现

- **1.7B no-evidence eval v2 没有成功启动**——`qwen3_1_7b_no_evidence_eval_v2/` 目录不存在，cuda:0 完全空闲。上个 session 提交的任务可能失败了。
- cuda:1 的 test eval 即将完成（~9 分钟内）。
- cuda:3 的 LLaMA SFT 也接近尾声（~14 分钟）。

---
