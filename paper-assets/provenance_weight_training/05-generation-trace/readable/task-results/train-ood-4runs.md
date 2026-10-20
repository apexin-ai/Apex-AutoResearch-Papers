# train ood 4runs

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ood_4runs_20260519T143538_result.json`
- **Structured JSON:** [`ec02f7e9888068ffad98.json`](../../sessions/ec/ec02f7e9888068ffad98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个训练全部启动成功，正在训练中：

| exp_id | GPU | 状态 | 显存 | max_steps |
|--------|-----|------|------|-----------|
| adaptive_ood_seed123 | cuda:0 | training (step 1/6103) | 45.6GB | 6103 |
| adaptive_ood_seed456 | cuda:1 | training (step 1/6103) | 40.9GB | 6103 |
| uniform_ood_seed123 | cuda:2 | training (loading) | 2.0GB | 6103 |
| uniform_ood_seed456 | cuda:3 | training (loading) | loading | 6103 |

参数确认：
- adaptive: `scored_data.jsonl` + `--contamination_ratio 0.4`，tau=0.8/n_min=2 为默认值
- uniform: `mixed_data.jsonl`
- 共通：200M tokens, bs=4, grad_accum=4, lr=5e-5, save_steps=6103, save_total_limit=2, save_only_model
- 预估每个 run ~5h（~3s/step × 6103 steps）

---
