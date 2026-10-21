# analysis controlb results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_controlb_results_20260515T141047_result.json`
- **Structured JSON:** [`655aa996206be739bae6.json`](../../sessions/65/655aa996206be739bae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## Control B 结果汇总

| 条件 | 正常 ρ | Shuffled ρ (均值) | Shuffled ρ (最佳层) | 判定 |
|------|--------|-------------------|---------------------|------|
| OpenVLA trained | **0.955** | 0.0012 | 0.0123 (L8) | PASS |
| OpenVLA untrained | **0.933** | 0.0003 | 0.0085 (L1) | PASS |
| DINOv2 baseline | — | 0.039 | — | ref |

**Null control 通过。** 两个实验 shuffled ρ 均 < 0.013，远低于 0.1 阈值，与正常实验的 ρ ≈ 0.95 相差 >100 倍。Probe 不是过拟合——正常实验的高 ρ 反映的是 OpenVLA features 中真实的 temporal-distance 信号。

报告已保存至 `artifacts/controlb_analysis/controlb_analysis.md`，两个实验 registry 已更新为 DONE/success。

---
