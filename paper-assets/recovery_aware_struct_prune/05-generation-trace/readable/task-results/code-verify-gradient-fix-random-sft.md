# code verify gradient fix random sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_gradient_fix_random_sft_20260517T092211_result.json`
- **Structured JSON:** [`9815288a60af9dbec9e2.json`](../../sessions/98/9815288a60af9dbec9e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**gradient SFT 状态**：原 PID 697500 已死（被之前的 Worker kill），另一 Worker 已重启为 PID 698173 但使用的是错误的 `save_strategy="no"`（硬编码）。已 kill 698173 并用正确参数重启。

- **新 PID**: 698674，运行在 tmux `scoring_ablation_v2`，使用 `--save_strategy epoch`
- GPU: cuda:0

**代码修改**：
1. **sft_recovery.py**: 添加 `--save_strategy` CLI 参数（default="epoch", choices=["no", "epoch", "steps"]），SFTConfig 中改为 `save_strategy=args.save_strategy`
2. **run_random_cka_ablation.sh**: 两处 SFT 调用（random、cka_only）均添加 `--save_strategy no`

**磁盘**：`/root/autodl-tmp` 250G 用 185G，剩余 66G (74%)

---
