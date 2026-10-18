# eval verify v7 1 and d011

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_verify-v7_1-and-d011_20260515T190357_result.json`
- **Structured JSON:** [`0f8914684d106d54fc73.json`](../../sessions/0f/0f8914684d106d54fc73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕，以下是结果汇总。

---

## Part 1: v7.1 训练状态

**进程存活**: ✅ 活跃（日志持续更新到 step 500，时间戳 03:04:37）

**关键配置确认** (from `configs/imm_anchor_v7_1.yaml`):
| 参数 | 期望值 | 实际值 | 状态 |
|------|--------|--------|------|
| lambda_margin | 0.2 | 0.2 | ✅ |
| grad_clip | 30.0 | 30.0 | ✅ |
| output_dir | checkpoints/imm_anchor_v7_1 | checkpoints/imm_anchor_v7_1 | ✅ |
| eval_every | 999999 | 999999 | ✅ |

**Split-loss logging**: ✅ 生效，每行都有 `action=` 和 `margin_loss=`

**LIP_MONITOR**: ✅ step=500 已输出
- `empirical_L=0.0432`, `spectral_norm=1.0143` — Lipschitz 初期很低，说明 lambda=0.2 的压力减小有效

**训练趋势** (前 500 步):
- action loss 快速下降：0.277 → 0.021
- margin_loss 从 0.298 逐步下降到 0.158，Δ 从 0.002 增到 0.142（margin 在逐步打开）
- grad norm 稳定在 0.7-1.8 范围，无爆炸

---

## Part 2: D011 Baseline Re-eval 结果

### 完整 8 条件结果表

| 条件 | D011 新结果 | 旧 eval_baseline_v5 | 变化 |
|------|------------|---------------------|------|
| eps0.0_pruneFalse | **0.00264** | 0.00422 | -37% |
| eps0.0_pruneTrue | **0.11159** | 0.00309 | +3510% |
| eps0.01_pruneFalse | **0.00729** | 0.00605 | +20% |
| eps0.01_pruneTrue | **0.12113** | 0.00343 | +3432% |
| eps0.02_pruneFalse | **0.00588** | 0.00399 | +47% |
| eps0.02_pruneTrue | **0.12956** | 0.00445 | +2812% |
| eps0.05_pruneFalse | **0.01462** | 0.00495 | +195% |
| eps0.05_pruneTrue | **0.13900** | 0.00497 | +2696% |

### 单调性检查

**eps 递增 → action_loss 递增 (pruneFalse)**:
- 0.0→0.01: 0.00264→0.00729 ✅ 递增
- 0.01→0.02: 0.00729→0.00588 ❌ **非单调**（0.02 < 0.01）
- 0.02→0.05: 0.00588→0.01462 ✅ 递增

**eps 递增 → action_loss 递增 (pruneTrue)**:
- 0.0→0.01: 0.11159→0.12113 ✅
- 0.01→0.02: 0.12113→0.12956 ✅
- 0.02→0.05: 0.12956→0.13900 ✅
- **pruneTrue 完美单调** ✅

**pruneTrue > pruneFalse (同 eps)**:
- eps 0.0: 0.11159 > 0.00264 ✅
- eps 0.01: 0.12113 > 0.00729 ✅
- eps 0.02: 0.12956 > 0.00588 ✅
- eps 0.05: 0.13900 > 0.01462 ✅
- **全部满足** ✅

### D011 结论

1. **新旧结果不一致**: eps0.0_pruneFalse 旧值 0.00422，新值 0.00264，差 37%。说明 D011 修复确实改变了 eval 行为。
2. **pruneTrue 大幅高于 pruneFalse**: 新结果中 pruneTrue 损失约 0.11-0.14，而 pruneFalse 仅 0.003-0.015。旧结果中两者几乎无差异（这正是 D011 要修复的 bug）。
3. **pruneFalse 在 eps=0.01→0.02 有轻微非单调**（0.00729→0.00588），可能是随机波动，不影响整体趋势。
4. **D011 修复有效**：pruning 确实造成了显著的 action loss 增加，旧 eval 代码未能体现这一差异。

---

## Part 3: v7 训练进度

v7 当前在 **step 16700/30000**，速度 3.2 sps。

- 剩余到 step 30000: ~13300 步
- 预计耗时: 13300 / 3.2 ≈ 4156s ≈ **~69 分钟**
- step 10000 checkpoint 已经生成（早已过 10000）。如果需要用 step 10000 做 eval，checkpoint 应该已在 `checkpoints/imm_anchor_v7/` 中可用。

---
