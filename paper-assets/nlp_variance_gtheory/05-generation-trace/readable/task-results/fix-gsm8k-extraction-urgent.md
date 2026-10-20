# fix gsm8k extraction urgent

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gsm8k_extraction_urgent_20260521T101957_result.json`
- **Structured JSON:** [`4ccbcdca3047e12110b1.json`](../../sessions/4c/4ccbcdca3047e12110b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 状态 |
|------|------|
| **benchmark_utils.py 修改时间** | `May 21 18:22`（刚修改） |
| **当前各 GPU 进度** | GPU0(qwen): HellaSwag Condition ~1073；GPU1(llama): HellaSwag Condition ~2260。仍在跑 HellaSwag，GSM8K 未开始 |
| **GSM8K 是否会使用修复后代码** | **会。** 脚本对每个 benchmark 启动独立 `python -m src.inference.run_experiment` 进程，GSM8K 是最后一个。新进程启动时会 import 修复后的 `benchmark_utils.py` |
| **Post-hoc re-extraction** | 不需要 |

修复内容：
- **截断**：在 `\nQ:` / `\nQuestion:` / `\nProblem:` / `\n\n##` 处截断，防止匹配幻觉文本
- **优先级**："The answer is N" > `#### N`（取最后一个）> 末尾数字
- **正则**：小数点后必须跟数字 `(?:\.\d+)?`，避免贪心匹配句号
- 9/9 测试全部通过

---
