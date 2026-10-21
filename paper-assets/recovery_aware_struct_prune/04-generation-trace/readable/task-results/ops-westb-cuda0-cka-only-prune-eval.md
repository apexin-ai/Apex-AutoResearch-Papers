# ops westb cuda0 cka only prune eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cuda0_cka_only_prune_eval_20260517T112543_result.json`
- **Structured JSON:** [`0d82e5acef4123054238.json`](../../sessions/0d/0d82e5acef4123054238.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已开始推理，0/200 samples。进程正常运行。

**报告：**

- **Pruning**: 成功完成
  - 模式: `cka_only` (score = 1 - CKA overlap)
  - 实际 sparsity: 19.09% (目标 20%)
  - 200/784 MLP groups 被剪掉，attention 未剪 (--skip_attention)
  - 产出: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20/` (12GB)

- **Eval GSM8K**: 已启动
  - PID 710113 (父进程 710613)，cuda:0 占用 12374 MiB
  - 200 samples，正在推理中
  - 日志: `/tmp/eval_cka_only_20.log`
  - 结果输出: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_cka_only_20_n200.json`

- **注意**: cuda:0 同时运行 SFT training (PID 704557, 50GB) 和本 eval (12GB)，总共 ~63GB / 98GB，空间充足。eval 速度可能略受影响。

---
