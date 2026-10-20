# ssh verify posthoc nli v2

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-posthoc-nli-v2_20260512T232601_result.json`
- **Structured JSON:** [`e9785e1cad6e8756e7e3.json`](../../sessions/e9/e9785e1cad6e8756e7e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. GRPO 进程已清理
PID 64364 不在 nvidia-smi 进程列表中，已确认死亡。

### 2. GPU 状态

| GPU | 进程 | PID | 显存占用 | GPU利用率 |
|-----|------|-----|---------|----------|
| cuda:0 | evaluate.py (SFT eval v2) | 40397 | 29993 / 97887 MiB | 86% |
| cuda:1 | **rerank_nli.py (posthoc_nli_v2)** | 64955 | 19878 / 97887 MiB | 72% |

posthoc_nli_v2 独占 cuda:1，显存充裕（仅用 ~20GB / 98GB）。

**注意：** cuda:0 上跑着一个 `evaluate.py --output_file ./outputs/sft/eval_results_v2.json`，这不是 GRPO，是 SFT 评估任务。

### 3. posthoc_nli_v2 进度
- 当前：**batch 8/124 → 64/985 样本**（~6.5%）
- 模型：`./outputs/sft/merged`（Mistral-Small-3.1-24B）
- batch_size=8，共 124 batches

### 4. 截断风险评估

**实际参数：`--max_new_tokens 1024`**（确认自 `/proc/64955/cmdline`）

- 日志中无任何 truncation / error / warning / incomplete 匹配
- 输出目录 `./outputs/posthoc_nli_v2/` 尚未写入文件（可能在全部生成完成后批量写入）
- 由于还没有输出文件可检查，**截断率目前无法直接评估**

**风险判断：** config.py 默认值是 2048，但实际启动用了 1024。DocRED 关系抽取输出通常是结构化 JSON（关系三元组列表），对于多关系文档，1024 tokens 可能偏紧。建议等到至少有 100+ 样本输出后再检查截断率——如果 `rerank_nli.py` 有 JSON 解析逻辑，截断的 JSON 会在 NLI rerank 阶段报错暴露出来。

### 5. 其他注意
- tokenizer regex 有已知 bug 警告（Mistral tokenizer issue），可能导致 tokenization 不完全正确
- `temperature/top_p/top_k` 被忽略（generation config 不接受这些参数），实际用的是 greedy decoding

---
