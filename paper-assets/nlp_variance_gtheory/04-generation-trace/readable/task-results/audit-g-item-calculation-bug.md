# audit g item calculation bug

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_g_item_calculation_bug_20260521T115034_result.json`
- **Structured JSON:** [`316590c9c42dc12c5f10.json`](../../sessions/31/316590c9c42dc12c5f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

---

## G_item 计算 Bug 审计报告

### 受影响文件汇总

| 文件 | Bug? | Bug 类型 | 影响 |
|------|------|----------|------|
| `scripts/gstudy_full.py` (exp-001 单模型) | **YES** | SS比例当ICC，非Henderson I方差分量 | G严重低估 |
| `scripts/exp001b_gstudy.py` (exp-001b) | **YES** | 同上 | G严重低估 |
| `scripts/task8_subject_gradient.py` (旧within-MMLU) | **YES** | tau=σ²(fixed)而非σ²(item) | G≈0（已知bug） |
| `scripts/compute_g_coefficients.py` (exp-001 cross-model) | **NO** | 正确公式 | — |
| `scripts/within_mmlu_gradient_4model.py` (新within-MMLU) | **NO** | 正确公式 | — |
| `scripts/dataset_a_gstudy.py` | **NO** | 正确公式 | — |
| `scripts/model_as_fixed_gstudy.py` | **NO** | 正确公式 | — |
| `src/analysis/variance_decomposition.py` | **N/A** | Henderson I实现正确 | — |

---

### Bug 详情

#### Bug 1: `gstudy_full.py` + `exp001b_gstudy.py` — ICC冒充G系数

**错误公式**（两个文件相同）:
```python
# gstudy_full.py line ~67
G = tau = components.get("item_id", 0) / total_var  # = SS(item)/SS(total)

# exp001b_gstudy.py line ~53
G_item = pct.get("item_id", 0) / 100  # 同上
```

这是ICC（类内相关），不是G-theory的G系数。问题有二：
1. 用SS比例代替Henderson I方差分量
2. G_item = σ²(item)/Σσ² 而非 σ²(item)/[σ²(item)+σ²(δ)]

**正确公式** (如 `compute_g_coefficients.py`):
```python
tau = vc['item_id']  # Henderson I估计的方差分量
delta = Σ(item交互项 / 非item facet levels) + residual / Π(所有非item levels)
G_item = tau / (tau + delta)
```

#### Bug 2: `task8_subject_gradient.py` — tau定义错误

```python
# tau = σ²(固定facets): precision + temperature ≈ 0
if len(random_in) == 0:
    sigma_tau += est  # 只有 fixed facets 进 tau
```

item_id 被放进 delta 而非 tau，导致 G ≈ 0。

---

### 修正前后数值对比

#### exp-001 单模型 (n_levels: prec=3, temp=3, prompt=6, seed=6, order=4, item=200)

| 指标 | 存储值 | 修正值 |
|------|--------|--------|
| G_item | 0.6108 | **0.9184** |

修正后 delta 分解:
| 分量 | σ² | 除数 | 贡献 |
|------|-----|------|------|
| precision:item_id | 0.01247 | 3 | 0.00416 |
| seed:item_id | 0.01120 | 6 | 0.00187 |
| temperature:item_id | 0.00543 | 3 | 0.00181 |
| prompt_template:item_id | 0.01086 | 6 | 0.00181 |
| ordering:item_id | 0.00145 | 4 | 0.00036 |
| residual | 0.04760 | 1296 | 0.00004 |
| **sigma_delta 合计** | | | **0.01004** |

tau=0.1129, delta=0.0100 → G=0.1129/(0.1129+0.0100)=**0.918**

#### exp-001b 重采样 (n_levels: temp=3, prompt=6, seed=6, order=4, item=200)

| 样本 | 存储 G_item | 修正 G_item |
|------|-------------|-------------|
| sample1 | 0.7588 | **0.9637** |
| sample2 | 0.7538 | **0.9620** |
| sample3 | 0.7218 | **0.9548** |
| **mean** | **0.745** | **0.960** |

#### within-MMLU subject gradient

| Subject | 旧 G_item (task8) | 新 G_item (4model) |
|---------|-------------------|---------------------|
| abstract_algebra | 0.0000 | 0.6222 |
| clinical_knowledge | 0.0000 | 0.8742 |
| college_physics | 0.0000 | 0.8206 |
| computer_security | 0.0011 | 0.8408 |
| high_school_mathematics | 0.0777 | 0.4516 |
| international_law | 0.0000 | 0.8905 |
| philosophy | 0.0000 | 0.8362 |
| professional_medicine | 0.0000 | 0.3057 |
| us_foreign_policy | 0.0000 | 0.7242 |
| world_religions | 0.0142 | 0.8703 |

---

### 受影响的 JSON 结果文件

1. **`results/analysis/llama_single_model_gstudy.json`** — `G_coefficient: 0.6108` → 应为 0.9184
2. **`results/analysis/exp001b_resampling_gstudy.json`** — `G_item: 0.7588/0.7538/0.7218` → 应为 0.9637/0.9620/0.9548；`stability.G_item.mean: 0.7448` → 应为 0.9602
3. **`results/analysis/within_mmlu_subject_gradient.json`** — 所有 `G_item` 值都错（≈0），已被 `within_mmlu_subject_gradient_4model.json` 替代

不受影响的文件：
- `results/analysis/cross_model_g_coefficients.json` — G_item=0.7069 ✓
- `results/analysis/dataset_a_gstudy.json` — 使用正确公式 ✓
- `results/analysis/model_as_fixed_gstudy.json` — 使用正确公式 ✓
- `results/exp001_analysis/within_mmlu_subject_gradient_4model.json` — 使用正确公式 ✓

---

### 对论文的影响

核心影响：**论文中如果引用了 exp-001 单模型 G=0.611 或 exp-001b G≈0.745 作为 item 信度指标，这些数字需要全部替换为修正值（0.918 和 0.960）**。

修正后的叙事实际上更好：item difficulty ranking 在所有条件下都非常稳定（G>0.9），进一步强化了"item是方差主要来源"的结论。但具体数值变化很大（0.611→0.918），所以论文正文、表格和 D-study 曲线都需要更新。

---
