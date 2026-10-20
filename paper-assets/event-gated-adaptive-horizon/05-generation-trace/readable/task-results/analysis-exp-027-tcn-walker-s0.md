# analysis exp 027 tcn walker s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_027_tcn_walker_s0_20260520T060817_result.json`
- **Structured JSON:** [`7f20569e7a17f8617710.json`](../../sessions/7f/7f20569e7a17f8617710.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**NEGATIVE。** TCN σ=0.5×std 双重失败：

1. **NVE 未被有效抑制**：出现两次 CIVO episodes，NVE 飙升到 1.7 (55K) 和 **4.0** (85K)。85K 的 4.0 比之前 registry 记录的 80K 数据更严重——之前只观察到恢复趋势，实际在 85K 发生了第二次更猛烈的爆发。
2. **eval 远低于目标**：峰值仅 239.9 (35K)，最终 95.5，仅为 baseline (~900) 的 10.6%。

训练正常跑完 105K 目标步数（EXIT_CODE=0），不是提前退出。

TCN 有一个有趣的"自修正"现象（NVE 飙升后能自发回落），但这是**事后修复**而非**事前预防**——修复发生时 eval 已经崩塌。σ=0.5×std 的噪声强度不足以阻止 critic 学到 dt-specific value bias。

报告已写入 artifacts 并注册 (`art_20260520_ec6135`)。

---
