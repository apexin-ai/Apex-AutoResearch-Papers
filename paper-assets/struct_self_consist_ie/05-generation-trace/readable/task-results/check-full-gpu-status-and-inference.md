# check full gpu status and inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full_gpu_status_and_inference_20260515T192920_result.json`
- **Structured JSON:** [`37822b4ea2bccb46728f.json`](../../sessions/37/37822b4ea2bccb46728f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | PID | 实验名 | 状态 | 进度 |
|-----|-----|--------|------|------|
| cuda:0 | 227128 | **SciERC 4B finetune v4** (`train_config_scierc_4b.yaml`) | 训练中 | **87/585 steps (15%)**, ~2.0s/it, 已跑 ~3min |
| cuda:1 | 224639 | **CoNLL 4B resume** (`train_config_conll2003_4b_resume.yaml`) | 训练中 | **4218/4390 steps (96%)**, loss=0.0096, 剩余 ~35s |
| cuda:2 | — | 空闲 | idle | — |
| cuda:3 | — | 空闲 | idle | — |

关键发现：

1. **CoNLL SCS inference 已不在运行** — cuda:0 被 SciERC finetune v4 占据（PID 227128，03:26 启动）。结果目录 `results/exp_qwen3_4b_conll_scs/` 不存在，inference 进程已消失，之前的推理被挤掉或已终止。

2. **SciERC finetune v4 正在 cuda:0 上跑** — 刚启动 ~3 分钟，87/585 steps (15%)，1861 样本 × 5 epochs，batch=16，预计总耗时 ~19 分钟。

3. **CoNLL resume 即将完成** — 4218/4390 (96%)，loss 降到 0.0096，trainer_log 最新记录到 step 4220。checkpoint-4200 已保存。预计 1-2 分钟内结束。

4. **seed789_v3 已完成** — 551 instances × 8 samples = 4408 total，parse rate 100%，耗时 229.7s。结果已写入 `results/exp_freeform_ablation_seed789/`。

---
