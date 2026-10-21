# code tau sweep analysis framework

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tau_sweep_analysis_framework_20260515T101943_result.json`
- **Structured JSON:** [`621b80ccb1266330e257.json`](../../sessions/62/621b80ccb1266330e257.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。

**文件**: `artifacts/analyze_tau_sweep.py`

**用法**:
- `python analyze_tau_sweep.py --dummy` — 用 dummy 数据生成示例图
- `python analyze_tau_sweep.py -i results.json -o ./figures` — 从 JSON 读取真实数据
- `--uniform-ppl` / `--grid-best-ppl` 可覆盖 baseline 值

**输出**:
- Figure 1: τ vs eval_ppl 曲线（含 uniform/grid-best baseline 虚线，τ=0.8 default 标注）
- Figure 2: τ vs Δ improvement 曲线
- Markdown 表格（stdout），含 Δ vs uniform、Δ vs grid-best、% of grid-best improvement

Dummy 数据验证显示 τ=0.8 处 PPL 最低（17.651），呈现预期的 U 型曲线。等真实 sweep 数据到位后，准备 JSON 文件运行即可。

---
