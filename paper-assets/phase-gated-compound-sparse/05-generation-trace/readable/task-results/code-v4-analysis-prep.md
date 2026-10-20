# code v4 analysis prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v4-analysis-prep_20260513T225247_result.json`
- **Structured JSON:** [`03240b43d46433a7d018.json`](../../sessions/03/03240b43d46433a7d018.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/pacs/profiling/analyze_v4_results.py`。

功能：
1. **Pass/Fail 判定** — 基于 CI 是否排除零，打印 overall verdict
2. **Per-phase II 表格** — 每个 (phase, level) 的 mean、CI、sign、pass/fail
3. **v3 对比** — `--v3_results` 传入后，逐 (phase, level) 对比 delta/方向/回归检测
4. **Importance vs Random 信号** — 检测 masking_method 字段，扫描 phase pair 间 II 符号相反的强信号
5. **Markdown 输出** — `--output_md` 生成 `.md` 文件，可直接贴入 report.md

CLI：`python analyze_v4_results.py --results /path/to/profiling_results.json [--v3_results /path/to/v3.json] [--output_md /path/to/summary.md]`

与 `analyze_results.py` 风格一致，无外部依赖（只用 stdlib + numpy），不导入项目内部模块。

---
