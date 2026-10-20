# analysis exp 029c tcn walker s0 sigma01

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_029c_tcn_walker_s0_sigma01_20260520T193233_result.json`
- **Structured JSON:** [`82dceb3d0a6c6059d600.json`](../../sessions/82/82dceb3d0a6c6059d600.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed for the complete analysis.

## 分析结果

- **训练完成情况**: 跑完，实际到 224K（超过目标 210K），EXIT_CODE=0
- **退出原因**: 正常完成
- **最终 step**: 215000（最后一次 eval），224000（最后一次 train log）
- **eval_return 最终值**: 328.3 @ 215K (peak: 490.7 @ 165K)
- **NVE max**: ~1.02 @ 85K-95K（registry 精确值 1.0218 @ 95K）
- **NVE 是否全程 < 1.5×**: 是，max 仅 1.02
- **NVE 曲线趋势**: 0→0.5(45K)→1.0(85-95K peak)→逐步下降→0.1(215K)。单峰，温和上升后平稳回落，全程远低于 CIVO 阈值
- **与 σ=0.2 对比**: eval 差距巨大（490.7 peak vs ~891 baseline），σ=0.2 达到 baseline 而 σ=0.1 仅达 55%。NVE 表现类似（两者都抑制了 CIVO）
- **建议 conclusion**: **negative**
- **理由**: σ=0.1 成功抑制 CIVO（NVE<1.5×），但 eval_return 远低于 baseline（peak 490 vs 891 = 55%），且后期出现策略不稳定（188K-224K train_return 在 15-665 之间剧烈振荡，双峰分布）。这说明 σ=0.1 低于最小有效剂量——能防 CIVO 但不足以稳定学习。三点剂量响应曲线：σ=0.1（防CIVO但性能差）< σ=0.2（防CIVO且达baseline）< σ=0.5（振荡性CIVO）。最优窗口在 σ≈0.2 附近。
- **checkpoint_path**: `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt`
- **W&B run_id**: 无（此实验未启用 W&B）

### 完整 NVE 曲线

| Step | ve_ratio | eval_return |
|------|----------|-------------|
| 5K   | —        | 35.6        |
| 15K  | 0.0      | 99.1        |
| 25K  | 0.2      | 140.7       |
| 35K  | 0.3      | 155.7       |
| 45K  | 0.5      | 160.9       |
| 55K  | 0.4      | 254.8       |
| 65K  | 0.5      | 268.7       |
| 75K  | 0.6      | 295.5       |
| 85K  | 1.0      | 220.8       |
| 95K  | 1.0      | 188.6       |
| 105K | 0.8      | 204.7       |
| 115K | 0.5      | 296.4       |
| 125K | 0.5      | 232.3       |
| 135K | 0.4      | 247.4       |
| 145K | 0.3      | 323.1       |
| 155K | 0.2      | 359.7       |
| 165K | 0.1      | **490.7**   |
| 175K | 0.3      | 246.2       |
| 185K | 0.3      | 220.6       |
| 195K | 0.3      | 212.8       |
| 205K | 0.2      | 256.9       |
| 215K | 0.1      | 328.3       |

### 关键发现

1. **CIVO 完全被抑制**：NVE 全程 ≤1.02，与 σ=0.2 表现一致
2. **性能严重不足**：eval peak 仅 490（baseline 的 55%），而 σ=0.2 达到 baseline
3. **后期策略崩溃**：188K+ train_return 出现双峰（~20 vs ~500），说明策略不稳定与 CIVO 无关
4. **dose-response 非单调**：σ=0.1 和 σ=0.2 都抑制 CIVO，但只有 σ=0.2 能同时维持性能，说明 TCN 在 σ=0.2 水平还提供了 CIVO 之外的额外正则化效果

---
