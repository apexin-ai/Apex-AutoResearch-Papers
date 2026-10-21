# 1.7B 非截断子集分析：排除截断混淆的真实 Evidence Tax

## 截断分布

| 类别 | 文档数 |
|------|--------|
| 总文档 | 985 |
| no-evi 截断 | 501 (50.9%) |
| with-evi 截断 | 314 (31.9%) |
| **两边都未截断（公平子集）** | **442 (44.9%)** |
| 仅 no-evi 截断（混淆子集） | 229 |
| 仅 with-evi 截断 | 42 |
| 两边都截断 | 272 |

no-evidence 模型截断率远高于 with-evidence（50.9% vs 31.9%），因为 no-evidence 输出不含 evidence 字段，模型倾向于生成更多 triples 直到 token 上限。

## 核心结果

### 公平子集（442 篇，两边均未截断）

| 模型 | Ign-F1 | Ign-P | Ign-R | F1 | pred | gold |
|------|--------|-------|-------|----|------|------|
| no-evidence | 0.5704 | 0.5140 | 0.6406 | 0.5843 | 4513 | 3798 |
| with-evidence | 0.6319 | 0.6079 | 0.6579 | 0.6455 | 3991 | 3798 |
| **evidence tax** | **+0.0616** | | | **+0.0612** | | |

### 全量对比

| 子集 | n | no-evi Ign-F1 | with-evi Ign-F1 | tax |
|------|---|---------------|-----------------|-----|
| All docs | 985 | 0.3982 | 0.4786 | +0.0804 |
| **Both non-trunc (FAIR)** | **442** | **0.5704** | **0.6319** | **+0.0616** |
| No-evi non-trunc | 484 | 0.5584 | 0.6014 | +0.0430 |
| With-evi non-trunc | 671 | 0.4827 | 0.5891 | +0.1064 |
| Both truncated | 272 | 0.2368 | 0.3072 | +0.0704 |
| CONFOUNDED (no-evi trunc, with-evi not) | 229 | 0.3431 | 0.5370 | +0.1940 |
| with-evi trunc, no-evi not | 42 | 0.4833 | 0.3909 | -0.0924 |

### Per-doc 胜负（公平子集，阈值 0.01）

- no-evi 赢: 125 篇 (28.3%)
- with-evi 赢: 218 篇 (49.3%)
- 平局: 99 篇 (22.4%)

## 关键发现

1. **真实 evidence tax = +0.0616（with-evi 更优），非截断导致的虚假效应。**
   - 全量 +0.0804 中，约 0.02 来自截断混淆（no-evi 截断率更高导致 no-evi 分数被人为压低）
   - 但即使排除截断，with-evidence 仍然显著优于 no-evidence

2. **混淆子集验证了截断确实是偏差来源：**
   - 229 篇"仅 no-evi 截断"的文档上，tax 高达 +0.1940（严重膨胀）
   - 42 篇"仅 with-evi 截断"的文档上，tax 反转为 -0.0924（with-evi 被截断惩罚）

3. **no-evidence 模型在公平子集上 Recall 高但 Precision 低：**
   - no-evi: P=0.5140, R=0.6406（pred=4513, 过度预测）
   - with-evi: P=0.6079, R=0.6579（pred=3991, 更精准）
   - evidence generation 确实起到了**正则化作用**——约束模型只输出有 evidence 支撑的关系，减少幻觉

4. **Director 假设部分成立：**
   - "截断严重混淆了结果" ✓ — 截断使全量 tax 从 0.0616 膨胀到 0.0804
   - "evidence generation 在小模型上起隐式正则化作用" ✓ — 公平子集上 with-evi P 比 no-evi 高 9.4pp，R 仅微降
   - 但 evidence tax 方向仍为正（with-evi 更好），**不存在"小模型 evidence 负担"**
