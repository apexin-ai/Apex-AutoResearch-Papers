# ops westd disk emergency and e2 resume

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_emergency_and_e2_resume_20260518T134440_result.json`
- **Structured JSON:** [`cd0d11da3835405e728f.json`](../../sessions/cd/cd0d11da3835405e728f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

```
磁盘: 清理前 100% (619G/619G) → 清理后 68% (418G/619G), 释放 201GB
MATH-500 evals: 正常运行，未受磁盘满影响
  - math500_standard_grpo_fair (GPU1): 21/500 进行中
  - math500_sft_cka_only_20 (GPU2): 18/500 进行中
  - math500_dense_unpruned (GPU3): 45/500 进行中
E2 resume: 已启动 PID=6346, step=111→300, GPU0 39.9GB
  save_steps=50, save_total_limit=3
  wandb: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/44cjdoiy
```

---
