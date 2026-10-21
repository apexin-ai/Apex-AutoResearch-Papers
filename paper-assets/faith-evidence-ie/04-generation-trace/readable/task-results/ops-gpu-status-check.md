# ops gpu status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260516T085930_result.json`
- **Structured JSON:** [`0a406dd5d63b52c5f8ac.json`](../../sessions/0a/0a406dd5d63b52c5f8ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU Status

| GPU | Name | VRAM Used | VRAM Total | Util |
|-----|------|-----------|------------|------|
| 0 | RTX 5090 | 10,405 MiB | 32,607 MiB (32%) | 56% |
| 1 | RTX 5090 | 16,238 MiB | 32,607 MiB (50%) | 86% |
| 2 | RTX 5090 | 24,091 MiB | 32,607 MiB (74%) | 46% |
| 3 | RTX 5090 | 0 MiB | 32,607 MiB (0%) | 0% |

## Process Status

| PID | exp_id | alive? | elapsed | GPU | status |
|-----|--------|--------|---------|-----|--------|
| 322215 | reeval_flat_nli_s44 | **YES** | 4m | cuda:0 | Inference 6/247 (2%), ~38s/it |
| 321094 | plan_006_qwen3_1_7b_no_evidence_sft | **YES** | 23m | cuda:2 | Training 362/570 (63%), epoch ~1.9/3 |
| 317310 | plan_006_qwen3_8b_sft_bf16 | **NO** | — | — | **COMPLETED** |
| 319245 | plan_006_qwen3_1_7b_sft_eval | **YES** | 47m | cuda:1 | Inference 104/247 (42%), ~26s/it |
| 319632 | plan_002_test_eval_s44_r2 | **YES** | 46m | cuda:1 | Inference 48/250 (19%), ~57s/it |

## Experiment Progress

**1. reeval_flat_nli_s44** — 刚启动 4 分钟，6/247 batches (2%)。ETA ~2.5h。输出目录空。

**2. plan_006_qwen3_1_7b_no_evidence_sft** — 362/570 steps (63%)，epoch 1.9/3。最新 metrics: loss=0.796, token_acc=0.812, lr=7.8e-5。Epoch 1 eval: eval_loss=0.889, token_acc=0.803。~3.6s/step → ETA ~12 min。输出目录有之前 run 的 checkpoint-570 和 adapter (278MB)，当前 run 完成后会覆盖。

**3. plan_006_qwen3_8b_sft_bf16** — **已完成** ✓。570/570 steps，3 epochs，65 min。Final metrics: train_loss=0.570, epoch 3 eval_loss=0.719, eval_token_acc=0.838。Adapter 已保存 (698MB) 到 `/root/autodl-tmp/sft_output_qwen3_8b_bf16/`。GPU 3 已释放。

**4. plan_006_qwen3_1_7b_sft_eval** — 104/247 batches (42%)，running 47 min。~26s/it → ETA ~62 min。输出目录空（结果在最后一步才写入）。

**5. plan_002_test_eval_s44_r2** — 48/250 batches (19%)，running 46 min。~57s/it → ETA ~3.2h。输出目录仅有 eval.log。

## Disk

```
/dev/md0  250G  243G  8.0G  97%  /root/autodl-tmp
```

**⚠️ 磁盘仅剩 8GB (97%)，需要关注。** 当前 4 个运行中的实验可能还会写入 checkpoint 和结果文件。8B SFT adapter 就占了 698MB。建议训练完成后清理旧 checkpoint。

---
