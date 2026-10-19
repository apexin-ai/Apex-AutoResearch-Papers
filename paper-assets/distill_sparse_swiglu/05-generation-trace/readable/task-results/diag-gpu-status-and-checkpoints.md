# diag gpu status and checkpoints

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_status_and_checkpoints_20260521T233009_result.json`
- **Structured JSON:** [`8a9d41b805be448bdbc2.json`](../../sessions/8a/8a9d41b805be448bdbc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-34887 ===
GPU Status:
  cuda:0 — idle (RTX PRO 6000 Blackwell, 0/97887 MiB, 0% util)
  cuda:1 — idle (RTX PRO 6000 Blackwell, 0/97887 MiB, 0% util)
  注意: 有一个 perlayer_kl_s456_boolq 进程挂起（SCP 卡在连 westd-41718），未占用 GPU

KL 30% Checkpoints (5 个，均 145M):
  checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt  (May 16)
  checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt    (May 18)
  checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt    (May 18)
  checkpoints/kl_30pct_s123/predictor_kl_normalized.pt         (May 17)
  checkpoints/kl_30pct_s456/predictor_kl_normalized.pt         (May 17)

BoolQ cache: MISSING

=== westd-41718 ===
GPU Status:
  cuda:0 — idle (RTX PRO 6000 Blackwell, 0/97887 MiB, 0% util)
  cuda:1 — idle (RTX PRO 6000 Blackwell, 0/97887 MiB, 0% util)
  无实验进程运行

KL 30% Checkpoints (5 个，均 145M):
  checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt  (May 16)
  checkpoints/kl_sparsity30_s123/predictor_kl_normalized.pt    (May 18)
  checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt    (May 18)
  checkpoints/kl_30pct_s123/predictor_kl_normalized.pt         (May 19)
  checkpoints/kl_30pct_s456/predictor_kl_normalized.pt         (May 19)

BoolQ cache: EXISTS
```

补充说明：westd-34887 上有个 `perlayer_kl_s456_boolq` 任务卡在 SCP 阶段（尝试从 westd-41718 拉 `perlayer_kl_30_s456/predictor_perlayer_kl.pt`），进程状态为 T (stopped)，未占用 GPU 但也不会自行恢复，可能需要手动清理。

---
