# ops check merged file requirement

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-merged-file-requirement_20260516T040855_result.json`
- **Structured JSON:** [`e6304bfbfef3a4fe950d.json`](../../sessions/e6/e6304bfbfef3a4fe950d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. RRF 不需要 merged 文件，可以直接用单独 signal 文件运行

`rrf_aggregation.py:62-117` 的 `load_signal_files()` 有完整的 fallback 逻辑：
- **优先**加载 `signals_merged_{benchmark}.json`（L70-77）
- **如果不存在**，自动加载各个单独 signal 文件 `signal_{s1_embedding,s2_minkpp,s4_selfcritique}_{benchmark}.json`，在内存中合并（L79-117）

两条路径产出完全相同的数据结构。

### 2. IRT 不直接消费 signal 文件

IRT（`exp006/run_irt_calibration.py`）消费的是 RRF 的输出——`exposure_scores.json`（通过 `--exposure-file` 参数传入）。它不接触原始 signal 文件。

### 3. 不需要 merge 命令

项目中没有独立的 merge 脚本。`signals_merged_*.json` 是 `exp002/compute_signals.py` 在计算信号时可选生成的副产品，不是必需的中间产物。

### 4. merged 文件的优势

唯一优势是**加载速度略快**——读 1 个文件 vs 读 3 个文件再合并。对于当前数据规模可忽略不计。

**d025_v3_s42 的 9 个单独 signal 文件可以直接进 RRF 管线，无需任何额外操作。**

---
