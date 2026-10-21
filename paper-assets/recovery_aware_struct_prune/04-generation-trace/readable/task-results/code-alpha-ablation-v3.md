# code alpha ablation v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha_ablation_v3_20260515T035339_result.json`
- **Structured JSON:** [`144b9b244954d27c1d83.json`](../../sessions/14/144b9b244954d27c1d83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。`scripts/run_alpha_ablation_v3.sh` 已创建。

### v3 关键参数与执行流程

**α 网格**: `{0.0, 0.25, 0.5, 1.0, 2.0}`

**执行顺序**（顺序执行，磁盘安全）：

| α | tag | 操作 | 模型路径 |
|---|-----|------|----------|
| 0.0 | `alpha0_0` | prune → eval → **删除** | `pruned_rasp_20_alpha_0_0` |
| 0.25 | `alpha0_25` | prune → eval → **删除** | `pruned_rasp_20_alpha_0_25` |
| 0.5 | `alpha0_5` | prune → eval → **删除** | `pruned_rasp_20_alpha_0_5` |
| 1.0 | `alpha1_0` | **复用** `/root/autodl-tmp/pruned_rasp_20` → eval only | 不删除 |
| 2.0 | `alpha2_0` | prune → eval → **删除** | `pruned_rasp_20_alpha_2_0` |

**其他参数**：
- Sparsity: 20%
- Eval: GSM8K N=100, bfloat16, max_new_tokens=4096
- GPU: 自动选择 cuda:0/cuda:1 中空闲显存最大的
- 已有结果自动跳过（`eval_alpha_*.json` 存在即 skip）
- 输出: `eval_results/alpha_ablation/eval_alpha_&lt;tag>.json`
- Summary: `eval_results/alpha_ablation/alpha_ablation_v3_summary.json`
- 支持 `--dry-run` 预检

---
