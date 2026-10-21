# exec fix scoring ablation skip attention

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_fix_scoring_ablation_skip_attention_20260517T053952_result.json`
- **Structured JSON:** [`6e75c53800b819d1a2ec.json`](../../sessions/6e/6e75c53800b819d1a2ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--skip_attention` 生效，所有层 Attn 保持 4/4 (100%)，只有 MLP groups 被剪枝。

**完成：**

1. **prune.py 修改**：
   - 第 219 行：添加 `--skip_attention` argparse flag
   - 第 332-334 行：排序后过滤掉所有 `stype == "attn"` 的条目

2. **run_scoring_ablation.sh 修改**：PRUNE_ARGS 添加 `--skip_attention`

3. **旧 pruned models 已删除**

4. **tmux session `scoring_ablation_v2` 已启动**，使用 cuda:0，magnitude 方法正在运行（MLP-only 剪枝确认生效）

5. `eval_unstructured_20` 仍在 cuda:1 正常运行，未受影响

---
