# Pythia-6.9B 实验结果整合方案

## 当前论文状态

| 指标 | 当前值 |
|------|--------|
| Model configurations | 8 |
| Architecture families | 5 (Pythia, OLMo, Qwen, LLaMA, Mistral) |
| K\*=2 on C4 | 7/8 (Mistral-7B 是唯一 K\*=1) |
| 1v2 AUC range (K\*=2) | 0.6112--0.6955 |
| Model scale range | 1B--8B |

**Pythia 族已在论文中**（via Pythia-1.4B），Pythia-6.9B 增加的是同族内的 scale 覆盖，不新增 family。

## 结果文件位置

- Pipeline 输出: `results/exp_pythia69b_c4/pairwise_auc.json`, `ordinal_results.json`
- Bootstrap CI（需额外运行）: `results/exp_pythia69b_c4/bootstrap_ci_results.json`
- 自动化脚本: `scripts/patch_pythia_results.py`

## 运行自动化脚本

```bash
cd /root/autodl-tmp/gen-depth-contamination
python scripts/patch_pythia_results.py --results_dir results/exp_pythia69b_c4
```

带 bootstrap CI:
```bash
python scripts/patch_pythia_results.py \
  --results_dir results/exp_pythia69b_c4 \
  --bootstrap_ci results/exp_pythia69b_c4/bootstrap_ci_results.json
```

---

## 场景 A: K\*=2（预期，与其他 >=7B 模型一致）

### 数值变更

| 指标 | 旧值 | 新值 |
|------|------|------|
| Config count | 8 | 9 |
| K\*=2 ratio | 7/8 | 8/9 |
| Family count | 5 | 5（不变） |
| Text "eight" | "eight model configurations" | "nine model configurations" |

### 需更新的文件和位置

#### 1. main.tex (abstract)
- `8 model configurations (5 architecture families, 1B--8B)` → `9 model configurations (5 architecture families, 1B--8B)`
- `7/8 configurations` → `8/9 configurations`

#### 2. introduction.tex
- **Line 19**: `8 model configurations (5 families, 1B--8B)` → `9 model configurations (5 families, 1B--8B)`
- **Line 21**: `7/8 model configurations` → `8/9 model configurations`

#### 3. experiments_c1.tex
- **Line 4**: `eight model configurations spanning five architecture families` → `nine model configurations spanning five architecture families`
- **Line 5**: `Pythia-1.4B, OLMo-1B` → `Pythia-1.4B, Pythia-6.9B, OLMo-1B`
- **Line 6**: 添加 `all in continuation mode except where noted` 前需确认 Pythia-6.9B 也是 continuation
- **Line 43**: `all 8 model configurations: 7/8 yield` → `all 9 model configurations: 8/9 yield`
- **Line 43**: AUC range `0.6112--0.6955` 可能需更新（取 min/max 含新值）
- **Scale paragraph (~line 48)**: 添加 Pythia-6.9B 作为 scale invariance 的新证据

#### 4. conclusion.tex
- **Line 5**: `7/8 configurations (5 families, 1B--8B` → `8/9 configurations (5 families, 1B--8B`

#### 5. discussion.tex (boundary_cases paragraph)
- `Of 8 tested model configurations on C4, 7 yield` → `Of 9 tested model configurations on C4, 8 yield`
- AUC gap range `$0.611$--$0.696$` 可能需更新

#### 6. main.tex (Limitations)
- `model scale $\leq$8B (5 architecture families)` → 无需修改（6.9B < 8B，family 不变）

#### 7. 表格
- **tab:kstar_ci_extended** (appendix.tex ~line 101): 添加 Pythia-6.9B 列（2列: AUC + CI）
- **tab:kstar_ci** (experiments_c1.tex:18): 主表已有 5 个 config 列，空间有限。建议：
  - 方案 a: 不加到主表，在正文引用 extended table
  - 方案 b: 替换主表中的 Pythia-1.4B 列为 Pythia-6.9B（不推荐，丢失 1.4B 数据）
  - **推荐方案 a**
- **tab:setup** (method.tex:60): 当前仅列 6 个 config（不含 LLaMA/Mistral），Pythia-6.9B 同理可不加

#### 8. 图表
- **fig:auc_decay**: 需添加 Pythia-6.9B 曲线（需重新运行 plot_fig2_merged.py）
- **fig:kstar_theta**: 需添加 Pythia-6.9B 的 θ sensitivity 曲线

#### 9. Scale invariance paragraph 建议新增文本
```
Pythia-6.9B further confirms within-family scale invariance
(1v2 $\auc = X.XXXX$ $[X.XXX, X.XXX]$), matching the Pythia-1.4B
boundary at $\Kempirical{=}2$ despite 5$\times$ scale increase.
```

---

## 场景 B: K\*=1（Mistral-like）

### 数值变更

| 指标 | 旧值 | 新值 |
|------|------|------|
| Config count | 8 | 9 |
| K\*=2 ratio | 7/8 | 7/9 |
| K\*=1 exceptions | Mistral-7B only | Mistral-7B + Pythia-6.9B |

### 影响评估

- **Framing 影响中等**: 7/9 (78%) vs 7/8 (88%) 的 K\*=2 占比下降
- "sole exception" 不再成立，需改写 boundary cases 段落
- 但 K\*=1 仍然 ≤ 2，不违反上界 claim
- **支撑 scale→lower K\* 假设**: Pythia-1.4B 是 K\*=2，Pythia-6.9B 是 K\*=1，与 discussion 中 "13B+ may yield K\*=1" 一致

### 需更新的位置

除场景 A 的通用更新外:
- experiments_c1.tex:43: `Mistral-7B is the sole exception` → `Mistral-7B and Pythia-6.9B are exceptions ($\Kempirical{=}1$)`
- discussion.tex boundary_cases: 强化 scale effect 论述
- 不更新 family count（仍为 5）
- 无需修改 Limitations

---

## 场景 C: K\*≥3（意外）

### 影响评估

- **Framing 影响大**: 与 scale→lower K\* 趋势矛盾
- 需要额外分析：是 Pythia 族特有特征还是更深层的规律
- 可能需要和 arXiv K\*=3 的 domain effect 做区分

### 处理建议

1. 首先排除实验 artifact（检查 repetition rate, token length distribution）
2. 如果确认 K\*≥3:
   - 在 discussion 新增 paragraph 讨论
   - 考虑是否需要重新审视 "web text → K\*=2" 的 claim（改为 "most models"）
   - 可作为 interesting finding 而非 counterevidence

---

## Bootstrap CI 运行方法

Pipeline 完成后运行：

```bash
cd /root/autodl-tmp/gen-depth-contamination
python scripts/exp016_bootstrap_ci.py  # 需修改 DATA_DIR 指向 exp_pythia69b_c4
```

或参考 `exp_14b_c4/bootstrap_ci_results.json` 的格式写专用脚本，10000 bootstrap + 1000 permutation。

---

## 速查 Checklist

结果到手后:
1. `cat results/exp_pythia69b_c4/pairwise_auc.json` — 确认 K\*
2. 运行 `python scripts/patch_pythia_results.py --results_dir results/exp_pythia69b_c4` — 生成 LaTeX 和 claim 清单
3. 按场景 A/B/C 执行对应 patch
4. 运行 bootstrap CI（如未在 pipeline 中运行）
5. 更新 fig:auc_decay 和 fig:kstar_theta
6. `latexmk -pdf main.tex` 检查编译
