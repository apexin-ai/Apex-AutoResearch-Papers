# code exp001 data sampling

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp001_data_sampling_20260520T195748_result.json`
- **Structured JSON:** [`cfb56222be6f0b9cb71f.json`](../../sessions/cf/cfb56222be6f0b9cb71f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件语法检查通过。修改总结：

1. **`sample_mmlu.py`** — 无需修改，已有 10 subjects × 20 items = 200，且包含 `--n-items` / `--n-subjects` 参数。

2. **`few_shot.py`** — 已有 4 orderings。新增 `--n-orderings` CLI 参数（默认 4），函数签名增加 `n_orderings` 参数，内部循环和打印使用该参数。

3. **`sample_benchmarks.py`** — 重写为统一 schema 输出。三个 benchmark（gsm8k/arc_challenge/hellaswag）各 200 items，每条记录包含 `item_id, benchmark, question, choices, answer_idx, answer, metadata`。GSM8K 用 `####` 正则提取数字答案，choices/answer_idx 为 null。支持 `--benchmark` 单采和 `--all` + `--output-dir` 批量采样。

---
