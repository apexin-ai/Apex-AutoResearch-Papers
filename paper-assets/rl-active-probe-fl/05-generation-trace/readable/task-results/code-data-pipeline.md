# code data pipeline

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-pipeline_20260514T044707_result.json`
- **Structured JSON:** [`715a18c44583bf878640.json`](../../sessions/71/715a18c44583bf878640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。创建的文件：

| 文件 | 说明 |
|------|------|
| `src/data_filter.py` | 从 HuggingFace 加载 DebugBench，过滤 Python single-bug 子集（683条），输出 JSONL |
| `src/generate_tests.py` | 用 Claude API 为每个样本生成 pytest 测试用例，支持并发/断点续传 |
| `src/validate_tests.py` | 验证 solution pass + buggy fail，只保留两者都符合的样本 |
| `src/distill_probes.py` | 用 Claude API 生成 good_probe/bad_probe/rationale 三元组，支持并发/断点续传 |
| `src/split_data.py` | 按 slug 去重分割 train/eval，seed=42 可复现 |
| `data/debugbench_python_single.jsonl` | 已生成，683 条（syntax 38.1%, reference 33.2%, logic 28.7%） |

Pipeline 执行顺序：`data_filter.py` → `generate_tests.py` → `validate_tests.py` → `distill_probes.py` → `split_data.py`。后三步需要 `ANTHROPIC_API_KEY`（generate_tests 和 distill_probes）或 pytest（validate_tests）。

---
