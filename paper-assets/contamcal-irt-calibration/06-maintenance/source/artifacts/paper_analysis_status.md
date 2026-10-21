# Paper & Analysis Status — 2026-05-19
## EMNLP 2026 ARR May 25 | 6 days remaining

---

## 1. Core Claims 实验支撑状态

### C1: Domain-Differential Characterization (PRIMARY)
- **≤3B 数据**: FROZEN, N=24, MMLU domain-level IRT 完成 (Math γ=+0.97, Science γ=+0.84, CS_Eng≈0, non-STEM PPP=1.0 misfit)
- **7B/14B 数据**: Phase 2 v2 eval 运行中 (ETA ~12:45 today)。v1 数据已有初步结论:
  - MMLU: 效应随 scale 递增 (≤3B ~0.7pp → 7B +1.34pp → 14B +1.92pp, d050 peak +2.28pp)
  - ARC: 7B -0.21pp, 14B -0.43pp (null/微负, benchmark-specific direction confirmed)
- **Cross-family**: Phi-4 方向一致 (MMLU +0.62pp at d005), OLMo-2 near-null (+0.4pp), Gemma-2 待 v2 eval
- **状态**: ⚠️ BLOCKED on v2 eval 完成。v1 数据因 ARC logprob bug 全部作废。IRT fitting 需用 v2 数据重跑。
- **14B Variant A/B**: 未定。14B d000_s123 + d050_s123 复现已批准但未开始训练。单 seed 无法判定灰色地带。

### C2: Signal Failure (CO-PRIMARY)
- **≤3B 数据**: FROZEN。Min-K++ reversal Cohen's d=-1.55 to -1.98, S1 AUC>0.95 confirmed。
- **7B+ 信号**: 未计算。需 v2 eval 完成后计算 (D143 hybrid strategy)。
- **状态**: ≤3B claim 稳固。7B+ 信号数据为 nice-to-have, 非 blocking。

### C3: Identifiability Boundaries
- **Simulation sweep**: FROZEN (20 conditions × 200 runs), AUC=0.55 at N≥50 confirmed。
- **Fisher Info derivation**: 附录 .stan 文件存在, 但完整推导 appendix 未确认完成。
- **状态**: ✅ 基本完成。CPU-only, 不依赖 v2 eval。

### C4: Conditional Calibration (DEMOTED)
- **≤3B 数据**: FROZEN。vanilla 2PL ≈ 2PL+γ on MAE (GSM8K 0.0063 vs 0.0062)。ARC MAE=0.035 passes gating。
- **7B+ calibration**: 需 v2 eval + IRT fitting 完成后重跑。
- **状态**: ⚠️ BLOCKED on v2 eval + IRT re-fitting。≤3B claim 稳固但论文需 4-family scope 数据。

---

## 2. 论文章节完成度

| Section | Word Budget | 状态 | 备注 |
|---------|------------|------|------|
| Abstract | 200 | 🔴 需完全重写 | scope 从 ≤3B → ≤14.7B + 4 families |
| Introduction | 850 | 🔴 ¶4 + Contributions 需重写 | ¶1-3 基本不动 |
| Related Work | 700 | 🟡 基本完成 | 需加 1-2 句 multi-family evaluation |
| Method | 1100 | 🟢 基本完成 | D120 decomposition 已写入 method.tex §3.4, 加 family indicator |
| Experimental Setup | 600 | 🟡 需大幅更新 | §4.2 从 Llama exploratory → 4-family controlled SFT |
| Results | 1500 | 🔴 需大幅更新 | 所有数据表需 v2 数据, 新增 Scale + Cross-Family sections |
| Discussion | 500 | 🟡 需更新 | 加 scale re-emergence / threshold framing |
| Conclusion | 350 | 🟡 需更新 | scope 升级 |
| Appendix | unlimited | 🟡 部分完成 | Fisher derivation 有, Llama section 需改为 cross-family |

**D139 状态**: Round 6 完成, 0 errors, ≤8 页 ACL 合规。但内容基于 ≤3B + Llama exploratory, 需全面升级到 4-family scope。

---

## 3. v2 Eval 完成后需更新的表格和图表

### Tables
| Table | 当前状态 | 需要的更新 |
|-------|---------|-----------|
| table_domain_gamma (§5.1) | ≤3B N=24 FROZEN | 加入 7B/14B/cross-family γ rows; v2 ARC 数据替换 |
| table_baselines (§5.4) | ≤3B FROZEN | 加入 7B+ calibration MAE/τ; 所有 ARC 数据用 v2 |
| table_dcr_comparison (§2/§5.4) | 定性对比 | 不依赖 v2, 可提前完成 |
| Table 1/2 (accuracy) | v1 数据 | 全部替换为 v2 数据 (25 models × 3 benchmarks) |

### Figures
| Figure | 当前状态 | 需要的更新 |
|--------|---------|-----------|
| fig_pipeline (§3) | ✅ DONE | 可能需 minor label update |
| fig_domain_gamma (§5.1, flagship) | 未生成 | 需 v2 数据 + IRT re-fitting 后生成 |
| fig_dose_response (§5.1) | NEEDS REGEN | 加 7B/14B/cross-family 数据, 用 v2 |
| fig_signal_heatmap (§5.2) | 未生成 for v2 | ≤3B 数据可用, 7B+ 待计算 |
| fig_identifiability_heatmap (§5.3) | 可用 (FROZEN) | 不依赖 v2 |
| fig_calibration (§5.4) | NEEDS REGEN | 加 vanilla 2PL 对照, 用 v2 数据 |
| **NEW: fig_scaling_curve** | 未生成 | 2-panel MMLU vs ARC, X=scale, Y=Δacc, 4 families |

---

## 4. IRT Fitting 前置条件

| 条件 | 状态 | 备注 |
|------|------|------|
| v2 eval 全部完成 (25 models × 3 benchmarks) | 🔴 运行中, ETA ~12:45 | ARC logprob bug 修复后全量重跑 |
| v1 vs v2 对比分析 | ❌ 待 v2 完成 | 量化 fix 影响, 确认 MMLU/GSM8K 变化小 |
| Exposure signals (S1-S4) for 7B+ models | ❌ 未开始 | D143: hybrid strategy, 需 eval 完成后 |
| IRT model selection (2PL+γ vs 4PL+γ) | ✅ 规则已定 | C008: 2PL+γ default, 4PL+γ only if N≥16 + MCQ |
| Stan models | ✅ 已有 | artifacts/mvp_simulation/ 中有 2PL/4PL .stan |
| ≤3B IRT results | ✅ FROZEN | N=24, domain-level 完成 |
| 7B+ IRT fitting | ❌ 需 v2 eval + signals | 需决定是否扩展到 cross-family pooled fit |

**结论**: IRT fitting 的关键前置是 v2 eval 完成 + 7B+ signals 计算。最早可开始时间: 今天下午 (如果 signals 计算快速)。

---

## 5. 关键路径 Blocking Items (按优先级)

### P0 — 今天必须完成
1. **v2 eval 完成** — 4 GPU 并行, ETA ~12:45。所有下游工作的 gate。
2. **v1 vs v2 对比分析** — 量化 ARC fix 影响, 确认 MMLU/GSM8K 无显著变化。
3. **Variant A/B 初步判定** — 用 v2 数据重新评估 14B MMLU 灰色地带 (+1.92pp)。

### P1 — Day 2-3 (May 20-21)
4. **7B+ signal computation** — S1 embedding similarity for 7B/14B/cross-family (S2-S4 可选)。
5. **IRT re-fitting with v2 data** — per-benchmark + domain-level, 包括 7B+ models。
6. **TOST equivalence test** — ARC null effects at 7B+ (bound ±1.5pp)。
7. **所有 figures 生成** — 7 figures (1 done, 6 需 v2 数据)。

### P2 — Day 3-4 (May 21-22)
8. **论文 Results section 重写** — 新增 Scale Invariance + Cross-Family Consistency sections。
9. **Experimental Setup §4.2 重写** — 4-family controlled SFT description。
10. **Tables 全部更新** — v2 数据 + 7B+/cross-family rows。

### P3 — Day 4-5 (May 22-23)
11. **Abstract + Introduction 重写** — scope 升级, 4-family framing。
12. **Discussion + Conclusion 更新** — scale re-emergence / threshold framing。
13. **Appendix 更新** — Cross-family analysis section, Fisher derivation check。

### P4 — Day 5-6 (May 23-24)
14. **Round 7 review** — 全文审校。
15. **AI 写作风格清零** — grep dash/ing-phrases/过度分段。
16. **投稿 checklist + 匿名化检查**。

### ⚠️ 风险项
- **14B s123 复现未启动** — Variant A/B 最终判定可能延迟, 需立即安排 GPU。
- **Gemma-2 结果决定性** — 如果 Gemma-2 MMLU 也 null, cross-family claim 降级 (2/4 positive + 2/4 null)。
- **v2 eval 如果暴露新问题** — 可能需要进一步 debug, 压缩下游时间。
- **论文重写量大** — Abstract/Intro/Results/Setup 四个 section 需大幅修改, 每个约 0.5-1 天。

---

## 6. 决策待定项

| 决策 | 依赖 | 预计时间 |
|------|------|---------|
| Variant A vs B (14B) | v2 数据 + 14B s123 复现 | May 20-21 |
| Cross-family claim 强度 (Layer 2) | Gemma-2 v2 结果 | May 19 evening |
| 三层叙事框架选择 (re-emergence / threshold / Qwen-specific) | 全部 v2 数据 + IRT | May 21 |
| 是否追加 14B d000_s123 + d050_s123 训练 | v2 数据分析 | May 19 (urgent) |
