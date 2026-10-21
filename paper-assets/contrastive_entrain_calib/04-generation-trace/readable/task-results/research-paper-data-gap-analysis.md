# research paper data gap analysis

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-data-gap-analysis_20260519T082749_result.json`
- **Structured JSON:** [`6f67f698c7db69ddbbd2.json`](../../sessions/6f/6f67f698c7db69ddbbd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Claim-by-Claim 缺口分析

---

### Claim 1: Directional discriminability + training stability
> d_syc 区分 sycophantic capitulation vs genuine belief revision (AUROC ≥ 0.82)，训练中方向稳定 (cosine ≈ 0.96)

**支撑实验:**
- ✅ **exp-001** (DONE, success): CV AUROC 0.827, layer progression (L19 best), per-strength AUROC (weak 0.675, medium 0.883, strong 0.929)
- ✅ **exp-002v2** (DONE, killed but有 stability 数据): step 500 cosine≈0.96 (D025 修正后), per-layer AUROC 0.78–0.84
- ⏳ **exp002v2-recalib** (RUNNING, ETA May 22): 将提供 recalibration 后的完整 stability 曲线

**缺口:**
- ⚠️ 完整训练曲线 stability (只有 step 500 一个点，需要 step 1000/2000/4000 等多个 checkpoint 的 cosine + AUROC)
- ⚠️ exp002v2-recalib 能否产出多 checkpoint stability 数据取决于是否在训练中保存了中间 checkpoint

**风险: LOW** — Claim 1 证据链基本完整。exp-001 + exp-002v2 step 500 数据已足够支撑。exp002v2-recalib 完成后可补充更多数据点。弱项是 weak evidence 子集 AUROC 只有 0.675，审稿人可能追问。

---

### Claim 2: DC-GRPO effectiveness
> DC-GRPO (用 d_syc angular alignment 作 R1) 降低 sycophantic capitulation 同时保留 genuine belief revision，打破 double-bind

**支撑实验:**
- ⏳ **exp002v2-recalib** (RUNNING, ETA May 22): DC-GRPO + recalibration，**但 R1 贡献仅 8%，极可能 ≈ exp-003 (R3-only)**
- 📝 **exp-002v3** (PREPARING): scaled cosine R1 (scale_factor=5, R1 weight=0.4)，**这才是 Claim 2 的关键实验，尚未启动**
- ⏳ **exp-003** (RUNNING, ETA May 21): R3-only baseline — 必须有此对照
- ⏳ **exp-004** (RUNNING, ETA 今晚): ACT baseline — 重要对照
- ⏳ **exp-008v3** (RUNNING, ETA May 22): Binary Probe GRPO baseline — ablation 对照
- ✅ **exp-016** (DONE): ActAdd inference-time steering — 辅助证据 (NoF 78.5% at α=5)

**缺口:**
- ❌ **无任何已完成的 DC-GRPO 实验有 effective R1 信号**。exp-002 (tanh 饱和 killed), exp-002v2 (killed), exp002v2-recalib (R1 信号弱 8%), exp-002v3 (未启动)
- ❌ **exp-002v3 是唯一能验证 Claim 2 的实验**，但还在 PREPARING 状态，需 ~52h 训练 + 4-8h eval
- ❌ **无 seed 复现**: exp-003-s2 等 GPU，DC-GRPO 更没有 s2
- ❌ **无 eval 结果**: 所有训练实验尚未有 NoF/WRR 评估数据
- ❌ **Reward weight sensitivity analysis**: 只有一组权重配置

**风险: CRITICAL** — 这是论文的核心 claim，目前 0 个实验能支撑。如果 exp002v2-recalib ≈ exp-003 (高概率)，且 exp-002v3 来不及完成或结果 negative，论文无法成立。

---

### Claim 3: Representation-level diagnostic value (R1-R3 disagreement)
> R1-R3 disagreement 分析：方向投影检测到行为奖励遗漏的 sycophantic internal reasoning

**支撑实验:**
- ❌ **无专门实验**。需从 DC-GRPO 训练日志中提取，前提是有一个 R1 有效的 DC-GRPO 完成训练

**缺口:**
- ❌ 依赖 Claim 2 的实验完成
- ❌ 无 disagreement frequency 统计
- ❌ 无 qualitative examples

**风险: HIGH** — 完全依赖 Claim 2 实验。但作为 analysis subsection (非 top-level contribution)，如果 Claim 2 实验有数据，可快速产出。

---

### Baselines 缺口（审稿人 "why didn't you compare with X"）

| Baseline | 状态 | 风险 |
|----------|------|------|
| R3-only (behavioral GRPO) | ⏳ exp-003 running, May 21 | OK |
| ACT (undifferentiated consistency) | ⏳ exp-004, 今晚完成 | OK |
| Binary Probe GRPO | ⏳ exp-008v3, May 22 | OK |
| Continuous Probe (exp-014) | ❌ killed (mode collapse) | ⚠️ 可作为 negative result 报告 |
| ActAdd inference-time | ✅ exp-016 done | OK |
| Vanilla (no training) | ⏳ eval 进行中 | OK |
| **SMART / "Pressure What Pressure"** | ❌ 无 | MEDIUM — 审稿人会问 |
| **BCT baseline** | ❌ 无 | MEDIUM — paper_framing 提到但无实验 |
| **Latent-GRPO (Zhang 2026)** | ❌ 无 | LOW — 太新，不太会要求 |
| **第二个 model family (Llama-3-8B)** | ❌ 无 | MEDIUM — paper_framing 承认 |

---

## 时间线可行性

```
May 19 (今天):
  - exp-004 完成 → eval 4-8h → May 20 早有结果
  - exp-002v3 代码完成 + deploy

May 20:
  - exp-002v3 开始训练 (~52h)
  - exp-004 eval 完成

May 21:
  - exp-003 完成 → eval 4-8h → May 22 有结果

May 22:
  - exp002v2-recalib 完成 → eval 4-8h → May 23 有结果
  - exp-008v3 完成 → eval 4-8h → May 23 有结果
  - exp-002v3 最早完成（如 May 20 中午启动）→ eval → May 23 结果

May 23:
  - 最乐观：所有 eval 完成，开始写论文
  - 距 DDL 仅 2 天

May 25:
  - DEADLINE
```

**结论: 时间线极度紧张，可行性 < 30%。**

关键瓶颈不是工程时间而是实验风险：
1. **exp-002v3 (52h)** 必须今天启动且结果 positive，否则 Claim 2 无法成立
2. 即使 exp-002v3 成功，May 23 才有结果，只剩 2 天写完整论文
3. **0 容错空间** — 任何一个环节出问题（训练 crash、eval bug、结果 negative）直接 miss DDL

---

## Overall 评估

| 维度 | 评级 |
|------|------|
| Claim 1 (方向可区分+稳定) | 🟢 基本就绪 |
| Claim 2 (DC-GRPO 有效性) | 🔴 关键缺失，核心风险 |
| Claim 3 (R1-R3 disagreement) | 🟡 依赖 Claim 2 |
| Baselines | 🟡 核心对照在跑，缺 SMART/BCT |
| 时间线 | 🔴 可行性 < 30% |

### 建议优先级

1. **P0 — 立即启动 exp-002v3**: 今天内完成代码 + dry-run + 部署。这是唯一能救 Claim 2 的实验。但需要 GPU — 只有等 exp-004 今晚完成释放 28034 GPU 0。

2. **P0 — 准备 Plan B (ARR August)**: 鉴于 May 25 可行性极低，强烈建议准备 fallback 到 ARR August cycle (~Aug 15 DDL)。多出 3 个月可以：
   - 跑完 exp-002v3 并充分 eval
   - 添加 seed 复现
   - 添加 SMART/BCT baseline
   - 尝试第二个 model family
   - 充分写作和润色

3. **P1 — exp-004 完成后立即 eval**: 今晚 exp-004 完成，eval 是 non-blocking 且结果有用（ACT baseline 无论论文何时提交都需要）。

4. **P1 — exp002v2-recalib vs exp-003 对比**: 如果两者结果几乎一致，直接确认 R1 signal weakness 假设，为 exp-002v3 的必要性提供证据。

5. **P2 — 如果 exp-002v3 positive 且冲 May 25**: 牺牲 seed 复现和 SMART/BCT baseline，最小化论文内容到 Claim 1 + Claim 2 (scaled R1) + 现有 baselines。在 Limitations 中承认 single seed / limited baselines。

**核心判断: May 25 提交的成功概率取决于 exp-002v3 是否 positive。如果 negative，论文故事需要根本性重构。建议与用户确认是否冲 May 25 还是转 August。**

---
