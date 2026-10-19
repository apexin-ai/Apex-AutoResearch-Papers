# Magnitude Multi-Seed Data Matrix (Object Benchmark)

> Generated: 2026-05-16
> Source: experiment registry (acr-vla-conformal-refinement)

## 注意事项

- SR 值为 0-1 scale（即 0.16 = 16% success rate）
- `eval-mag-*` 命名的实验视为 seed=42（原始 magnitude sweep）
- `eval-{method}-object-seed{XX}` 无 norm 标注的视为 norm=0.10（标准配置）
- 有 retry（-r2/-r3）的取最新有效结果
- perdof norm=0.10 seed=44: 旧实验 sr=0.08，新命名实验 RUNNING 中（疑似 re-run）

---

## 1. obs_only (norm × seed)

| norm | seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |
|------|---------|---------|---------|---------|---------|---------|
| 0.03 | **0.16** | — | — | — | — | — |
| 0.05 | **0.13** | — | — | — | — | — |
| 0.10 | — | **0.12** | **0.16** | RUNNING | — | — |
| 0.20 | *(no SR)* | **0.16** | **0.16** | **0.16** | RUNNING | RUNNING |
| 0.30 | **0.19** | — | **0.18** | RUNNING | — | — |
| 1.42 | — | — | **0.16** | RUNNING | — | — |

## 2. perdof (norm × seed)

| norm | seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |
|------|---------|---------|---------|---------|---------|---------|
| 0.03 | **0.14** | — | — | — | — | — |
| 0.05 | **0.14** | — | — | — | — | — |
| 0.10 | — | **0.12** | **0.08** | RUNNING | — | — |
| 0.20 | **0.11** | **0.09** | — | RUNNING | — | — |
| 0.30 | **0.04** | — | RUNNING | RUNNING | — | — |
| 1.42 | — | — | RUNNING | RUNNING | — | — |

## 3. argmin (no norm dimension)

| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |
|---------|---------|---------|---------|---------|---------|
| — | **0.17** | **0.13** | RUNNING | RUNNING | RUNNING |

## 4. scalar (no norm dimension)

| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |
|---------|---------|---------|---------|---------|---------|
| — | **0.10** | **0.06** | RUNNING | — | — |

## 5. vla_mean (no norm dimension)

| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |
|---------|---------|---------|---------|---------|---------|
| **0.12** | **0.15** | **0.10** | RUNNING | — | — |

## 6. vla_only (no norm dimension)

| seed 42 | seed 43 | seed 44 | seed 45 | seed 46 | seed 47 |
|---------|---------|---------|---------|---------|---------|
| **0.12** | **0.12** | **0.10** | **0.09** | — | — |

---

## 覆盖率统计

| 类别 | 总 cells | 已完成 | RUNNING | 未部署 | 完成率 |
|------|----------|--------|---------|--------|--------|
| obs_only (6 norms × 6 seeds) | 36 | 10 | 5 | 21 | 28% |
| perdof (6 norms × 6 seeds) | 36 | 7 | 7 | 22 | 19% |
| argmin (6 seeds) | 6 | 2 | 3 | 1 | 33% |
| scalar (6 seeds) | 6 | 2 | 1 | 3 | 33% |
| vla_mean (6 seeds) | 6 | 3 | 1 | 2 | 50% |
| vla_only (6 seeds) | 6 | 4 | 0 | 2 | 67% |
| **总计** | **96** | **28** | **17** | **51** | **29%** |

---

## Mean ± Std（≥2 seeds 完成的组合）

### obs_only by norm

| norm | n_seeds | mean | std | seeds used |
|------|---------|------|-----|------------|
| 0.10 | 2 | 0.140 | 0.028 | 43, 44 |
| 0.20 | 3 | 0.160 | 0.000 | 43, 44, 45 |
| 0.30 | 2 | 0.185 | 0.007 | 42, 44 |

### perdof by norm

| norm | n_seeds | mean | std | seeds used |
|------|---------|------|-----|------------|
| 0.10 | 2 | 0.100 | 0.028 | 43, 44 |
| 0.20 | 2 | 0.100 | 0.014 | 42, 43 |

### Methods without norm

| method | n_seeds | mean | std | seeds used |
|--------|---------|------|-----|------------|
| argmin | 2 | 0.150 | 0.028 | 43, 44 |
| scalar | 2 | 0.080 | 0.028 | 43, 44 |
| vla_mean | 3 | 0.123 | 0.025 | 42, 43, 44 |
| vla_only | 4 | 0.108 | 0.014 | 42, 43, 44, 45 |

---

## 缺失数据清单

### 高优先级（有部分 seed 完成，需补齐 error bar）

**obs_only norm=0.20** — 最接近完整，缺 seed 42 结果（实验存在但无 SR）, seed 46/47 RUNNING
**obs_only norm=0.10** — 缺 seed 42, 45(RUNNING), 46, 47
**obs_only norm=0.30** — 缺 seed 43, 45(RUNNING), 46, 47
**vla_only** — 缺 seed 46, 47（4 seeds 已完成，可能足够）
**vla_mean** — 缺 seed 45(RUNNING), 46, 47
**argmin** — 缺 seed 42, 45/46/47(RUNNING)

### 中优先级（只有 1-2 个 seed）

**obs_only norm=0.03** — 仅 seed 42
**obs_only norm=0.05** — 仅 seed 42
**obs_only norm=1.42** — 仅 seed 44, seed 45 RUNNING
**perdof norm=0.03** — 仅 seed 42
**perdof norm=0.05** — 仅 seed 42
**perdof norm=0.30** — 仅 seed 42 (sr=0.04), seed 44/45 RUNNING
**perdof norm=1.42** — 无完成，seed 44/45 RUNNING
**scalar** — 仅 seed 43/44

### 未部署（完全没有实验）

| method | norm | missing seeds |
|--------|------|---------------|
| obs_only | 0.03 | 43, 44, 45, 46, 47 |
| obs_only | 0.05 | 43, 44, 45, 46, 47 |
| obs_only | 0.10 | 42, 46, 47 |
| obs_only | 0.20 | — (全部已有或 RUNNING) |
| obs_only | 0.30 | 43, 46, 47 |
| obs_only | 1.42 | 42, 43, 46, 47 |
| perdof | 0.03 | 43, 44, 45, 46, 47 |
| perdof | 0.05 | 43, 44, 45, 46, 47 |
| perdof | 0.10 | 42, 46, 47 |
| perdof | 0.20 | 44, 46, 47 |
| perdof | 0.30 | 43, 46, 47 |
| perdof | 1.42 | 42, 43, 46, 47 |
| argmin | — | 42 |
| scalar | — | 42, 46, 47 |
| vla_mean | — | 46, 47 |
| vla_only | — | 46, 47 |

---

## 实验 ID 到结果映射（完整参考）

### obs_only
| exp_id | norm | seed | status | overall_sr |
|--------|------|------|--------|------------|
| eval-mag-obsonly-norm003-object | 0.03 | 42 | DONE | 0.16 |
| eval-mag-obsonly-norm005-object | 0.05 | 42 | DONE | 0.13 |
| eval-obs-only-object-seed43 | 0.10 | 43 | DONE | 0.12 |
| eval-obs-only-object-norm01-seed44 | 0.10 | 44 | DONE | 0.16 |
| eval-obs-only-object-norm01-seed45 | 0.10 | 45 | RUNNING | — |
| eval-mag-obsonly-norm02-object | 0.20 | 42 | DONE | *(no SR)* |
| eval-obs-only-object-norm02-seed43-r2 | 0.20 | 43 | DONE | 0.16 |
| eval-obs-only-object-norm02-seed44-r2 | 0.20 | 44 | DONE | 0.16 |
| eval-obs-only-object-norm02-seed45 | 0.20 | 45 | DONE | 0.16 |
| eval-obs-only-object-norm02-seed46 | 0.20 | 46 | RUNNING | — |
| eval-obs-only-object-norm02-seed47 | 0.20 | 47 | RUNNING | — |
| eval-mag-obsonly-norm03-object | 0.30 | 42 | DONE | 0.19 |
| eval-obs-only-object-norm03-seed44 | 0.30 | 44 | DONE | 0.18 |
| eval-obs-only-object-norm03-seed45-r2 | 0.30 | 45 | RUNNING | — |
| eval-obs-only-object-default-seed44 | 1.42 | 44 | DONE | 0.16 |
| eval-obs-only-object-default-seed45 | 1.42 | 45 | RUNNING | — |

### perdof
| exp_id | norm | seed | status | overall_sr |
|--------|------|------|--------|------------|
| eval-mag-perdof-norm003-object | 0.03 | 42 | DONE | 0.14 |
| eval-mag-perdof-norm005-object | 0.05 | 42 | DONE | 0.14 |
| eval-perdof-object-seed43 | 0.10 | 43 | DONE | 0.12 |
| eval-perdof-object-seed44 | 0.10 | 44 | DONE | 0.08 |
| eval-perdof-object-norm01-seed44 | 0.10 | 44 | RUNNING | — |
| eval-perdof-object-norm01-seed45 | 0.10 | 45 | RUNNING | — |
| eval-mag-perdof-norm02-object | 0.20 | 42 | DONE | 0.11 |
| eval-mag-perdof-norm02-seed43-object-r3 | 0.20 | 43 | DONE | 0.09 |
| eval-perdof-object-norm02-seed45 | 0.20 | 45 | RUNNING | — |
| eval-mag-perdof-norm03-object-r3 | 0.30 | 42 | DONE | 0.04 |
| eval-perdof-object-norm03-seed44 | 0.30 | 44 | RUNNING | — |
| eval-perdof-object-norm03-seed45-r2 | 0.30 | 45 | RUNNING | — |
| eval-perdof-object-default-seed44 | 1.42 | 44 | RUNNING | — |
| eval-perdof-object-default-seed45 | 1.42 | 45 | RUNNING | — |

### argmin
| exp_id | seed | status | overall_sr |
|--------|------|--------|------------|
| eval-argmin-object-seed43 | 43 | DONE | 0.17 |
| eval-argmin-object-seed44-r2 | 44 | DONE | 0.13 |
| eval-argmin-object-seed45 | 45 | RUNNING | — |
| eval-argmin-object-seed46 | 46 | RUNNING | — |
| eval-argmin-object-seed47 | 47 | RUNNING | — |

### scalar
| exp_id | seed | status | overall_sr |
|--------|------|--------|------------|
| eval-scalar-object-seed43 | 43 | DONE | 0.10 |
| eval-scalar-object-seed44-r2 | 44 | DONE | 0.06 |
| eval-scalar-object-seed45 | 45 | RUNNING | — |

### vla_mean
| exp_id | seed | status | overall_sr |
|--------|------|--------|------------|
| eval-vla-mean-object | 42 | DONE | 0.12 |
| eval-vla-mean-object-seed43 | 43 | DONE | 0.15 |
| eval-vla-mean-object-seed44 | 44 | DONE | 0.10 |
| eval-vla-mean-object-seed45 | 45 | RUNNING | — |

### vla_only
| exp_id | seed | status | overall_sr |
|--------|------|--------|------------|
| eval-vla-only-object | 42 | DONE | 0.12 |
| eval-vla-only-object-seed43 | 43 | DONE | 0.12 |
| eval-vla-only-object-seed44-r2 | 44 | DONE | 0.10 |
| eval-vla-only-object-seed45 | 45 | DONE | 0.09 |
