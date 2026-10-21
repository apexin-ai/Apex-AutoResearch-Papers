# TY/diff_xcorr 跨脚本不一致 Root Cause 调查报告

**日期**: 2026-05-20
**状态**: P0 CRITICAL — 已定位 root cause
**调查范围**: `run_5method_s43.py` vs `batch_analysis.py`
**验证数据**: `alpha_sweep/a060_s43_fp32` (T=10), `alpha_sweep/a050_s43_fp32` (T=11)

---

## 1. 关键参数/方法差异表

| 维度 | run_5method_s43.py | batch_analysis.py | 影响 |
|------|-------------------|-------------------|------|
| **DOWNSTREAMS** | distinct_1/2/3, **perplexity** | distinct_1/2/3, **mauve** | 8 pair 中 2 pair 完全不同 |
| **LOWER_IS_WORSE** | 不含 mauve | 含 mauve | orient 方向不同（但 diff_xcorr 对称，不影响结果） |
| **Direction check** | `peak_lag > 0` (**WRONG**, 违反 C009) | `peak_lag < 0` (正确) | naive/diff 计数完全反转 |
| **TY ADF regression** | 默认 `"c"` (constant only) | `"ct"` (constant + trend) | d_max 判定不同 |
| **TY ADF maxlag** | `min(2, T//3-1)` | `min(3, T//3-1)` | batch_analysis 在短序列上触发 bug |
| **TY d_max 逻辑** | 简单 p>0.05→1, 封顶 1 | 迭代差分 _determine_d_max, 封顶 2 | **batch_analysis 有 bug**（见下） |
| **TY lag 选择** | AIC 搜索 p∈{1,2} | 固定 max_lag=1 | 模型结构不同 |
| **TY 检验统计量** | F-test: `F = ((RSS_r-RSS_u)/q) / (RSS_u/df)` | Wald χ²: `W = n*(RSS_r-RSS_u)/RSS_u` | 小样本下 F 更准确，χ² 是渐近的 |
| **TY p-value 分布** | `stats.f.cdf(F, q, df_resid)` | `stats.chi2.cdf(W, q)` | 自由度处理完全不同 |
| **PermG 实现** | 相同 | 相同 | **一致** |
| **FDR 校正范围** | diff_xcorr, perm_granger | diff_xcorr, perm_granger_fwd, perm_granger_rev | 实质等价 |

---

## 2. Per-Pair 结果对比

### 2.1 TY Granger (alpha_sweep/a060_s43_fp32, T=10)

| Pair | r5 sig | r5 p | r5 d_max | ba sig | ba p | ba d_max | 一致? |
|------|--------|------|----------|--------|------|----------|-------|
| token_entropy→distinct_1 | False | N/A* | 1 | False | 0.607 | 1 | == |
| token_entropy→distinct_2 | False | N/A* | 1 | **True** | 0.014 | 1 | **!!** |
| token_entropy→distinct_3 | False | 0.272 | 1 | **True** | 0.028 | 1 | **!!** |
| token_entropy→mauve | False | 0.966 | 1 | False | 0.940 | 1 | == |
| ece→distinct_1 | False | 0.261 | **0** | **True** | 0.003 | **1** | **!!** |
| ece→distinct_2 | **True** | **2e-6** | **0** | False | 0.060 | **1** | **!!** |
| ece→distinct_3 | **True** | **4e-6** | **0** | False | 0.579 | **1** | **!!** |
| ece→mauve | False | 0.154 | 1 | **True** | 0.002 | 1 | **!!** |

\*N/A = n too small (p_aug 过大导致残差自由度不足)

**TY 计数**: run_5method = **2/8**, batch_analysis = **4/8** (6/8 pair 结果不同)

### 2.2 TY Granger (alpha_sweep/a050_s43_fp32, T=11)

| Pair | r5 sig | r5 p | r5 d_max | ba sig | ba p | ba d_max | 一致? |
|------|--------|------|----------|--------|------|----------|-------|
| token_entropy→distinct_1 | True | 0.045 | 1 | True | 0.000 | 0 | == |
| token_entropy→distinct_2 | False | 0.449 | 1 | **True** | **4e-6** | 0 | **!!** |
| token_entropy→distinct_3 | False | 0.993 | 1 | False | 0.266 | 2 | == |
| token_entropy→mauve | False | 0.791 | 1 | False | 0.661 | 2 | == |
| ece→distinct_1 | False | 0.052 | 1 | **True** | **4e-5** | 1 | **!!** |
| ece→distinct_2 | False | 0.349 | 1 | **True** | 0.006 | 1 | **!!** |
| ece→distinct_3 | False | 0.335 | 1 | **True** | **0.000** | 2 | **!!** |
| ece→mauve | False | 0.334 | 1 | False | 0.225 | 2 | == |

**TY 计数**: run_5method = **1/8**, batch_analysis = **5/8**

### 2.3 diff_xcorr (两实验均确认)

**Per-pair 结果完全一致** — 两套脚本的 diff_xcorr 核心计算（差分、pearsonr、peak_lag 选择）相同。计数差异 **100% 来自 direction check**：

| 实验 | peak_lag > 0 (r5, WRONG) | peak_lag < 0 (ba, CORRECT) |
|------|--------------------------|---------------------------|
| a060_s43_fp32 | 0/8 | 6/8 |
| a050_s43_fp32 | 0/8 | 6/8 |

run_5method 在这两个实验上 diff_xcorr 会报 **0/8**（因 forward 信号全在 lag<0），而 batch_analysis 报 **6/8**。

---

## 3. Root Cause 汇总

### RC-1 (CRITICAL): DOWNSTREAMS 列表不同

- `run_5method_s43.py`: distinct_1/2/3 + **perplexity**
- `batch_analysis.py`: distinct_1/2/3 + **mauve**
- 8 pair 中 2 pair（canary→perplexity vs canary→mauve）在不同数据上计算
- 无法直接对比

### RC-2 (CRITICAL): Direction check 符号反转 — 违反 C009/M035

- `run_5method_s43.py` 共识计数: `(peak_lag or 0) > 0` → **反向因果**
- `batch_analysis.py` 共识计数: `(peak_lag or 0) < 0` → **正向因果**（正确）
- xcorr 约定: lag<0 = canary leads downstream = forward causation
- 影响: naive_xcorr 和 diff_xcorr 的 forward significant 计数完全反转
- 这是 D111/M035 sign reversal bug 的残留 — batch_analysis 已修正，run_5method 未修正

### RC-3 (CRITICAL): TY Granger 实现完全不同

**3a: ADF 回归类型**
- run_5method: `regression="c"` (constant) → ece 等单调序列容易判为平稳 (d_max=0)
- batch_analysis: `regression="ct"` (constant+trend) → 更保守，有 trend 的序列更难拒绝单位根

**3b: _determine_d_max BUG（batch_analysis）**

```
_determine_d_max 流程 (T=10):
  d=0: ADF(T=10, maxlag=2, ct) → 成功, p>0.05 → 差分
  d=1: ADF(T=9, maxlag=2, ct) → CRASH!
       约束: maxlag < nobs/2 - 1 - ntrend = 9/2 - 1 - 2 = 1.5
       maxlag=2 > 1.5 → ValueError
  except → return d=1  ← 不是真正的平稳性判定!
```

大多数 metric 获得 d_max=1 是因为 **ADF 异常被静默吞掉**，不是因为真正需要一阶差分。

**3c: Lag 阶数选择**
- run_5method: AIC 选择 p∈{1,2}，可能选 p=2 → 更多参数、更高拟合
- batch_analysis: 固定 max_lag=1 → 更简约

**3d: 检验统计量**
- run_5method: F-test（有限样本精确分布）
- batch_analysis: Wald χ²（渐近分布）
- T=10-11 远未达到 χ² 渐近条件，两者 p-value 可差 1-2 个数量级

### RC-4: 为什么 PermG 一致

1. **代码路径相同**: 两套脚本的 `perm_granger()` / `_granger_f_stat()` / `_build_lag_matrix()` 实现完全一致
2. **参数相同**: max_lag=1, n_perm=5000, seed=42, difference=True
3. **无 direction filter**: PermG 天然有方向性（测试 x→y），不需要 peak_lag 方向判定
4. **不依赖 ADF/d_max**: 内部自行差分，避开了 ADF 不一致问题
5. **FDR 校正一致**: 两套都对 PermG p-value 做 BH FDR

---

## 4. 推荐

### 4.1 选择哪套脚本

**batch_analysis.py 更接近正确**，但仍有 bug 需修：

| 项目 | run_5method_s43.py | batch_analysis.py |
|------|-------------------|-------------------|
| Direction check | ✗ (peak_lag>0, 违反 C009) | ✓ (peak_lag<0) |
| DOWNSTREAMS | ✗ (用 perplexity，不含 mauve) | ✓ (用 mauve) |
| TY d_max | 简单但无 bug | **有 _determine_d_max 异常 bug** |
| TY test stat | F-test（小样本更优） | χ²（渐近，T≤11 不适用） |
| 通用性 | 硬编码路径/实验 | 参数化 CLI |

### 4.2 需要修复的问题

1. **[P0] 废弃 run_5method_s43.py** — 方向错误、downstreams 错误、硬编码路径。不应再用于任何分析
2. **[P0] 修复 batch_analysis.py 的 _determine_d_max bug**:
   ```python
   # 修正: 考虑 regression="ct" 的 ntrend=2 约束
   def _determine_d_max(series, max_d=2, alpha=0.05):
       for d in range(max_d + 1):
           try:
               nobs = len(series)
               ntrend = 2  # "ct" = constant + trend
               safe_maxlag = max(1, nobs // 2 - 1 - ntrend - 1)
               result = adfuller(series, maxlag=safe_maxlag,
                                 regression="ct", autolag="AIC")
               if result[1] < alpha:
                   return d
               series = np.diff(series)
           except Exception:
               return min(d, 1)  # fallback 但不超过 1
       return max_d
   ```
3. **[P1] TY 检验统计量**: 对 T≤15 的短序列，改用 F-test 代替 χ²，或直接标注 TY 为 "underpowered"
4. **[P2] 考虑 TY 降级**: 鉴于 C003 已确认 TY 在低 α 下种子不稳定，且 _determine_d_max 有系统性 bug，建议 K≥3 投票中降低 TY 权重或排除

### 4.3 对 K≥3 投票的影响评估

| 方法 | 可信度 | 问题 |
|------|--------|------|
| **PermG** | ✓ 高 | 两套脚本一致，无 direction/ADF 依赖 |
| **threshold_onset** | ✓ 中高 | 两套实现一致（D105 3σ 标准另行校验） |
| **diff_xcorr** | ⚠ 依赖脚本 | 核心计算一致，但 run_5method 方向错误导致计数反转 |
| **naive_xcorr** | ⚠ 依赖脚本 | 同上 |
| **TY Granger** | ✗ 不可信 | 两套实现给出相反结论，batch_analysis 有 d_max bug，run_5method 有方向 bug |

**结论**: 使用 run_5method 产出的任何包含 TY 或 diff/naive direction check 的 K≥3 数值**全部不可信**。batch_analysis 的 diff_xcorr 和 PermG 可信，但 TY 需修 bug 后重跑。

**K≥3 修正策略**:
- 短期: K≥3 仅基于 PermG + threshold_onset + diff_xcorr (batch_analysis 版)，3 method 中 K≥2 为显著
- 中期: 修复 _determine_d_max 后重跑 TY，恢复 5-method 投票

---

## 5. 附录: 诊断脚本

诊断脚本位于服务器: `/root/autodl-tmp/distrib_canary_collapse/diagnostic_compare.py`

运行方式:
```bash
python diagnostic_compare.py results/alpha_sweep/a060_s43_fp32
```
