# experiment wild2 ascii perturbation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_wild2-ascii-perturbation_20260520T074223_result.json`
- **Structured JSON:** [`39414ce81f36f0bd21e9.json`](../../sessions/39/39414ce81f36f0bd21e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

| Group | Description | K | κ | Eff-K | SC Acc |
|-------|-------------|---|---|-------|--------|
| A | Standard prompt | 4 | 0.3906 | 1.84 | 53.92% |
| B | Fixed ASCII padding | 4 | 0.4006 | 1.82 | 57.84% |
| C | Variable ASCII padding | 4 | 0.3638 | 1.91 | 53.92% |

**核心发现：**
- 三组 κ 值几乎无差异（0.36–0.40），ASCII padding 并未显著降低 trace 间一致性
- Fixed padding (B) 的 κ 反而略高于 baseline (A)，SC Acc 也最高（57.84% vs 53.92%）
- Variable padding (C) 的 κ 略低（0.3638），但差异很小（Δκ = -0.027）
- 这支持论文 2603.06612 的结论：inter-trace 相关性主要来自模型架构偏置，而非 prompt 内容驱动

**产出文件：**
- 服务器：`/root/symb_invariant_consensus/results/wild2_ascii_perturbation/results.json`
- 本地：`artifacts/wild2_ascii_results.json`（已注册 `art_20260520_5c5dfb`）
- 脚本：`/root/symb_invariant_consensus/analysis_ascii_perturbation.py`
- 总耗时：~17分钟（204题 × 12 traces）

---
