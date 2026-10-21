# code xnli data prep 110

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_xnli-data-prep-110_20260522T035858_result.json`
- **Structured JSON:** [`876458242ce4c5454d6f.json`](../../sessions/87/876458242ce4c5454d6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已完成的工作：**

1. **读取现有代码**：理解了 `collect_activations.py` 期望的 JSONL 格式（`context`/`question`/`label` 字段，label 为 "conflict"/"no_conflict"）和 `build_prompt()` 的模板结构

2. **编写 `src/prepare_xnli.py`**：
   - 从 hf-mirror.com 下载 XNLI validation parquet（绕过 `datasets` 库 4.8.5 不支持 loading script 的问题）
   - 提取 EN/ZH 平行语料，过滤 neutral，保留 entailment+contradiction
   - 映射 label：entailment→"conflict"(1)，contradiction→"no_conflict"(0)
   - 80/20 split，输出到 `data/xnli/`

3. **验证**：脚本已运行成功，输出 4 个 JSONL 文件（EN/ZH × train/test），字段结构与 `collect_activations.py` 完全兼容

4. **产出报告**：写入 `artifacts/plan_110_xnli_baseline_report.md`，含数据统计、命令模板、兼容性说明

**数据规模**：EN 800 train + 200 test，ZH 800 train + 200 test，label 分布约 50/50。

---
