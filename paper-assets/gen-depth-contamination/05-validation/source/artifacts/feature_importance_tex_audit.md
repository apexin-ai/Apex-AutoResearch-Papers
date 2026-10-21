# Feature Importance TeX Audit (2026-05-21)

## Result: 无需更新

论文中 **不包含** feature importance 的具体 ΔAUC 数值。所有 feature importance 相关内容均以定性描述或排名相关性形式出现：

### 搜索覆盖范围
- `experiments_c1.tex` — 无 ΔAUC 数值
- `appendix.tex` — 无 ΔAUC 数值
- `appendix_extended.tex` — 无 ΔAUC 数值
- `method.tex` — 无 ΔAUC 数值
- `discussion.tex` — 无 ΔAUC 数值

### 论文中 feature importance 的表述方式
1. **排名** (experiments_c1.tex:87-89): "top-3 features (surp_d1_std, surp_std, surp_d2_std) are shared across all three families" — 排序不变，无需修改
2. **Spearman ρ** (experiments_c1.tex:87): "ρ ≥ 0.85" — 衡量排名一致性，非 ΔAUC 值
3. **定性描述** (experiments_c1.tex:89): "Qwen-rewrite diverges (freq_entropy dominates)" — 定性，无需修改
4. **Appendix Table** (appendix.tex:20-31): Top-3 feature ranking table — 排序不变

### 修正后数据确认
修正后 1v2 排序（按 Pythia-1.4B）：Surprisal σ > Freq Entropy > Surprisal μ > Hapax Ratio — 与论文描述的 surp_d1_std 主导一致。

### 结论
排序未变，论文未引用具体 ΔAUC 数值 → **无需修改**。
