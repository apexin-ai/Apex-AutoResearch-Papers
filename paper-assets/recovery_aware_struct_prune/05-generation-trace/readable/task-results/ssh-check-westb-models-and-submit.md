# ssh check westb models and submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westb_models_and_submit_20260521T192943_result.json`
- **Structured JSON:** [`5b66646a9e1227c06eb4.json`](../../sessions/5b/5b66646a9e1227c06eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 启动成功，模型正在加载。

**已提交**: `eval_math500_sft_cka_only_20_v5` → westb:1 (cuda:1)
- 模型: `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20` (CKA-only 20% SFT, 12GB)
- 参数: `--max_new_tokens 2048 --seed 42`
- 输出: `/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_20/results.json`
- Registry: `eval_math500_sft_cka_only_20_v5` (RUNNING)

**westb GPU 占用**:
- cuda:0: `eval_math500_grpo_standard_25_v2` (RUNNING)
- cuda:1: `eval_math500_sft_cka_only_20_v5` (刚提交)

**说明**: 虽然 `eval_math500_sft_cka_only_20_v4_restart` 在 registry 中标记为 success，但其结果文件不在 westb 上（可能在 westd）。Dense unpruned baseline 在 westb 上也没有完整模型（HF cache 只有 4KB refs）。westb 上能跑的最有价值的缺失数据点就是这个 CKA-only 20% SFT。

---
