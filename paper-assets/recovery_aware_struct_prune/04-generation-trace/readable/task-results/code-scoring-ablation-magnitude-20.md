# code scoring ablation magnitude 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scoring_ablation_magnitude_20_20260518T024943_result.json`
- **Structured JSON:** [`e82c03c7165fd4a54703.json`](../../sessions/e8/e82c03c7165fd4a54703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程运行 3:52 分钟 (含 ~2 分钟加载)，实际 eval ~2 分钟。约完成 2-3 个 sample。

当前状态总结：

**已完成：**
- Magnitude pruning at 20%: 成功，actual sparsity 18.99%
- 剪枝模式：MLP-only（199/784 groups），集中在 layer 0-10（各剪 16/28 groups），后层几乎保留全部
- Pruned model 保存到 `/root/autodl-tmp/recovery_aware_struct_prune/pruned_magnitude_20/`

**进行中：**
- GSM8K eval (200 samples)，~57s/sample，预计 ~3 小时完成（~11:50 UTC 前后）
- 速度慢是因为模型严重损坏（早期层被大量剪枝），每个 sample 都生成到 max_new_tokens=4096

**预期结果：**
- 根据之前的 continue 脚本注释 "acc=0%"，post-prune accuracy 很可能为 0% 或接近 0%

任务 `scoring_ablation_magnitude_20` 在 westb-23072 cuda:0 上运行，tmux session 同名，3 小时 timeout。如果想加速，可以 kill 后用更小的 `--max_new_tokens`（如 2048）重跑，但结果不会有实质差异。

---
