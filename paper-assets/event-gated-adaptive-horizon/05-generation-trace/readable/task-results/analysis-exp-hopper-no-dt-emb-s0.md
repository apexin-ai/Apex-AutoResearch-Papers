# analysis exp hopper no dt emb s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_hopper_no_dt_emb_s0_20260527T111234_result.json`
- **Structured JSON:** [`46cf2e243a7134c129fb.json`](../../sessions/46/46cf2e243a7134c129fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE(success)。

## 结果摘要

**Hypothesis: SUCCESS** — 移除 dt_embedding (dt_embed_dim=0) 后 Hopper 仍表现 severe learning delay，确认 gate 机制本身是根因。

### 关键数据

| 实验 | 配置 | eval_return_final | 状态 |
|------|------|-------------------|------|
| baseline | 无 gate | 96.43 @ 105K | 正常学习 |
| trained_s0_ext | trained dt_emb | 81.58 @ 150K | 延迟后恢复 |
| **no_dt_emb_s0** | **无 dt_emb** | **10.76 @ 105K** | **严重延迟** |
| frozen_s0_ext | frozen dt_emb | 0.56 @ 160K | 不可恢复 |

### CIVO/NVE 分析
- NVE 在 35K(4.37)、75K(1.60)、95K(3.77) 有孤立尖峰，但**无连续 ≥2 点 > 1.5×**
- D155 CIVO 三维判据**不满足** — 无持续性 value overestimation
- 65K 处 ve_ratio=131071 为除零膨胀（eval_return=0.0），已排除

### 核心证据
1. eval_return 仅为 baseline 的 11.2%
2. 策略 entropy 保持近最大值（~5.5）到 55K，比 baseline 延迟 ~30K 步
3. Value function 发育严重受阻（105K 时仅 baseline 的 4.3%）
4. 无 dt_emb 的表现甚至略差于 trained dt_emb 在同步数下的表现

**结论**: Hopper 的 failure 是 gate 机制（subsample + fixed dt）导致的，与 dt_emb CIVO 无关，支持 D162 重分类。

---
