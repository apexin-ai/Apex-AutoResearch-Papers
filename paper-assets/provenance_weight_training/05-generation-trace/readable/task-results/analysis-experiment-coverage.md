# analysis experiment coverage

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_experiment_coverage_20260515T155300_result.json`
- **Structured JSON:** [`4bec2f6811b80c466f3b.json`](../../sessions/4b/4bec2f6811b80c466f3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，已注册为 artifact `coverage_analysis`。

## 核心结论

**总体覆盖率 29.4% (10/34)**，10 天内需集中填补以下缺口：

### P0 缺口排序

| 优先级 | 实验 | Claim | 原因 |
|--------|------|-------|------|
| **P0-1** | grid_b_low ×3 seeds 重跑 | C2 | b=0.5 是否全局最优未确认，**Claim 2 有翻车风险** |
| **P0-2** | τ sweep (等待) | C3 | 4 个已在跑，但 τ=0.6 已 negative |
| **P0-3** | 60% contamination pipeline | C1+C2 | "small effect size" 的主要防御线，完全未启动 |
| **P0-4** | batch_size=8/16 ablation | C1 | 回应 "only bs=4" concern，完全空白 |
| **P0-5** | n_min=4/5 + ESS-only seed123 | C1 | 正在 PREPARING，等待即可 |

### 各 Claim 状态

- **Claim 1** (25%): ESS-only baseline 已证明 dual > ESS-only (+0.08 PPL)，核心证据到位。缺 batch_size ablation 和完整 n_min curve
- **Claim 2** (40%): MVP PASS，但 **grid_b_low 失败未重跑是最大风险**——如果 b<0.5 更优，aggregate ratio 需重算
- **Claim 3** (20%+running): τ sweep 正在跑。τ=0.6 已 negative，若 τ=0.7 也 negative 需收窄 robust range

### 立即行动

1. **grid_b_low 重跑** — 不能再等
2. **60% datagen 启动** — unblock 整个 contamination pipeline
3. τ sweep 和 n_min=4 等完成即可

---
