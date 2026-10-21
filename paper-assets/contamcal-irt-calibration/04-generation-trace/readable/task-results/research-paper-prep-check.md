# research paper prep check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-prep-check_20260514T030536_result.json`
- **Structured JSON:** [`b572ac0aa6f30e209036.json`](../../sessions/b5/b572ac0aa6f30e209036.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。下面是分析报告。

---

## Paper Framing 状态

### Core Claims
| Claim | 内容 | 实验证据就绪度 |
|-------|------|---------------|
| **C1 — Calibration** | 4PL+γ IRT 从被污染的 benchmark score 中恢复真实性能，MAE 显著优于 baselines，coverage 达标 | **无** — exp-006 (IRT calibration) 尚未启动，前置依赖链 exp-002→003→006 全未开始 |
| **C2 — Signal Survival** | 检测信号在 RL 后训练下 cliff-like 退化；RRF fusion 提供鲁棒聚合 | **无** — exp-002 (signal pipeline)、exp-003 (RRF)、exp-008 (signal survival analysis) 均未启动 |
| **C3 — Identifiability** | Fisher Information 分析 + 144-condition simulation 建立最低信号质量阈值 | **部分** — 2 个 MVP simulation 通过 (γ recovery + confounding)；exp-004 sweep RUNNING；exp-005 noise propagation 2次失败 |

---

## 实验覆盖矩阵

### experiment_plan 定义 vs registry 实际状态

| 实验 | 优先级 | 计划状态 | Registry 状态 | 阻塞情况 |
|------|--------|---------|--------------|---------|
| **exp-001** SFT injection | P0 | 3 scale × 5 dosage = 15 runs | 训练: 8 DONE, 1 RUNNING; 评估: 1 DONE, 7 RUNNING | 25%/50% dosage 全未注册; 3B 无污染训练; 1.5B 仅 100% running |
| **exp-002** signal pipeline | P0 | 4 signals × all models | **完全未启动** | 依赖 exp-001 eval 完成 |
| **exp-003** RRF aggregation | P0 | RRF vs ablations | **完全未启动** | 依赖 exp-002 |
| **exp-004** simulation sweep | P0 | 144 conditions | **RUNNING** (CPU) | — |
| **exp-005** noise propagation | P0 | ME model | **2次失败** | 需根本性重新设计 |
| **exp-006** IRT calibration | P0 | 4PL+γ + 7 baselines | **完全未启动** | 依赖 exp-003 (整条链断裂) |
| **exp-007** 7B bridging | P1 | 7B SFT injection | 未启动 | — |
| **exp-008** signal survival | P0 | 4×4 heatmap | **完全未启动** | 依赖 exp-002 |
| **exp-009** RL case study | P1 | observational | 未启动 | 依赖 exp-006 + exp-008 |
| exp-014 multi-family | P1 | Llama/Pythia | 未启动 | — |
| exp-015 QC-only 100% | P1 | 0.5B clean contam | 未启动 | — |

### exp-001 细分覆盖（训练 + 评估）

| Scale | 0% s42 | 0% s123 | 5% | 25% | 50% | 100% |
|-------|--------|---------|-----|-----|-----|------|
| **0.5B train** | DONE | DONE | DONE | — | — | DONE |
| **0.5B eval** | RUNNING | DONE | RUNNING | — | — | RUNNING |
| **1.5B train** | DONE | DONE | PREPARING | — | — | RUNNING |
| **1.5B eval** | RUNNING | RUNNING | — | — | — | — |
| **3B train** | DONE | DONE | — | — | — | — |
| **3B eval** | RUNNING | RUNNING | — | — | — | — |

"—" = 未注册，完全缺失

---

## 文献覆盖

**literature_map.yaml 不存在**。无法评估 direct-competitor 覆盖。paper_framing.md 中列出的引用需求：

- 核心必引：Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Mislevy 1986, Lalor et al. AAAI 2024
- Dream D2 补充（DIF、ML calibration、conformal prediction、data attribution、MIRT）：未知是否已进 bib
- DCR (EMNLP 2025)：唯一 direct competitor，必须对比
- Emperor's New Clothes (ICML 2025)：关键 motivator

建议尽快创建 literature_map.yaml 或检查 .bib 文件完整性。

---

## 关键风险

### 1. 核心依赖链完全断裂（RED）
exp-002 → exp-003 → exp-006 是论文的**核心实验**（C1 Calibration Claim 的唯一证据来源），整条链尚未启动。exp-006 的结果直接产出论文的 headline number。11 天内完成这条链需要：
- exp-001 eval 全部跑完（当前 7 个 RUNNING）
- exp-002 signal pipeline 实现 + 运行 (~20 GPU hrs)
- exp-003 RRF aggregation (~2 GPU hrs)
- exp-006 IRT fitting + 7 baselines (~8 GPU hrs)

最乐观估计需要 5-7 天纯执行时间，不含 debug。

### 2. 25%/50% dosage 实验完全缺失（RED）
paper_framing 要求 "dose-response monotonicity" 作为第 5 个评估指标。当前只有 0%/5%/100% 三个点（且仅 0.5B），25%/50% 从未注册。5 个点的 dose-response curve 至少需要 4 个点才有说服力。

### 3. 3B scale 无污染实验（YELLOW）
C1 声称 "3+ model scales"，但 3B 仅有 clean baselines，无任何污染训练。如果删减到 2 scales (0.5B + 1.5B)，需要修改 claim。

### 4. exp-005 noise propagation 连续失败（YELLOW）
C3 的 measurement error model 是论文的理论亮点之一。2 次实现都失败，需要诊断根因。如果放弃，C3 claim 需降级。

### 5. 11 天内无法完成的实验
- **exp-007 (7B)**：30 GPU hrs 训练 + eval，P1 优先级 → 建议放弃
- **exp-009 (RL case study)**：依赖 exp-006/008 → 时间上不可能
- **exp-012 (72B)**：P2 → 放弃
- **exp-014 (multi-family)**：原定 rebuttal-ready → 保持不变

### 6. 论文 Claim 与 Evidence 的 Gap 总结

| Claim | 所需证据 | 已有 | Gap |
|-------|---------|------|-----|
| C1 headline MAE | exp-006 output | 零 | **致命**：核心 claim 无任何数字支撑 |
| C1 dose-response | 5 dosage × 3 scale eval | 1 eval done | 极大 |
| C2 signal heatmap | exp-008 output | 零 | 大 |
| C2 RRF vs ablations | exp-003 output | 零 | 大 |
| C3 simulation sweep | exp-004 output | RUNNING | 中（等待完成） |
| C3 noise prop | exp-005 output | 失败 | 中 |
| Figures (5 required) | 全部依赖实验结果 | 零 | 致命 |

**底线评估**：以当前进度，11 天内完成 EMNLP 2026 ARR May 25 提交的概率很低。建议立即评估是否转向 fallback venue (AAAI 2027, deadline Jul-Aug 2026)，或大幅削减 scope（例如只用 0.5B single-scale + 3 dosages 做 proof-of-concept）。

---
