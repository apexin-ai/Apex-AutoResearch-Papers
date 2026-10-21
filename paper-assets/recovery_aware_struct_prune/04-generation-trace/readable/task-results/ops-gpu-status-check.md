# ops gpu status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260516T225855_result.json`
- **Structured JSON:** [`c3d5b2adfb51649feaaf.json`](../../sessions/c3/c3d5b2adfb51649feaaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672

| GPU | PID | 进程 | GPU 利用率 | 显存 |
|-----|-----|------|-----------|------|
| cuda:0 | — | — | 0% | 0 MiB | **空闲** |
| cuda:1 | 48541 | eval_grpo_standard_25 (`eval_gsm8k.py --model_path grpo_standard_25 --max_samples 1319`) | 98% | 28902 MiB | **运行中** |
| cuda:2 | 51283 | eval_pass_k8_v2 (`eval_gsm8k.py --model_path grpo_standard_qwen_math --pass_k 8 --num_samples_per_prompt 8 --max_samples 200`) | 91% | 29584 MiB | **运行中** |
| cuda:3 | 54980 | alpha_ablation SFT (`sft_recovery.py --model_path pruned_alpha_2.0 --gpu 3`) | 83% | 51025 MiB | **运行中**（已跑到最后一个 alpha=2.0） |

## westb-23072

| GPU | PID | 进程 | GPU 利用率 | 显存 |
|-----|-----|------|-----------|------|
| cuda:0 | 639423 | eval_grpo_rasp_25 (`eval_gsm8k.py --model_path grpo_rasp_25 --max_samples 1319`) | 98% | 28922 MiB | **运行中** |
| cuda:1 | 648993 | eval_sft_rasp_20_full (`eval_gsm8k.py --model_path sft_rasp_20 --max_samples 1319`) | 98% | 29644 MiB | **运行中**（已启动，PID 648993，父 shell PID 648988） |

**总结**：6 张 GPU 中 5 张在跑任务，westd cuda:0 空闲。alpha ablation SFT 已到最后一轮 (alpha=2.0)，完成后 cuda:3 也将释放。

---
