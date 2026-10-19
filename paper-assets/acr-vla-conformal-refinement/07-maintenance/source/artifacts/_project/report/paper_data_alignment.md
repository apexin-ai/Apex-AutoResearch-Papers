# Paper Claims vs Data Alignment Report
> Generated: 2026-05-17

---

## Claim 1: Sample-then-correct pipeline yields statistically significant improvement over argmin baseline

**Paper states**: obs_only ε=0.2 pooled 105/600 (17.5%) vs argmin 74/600 (12.3%), +5.2pp, Fisher exact p=0.0074, Cohen's d=1.21 (paired), 5/6 seeds obs_only > argmin. VLA-only mean 10.8%.

### 支撑实验

**obs_only ε=0.2 (6 seeds, all confirmed):**
| seed | exp_id | SR |
|------|--------|-----|
| 42 | eval-acr-object-obs-only-norm02 | 22% |
| 43 | eval-obs-only-object-norm02-seed43-r2 | 16% |
| 44 | eval-obs-only-object-norm02-seed44-r2 | 16% |
| 45 | eval-obs-only-object-norm02-seed45 | 16% |
| 46 | eval-obs-only-object-norm02-seed46 | 15% |
| 47 | eval-obs-only-object-norm02-seed47 | 20% |

**argmin (6 seeds, all confirmed):**
| seed | exp_id | SR |
|------|--------|-----|
| 42 | eval-reconvla-object | 12% |
| 43 | eval-argmin-object-seed43 | 17% |
| 44 | eval-argmin-object-seed44-r2 | 13% |
| 45 | eval-argmin-object-seed45 | 12% |
| 46 | eval-argmin-object-seed46 | 10% |
| 47 | eval-argmin-object-seed47 | 10% |

**VLA-only (4 seeds):**
| seed | exp_id | SR |
|------|--------|-----|
| 42 | eval-vla-only-object | 12% |
| 43 | eval-vla-only-object-seed43 | 12% |
| 44 | eval-vla-only-object-seed44-r2 | 10% |
| 45 | eval-vla-only-object-seed45 | 9% (18/200) |

VLA-only mean = (12+12+10+9)/4 = 10.75% ≈ 10.8% ✅

**5/6 seed-wise wins**: 42(+10), 43(-1), 44(+3), 45(+4), 46(+5), 47(+10) → 5/6 ✅

### 数据充分度: ✅ 充分
- 6v6 seeds, 每组 600 trials
- Fisher exact p=0.0074 (D047 confirmed)
- Cohen's d=1.21 (paired) verified
- 无缺口

---

## Claim 2: Conditioning-magnitude interaction — obs_only stable vs perdof progressive collapse

**Paper states**: obs_only stable ~17% across norms 0.03–1.42; perdof progressive collapse 14% → 10% → 4% → 0%.

### 支撑实验 — obs_only magnitude curve (Object)

| norm | seeds done (values) | seeds running | total after | mean |
|------|---------------------|--------------|-------------|------|
| 0.03 | 1: 42=16% | 0 | 1 | 16% |
| 0.05 | 1: 42=13% | 0 | 1 | 13% |
| 0.10 | 3: 42=19%, 43=12%, 44=16% | 3 (s45,s46,s47) | 6 | 15.7% |
| 0.20 | 6: 22/16/16/16/15/20 | 0 | 6 | 17.5% |
| 0.30 | 3: 42=19%, 44=18%, 45=14% | 1 (s46) | 4 | 17.0% |
| default | 2: 42=17%, 44=16% | 1 (s45) | 3 | 16.5% |

### 支撑实验 — perdof magnitude curve (Object)

| norm | seeds done (values) | seeds running | total after | mean |
|------|---------------------|--------------|-------------|------|
| 0.03 | 1: 42=14% | 0 | 1 | 14% |
| 0.05 | 1: 42=14% | 0 | 1 | 14% |
| 0.10 | 4: 42=11%, 43=12%, 44=8%, 45=11% | 2 (s46,s47) | 6 | 10.5% |
| 0.20 | 2: 42=11%, 43=9% | 3 (s44,s45,s46) | 5 | 10.0% |
| 0.30 | 3: 42=4%, 44=4%, 45=6% | 0 | 3 | 4.7% |
| default | 1: 42=0% | 0 | 1 | 0% |

### 数据充分度: ⚠️ 部分支撑
- **趋势清晰**: obs_only 13–17.5% 稳定 vs perdof 14%→10%→4.7%→0% 坍塌模式明显
- **核心缺口 — 低 norm 端 (0.03, 0.05) 双方法仅 1 seed**:
  - 无法加 error bars，Figure 2 在端点可信度不足
  - 审稿人可能质疑端点数据
  - 无 RUNNING 实验覆盖这些点
- **perdof default 仅 1 seed (0%)**:
  - 虽然 0% (0/100) 极端值不太可能是偶然，但单 seed 仍有风险
  - 无 RUNNING 实验补充
- **RUNNING 实验完成后改善**: norm 0.1 → 6v6 seeds; perdof norm 0.2 → 5 seeds; obs_only norm 0.3 → 4 seeds
- **paper_framing.md 数据需更新**:
  - obs_only default 写 "1s: 17%"，实际已有 2 seeds (42=17%, 44=16%)
  - perdof norm 0.1 ROADMAP 写 "3s: 11/11/8"，实际有 4 seeds (含 43=12%)
  - perdof norm 0.2 写 "1s: 11%"，实际已有 2 seeds (42=11%, 43=9%)

---

## Claim 3: Per-DOF conformal features do not generalize — honest negative result

**Paper states**: per-DOF scores fail beyond narrow safe region; root cause = K=10 rank-deficient covariance in 30D; spatial benchmark shows no method separates from baseline (34-35%).

### 支撑实验 — Spatial benchmark (all single seed=42)

| method | norm | exp_id | SR |
|--------|------|--------|-----|
| obs_only | 0.03 | eval-mag-obsonly-norm003-b2 | 34% |
| obs_only | 0.05 | eval-mag-obsonly-norm005 | 35% |
| obs_only | 0.10 | eval-acr-spatial-v4-obs-only-r3 | 35% |
| obs_only | 0.20 | eval-mag-obsonly-norm02 | 35% |
| obs_only | 0.30 | eval-mag-obsonly-norm03-r2 | 36% |
| perdof | 0.03 | eval-mag-perdof-norm003 | 30% |
| perdof | 0.05 | eval-mag-perdof-norm005 | 31% |
| perdof | 0.10 | eval-acr-spatial-v4-small-r2 | 35% |
| perdof | 0.30 | eval-mag-perdof-norm03 | 26% |
| argmin | — | eval-argmin-only-spatial-r2 | 34% |
| VLA-only | — | eval-spatial-v7-full | 30% |
| VLA-mean | — | eval-vla-mean-spatial | 32% |

### 数据充分度: ⚠️ 部分支撑
- **趋势支撑 claim**: 所有方法 spatial 聚集在 26-36%，无明显分离
- **所有 spatial 数据仅 1 seed**: 审稿人可能质疑
- **perdof spatial 也有坍塌趋势 (35%→26%)**: 论文说 "30-35%"，但 norm 0.3 实际 26%，低于该范围
  - 选项 A: 修正范围为 "26-35%"
  - 选项 B: 指出 spatial 也出现 perdof 衰退（反而加强 Claim 2）
- **Rank-deficiency 机制 (K=10, 30D)**: 理论论证，由 magnitude curve 模式间接支撑，无独立验证实验
- 无 RUNNING spatial 实验

---

## Supporting Claims (Additional baselines)

### scalar CRM
**Paper states**: scalar CRM seed42 = 15% (single seed)

**Registry data**:
| seed | exp_id | SR |
|------|--------|-----|
| 42 | eval-acr-object-v4-scalar | **9%** (conclusion: negative) |
| 43 | eval-scalar-object-seed43 | 10% |
| 44 | eval-scalar-object-seed44-r2 | 6% (conclusion: negative) |

**❌ 数据不一致**: paper_framing 写 15%，registry 实际为 9%。需核实来源，可能是旧版本模型数据或笔误。

### VLA-mean (K=10 mean aggregation)
**Paper states**: seed42=12%, seed43=15%, seed45=running

**Registry data**:
| seed | exp_id | SR |
|------|--------|-----|
| 42 | eval-vla-mean-object | 12% ✅ |
| 43 | eval-vla-mean-object-seed43 | 15% ✅ |
| 44 | eval-vla-mean-object-seed44 | 10% (paper 未记录) |
| 45 | eval-vla-mean-object-seed45 | 13% (paper 标记 running，实际已完成) |

paper_framing 需更新：seed44=10%, seed45=13% 已完成。4-seed mean = 12.5%。

### Direct correction (K=1 CRM)
**Paper states**: seed42 = 14% (not significant vs VLA-only)
**Registry**: eval-direct-correction-object-seed42-r3 = 14% ✅ 单 seed。

---

## Summary

| 状态 | 数量 | Claims |
|------|------|--------|
| ✅ 充分支撑 | 1 | Claim 1 (6v6 pipeline improvement, p=0.0074) |
| ⚠️ 部分支撑 | 2 | Claim 2 (magnitude curve 低 norm 端仅 1 seed), Claim 3 (spatial 全部单 seed) |
| ❌ 缺乏支撑 | 0 | — |

### 数据错误
- **scalar CRM**: paper_framing 写 seed42=15%，registry 实为 9%

### 当前 RUNNING 实验能填补的缺口
| 缺口 | RUNNING 实验 | 完成后状态 |
|------|-------------|-----------|
| obs_only norm=0.1 仅 3 seeds | s45, s46, s47 running | → 6 seeds ✅ |
| obs_only norm=0.3 仅 3 seeds | s46 running | → 4 seeds |
| obs_only default 仅 2 seeds | s45 running | → 3 seeds |
| perdof norm=0.1 仅 4 seeds | s46, s47 running | → 6 seeds ✅ |
| perdof norm=0.2 仅 2 seeds | s44, s45, s46 running | → 5 seeds ✅ |
| scalar seed45 | running | → 4 seeds |

### 仍无法填补的缺口（无 RUNNING 实验，需手动启动）
1. **obs_only norm=0.03 / 0.05**: 各仅 1 seed，Figure 2 端点无 error bars
2. **perdof norm=0.03 / 0.05**: 各仅 1 seed
3. **perdof default**: 仅 1 seed (0%)
4. **所有 spatial 数据**: 全部单 seed，无补充计划

### 建议优先使用 8 张空闲 GPU
1. perdof norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端
2. obs_only norm=0.03 seed43/44 (2 GPUs) — 补 Figure 2 低 norm 端
3. perdof default seed44/45 (2 GPUs) — 补坍塌终点
4. perdof norm=0.05 seed43 + obs_only norm=0.05 seed43 (2 GPUs) — 低 norm 端
