# code alpha ablation v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha_ablation_v2_20260515T034726_result.json`
- **Structured JSON:** [`8b25d8f7e9fb475aad72.json`](../../sessions/8b/8b25d8f7e9fb475aad72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。

**`scripts/run_alpha_ablation_v2.sh` 已就绪**，核心设计：

| 项目 | 内容 |
|------|------|
| α 网格 | {0.0, 0.25, 0.5, 0.75, 1.0} |
| 流程 | 顺序执行：prune → eval(GSM8K N=100) → 删除模型 → 下一个 α |
| α=1.0 | 复用 `/root/autodl-tmp/pruned_rasp_20`，仅 eval，不删除 |
| 磁盘安全 | 每轮结束立即 `rm -rf` 临时模型，峰值仅占 ~12GB |
| GPU | 自动选择显存最多的 GPU（cuda:0 或 cuda:1） |
| 输出 | `eval_results/alpha_ablation/eval_alpha_{0_0,0_25,...}.json` + 汇总 JSON |
| 执行 | `bash scripts/run_alpha_ablation_v2.sh`（一键）或 `--dry-run`（验证） |

---
