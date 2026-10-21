# code fix exp026 temperature restart

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-exp026-temperature-restart_20260518T114541_result.json`
- **Structured JSON:** [`020c407b40b0e9933e61.json`](../../sessions/02/020c407b40b0e9933e61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 产出报告

### 1. 旧进程
- PID 25172 (exp-026 worker) — 已 kill ✓
- PID 25162 (父进程) — 已 kill ✓

### 2. 修改的文件

| 文件 | 行号 | 修改 |
|------|------|------|
| `run_full_mvp.py` | 201 | `default=0.3` → `default=0.7` |
| `scripts/run_folio_trace_regen.sh` | 65 | `--temperature 0.3` → `--temperature 0.7` |
| `scripts/run_case_study_extract.sh` | 64 | `--temperature 0.3` → `--temperature 0.7` |

`constraint_extractor.py` 的 VLLMBackend 默认 T_ext=0.3 未改（已正确），且 `build_extractor()` 不传 `args.temperature` 给 VLLMBackend。

### 3. 温度验证
- `run_full_mvp.py --temperature` default = **0.7** ✓
- `run_folio_trace_regen.sh --temperature` = **0.7** ✓
- `run_case_study_extract.sh --temperature` = **0.7** ✓
- VLLMBackend (constraint_extractor.py:120) default = **0.3** ✓

### 4. 新进程
- **PID 25650** — `python -u run_full_mvp.py --mode vllm --k 12 --temperature 0.7 ...`
- 已加载 204 FOLIO 问题，正在处理 folio_0
- 错误结果目录 `results/folio_204_14b/` 已清空
- 日志：`logs/folio_regen_restart_20260518_194658.log`

---
