# analysis llama sft s44 train eval r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_sft_s44_train_eval_r3_20260520T141646_result.json`
- **Structured JSON:** [`54332ce140a97f5384fb.json`](../../sessions/54/54332ce140a97f5384fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
ign_f1=0.4802
f1=0.4902
evi_f1_joint=0.3913
evi_f1_tp=0.8502
edcr=0.6579
ign_precision=0.4695
ign_recall=0.4915
train_loss=0.526
eval_loss=0.6931 (epoch2, best); 0.7367 (epoch3)
format_compliance=1.0000
n_truncated=240
n_documents=985
inference_time_seconds=7227.4

CHECKPOINT_PATH: /root/autodl-tmp/sft_output_llama_3_1_8b_s44
LOG_PATH: ~/runs/faith-evidence-ie/llama_sft_s44_train_eval_r3.log

WANDB_RUN_ID: (无，日志中未找到 W&B 链接)

CONCLUSION: success（ign_f1=0.4802 > 0.45，训练正常完成 EXIT_CODE=0）
```

**3-seed SFT baseline 对比：**

| Seed | ign_f1 | f1 | evi_f1_joint | edcr |
|------|--------|----|-------------|------|
| s42 | 0.5384 | — | — | — |
| s43 | 0.5142 | — | — | — |
| **s44** | **0.4802** | 0.4902 | 0.3913 | 0.6579 |
| **Mean** | **0.5109** | — | — | — |
| **Std** | **0.0238** | — | — | — |

s44 比 s42 低 5.8pp，比 s43 低 3.4pp，是三个 seed 中最低的。3-seed mean=0.5109±0.0238，方差偏大。与 RSFT 3-seed mean (0.5654±0.0052) 相比，SFT baseline 低 5.5pp 且方差大约 4.6 倍。

---
