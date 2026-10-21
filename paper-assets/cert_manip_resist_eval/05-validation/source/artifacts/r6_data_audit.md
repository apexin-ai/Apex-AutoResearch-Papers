# R6 数据审计报告

审计日期：2026-05-25
审计范围：`docs/paper/*.tex` 中所有定量 claim vs V2 registry 数据

---

## 1. Fractional Logit 数字

### V2 正确数据（Fractional logit, clustered SE）
| K | K_eff sig | η_max sig |
|---|-----------|-----------|
| 3 | 4/12      | 7/12      |
| 5 | 9/12      | 5/12      |
| 7 | 10/12     | 5/12      |

### 发现的不一致

#### ❌ results.tex:24 — 方法对比表（K=3）
```
Frac.\ logit (clust.)  & 6/12  & 9/12  \\
```
- 论文：η_max=6/12, K_eff=9/12
- 正确：η_max=**7/12**, K_eff=**4/12**
- **两个数字都错**

#### ❌ results.tex:43 — 正文描述
```
$K{=}3$ pattern is method-sensitive: $K_{\mathrm{eff}}$ significance ranges from 0/12 (clustered SE) to 12/12 (OLS), with fractional logit giving 9/12.
```
- 论文：fractional logit K_eff = 9/12（K=3）
- 正确：**4/12**

#### ❌ results.tex:99 — Fractional Logit Robustness 段落
```
$K_{\mathrm{eff}}$ significance is 9/12 across all panel sizes ($K{=}3,5,7$)
```
- 论文：声称三个 K 值均为 9/12
- 正确：K=3: **4/12**, K=5: 9/12, K=7: **10/12**
- **需要改写为按 K 分别报告**

#### ❌ introduction.tex:20 — 贡献 1
```
fractional logit confirms the positive association (9/12 across all $K$)
```
- 同上，9/12 uniform 不正确
- 正确：4/12, 9/12, 10/12

#### ❌ analysis.tex:15 — Confound 段落
```
fractional logit confirms the positive association (9/12 at all $K$)
```
- 同上

#### ❌ appendix.tex:159 — Robustness Checks 表（K=5）
```
Fractional logit     & 0.81 & 4/12 & 9/12 & \checkmark \\
```
- 论文：η_max=4/12, K_eff=9/12
- 正确：η_max=**5/12**, K_eff=9/12 ✅
- **η_max 差 1（4→5）**

#### ⚠️ results.tex:99 — 方向一致性声明
```
98.6\% directional concordance with OLS (71/72)
```
- 如果 fractional logit 数字改变，此声明可能需要重新验证
- **需与 registry 核实 71/72 是否仍成立**

#### ⚠️ appendix.tex:162 — 同一声明
```
98.6\% directional agreement (71/72 direction matches; the single discordance is $\eta_{\max}$ at $K{=}7$ for ARC $\times$ score manipulation)
```
- 同上，需核实

---

## 2. Adaptive R²

### V2 正确数据
- k5_rf_contrast.adaptive_r2_mean = **0.256**

### 发现的不一致

#### ❌ introduction.tex:16
```
adaptive attack reduces predictability to $R^2 = 0.275$
```
- 论文：0.275
- 正确：**0.256**

#### ❌ results.tex:66
```
adaptive attack reduces predictability ($R^2{=}0.275$ at $K{=}5$)
```
- 论文：0.275
- 正确：**0.256**

---

## 3. WCB Bootstrap 数字（majority vote, B=9999, Rademacher）

### V2 正确数据
| K | K_eff sig | η_max sig |
|---|-----------|-----------|
| 3 | 4/12      | 3/12      |
| 5 | 7/12      | 2/12      |
| 7 | 8/12      | 1/12      |

### 审计结果：全部一致 ✅

| 位置 | 内容 | 状态 |
|------|------|------|
| results.tex:11 | bootstrap (η_max 3/12, K_eff 4/12) | ✅ |
| results.tex:50 caption | 3/12→2/12, 4/12→7/12 | ✅ |
| results.tex:61 | K=3: η_max 3/12, K_eff 4/12; K=5: η_max 2/12, K_eff 7/12 | ✅ |
| introduction.tex:14 | K=3: η_max 3/12, K_eff 4/12; K≥5: 7/12, 8/12; η_max: 2/12, 1/12 | ✅ |
| introduction.tex:21 | 同上重复 | ✅ |
| analysis.tex:5 | bootstrap 4/12 at K=3, 7/12 at K=5 | ✅ |
| appendix.tex:39-41 | Crossed RE 表 bootstrap 列 | ✅ |
| appendix.tex:56 | η_max 3/12, K_eff 4/12 | ✅ |
| appendix.tex:155 | Full bootstrap: η_max 2/12, K_eff 7/12 (K=5) | ✅ |

---

## 4. OLS 显著性计数

### V2 正确数据：K_eff 12/12, η_max 10/12

| 位置 | 内容 | 状态 |
|------|------|------|
| results.tex:9 | K_eff 12/12, η_max 10/12 | ✅ |
| results.tex:20 | OLS: η_max 10/12, K_eff 12/12 | ✅ |
| appendix.tex:141 | OLS (η_max 10/12, K_eff 12/12) | ✅ |
| methodology.tex:21-33 | 逐条件 dominance 表 | ✅ |

---

## 5. Dominance 分布

### V2 正确数据：Co:10, K:2, η:0

| 位置 | 内容 | 状态 |
|------|------|------|
| results.tex:9 | 10 co-dominant, 2 K_eff-dominant, zero η_max-dominant | ✅ |
| methodology.tex:21-33 | 表格逐条件：Co×10, K×2 | ✅ |

---

## 6. Bayesian 方向 & K=7 neutralization

### V2 正确数据：5+/1−; K=7 neutralization 0/12

| 位置 | 内容 | 状态 |
|------|------|------|
| results.tex:88 | Bayesian: 5+/1− | ✅ |
| results.tex:96 | Bayesian attenuates K_eff (5+/1−) | ✅ |
| analysis.tex:30 | 5+/1− | ✅ |
| introduction.tex:22 | 5+/1− | ✅ |
| analysis.tex:35 | K=7 Bayesian neutralizes (0/12) | ✅ |
| appendix.tex:118 | Bayesian: K_eff 0/12 (K=7 table) | ✅ |
| appendix.tex:121 | full K_eff neutralization (0/12) | ✅ |
| appendix.tex:468 | 0/12 significant | ✅ |

---

## 7. 其他数字（抽查）

| 位置 | Claim | 状态 |
|------|-------|------|
| introduction.tex:20 | Cinelli-Hazlett 69% (25/36) | ✅ 与 appendix 表一致 |
| introduction.tex:22 | R²: threshold 0.83, Bayesian 0.09 | ✅ 四舍五入自 0.829, 0.087 |
| results.tex:85-88 | 聚合表 R² 值 (0.829, 0.327, 0.328, 0.087) | ✅ 内部一致 |
| appendix.tex:94 | Weighted R̄²=0.275 (K=5 aggregation) | ⚠️ 不是 adaptive R²，是不同指标；但与错误的 adaptive R² 同值，建议与 registry 核实 |

---

## 汇总

| 类别 | 不一致数 | 严重性 |
|------|---------|--------|
| Fractional logit 显著性计数 | **6处** | 🔴 高（含 introduction, results, analysis, appendix） |
| Adaptive R² | **2处** | 🔴 高（introduction + results） |
| WCB bootstrap 数字 | 0 | ✅ |
| OLS 数字 | 0 | ✅ |
| Dominance 分布 | 0 | ✅ |
| Bayesian 方向/neutralization | 0 | ✅ |
| 方向一致性 98.6% (71/72) | 需验证 | ⚠️ |

**共 8 处需修正，2 处需核实。**
