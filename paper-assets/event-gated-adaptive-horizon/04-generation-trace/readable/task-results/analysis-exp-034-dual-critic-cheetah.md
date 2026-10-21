# analysis exp 034 dual critic cheetah

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_034_dual_critic_cheetah_20260521T120432_result.json`
- **Structured JSON:** [`239860adea70159723a5.json`](../../sessions/23/239860adea70159723a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE + negative。

## exp_034 结论: **negative**

### 核心数据
| 指标 | 值 |
|------|-----|
| Eval peak | 315.7 @ 45K |
| Eval final | 97.5 @ 215K |
| ve_ratio peak | **1.8** @ 55K（超 1.5× 阈值）|
| CIVO alerts | 2 次（95K, 105K）|
| v1 ≈ v2 | 全程 ρ>0.999 |
| Gate | dt=2 固定，entropy=0 |

### 训练动态：双波 CIVO
1. **First wave (45K→55K)**: eval 从 315.7 崩至 34.5, ve_ratio 飙至 1.8
2. **Partial recovery (65K→75K)**: eval 回到 183.0
3. **Second wave (85K→105K)**: eval 再崩至 27.2, ve_ratio=1.6
4. **Long tail (115K→215K)**: eval 在 50-150 波动，value 持续衰退至 14.2

### 对比

| | Baseline (010b) | Dual-critic (034) | Walker DC (032 s0) |
|--|----------------|-------------------|-------------------|
| Peak ve_ratio | NVE=70.64 | **1.8** | <1.0 |
| Final eval | 0.83 | **97.5** | 787.7 |
| CIVO suppressed? | No (catastrophic) | **No (partial)** | Yes |

### 判定理由
- CIVO 未完全抑制（ve_ratio > 1.5×，eval 从 peak 跌 91%）→ 不能声称跨环境通用性
- 但 dual-critic 将 Cheetah 的 overestimation 压制了 ~40×（1.8 vs 70.64），防止了灾难性崩溃
- v1≈v2 确认两个 critic 无差异化响应 → dual-critic 不通过 critic 分歧工作
- 在 intervention hierarchy 中: **architecture-level (dual-critic) > representation-level (SGS)** 在 Cheetah 上成立，但仍不足以完全抑制

---
