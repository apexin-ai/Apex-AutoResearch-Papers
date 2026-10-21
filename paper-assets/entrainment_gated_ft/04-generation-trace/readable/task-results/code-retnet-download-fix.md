# code retnet download fix

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_retnet_download_fix_20260518T145025_result.json`
- **Structured JSON:** [`8a0c4a01a576b58d621c.json`](../../sessions/8a/8a0c4a01a576b58d621c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果汇总：

---

### 1. RetNet-pure 下载/修复状态
shard-1 (5.00GB) 和 shard-2 (0.20GB) 均完整存在，无需修复。之前报告的"shard-1 被删除"是误报。

### 2. RetNet-pure 模型加载验证
加载成功，1.30B 参数，weight tying 已正确应用 (`lm_head.weight = model.embeddings.weight`)。

### 3. RetNet-pure lambada 结果
- **acc** = 0.5166
- **perplexity** = 10.0067

### 4. RetNet-pure 6-task 完整结果

| Task | Metric | Score |
|------|--------|-------|
| lambada_openai | acc | 0.5166 |
| lambada_openai | ppl | 10.0067 |
| hellaswag | acc | 0.4419 |
| hellaswag | acc_norm | 0.5799 |
| winogrande | acc | 0.6038 |
| arc_easy | acc | 0.7121 |
| arc_easy | acc_norm | 0.6477 |
| arc_challenge | acc | 0.3729 |
| arc_challenge | acc_norm | 0.3771 |
| mmlu | acc | 0.2452 |

结果已保存至 `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json`

### 5. RetNet-hybrid-12-1 完整性
两个 shard 均存在，模型完整。

### 6. fix_downloads.py 状态
PID 316964 仍在运行（已运行 37 分钟），当前正在下载 **HGRN2-pure shard-1** (4.65GB)。

---
