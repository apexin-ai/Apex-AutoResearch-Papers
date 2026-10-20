# analysis exp 088 cheetah 008d s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_088_cheetah_008d_s1_20260525T210614_result.json`
- **Structured JSON:** [`b82822f7e96b165d581a.json`](../../sessions/b8/b82822f7e96b165d581a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## exp_088_cheetah_008d_s1 分析总结

**Conclusion: negative — CIVO 未触发，跨 seed 复制失败。**

### 关键指标
| 指标 | exp_088 (s1) | exp_078 (s0) |
|------|-------------|-------------|
| NVE peak | **0.52×** @45K | **4.1×** @75K |
| NVE onset | 无 | 45K (NVE=1.7×) |
| NVE classification | **no_onset** | onset_self_correcting |
| CIVO | **false** | true |
| ve_ratio peak | 0.31 @45K | 2.32 @75K |
| eval_return final | 309.3 (69.6% baseline) | 119.5 (~27% baseline) |
| eval_return peak | 309.3 @105K | 213.7 @35K |
| gate entropy | 0.0 (stuck dt=2) | — |

### 核心发现

1. **NVE 全程远低于 1.5× 阈值**：peak 仅 0.52×，D155 三维标准全部未满足。
2. **Gate 完全未学习**：dt_mean=2.0, dt_2_frac=1.0, entropy=0.0 — 全程锁定在 dt=2，无自适应行为。
3. **与 parent 模式相反**：exp_078 出现强烈 value expansion（ve_ratio 从 0.04 飙升到 2.32 再回落），exp_088 的 ve_ratio 始终低平（0.01–0.31），无任何 onset 迹象。
4. **但 eval 性能反而更好**：exp_088 final 309.3 vs exp_078 final 119.5。没有 value expansion 反而带来了更稳定的训练——这提示 exp_078 的 CIVO 现象可能是 seed-specific 的训练不稳定性，而非 systematic mechanism。

### 结论
Cheetah Run 的 CIVO onset 不具备跨 seed 可复现性。seed=1 在相同配置下未出现 value expansion，且 gate 完全退化为固定 dt=2。exp_078 的 NVE=4.1× 可能是 seed=0 特有的训练动态，而非由 trained dt_emb + subsample 机制 systematically 引发。

---
