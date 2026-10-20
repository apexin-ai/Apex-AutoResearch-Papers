# code c5b pilot prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c5b_pilot_prep_20260514T173813_result.json`
- **Structured JSON:** [`055c419651889ac2c457.json`](../../sessions/05/055c419651889ac2c457.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

- **`/root/autodl-tmp/pacs/run_c5b_pilot.py`** (582行) — 完全独立的 C5b pilot 入口脚本
  - CLI: `--sparsity`, `--strategy {oracle,heuristic,baseline,all}`, `--gpu`, `--model_path`, `--data_path`, `--output_dir`
  - 复用 `pacs.profiling.*` 的模型加载、II 计算、phase segmentation 基础设施
  - 内联了 `compute_phase_aware_sparsity`（s_trans cap ≤ 0.50）、`assign_heuristic_phases`、`eval_condition` 等核心逻辑（解决 `run_mitigation_pilot.py` 不在 `pacs/profiling/` 包内的导入问题）
  - `--strategy all`（默认）共享 generation + dense forward，最高效
  - 输出 `mitigation_pilot_results.json`，含 per_problem + summary + gate_pass

- **`/root/autodl-tmp/pacs/run_c5b_pilot.sh`** (35行) — 2 次调用覆盖全部 6 条件（all策略 × s025/s030），支持 `bash run_c5b_pilot.sh [GPU]`

- **Dry-run**: `--help` 正常解析，shell 语法通过

---
