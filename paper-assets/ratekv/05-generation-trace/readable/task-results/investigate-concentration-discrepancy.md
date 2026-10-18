# investigate concentration discrepancy

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_concentration_discrepancy_20260514T200222_result.json`
- **Structured JSON:** [`e62961696a8556ba3662.json`](../../sessions/e6/e62961696a8556ba3662.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。报告已写入 `/root/ratekv/concentration_investigation.txt`。

**根因**：`run_qwen_hires_constrained.py` 加载的 `qwen_float32_profiles.json` 是由 `qwen_float32_validate.py` 生成的 **lowres** profiles（`FullBitwidthProfiler`, 16 samples, seq_len=512），不是 hires 数据。文件名中的 "float32" 指精度而非分辨率，元数据标签 "D048 float32 hires" 是误标。

**正确值**：
| 文件 | 类型 | Concentration |
|------|------|--------------|
| `qwen_float32_profiles.json` | lowres | **0.4220** |
| `hires_profiles.json` / `qwen_hires_results.json` | hires | **0.6104** |

**修复方向**：`run_qwen_hires_constrained.py` 第 18 行应将 `profiles_path` 改为 `hires_profiles.json`（或从 `qwen_hires_results.json` 中提取 profiles）。

---
