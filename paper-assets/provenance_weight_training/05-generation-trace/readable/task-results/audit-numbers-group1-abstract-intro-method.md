# audit numbers group1 abstract intro method

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_numbers_group1_abstract_intro_method_20260525T194156_result.json`
- **Structured JSON:** [`7f555d6fc0e01a6f1d66.json`](../../sessions/7f/7f555d6fc0e01a6f1d66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是审计报告。

---

## 数字真实性审计报告 — Group 1

**审计范围**: abstract.tex, introduction.tex, method.tex, related_work.tex  
**审计数字总数**: 39 个

---

### 一、各文件数字清单与验证结果

#### abstract.tex (5 个数字)

| # | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|
| 1 | Qwen3-0.6B | 模型规格 | ✅ | registry: `Qwen/Qwen3-0.6B` |
| 2 | 132M tokens | 数据规格 | ✅ | registry: 132,033,764 |
| 3 | 5 seeds | 实验设计 | ✅ | seeds 42/123/456/789/234 |
| 4 | >95% | 实验结果 | ✅ | 计算: (0.424-0.017)/0.424=96.0% |
| 5 | ρ ≥ 0.4 | 阈值声明 | ✅ | ρ=0.4 显著, ρ=0.2 失败 |

#### introduction.tex (20 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 6 | L1 | 20–60% | 外部引用 | 📖 | Cheng 2025, 与 related_work 一致 |
| 7 | L20 | Qwen3-0.6B | 模型规格 | ✅ | |
| 8 | L20 | 132M | 数据规格 | ✅ | |
| 9 | L20 | ρ=0.4 | 超参 | ✅ | |
| 10 | L20 | 5 seeds | 实验设计 | ✅ | |
| 11 | L20 | ρ∈{0.2, 0.6} | 扩展实验 | ✅ | registry 有对应实验 |
| 12 | L20 | 1.7B | 扩展规模 | ✅ | registry 有 1.7B 实验 |
| 13 | L11 | b*≈0.9 | 实验结果 | ✅ | registry b_star_mean=0.894 |
| 14 | L11 | b≈3.5 | 实验结果 | ✅ | registry ESS-only mean≈3.53 |
| 15 | L26 | 17.250 | PPL | ✅ | D&R q>0.3 3-seed mean, results.tex 确认 |
| 16 | L26 | 17.674 | PPL | ✅ | adaptive τ=0.7, 3-seed=5-seed=17.674 |
| 17 | L26 | >95% | 派生 | ✅ | 同 abstract |
| 18 | L26 | Δ=0.017 | PPL差 | ✅ | 17.674-17.657(epoch-matched)=0.017 |
| 19 | L26 | 3 seeds | 实验设计 | ✅ | |
| 20 | L32 | ~50% batches | 实验结果 | ⚠️ | **registry 无此聚合值，需训练日志验证** |
| 21 | L32 | ≈5.9× | 比值 | ⚠️ | **见问题清单 #1** |
| 22 | L34 | Δ=-0.023 | PPL差 | ✅ | 17.674-17.697(5-seed uniform)=-0.023 |
| 23 | L34 | Δ=-0.032 | PPL差 | ✅ | 17.731-17.763=-0.032 |
| 24 | L34 | τ=0.7 | 超参 | ✅ | |
| 25 | L34 | ⌊B/2⌋ | 公式 | ✅ | |

#### method.tex (5 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 26 | L17 | r≈0.79 | 统计量 | ⚠️ | **registry 无此值，来自分析脚本** |
| 27 | L41 | B=4, τ=0.7, N_min=2 | 示意图参数 | ✅ | 2=⌊4/2⌋ ✓ |
| 28 | L48 | O(B log(b_max/ε)) | 复杂度 | ✅ | 理论声明 |
| 29 | L49 | τ=0.7 | 超参默认值 | ✅ | 与 intro 一致 |
| 30 | L49 | ⌊B/2⌋ | 超参默认值 | ✅ | 与 intro 一致 |

#### related_work.tex (9 个数字)

| # | 行号 | 数字 | 类型 | 验证 | 备注 |
|---|------|------|------|------|------|
| 31 | L4 | 20–60% | 外部引用 | 📖 | 与 intro L1 一致 |
| 32 | L13 | b=10 (≤360M), b=1 (1.7B) | 外部引用 | 📖 | Drayson et al. |
| 33 | L15 | AUC=0.94 | 检测器指标 | ✅ | registry: 0.939→0.94 |
| 34 | L15 | 132M+ tokens | 数据规格 | ✅ | |
| 35 | L15 | ModernBERT-150M, AUC=0.986 | 外部引用 | 📖 | Drayson et al. |
| 36 | L15 | ~2M tokens (WikiText-2) | 外部引用 | 📖 | |
| 37 | L18 | ESS=n/E[w²] | 数学恒等式 | ✅ | |
| 38 | L21 | ≈0.62 | 数学常数 | ✅ | 1/φ=0.618, registry w=0.618 |
| 39 | L22 | α | 理论变量 | ✅ | Wang 2026 motivation |

---

### 二、问题清单

#### 问题 #1：≈5.9× 比值存疑
- **位置**: introduction.tex:32
- **论文值**: ≈5.9×
- **registry 可算值**: ESS-only mean b≈3.53, adaptive mean b≈0.894 → 比值 3.95×
- **分析**: 句子 "binds in ~50% of batches at ≈5.9× lower sharpening exponents" 可能指的是仅在 α_eff-binding batches 中的条件均值比，而非总体均值比。总体均值比只有 ~3.9×。但 5.9× 无法从 registry 聚合指标复现。
- **处理**: **无法确认正确性，需作者确认是否来自 per-batch 训练日志的条件统计。标记为出处存疑。**

#### 问题 #2：~50% batches 质量约束激活比例
- **位置**: introduction.tex:32
- **论文值**: ~50%
- **registry**: 无直接对应指标（仅有 `rho02_adaptive_tau09` 的 `alpha_eff_pct_at_max=42.95%`，不同配置）
- **处理**: **无法从 registry 验证，需训练日志确认。标记为出处存疑。**

#### 问题 #3：Pearson r ≈ 0.79
- **位置**: method.tex:17
- **registry**: 无此指标
- **处理**: **来自分析脚本而非 registry 实验。标记为出处存疑。**

---

### 三、跨文件一致性检查

| 数字 | 出现位置 | 一致? |
|------|----------|-------|
| 132M tokens | abstract:2, intro:20, related_work:15 | ✅ |
| Qwen3-0.6B | abstract:2, intro:20 | ✅ |
| 5 seeds | abstract:2, intro:20 | ✅ |
| >95% | abstract:3, intro:26 | ✅ |
| ρ=0.4 | abstract:6, intro:20, intro:34 | ✅ |
| τ=0.7 | intro:34, method:49 | ✅ |
| ⌊B/2⌋ | intro:34, method:49 | ✅ |
| 20–60% | intro:1, related_work:4 | ✅ |
| AUC=0.94 | related_work:15 (与 experiments.tex:7 一致) | ✅ |

无跨文件不一致。

---

### 四、总结

- **审计数字**: 39 个
- **验证通过**: 33 个 (✅)
- **外部引用（未核实原文）**: 5 个 (📖)
- **出处存疑**: 3 个 (⚠️)
  1. `≈5.9×` — 总体均值比为 ~3.9×，5.9× 来源不明
  2. `~50%` batches — registry 无对应聚合值
  3. `r≈0.79` — registry 无此指标
- **已发现错误并修复**: 0 个
- **跨文件不一致**: 0 个

**建议**: #1 的 5.9× 数字风险最高——如果 reviewer 用 b≈0.9 和 b≈3.5（论文自己报告的均值）做除法会得到 ~3.9×，与 5.9× 矛盾。建议作者立即确认计算来源，必要时修正为 ~3.9× 或补充说明是条件统计。

---
