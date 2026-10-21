# code math500 sft evals westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_math500_sft_evals_westd_20260518T130015_result.json`
- **Structured JSON:** [`3ececc82984626bf509f.json`](../../sessions/3e/3ececc82984626bf509f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理已启动。500 题，~2.1s/it，预估约 17 分钟完成。

**汇报：**

| 项目 | 状态 |
|------|------|
| **SFT CKA-only 20% MATH-500** | 运行中，PID 2529，cuda:2，~17min 完成 |
| 模型路径 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20` |
| 输出路径 | `.../results/math500_sft_cka_only_20.json` |
| 日志 | `~/runs/recovery_aware_struct_prune/math500_sft_cka_only_20.log` |
| **SFT Unpruned baseline** | **缺失** — 两台服务器均无模型权重（westd 目录为空，westb 不存在）|
| **Dense Unpruned baseline** | 已有结果：`eval_math500_unpruned.json`，accuracy = **73.6%**（模型: DeepSeek-R1-Distill-Qwen-7B）|

**SFT Unpruned 缺失说明**：需要先在某台服务器上对 dense 模型做 SFT 训练，才能得到 SFT Unpruned baseline。如果只是需要 "unpruned 在 MATH-500 上的表现"，dense 模型的 73.6% 已经可用。

另外注意 cuda:1 上有另一个 eval 在跑（`math500_standard_grpo_fair`），CKA-only 完成后如果需要串行第二个 eval，cuda:2 可以复用。

---
