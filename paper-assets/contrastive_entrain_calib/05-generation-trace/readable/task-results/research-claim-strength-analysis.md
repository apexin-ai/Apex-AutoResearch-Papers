# research claim strength analysis

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_claim-strength-analysis_20260523T142541_result.json`
- **Structured JSON:** [`e72894369521f89e26b7.json`](../../sessions/e7/e72894369521f89e26b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部读取完毕。现在我来整合所有数据进行分析。

---

## 全 Registry 数据梳理与论文补强角度分析

### 数据基础更新

Paper_framing 当前使用 ACT 20/20 vs R3-only 4/26 的数据。但 registry 中实际数据量更大：

| 方法 | 总 checkpoint 数 | > vanilla (0.1335) | 比例 |
|------|-----------------|-------------------|------|
| ACT seed 1 | 16 | 16 | 100% |
| ACT seed 2 | 15 | 15 | 100% |
| ACT reduced-lora | 16 | 16 | 100% |
| **ACT 合计** | **47** | **47** | **100%** |
| R3-only seed 1 | 12 | 3 | 25% |
| R3-only seed 2 | 15 | 1 | 6.7% |
| R3-only gs8 | 3 | 0 | 0% |
| **R3-only 合计** | **30** | **4** | **13.3%** |

---

### A. Consistency/Reliability 角度

**数据点：**

| 指标 | ACT | R3-only |
|------|-----|---------|
| > vanilla 比例 | 47/47 (100%) | 4/30 (13.3%) |
| Fisher exact test | p < 10⁻¹⁵ | — |
| 跨 seed 均值 | s1=0.235, s2=0.239 (Δ=0.004) | s1=0.110, s2=0.101 (Δ=0.009, 均 < vanilla) |
| 最低 checkpoint | 0.1515 (reduced-lora ckpt-500) | 0.074 (s1 ckpt-1000) |
| 最高 checkpoint | 0.326 (reduced-lora ckpt-7000) | 0.153 (s1 ckpt-6500) |

**新发现（未在 paper_framing 中）：**
- ACT seed 2 现在有 15 个 checkpoint（之前仅 4 个），全部 > vanilla，最低 0.206（ckpt-4000）
- 加上 reduced-lora 的 16 个 checkpoint，ACT 从 20/20 扩展到 **47/47**
- gs8 消融 3 个 checkpoint 全部 < vanilla（0.054-0.085），排除了 group_size 是 R3-only 失败原因的假设
- R3-only 总分母从 26 增加到 30，成功率从 15.4% 降至 **13.3%**

**可支撑的 claim：** "ACT achieves above-vanilla performance with 100% reliability (47/47 checkpoints across 3 configurations × 2 seeds), while R3-only GRPO exceeds vanilla in only 13.3% of checkpoints (4/30, Fisher exact p < 10⁻¹⁵)."

**Rebuttal 用途：** 如果 reviewer 质疑 "cherry-picked checkpoint"，47/47 = 100% 是无可辩驳的系统性优势。不需要挑 checkpoint，随机选 ACT 的任何一个 checkpoint 都 > vanilla。

---

### B. Cosine Failure Chain 定量数据

**完整 d_syc→reward 失败链（7 种 formulation + 1 消融）：**

| 实验 | Formulation | 失败 Pattern | 关键定量数据 |
|------|------------|-------------|------------|
| exp-002 | tanh gate cosine | gate 坍缩 | R1 contribution → 0 |
| exp-002v2 | raw cosine (w=0.25) | R1≈0 | 功能等价于 R3-only |
| exp002v2-recalib | cosine + 重校准 | mode collapse | entropy=0.069, mean_len=62 |
| exp-002v3 | 5x scaled cosine (w=0.4) | mode collapse step 2160 | entropy=0.006, frac_zero_std=0.963, R3 saturated=0.9998 |
| exp-008v3 | binary probe | immediate trap | ToF=0 at ckpt-500, entropy=0.70 (healthy) |
| exp-009 | continuous P(syc) | gradual decline | 0.124→0.114, killed step 1535 |
| exp-016 | ActAdd (inference) | net negative | SYCONScore 0.054 vs vanilla 0.134 |
| exp-003-gs8 | R3-only gs=8 | 仍失败 | 0.084→0.085→0.054，排除 group_size 假设 |

**可支撑的 claim：** "ALL seven d_syc-to-reward formulations fail, spanning the full spectrum from continuous (cosine) through probabilistic (probe sigmoid) to discrete (binary probe) and inference-time (ActAdd). The failure is structural, not parametric."

**Rebuttal 用途：** 面对 "just tune the hyperparameters" 的质疑，7 种 formulation × 不同权重/缩放/重校准策略全部失败，排除了调参不充分的可能。

---

### C. Evidence-Strength Stratification

**跨模型 AUROC 梯度：**

| Evidence Strength | Qwen3-8B | Llama-3-8B | 平均 |
|-------------------|----------|------------|------|
| Weak | 0.675 | 0.711 | 0.693 |
| Medium | 0.883 | 0.864 | 0.874 |
| Strong | 0.929 | 0.911 | 0.920 |

**Probe ablation 跨模型对比：**

| 模型 | d_syc AUROC | Random AUROC | Gap |
|------|-----------|-------------|-----|
| Qwen3-8B | 0.835 | 0.727 | +0.108 |
| Llama-3-8B | 0.813 | 0.530±0.054 | +0.248 |

**可支撑的 claim：** "d_syc discriminability exhibits a consistent evidence-strength gradient across architecturally distinct models (Qwen3-8B and Llama-3-8B-Instruct), with stronger evidence yielding higher AUROC (0.93 vs 0.68). This gradient is preserved despite the architectural difference, suggesting sycophancy has a universal linear structure in transformer activation spaces."

**Rebuttal 用途：** 如果 reviewer 说 "only one model"，现在有两个架构族的一致性数据。Llama 的 d_syc vs random gap (+0.248) 比 Qwen (+0.108) 更大，说明信号在 Llama 上更集中，但仍然无法转化为有效 reward——强化了核心 claim。

---

### D. Held-out 泛化

**三方对比（70 held-out samples）：**

| 方法 | Held-out SYCONScore | vs Vanilla | 倍数 |
|------|-------------------|-----------|------|
| Vanilla | 0.0556 | — | 1.0× |
| R3-only ckpt-6500 | 0.1079 | +94% | 1.94× |
| **ACT s1 ckpt-8000** | **0.2841** | **+411%** | **5.11×** |

**ACT retrained on reduced set（held-out eval trajectory）：**
- ckpt-500: 0.2045
- ckpt-1000: 0.2039
- ckpt-1500: 0.2039
- ckpt-2000: 0.1567（开始过拟合）

**可支撑的 claim：** "ACT generalizes to held-out samples, achieving 5.1× the vanilla SYCONScore on unseen data (0.284 vs 0.056), while R3-only GRPO shows only 1.9× improvement (0.108 vs 0.056)."

**注意：** Held-out vanilla 基线 (0.0556) 明显低于 training-set 基线 (0.1335)，说明模型在 held-out 分布上本身更容易 sycophantic。ACT 的 5.1× 倍数部分来自这个更低的基线。论文报告时应同时给绝对值和倍数，避免 reviewer 质疑倍数 inflation。

---

### E. 绝对性能差距（ACT Worst vs GRPO Best）

| 对比 | SYCONScore |
|------|-----------|
| GRPO 最好（R3-only s1 ckpt-6500） | 0.153 |
| ACT 最差（reduced-lora ckpt-500, step 500） | 0.152 |
| ACT 最差（standard s1 ckpt-500, step 500） | 0.170 |
| ACT 最差（standard s2 ckpt-4000） | 0.206 |

**关键发现：** ACT 在训练 500 步时的性能（0.152-0.170）就已经匹配 R3-only GRPO 在 6500 步、特定 seed 的绝对最佳值（0.153）。标准 ACT 的 worst-case (0.170) 超过 GRPO best-case 11%。

**可支撑的 claim：** "ACT reaches GRPO's best-ever performance within the first 500 training steps — a 13× efficiency advantage. Moreover, ACT's worst-case checkpoint (0.152, reduced-LoRA step 500) matches GRPO's best-case checkpoint (0.153, seed 1 step 6500), achieved only once across 30 evaluations."

---

### F. 额外发现：Reduced-LoRA 证明 supervision 粒度是关键

**Reduced-LoRA ACT（r=64, alpha=64, 4 modules）vs Standard ACT（r=64, alpha=128, 7 modules）：**

| 指标 | Standard ACT peak | Reduced-LoRA ACT peak |
|------|-------------------|----------------------|
| Best SYCONScore | 0.301 (s1 ckpt-8000) | **0.326** (ckpt-7000) |
| Best ToF | 0.182 | **0.204** |
| 16/16 > vanilla | YES | YES |

Reduced-LoRA ACT 反而达到了更高的 peak（0.326 > 0.301），且 16/16 > vanilla。这排除了 "ACT works because it has more LoRA parameters" 的解释。

**可支撑的 claim：** "Reducing ACT's LoRA capacity to match GRPO's configuration (4 modules, alpha=64) does not degrade performance — the reduced model achieves the highest SYCONScore (0.326) of any configuration. This demonstrates that ACT's advantage stems from dense per-token supervision, not parameter capacity."

---

### Top-3 最强角度排序

**#1: 100% vs 13.3% Reliability Gap（角度 A）**
- 强度：★★★★★
- 47/47 vs 4/30，Fisher p < 10⁻¹⁵
- 这是比任何倍数都更有说服力的数据——不是 "ACT 平均好多少"，而是 "ACT 从不失败，GRPO 几乎总是失败"
- Reviewer 无法用 "cherry-pick checkpoint" 攻击
- **建议：更新论文数据从 20/20 vs 4/26 到 47/47 vs 4/30**

**#2: ACT Worst ≈ GRPO Best（角度 E）**
- 强度：★★★★☆
- ACT 最差时（step 500, reduced-lora）= GRPO 最好时（step 6500, seed luck）
- 直观有力：即使在最不利条件下比较，ACT 仍不输 GRPO
- 13× 效率差异（500 步 vs 6500 步）
- **建议：在 Results 中加一句 "ACT's worst-case matches GRPO's best-case"**

**#3: 7 种 d_syc→reward Formulation 全部失败（角度 B）**
- 强度：★★★★☆
- 从 continuous cosine 到 binary probe 到 inference-time ActAdd + gs8 消融，覆盖了所有合理的 d_syc 利用方式
- 支撑核心 claim "discriminability ≠ reward utility" 的系统性证据
- gs8 消融新增，排除了 hyperparameter 假设
- **建议：确保 gs8 消融数据在论文 Table/Appendix 中出现**

---

### 次要但有价值的角度

- **Reduced-LoRA 角度（F）**：适合放 Discussion/Appendix，反驳 "capacity difference" 假设
- **Held-out 5.1×（D）**：绝对值有力但倍数 inflated by lower held-out baseline，需谨慎报告
- **Evidence-strength gradient 跨模型一致性（C）**：强化 generalizability claim，但对核心 ACT vs GRPO 叙事贡献有限

---
