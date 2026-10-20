# ssh ablation data gen

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ablation-data-gen_20260514T221315_result.json`
- **Structured JSON:** [`92858470bcf4d73afd59.json`](../../sessions/92/92858470bcf4d73afd59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现状总结：

- **消融数据已存在**：`ablation/sft_taxei_v4_inject10.jsonl` (4842行) 和 `sft_taxei_v4_inject25.jsonl` (5810行) 都已生成
- **cuda:2 正在训练**（PID 94635）：跑的是 `sft_taxei_v4_fixed_inject10.jsonl` → `output/v4-fixed-inject10`，已运行 3.5 分钟
- **cuda:3 空闲**

cuda:2 不可用。我先在 cuda:3 上提交一个训练任务。

两个选项：
1. cuda:3 先跑 inject10，等 cuda:2 空闲后跑 inject25
2. cuda:3 先跑 inject25，等 cuda:2 空闲后跑 inject10

你想先跑哪个？还是直接 cuda:3 跑 inject10（对应原计划 cuda:2 的任务），等 cuda:2 释放后再提交 inject25？

另外，现有 `inject25` 数据用的是 `n_clean * 0.25 / 0.75 = 1452` 条 injected（总 5810 行，实际注入率 25%），与你任务描述中的 1090 条（25% of clean，实际注入率 20%）不一致。确认用哪个版本？现有数据对应"总占比 25%"，你的描述对应"clean 数量的 25%"。

---
