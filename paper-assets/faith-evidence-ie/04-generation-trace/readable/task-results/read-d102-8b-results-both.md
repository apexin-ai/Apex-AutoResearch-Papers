# read d102 8b results both

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_d102_8b_results_both_20260518T121449_result.json`
- **Structured JSON:** [`d86ce9522bae1e76c9ee.json`](../../sessions/d8/d86ce9522bae1e76c9ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 8B k=1 s42 eval ===
rel_f1=0.5549, ign_f1=0.5376, evi_f1=0.8136, edcr=0.6231
num_preds=16314, truncated=242/985, format_ok=985/985
model: rsft_output_qwen3_8b_k1

=== 8B k=1 s43 eval ===
rel_f1=0.5651, ign_f1=0.5471, evi_f1=0.8180, edcr=0.6094
num_preds=16226, truncated=231/985, format_ok=985/985
model: rsft_output_qwen3_8b_k1_s43

=== 8B k=3 baseline (plan_006, dev) ===
路径: plan_006_qwen3_8b_rsft_eval (checkpoint-3393)
rel_f1=0.5606, ign_f1=0.5433, evi_f1=0.8052, edcr=0.6377
num_preds=16831, truncated=267/985, format_ok=985/985
注: plan_006_qwen3_8b_rsft_test 是 test split，无 dev metrics（需 CodaLab）

=== k=1 vs k=3 对比 (8B Qwen) ===
           | rel_f1 | ign_f1 | evi_f1 | edcr   | truncated
k=3 (p006) | 0.5606 | 0.5433 | 0.8052 | 0.6377 | 267
k=1 s42    | 0.5549 | 0.5376 | 0.8136 | 0.6231 | 242
k=1 s43    | 0.5651 | 0.5471 | 0.8180 | 0.6094 | 231

k=1 s43 在 rel_f1/ign_f1/evi_f1 均优于 k=3 baseline，edcr 降低（更少 distractor citations）。
k=1 s42 略低于 k=3 baseline 的 rel/ign_f1，但 evi_f1 更好。
truncated 数从 267→231 改善，说明 k=1 输出更紧凑。

=== LLaMA s43 训练状态 ===
进行中, PID 537136, GPU 3
step 632/1107 (~57%), ~3.0s/it, 预计剩余 ~24 min
loss ≈ 0.49-0.56, checkpoints: 550, 600
训练稳定

=== GPU 状态 ===
GPU 0: 0 MiB, 0%
GPU 1: 0 MiB, 0%
GPU 2: 0 MiB, 0%
GPU 3: 30593 MiB, 69% (LLaMA s43 训练)
```

---
