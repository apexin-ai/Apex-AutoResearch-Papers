# analysis openvla pertask gap

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla-pertask-gap_20260517T224144_result.json`
- **Structured JSON:** [`75b94b6f967351cad1cd.json`](../../sessions/75/75b94b6f967351cad1cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，已写入 `artifacts/openvla_gap_analysis.md`。

核心发现：

**69% 的数字不可靠。** 10 trials/task 的方差极大（bbq_sauce 仅 2/10 但真实 SR 可能在 50-60%）。三个低分 task 拖低了均值 ~12pp。

**主要 gap 来源：**
1. 样本量过小（10 vs 50 trials，贡献 8-12pp 误差）
2. 只采样了 initial_states[0:9]，可能命中较难配置
3. seed=42 vs 论文 seed=7 + 3-seed 平均
4. RTX 4090 vs A100 的 GPU 非确定性

**建议：** 用 seed=7、50 trials/task 重跑一次完整 eval。预期结果应在 80-85% 范围，剩余 3-8pp gap 属于已知复现问题，可接受作为 baseline。当前 69% 不应作为论文中引用的 OpenVLA baseline 数值。

---
