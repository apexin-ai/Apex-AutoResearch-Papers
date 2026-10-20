# ops urgent kill 30pct submit next

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_kill_30pct_submit_next_20260520T115519_result.json`
- **Structured JSON:** [`f95014a3e4c5eb8dd479.json`](../../sessions/f9/f95014a3e4c5eb8dd479.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。westd-29022 GPU 分布：

| GPU | PID | 实验 | VRAM | 状态 |
|-----|-----|------|------|------|
| cuda:0 | 245522 | grpo_cka_only_20_seed456 | 56GB | 训练中，~12.7s/step |
| cuda:1 | 246464 | grpo_cka_only_15_v2 | 54GB | 训练中，~13.2s/step |
| cuda:2 | 226966 | eval_grpo_standard_20_seed123 | 29GB | eval 进行中（不动） |
| cuda:3 | 227043 | eval_grpo_standard_20_seed456 | 29GB | eval 进行中（不动） |

**执行摘要：**

1. **Kill 30% eval** — 已终止 PID 201928（cka_only_30）和 202006（standard_30）
2. **Registry 更新** — prune_eval_cka_only_30: acc=1.60%（500/1319），prune_eval_standard_30: acc=2.80%（500/1319），均标记 DONE/success
3. **grpo_cka_only_20_seed456** — cuda:0 RUNNING，PID 245522，ETA ~21min
4. **grpo_cka_only_15_v2** — cuda:1 RUNNING，PID 246464，ETA ~22min。checkpoint-20 损坏，改为从 sft_cka_only_15 全新训练

**注意事项：**
- `--save_only_model` 参数不存在，已省略并记录到 registry
- `--gpu` 参数仅做 metadata 记录，不控制 GPU 分配，必须显式设 `CUDA_VISIBLE_DEVICES`

---
