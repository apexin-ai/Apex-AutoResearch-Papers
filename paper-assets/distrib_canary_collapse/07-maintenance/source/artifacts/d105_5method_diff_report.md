# D105 Task 2+3: 5method 文件差异报告

## Task 2: `5method_leadlag.json` vs `unified_5method.json` 差异分析

### 文件位置

- `results/generalize/pythia1b_c4_a100_s42/analysis/5method_leadlag.json`
- `results/generalize/pythia1b_c4_a100_s42/analysis/unified_5method.json`

两个文件均由 `d102_rerun_8pair.py` 生成（D102 统一 8-pair 重分析）。

### 核心数值差异

| 指标 | `5method_leadlag.json` | `unified_5method.json` |
|------|----------------------|----------------------|
| K≥4 | **5/8** | **8/8** |
| K≥3 | 8/8 | 8/8 |

差异的 3 个 pair：token_entropy→{distinct_1, distinct_2, mauve}，leadlag 中 votes=3（diff+threshold+perm），缺 naive 和 ty。

### 根因：naive_xcorr 方向过滤器符号反转

**`d102_rerun_8pair.py` 的 `also_save_old_format` 函数，第约 280 行：**

```python
if np_res["sig_raw"] and np_res.get("peak_lag", 0) > 0:
    votes += 1; methods.append("naive")
```

**`method_ablation.py` 的 lag 约定（d102 调用的底层函数）：**

```python
# naive_pearson():
for lag in range(-max_lag, max_lag + 1):
    if lag >= 0:
        a, b = x[lag:], y[:n - lag]   # lag>0 → downstream 领先 canary
    else:
        a, b = x[:n + lag], y[-lag:]   # lag<0 → canary 领先 downstream
```

`peak_lag > 0` 在此约定下 = **downstream 领先 canary**（与 canary-lead 假设方向相反）。

**实测 C4 s42 各 pair 的 naive peak_lag：**

| Pair | peak_lag | 方向含义 | leadlag consensus 是否计入 |
|------|----------|---------|------------------------|
| token_entropy→distinct_1 | **-1** | canary 领先 ✓ | ✗ 被错误排除 |
| token_entropy→distinct_2 | **-1** | canary 领先 ✓ | ✗ 被错误排除 |
| token_entropy→distinct_3 | **+4** | downstream 领先 | ✓ 被错误计入 |
| token_entropy→mauve | **-1** | canary 领先 ✓ | ✗ 被错误排除 |
| ece→distinct_1 | **-1** | canary 领先 ✓ | ✗ 被错误排除 |
| ece→distinct_2 | **-1** | canary 领先 ✓ | ✗ 被错误排除 |
| ece→distinct_3 | **+3** | downstream 领先 | ✓ 被错误计入 |
| ece→mauve | **-1** | canary 领先 ✓ | ✗ 被错误排除 |

**结论：方向过滤器的符号完全反转。** 它排除了 canary 领先的正向证据（6/8 pair），反而保留了 downstream 领先的反向证据（2/8 pair）。leadlag 的 K≥4=5/8 包含了 2 个因 naive 的方向错误而"意外"达标的 pair（distinct_3 系列），以及 3 个靠 TY Granger 补票的 ece pair。

### 其他参数差异（不影响 K≥4）

| 参数 | `5method_leadlag.json` | `unified_5method.json` |
|------|----------------------|----------------------|
| Threshold σ | 3σ | 2σ |
| Consensus 中 diff/perm 的显著性 | FDR-corrected (`sig_fdr_permethod`) | raw + FDR 双报 |
| FDR 策略 | per-method BH-FDR | per-method + pooled BH-FDR |
| Method 命名 | naive_xcorr / diff_xcorr / perm_granger / ty_granger | naive_pearson / differenced_xcorr / permutation_granger / toda_yamamoto |

Threshold 差异（3σ vs 2σ）对 C4 无影响：两文件中 threshold 均为 8/8 significant。

### 论文 MMCT 定义应对应哪个文件

**`unified_5method.json` 为权威数据源。** 理由：

1. D102 设计意图：d102_rerun_8pair.py 的统一分析输出就是 unified_5method.json，leadlag 格式是为向后兼容生成的 legacy 输出
2. 无方向过滤器 bug：unified 的 consensus 按 `significant=True`（p < α）计票，不依赖有 bug 的 `peak_lag > 0` 过滤
3. 含完整 FDR 信息：method_summary 报告 raw / fdr_permethod / fdr_pooled 三级显著性，论文可选最保守的 FDR_pooled（C4 K≥4 仍为 8/8）
4. 结构与论文 Table 7 匹配

**`5method_leadlag.json` 不应用于论文 MMCT 数值。** 其 K≥4=5/8 包含方向 bug，但 5method_summary.txt 更糟——仍为 pre-D102 旧数据（含 perplexity，threshold=0/8）。

---

## Task 3(a): "Rev 3/8 全部来自 ECE→diversity pairs" claim 核查

**当前 registry 不含此 claim。** `generalize_pythia1b_c4_a100_s42_v2` 的 notes 为：

> "D102 unified 8-pair. PermG fwd 8/8 (C4 mauve strong). D102决策: Table 7 主指标=PermG fwd. C4域最强信号."

全量 102 条 registry 记录中无任何条目包含 "Rev 3/8" 或类似表述。`generalize_pythia1b_c4_a100_s43` 的 notes 明确记载 "rev 0/8 (perfect asymmetry)"。

**可能来源：** 此 claim 可能出自 D102 之前的某个 session 分析（如 c4_8pair_6method_analysis.json 中包含 6 method 含 reverse PermG），但在 D102 重分析时被覆盖。

**结论：** 无需 update_registry 删除——该 claim 已不存在于 registry 中。

## Task 3(b): `scale_14b` 实验检查

**`scale_14b_a100_s42_fp32` 不存在。** Registry 中存在的是：
- `scale_14b_a050_s42`（DONE/success，无 notes）
- `scale_14b_a050_s42_bf16`（DONE，无 notes）

服务器上 `results/*scale_14b*/` 目录不存在。14B 数据位于 `results/generalize/pythia14b_wiki_a100_s42/`（对应 registry `generalize_pythia14b_wiki_a100_s42`）。

**14B s42 的 `5method_summary.txt` 状态：**

```
Robust pairs (>=3/5 methods agree): 1/8
Perm Granger (FDR): 2/8
Threshold Onset: 0/8
```

确认使用旧 →ppl pairs（pre-D102）。但 `unified_5method.json` 已存在且使用 D102 8-pair 配置（K≥4 raw=5/8, FDR_permethod=2/8, FDR_pooled=4/8）。

**结论：** `5method_summary.txt` 确实过时，但 `unified_5method.json` 已是权威数据。无需重新生成——论文应直接引用 unified 文件。如需对齐 summary.txt 可重跑 d102_rerun_8pair.py，但优先级低。
