# Random β=0.1 Pooled Statistics Recalculation Checklist

## Trigger
Random s43/s44 旧数据 DEPRECATED（原 checkpoint 丢失无法溯源）。等待重训完成：
- `plan018-additive-random-b01-s43-r3` — status: RUNNING
- `plan018-additive-random-b01-s44-r2` — status: ALLOCATED

重训完成后，需对两个新 checkpoint 执行 eval_sta.py（C008: `--data_path data/proofwriter_fol_100.jsonl`），然后用新数据重算以下所有统计量。

## 已有数据（不变）

### Random s42 (plan018-additive-random-b01-s42, D086 clean run)
- n_proved = 79, n_problems = 100
- H7 = 0, H1_exact = 56, H1_near = 8, H8 = 3
- genuine (D084 标准: proved − H7 − H1_exact − H8) = **18** (22.8%)
  - Note: registry strict genuine=12 扣了 H1-near; D084 标准不扣 H1-near → 79-0-56-3=20; D086 clean run 报告 18. 以 D086 为准。
- proved_only_ISR = 0.1314

### ISR β=0.1 3-seed (已闭环，不变)
- s42: n_proved=81, H7=13, H1=42, H8=12, genuine=14 (17.3%)
- s43: n_proved=61, H7=59, H1=0, genuine≈2 (~3%)
- s44: n_proved=89, H7=89 (H7a=77+H7b=12, FN corrected), genuine=0 (0%)
- **ISR pooled**: 231 proved, 16 genuine, genuine_rate = 6.9%

---

## 统计量重算清单

### 1. Random 3-seed Pooled Genuine Rate

**公式**: `genuine_pooled = (g_s42 + g_s43_new + g_s44_new) / (n_s42 + n_s43_new + n_s44_new)`

**输入**:
| Seed | Source | n_proved | genuine |
|------|--------|----------|---------|
| s42 | plan018-additive-random-b01-s42 | 79 | 18 |
| s43 | plan018-additive-random-b01-s43-r3 eval | ? | ? |
| s44 | plan018-additive-random-b01-s44-r2 eval | ? | ? |

**Genuine 分类标准 (C013/D084)**: genuine = proved − H7 − H1_exact − H8. H1-near 保留为 genuine 但单独标记。

**旧值 (DEPRECATED)**: 47/256 = 18.4% (含 s43=6, s44=18 推算值)

### 2. Fisher Exact Test: Random vs ISR Genuine Rates

**公式**: 2×2 contingency table, scipy.stats.fisher_exact

```
              ISR     Random
genuine       16      g_random_new
non-genuine   215     n_random_new - g_random_new
```

**两种场景**:
- A (H8-only, 保守): ISR genuine = 28/231
- B (H8 + s44 FN, 完整): ISR genuine = 16/231

两种都需重算：`fisher_exact([[isr_g, random_g], [isr_ng, random_ng]])`
- two-sided p
- one-sided p (ISR < Random)

**旧值 (DEPRECATED)**: 场景A p=0.060, 场景B p=0.0002

### 3. Wilson CI for Random Genuine Rate

**公式**: Wilson score interval, 95% CI

```python
from statsmodels.stats.proportion import proportion_confint
ci_low, ci_high = proportion_confint(g_random, n_random, alpha=0.05, method='wilson')
```

**输入**: g_random_new, n_random_new (from item 1)

**旧值 (DEPRECATED)**: 需重算

### 4. H7/H1/H8 Distribution — Random 3-seed 汇总

**需要新 eval 结果中的分类计数**:

| Seed | H7 | H1_exact | H1_near | H8 | Genuine | n_proved |
|------|----|---------|---------|----|---------|----------|
| s42 | 0 | 56 | 8 | 3 | 18 | 79 |
| s43_new | ? | ? | ? | ? | ? | ? |
| s44_new | ? | ? | ? | ? | ? | ? |
| **Pooled** | Σ | Σ | Σ | Σ | Σ | Σ |

**验证**: H7 应全部为 0（β=0.1 Random H7=0% 是核心 claim C136/C192）

### 5. Premise-Count-Matched ISR Comparison (更新 1.06x)

**公式**: 在 n_prem ≥ 3 的 genuine 样本中，比较 ISR s42 vs Random s42 的 mean ISR

**当前值**: ISR genuine n_prem≥3: mean_ISR=0.2578 (n=11), Random genuine n_prem≥3: mean_ISR=0.2434 (n=21), ratio=1.06x

**是否需要更新**: 取决于是否 pool 3-seed genuine 做 premise-matched 分析。
- 如果仅用 s42 单 seed（当前方案）：**不需要更新**，因为 ISR s42 和 Random s42 数据不变
- 如果扩展到 3-seed pooled：需要新 s43/s44 的 per-sample ISR + n_premise 数据

**建议**: 保持 s42 单 seed 分析（D051 原始方案），新 s43/s44 作为 robustness check

---

## 执行步骤

1. **等待训练完成**: 监控 plan018-additive-random-b01-s43-r3 和 plan018-additive-random-b01-s44-r2
2. **Eval**: 对每个新 checkpoint 执行:
   ```bash
   export CUDA_VISIBLE_DEVICES=N  # C005
   python eval_sta.py \
     --model_path <checkpoint_path> \
     --data_path data/proofwriter_fol_100.jsonl \  # C008
     --output_dir /root/autodl-tmp/outputs/<exp_id>/
   ```
3. **Taxonomy 分类**: 对 eval 输出执行 H7/H1/H8 分类（确保 C013 对称标准）
4. **计算统计量**: 用上述公式重算 items 1-5
5. **更新 paper_framing.md**: 替换所有 DEPRECATED/PROVISIONAL 标记的数字
6. **更新 provenance**: 确保新 exp_id 注册到相关 claims
7. **更新论文 LaTeX**: 更新 Table 1、Abstract、§4.2 中的 Random pooled 数字

## 依赖关系
```
s43-r3 完成 ──┐
              ├─→ eval s43 ──┐
s44-r2 完成 ──┤              ├─→ 统计量重算 → 更新 framing/paper
              └─→ eval s44 ──┘
```
