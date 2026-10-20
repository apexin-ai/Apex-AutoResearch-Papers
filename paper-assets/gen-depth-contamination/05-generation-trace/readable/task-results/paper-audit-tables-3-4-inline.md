# paper audit tables 3 4 inline

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_audit_tables_3_4_inline_20260523T112128_result.json`
- **Structured JSON:** [`cc24453526502c80b7bb.json`](../../sessions/cc/cc24453526502c80b7bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All clear rounding errors fixed. Here is the complete audit report:

---

## 全文数据审计报告

### 已修复（来源明确的舍入错误）

| 位置 | 论文原值 | Registry值 | 修正后 |
|------|---------|-----------|--------|
| Tab4 arXiv/Qwen 2v3 AUC | .644 | 0.6427→.643 | **.643** |
| Tab S12 arXiv 2v3 | .644 | 同上 | **.643** |
| experiments_c1 inline arXiv 2v3 | 0.644 | 同上 | **0.643** |
| appendix_extended DeBERTa table | 0.644 | 同上 | **0.643** |
| experiments_c1 inline LLaMA arXiv 2v3 | 0.620 | 0.6215→.622 | **0.622** |
| Tab4 Code/LLaMA 2v3 AUC | .510 | 0.5112→.511 | **.511** |
| Tab S12 arXiv 4v5 | .530 | 0.5294→.529 | **.529** |

### 需要人工确认的不匹配（严重度从高到低）

#### CRITICAL: Neural probe OLMo (experiments_c1.tex Table neural_probe_crossmodel)

| 位置 | 论文值 | Registry exp_id | Registry值 |
|------|--------|----------------|-----------|
| OLMo 1v2 AUC | 0.5054 | exp_015 | **0.657** |
| OLMo 2v3 AUC | 0.5056 | exp_015 | **0.589** |
| OLMo K* | 1 | exp_015 | **2** |

论文值（0.505x）酷似 15D OBD cross-scored 结果（exp_002: 1v2=0.5001），疑似误用了 OBD 值替代 neural probe 值。如果 registry 正确，则 OLMo neural probe K*=2，论文中 K*=1 的结论需修改，连带 discussion.tex 中引用此结果的段落。

#### HIGH: Mistral-7B 全部 AUC (Tab kstar_ci_extended)

| 位置 | 论文值 | exp_019 (self) | exp_019b (cross) |
|------|--------|---------------|-----------------|
| 0v1 | .9170 | 0.9843 | 0.9209 |
| 1v2 | .5750 | 0.5935 | 0.5695 |
| 2v3 | .5369 | 0.5402 | 0.5335 |
| 3v4 | .5174 | 0.5232 | 0.5140 |

论文值既不等于 self-scored 也不等于 cross-scored。2v3 值恰好等于两者均值 (0.5402+0.5335)/2=0.5369，但其他行不符合此规律。来源不明。

#### HIGH: Table S8 Pythia/OLMo 混用 self/cross-scored 数据

| 位置 | 论文值 | exp_007 (self) | exp_001/002 (cross) |
|------|--------|---------------|-------------------|
| S8 Pythia 1v2 | .607 | 0.6539 | 0.6074 (exp_001) |
| S8 OLMo 全5行 | .986/.500/.497/.502/.494 | .997/.614/.550/.509/.505 | ≈matches AUC only, CI无来源 |

Table S8 标注为 exp-007 bootstrap CI，但 OLMo 行使用了 cross-scored AUC（无对应 CI），Pythia 1v2 同样混用。CIs 无法追溯到任何 registry 实验。

#### HIGH: Table S10 Pythia Decoding (10/20 cells mismatch)

10个值与 exp_020 相差 0.002–0.008，非系统性偏差，可能来自 rerun 或 bootstrap-mean vs OOF-AUC 的差异。涉及行：1v2/nuc09, 2v3全行, 3v4/nuc09+t07+t12, 4v5/greedy+t12。

#### MODERATE: OLMo 3v4/4v5 (Table 1)

| 位置 | 论文值 | exp_002 |
|------|--------|---------|
| 3v4 | .5024 | 0.5034 |
| 4v5 | .4942 | 0.4971 |

差异 0.001–0.003，可能来自 scorer 更新前的旧值。

#### MODERATE: Discussion inline 数字

| 位置 | 论文值 | Registry值 |
|------|--------|-----------|
| "≈+1.9 pp" Mistral gap | 1.9 pp | 2.4 pp (0.5935−0.5695) |
| "0.15–0.27" JSD (≤1.5B) | 0.15–0.27 | 0.164–0.286 (registry range) |

### 匹配确认（所有其他值）

- **Table 1 (tab:kstar_ci)**: Qwen-rw/Pythia/Qwen-cont/Qwen-7B 全部 25 个 AUC + CI 值 ✓（OLMo 0v1/1v2/2v3 也 ✓）
- **Extended table**: Qwen-base 全 5 行 ✓, LLaMA-8B 全 5 行 ✓, Pythia-6.9B 全 ✓, Gemma-2B 全 ✓
- **Table S1 (transfer matrix)**: 16/16 cells ✓, retention% inline claims ✓
- **Table S2 (decoding ablation)**: 20/20 AUC + CI cells ✓（Spearman ρ 6个值不在 registry，无法验证）
- **Table 4 (domain)**: 其余 10/12 cells ✓
- **Filtering table**: 7/7 rows 全 ✓
- **experiments_c3.tex inline**: −1.53pp ✓, −0.77pp ✓, ~50% ✓, p 值全 ✓
- **introduction.tex**: MMLU 0.5941 ✓, base 0.6018 ✓, p≤0.002 ✓
- **discussion.tex**: 0v1 AUC≥0.92 ✓, 96% recall ✓, 14–22% ✓, 8–38% ✓, retrain chain 0.68–0.80 ✓, 6v7 0.634–0.641 ✓, Δauc −0.021 ✓

### 无法验证（registry 未存储）

- η²_p = .166 / .146（ANOVA 未单独注册实验）
- Table S2 Spearman ρ 6 个值（exp_003 未存储）
- Table S11 除 1v2 外的 12 个值（exp_021 仅存 1v2）
- Table S12 Wiki 0v1/3v4/4v5（exp_023 仅存 1v2/2v3）
- 部分 CI（Pythia 2v3, OLMo 全部, Gemma 多数）

---
