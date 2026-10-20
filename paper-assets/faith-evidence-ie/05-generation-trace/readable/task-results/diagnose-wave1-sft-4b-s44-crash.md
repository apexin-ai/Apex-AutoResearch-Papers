# diagnose wave1 sft 4b s44 crash

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_wave1_sft_4b_s44_crash_20260518T135847_result.json`
- **Structured JSON:** [`5e1111695a545335b76c.json`](../../sessions/5e/5e1111695a545335b76c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 SFT 训练都**正常结束**。

## wave1_sft_4b_s44（seed44）

- **状态**: 正常完成，21:57:22 结束
- **训练 metrics**:
  - `train_loss`: **0.7008**
  - `train_runtime`: 4379s (~73 min)
  - `train_steps`: 144 steps, 3 epochs
  - `train_samples_per_second`: 2.074
- **Eval metrics** (epoch 3):
  - `eval_loss`: **0.7478**
  - `eval_mean_token_accuracy`: **0.8299**
  - `eval_entropy`: 0.6943
- **Checkpoint 路径**: `/root/autodl-tmp/sft_output_seed44/`（含 `adapter_model.safetensors` 528MB，checkpoint-96 和 checkpoint-144）

## wave1_sft_4b_s43（seed43）

- **状态**: 正常完成，21:58:29 结束
- **训练 metrics**:
  - `train_loss`: **0.7011**
  - `train_runtime`: 4455s (~74 min)
  - `train_steps`: 144 steps, 3 epochs
  - `train_samples_per_second`: 2.039
- **Eval metrics** (epoch 3):
  - `eval_loss`: **0.7482**
  - `eval_mean_token_accuracy`: **0.8300**
  - `eval_entropy`: 0.6933
- **Checkpoint 路径**: `/root/autodl-tmp/sft_output_seed43/`（同样结构）

## GPU 当前状态

| GPU | 占用 | 进程 |
|-----|------|------|
| cuda:0 | 空闲 (0 MiB) | — |
| cuda:1 | 空闲 (0 MiB) | — |
| cuda:2 | 16.6 GB | PID 542126 - GRPO trainer (`grpo_bf16_g4`) |
| cuda:3 | 18.4 GB | PID 541954 - eval inference (`d102_llama_k1_s43`) |

两个 SFT 都已正常训练完成并保存了 adapter，s43 和 s44 的 loss/accuracy 非常接近。cuda:0 和 cuda:1 现在空闲可用。

---
