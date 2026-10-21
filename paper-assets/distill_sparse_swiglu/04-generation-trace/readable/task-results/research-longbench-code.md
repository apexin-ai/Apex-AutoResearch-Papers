# research longbench code

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_longbench_code_20260525T054838_result.json`
- **Structured JSON:** [`2e9abe8b781da10b440c.json`](../../sessions/2e/2e9abe8b781da10b440c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析报告已存在于 `artifacts/longbench_code_analysis.md`（147 行），内容完整覆盖了你要求的所有点。同时还有 `artifacts/longbench_diagnosis.md` 作为补充。

## 核心发现摘要

**集成方式**：LongBench 没有独立脚本，走 `benchmark_eval.py` → `lm-eval-harness` 的 `simple_evaluate`，与 ARC/MMLU/GSM8K 共用入口。通过 `LM_EVAL_DEFAULTS` 白名单注册了 9 条 longbench 条目（4 个具体子任务 + 5 个聚合名）。

**数据加载**：lm-eval-harness 内部通过 datasets 库加载 `Xnhyacinth/LongBench`（parquet 镜像）。原始 `THUDM/LongBench` 因 datasets ≥3.x 禁用 loading script 而不可用——这是 v1-v5 连续失败的根因。

**序列长度**：`--seq_len` 参数只用于 wikitext2，对 LongBench 无效。LongBench 的 truncation/max_length 由 lm-eval task YAML 控制，代码不传任何覆写参数。

**生成方式**：全部是 `generate_until` 生成式评测（narrativeqa/qasper → QA F1，gov_report/multi_news → ROUGE）。

**关键问题点**：
1. 5 个聚合 task 名（`longbench`/`longbench_single` 等）可能在 lm-eval 中不存在
2. `--batch_size` 默认 8 对 LongBench 致命，必须显式设 1
3. 多卡必须靠外层 `from_pretrained(device_map="auto")` 实现
4. `--seq_len` 完全不影响 LongBench，worker 之前反复误用

**当前状态**：v6 已跑通（`--multi_gpu --batch_size 1` + 预缓存数据），dense 和 kl30_uniform 都有完整结果。

报告已就绪，无需重新生成。需要我更新或补充某个部分吗？

---
