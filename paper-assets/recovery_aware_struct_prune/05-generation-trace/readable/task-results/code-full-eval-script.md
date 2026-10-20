# code full eval script

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-eval-script_20260515T022654_result.json`
- **Structured JSON:** [`6b5afc468487a3da132f.json`](../../sessions/6b/6b5afc468487a3da132f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。

**产出总结**：

**eval_gsm8k.py** — 无需修改，已支持 per-sample 输出（每个样本保存 question, gold, prediction, correct, response, response_length, hit_eos 到 JSON 的 `examples` 数组）。

**`/root/recovery_aware_struct_prune/src/run_full_eval.sh`** — 已创建，功能：

| 命令 | 作用 |
|------|------|
| `bash run_full_eval.sh phase1` | 跑 baseline + pruned_rasp_20 + sft_rasp_20 + sft_standard_20 |
| `bash run_full_eval.sh phase2` | 跑 grpo_rasp_20 + grpo_standard_20 |
| `bash run_full_eval.sh all` | 全部 |

**GPU 分配**：
- Phase 1: GPU0 → baseline + sft_rasp_20, GPU1 → pruned_rasp_20 + sft_standard_20（并行）
- Phase 2: GPU0 → grpo_rasp_20, GPU1 → grpo_standard_20（并行）

**跳重机制**：已评估的模型（输出文件已存在）自动跳过。

**预估运行时间**（7B 模型, 1319 样本, greedy, max_new_tokens=4096）：
- 每个模型约 40-60 分钟（取决于平均生成长度）
- Phase 1: ~60 分钟（两组并行，每组 2 个模型串行）
- Phase 2: ~40 分钟（两个模型并行）
- 总计: ~1.5-2 小时

---
