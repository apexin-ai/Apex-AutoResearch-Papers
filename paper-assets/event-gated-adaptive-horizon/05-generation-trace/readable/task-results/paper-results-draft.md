# paper results draft

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results-draft_20260516T051130_result.json`
- **Structured JSON:** [`12c683232eefde00de41.json`](../../sessions/12/12c683232eefde00de41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results section draft written to `paper/sections/results.md` and registered as `art_20260516_b7768b`.

**覆盖内容：**

- **F1** (C1): 所有 dt>1 配置退化 — exp_001/005/006/007 对比，含学习曲线占位
- **F2** (C2): 核心发现 — NVE>1.5x 阈值 4/4 分离表、2×2 因果矩阵表（trained×multi-rate）、008d 两 seed post-CIVO 轨迹（seed 1 振荡退化 + actor_loss 翻正、seed 2 自修正至 278.5@95K）
- **F3** (C3): 008a 值抑制 — 105K=777.7（85% baseline），NVE 0.59-0.93x，两个 V 形恢复周期
- **F4** (C4): dt=2 > dt=4 单调退化，007 的 v/e=0.126 表明预测质量过差无法触发 CIVO
- **F5** (C5): horizon/subsample 次要 — 008e_v3 s1=95% baseline, 008c vs 008a 对比
- **梯度分解**: 93%/7%/0% 表（标注 step 95K），016e 作为 no-op 解释，reward gradient = "numerically negligible—zero to within floating-point precision"
- **三种崩溃机制**: CIVO / Gradient Starvation / IRD 对比表，各附 representative exp 和机制描述
- **018/019 占位符**: Full-pathway SGS + PickCube 跨环境验证

**遵守的写作规则**: 009b peak=278.5@95K、008a 标注为 "trained-but-unexposed"、016e NVE=10.42x (normalized)、016e vs 008d 差异归因于 "cross-seed variation"、008e_v3_s2 标注为 IRD（非 CIVO）、015b 标注为 gradient starvation。

---
