# code multi temp sampling

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi-temp-sampling_20260519T014610_result.json`
- **Structured JSON:** [`b1609967bb4a6eea86ee.json`](../../sessions/b1/b1609967bb4a6eea86ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

### 产出总结

**创建文件**: `/root/symb_invariant_consensus/run_multi_temp.py`

**新增参数**（替代原 `--temperature` 和 `--k`）:
| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--temperatures` | str | `0.3,0.7,1.2` | 逗号分隔温度列表 |
| `--k-per-temp` | str | `4,4,4` | 每个温度的 trace 数量，需与 temperatures 长度匹配 |

其余参数（`--mode`, `--model`, `--api-base`, `--output`, `--resume`, `--save-intermediates` 等）与 `run_full_mvp.py` 一致。

**新增类/函数**:
- `MultiTempVLLMGenerator` — 单 async client，所有温度组并发生成，每条 trace 附带 `temperature` 字段
- `MultiTempAPIGenerator` — 顺序生成的 API 版本
- `parse_temp_k_pairs()` — 解析并校验温度/k 配置
- `build_multi_temp_generator()` — 工厂函数

**复用自 `run_full_mvp.py`**:
- `load_all_problems`, `load_checkpoint`, `build_extractor`, `compute_summary`, `print_summary`

**温度元数据记录位置**:
- 每条 trace dict 的 `"temperature"` 字段（vllm/api 模式）
- `per_trace_constraints/{id}.json` 中每条 trace 的 `"temperature"` 字段
- `summary` 中的 `"temperatures"` 和 `"k_per_temp"` 字段

**Dry-run 结果**: `--help` 解析正确，mock 模式完整 pipeline 跑通（2 题，12 traces = 4+4+4），参数校验（长度不匹配报错、单温度、不等分配）全部通过。

---
