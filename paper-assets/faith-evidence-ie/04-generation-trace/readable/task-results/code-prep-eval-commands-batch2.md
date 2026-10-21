# code prep eval commands batch2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-eval-commands-batch2_20260515T232114_result.json`
- **Structured JSON:** [`15fe15c68e1465abbc6a.json`](../../sessions/15/15fe15c68e1465abbc6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 命令已准备完毕，脚本已写入服务器，registry 已更新。

## 总结

| # | exp_id | checkpoint | 关键差异 |
|---|--------|-----------|---------|
| 1 | `eval_flat_nli_s44` | `rsft_output_flat_nli_s44/checkpoint-507` | `--sft_adapter` + `--seed 44` |
| 2 | `eval_flat_nli_seed45` | `rsft_output_flat_nli_s45/checkpoint-507` | `--sft_adapter` + `--seed 45` |
| 3 | `eval_plan_014_no_evidence` | `sft_no_evidence_output` | **无** `--sft_adapter`，加 `--no_evidence`，`--seed 42` |

所有命令统一使用 `--batch_size 4 --no-quantize`，目标 GPU `cuda:0`。

- 脚本路径：`/root/autodl-tmp/scripts/next_eval_commands.sh`
- 3 个 registry 条目均已更新 `spec.command`，状态 PREPARING
- eval 脚本原生支持 `--no_evidence`（inference.py:273），无需改代码
- 注意：seed44 训练仍在 RUNNING，目录中尚无最终 adapter 文件，但 `checkpoint-507` 已存在可用

---
