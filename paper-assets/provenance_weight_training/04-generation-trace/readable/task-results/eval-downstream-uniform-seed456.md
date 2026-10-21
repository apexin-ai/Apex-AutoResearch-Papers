# eval downstream uniform seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_downstream_uniform_seed456_20260519T194814_result.json`
- **Structured JSON:** [`46ce5537f1a6b19dc478.json`](../../sessions/46/46ce5537f1a6b19dc478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这个 eval 已经跑完了，结果文件已存在。直接汇总：

```
uniform_ood_seed456 downstream results:
- arc_easy acc_norm: 0.6166
- arc_challenge acc_norm: 0.3439
- hellaswag acc_norm: 0.4826
- piqa acc_norm: 0.6795
- winogrande acc: 0.5667
```

结果来自 `/root/autodl-tmp/provenance_weight_training/output/eval/downstream_uniform_ood_seed456/`，eval 耗时 446 秒，使用 lm_eval 0.4.11，0-shot，dtype 未特别指定（模型以 float16 推理），`--batch_size auto`，`--log_samples` 开启。

---
