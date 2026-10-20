# code alpha sweep aggregation script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha_sweep_aggregation_script_20260514T211956_result.json`
- **Structured JSON:** [`4d8ca8d803cecea70fc6.json`](../../sessions/4d/4d8ca8d803cecea70fc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已部署并验证通过。

**输出**:
- `results/alpha_sweep_analysis/phase_diagram.csv` — 每行一个 (α, seed, channel) 组合，包含 lag, r_value, p_value, is_significant, lead_time_generations
- `results/alpha_sweep_analysis/phase_diagram.json` — 完整结果 + 按 α 分组汇总 + phase boundary 检测

**当前状态**: 只有 `a000_s42`（6 代）可分析，`a025_s42` 仅 1 代被跳过。α=0.0 下所有 channel 的 permutation test 均不显著（样本量太小，只有 6 个时间点）。等更多 α 和 seed 的实验跑完后，重新执行即可获得完整 phase diagram 数据。

---
