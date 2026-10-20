# ssh exp001 mmlu gsmk prep

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001_mmlu_gsmk_prep_20260522T061523_result.json`
- **Structured JSON:** [`c6ad7dcdccf2491b25ba.json`](../../sessions/c6/c6ad7dcdccf2491b25ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### 1. 数据文件
| 文件 | 行数 | 大小 |
|------|------|------|
| `exp001/data/mmlu/mmlu_500.jsonl` | 500 | 284KB |
| `exp001/data/gsm8k/gsm8k_500.jsonl` | 500 | 305KB |

MMLU 覆盖 **57 个 subject**，按比例分层抽样。GSM8K 从 test split (1319题) 随机抽 500。

### 2. Prompt Template
`exp001/prompts/pointwise_template.py` — 包含 MMLU 和 GSM8K 各自的 system prompt + user prompt 模板，使用 `[[rating]]` 格式与 `judge_interface.py` 的解析器兼容。

### 3. 收集脚本
`exp001/collect_pointwise.py` + `exp001/config_pointwise.yaml`

功能：
- `--generate-responses`: 用 target model 生成 MMLU/GSM8K 的 response
- 默认模式：对每个 (item, model, judge) 收集 pointwise 评分
- `--benchmark mmlu/gsm8k` + `--judge &lt;name>` 支持增量运行
- 断点续传：跳过已完成的 key，failed 会重试
- RateLimiter 复用 collect.py 的 token-bucket 模式
- 输出到 `results/pointwise/{benchmark}_judgments.jsonl`

### 4. 开始收集前还需要
**Target model responses**（最关键的缺失项）：需要先用 `--generate-responses` 为 8 个 target model 各生成 500 MMLU + 500 GSM8K 的 response，存到 `data/responses/{mmlu,gsm8k}/{model}.jsonl`。

运行方式：
```bash
python collect_pointwise.py --config config_pointwise.yaml --generate-responses --judge gpt-5.5-proxy
```

### 5. Judgment 数量预估
每个 judge 需评 **500 items × 8 models = 4,000 judgments**（每个 benchmark），两个 benchmark 合计 **8,000 judgments/judge**。

8 个 judge 总计：**64,000 judgments**。

---
