# prep eval 1 7b seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_eval_1_7b_seed456_20260520T164725_result.json`
- **Structured JSON:** [`7849c4bbfc924cb66d13.json`](../../sessions/78/7849c4bbfc924cb66d13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `artifacts/eval_commands_seed456_1_7b.sh`。

**汇总：**

| GPU | 模型 | 任务 | 预计耗时 |
|-----|------|------|---------|
| cuda:0 | uniform_1_7b_seed456 | holdout PPL + OOD (openwebtext + wikipedia) | ~7min |
| cuda:1 | adaptive_1_7b_seed456 | holdout PPL + OOD (openwebtext + wikipedia) | ~7min |
| cuda:2 | uniform_1_7b_seed456 | downstream (arc_easy, arc_challenge, hellaswag, piqa, winogrande) | ~2min |
| cuda:3 | adaptive_1_7b_seed456 | downstream (同上) | ~2min |

**已验证：**
- `eval_perplexity.py` 和 `lm_eval` 0.4.11 均已就绪
- 三个数据文件存在：`eval_holdout.jsonl` (237MB)、`eval_openwebtext.jsonl` (25MB)、`eval_wikipedia.jsonl` (71MB)
- 结果输出到 `output/eval/`，命名与 seed42_v5 和 seed123 一致
- 脚本带 sanity check，训练未完成会直接报错退出

**注意：** seed42_v5 的 OOD PPL 也还没跑。如果需要补跑可以一起安排。

**执行方式：** 训练完成后 SSH 到服务器，`nohup bash eval_commands_seed456_1_7b.sh > /tmp/eval_seed456_all.log 2>&1 &`

---
