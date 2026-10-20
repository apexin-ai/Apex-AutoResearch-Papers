# code constat comparison prep

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_constat-comparison-prep_20260521T080559_result.json`
- **Structured JSON:** [`f58725d5b8d8b000954f.json`](../../sessions/f5/f58725d5b8d8b000954f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**产出**：
1. **ConStat 仓库** — 已 clone 到 `/root/autodl-tmp/ConStat/`，`pip install -e .` 完成
2. **适配脚本** — `/root/autodl-tmp/constat_comparison/run_constat.py`（可行性分析 + 模拟对比 + 信息成本表）
3. **结果 JSON** — `/root/autodl-tmp/constat_comparison/results/constat_comparison.json`
4. **分析报告** — 已写入 memory.md "## ConStat 对比分析" 段

**核心发现**：

ConStat 在我们的 ctrl-contam 数据上 **不可用**（4 项必需输入仅有 1 项）。这正是论文 "minimal information" 论证的关键：

| | ConStat | lz\* |
|---|---|---|
| 每次检测所需 eval runs | 42 (2 benchmarks × 21 models) | 1 |
| 需要 reference benchmark | 是 | 否 |
| 需要 reference models | ≥5 | 0 |
| 适用于第三方审计 | 否（需控制评估流程） | 是 |

模拟中 ConStat 在有完整输入时 power 很高（25%+ contam → 100%），但 lz\* 的 absolute right-tail test 因 θ-shift 效应 power=0——这与 ctrl-contam-pilot 实验中的 θ-shift 发现完全一致，论文中使用 Δlz\*（对比 clean baseline）来规避这一问题。

---
