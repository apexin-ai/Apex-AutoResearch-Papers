# analysis exp 032b dual critic walker s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_032b_dual_critic_walker_s1_20260521T054939_result.json`
- **Structured JSON:** [`0528d22ca19a545ef332.json`](../../sessions/05/0528d22ca19a545ef332.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, report registered. Here's the summary:

---

## exp_032b_dual_critic_walker_s1 — Conclusion: **NEGATIVE**

### 核心数据
| 指标 | 值 | 标准 | 判定 |
|------|-----|------|------|
| Peak NVE | **1.4** (@ 85K) | < 1.5 | PASS |
| Final eval | **516** (@ 215K) | ~900 | **FAIL (57%)** |

### NVE 轨迹
```
15K→0.0  25K→0.2  35K→0.4  45K→0.8⚠  55K→0.7  65K→0.7  75K→0.7
85K→1.4★ 95K→0.7  105K→0.5  115K→0.9  125K→0.3  135K→0.4
145K→0.3  155K→0.2  165K→0.2  175K→0.2  185K→0.1  195→215K→0.1
```
NVE 全程 < 1.5，85K 短暂 spike 后迅速回落。CIVO 被有效抑制。

### Eval Return 轨迹
缓慢上升：75K→241, 105K→228, 155K→361, 195K→544, 205K→552(peak), 215K→516。始终远低于 baseline ~900。

### 关键发现
1. **Value1 ≈ Value2**：两个 critic 输出几乎一致（差异 < 0.5），min(Q1,Q2) 未产生保守估计效应
2. **Gate 完全坍塌**：gate_dt_2_frac = 1.0 全程，adaptive horizon 无效
3. **Actor loss ≈ 0**：后期 actor 梯度信号极弱，学习停滞

### 对 Intervention Hierarchy 的含义
Dual-critic 成功抑制 NVE 但性能代价过大（43% drop）。不过 gate 坍塌（dt=2 锁定）是独立 confound——无法确定性能损失来自 dual-critic 还是 gate 问题。**两个受影响的 decisions（D120 wide-single-critic ablation, D121 Cheetah dual-critic）需要结合这个 negative 结论重新评估。**

---
