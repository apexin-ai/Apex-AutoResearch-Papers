# ops mmlu domain grouping audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mmlu_domain_grouping_audit_20260517T064324_result.json`
- **Structured JSON:** [`01d9905e2c584c5686e2.json`](../../sessions/01/01d9905e2c584c5686e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收齐了。以下是三个问题的答案：

---

## Q1: "Math γ=0.97, Science γ=0.84" 来自哪里？

来自 **`/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/`** 目录（N=23 版本，包含 0.5B+1.5B+3B 三个 scale）。

具体值：
- **STEM_Math**: γ_mean = **0.9688**, 95% CI [0.527, 1.430], PPP=0.438, N=23 models, 1190 items
- **STEM_Science**: γ_mean = **0.838**, 95% CI [0.385, 1.274], PPP=0.807, N=23 models, 1397 items

记录在 `artifacts/analysis_2pl_gamma_refit_0516.md` 中。

---

## Q2: J=16 结果中 "STEM_Math" 的定义

J=16 结果位于 `/root/autodl-tmp/exp006/results_mmlu_domain_gamma/`，**使用 `run_mmlu_domain_gamma.py` 中的 DOMAIN_MAP**：

**STEM_Math** (478 items, J=16) =
- abstract_algebra, college_mathematics, elementary_mathematics, high_school_mathematics, high_school_statistics, formal_logic

J=16 结果：γ_mean = **-0.549**（注意：与 N=23 版本方向相反，因为 J=16 只含 1.5B 模型，没有 0.5B/3B 的 scale 变异）

---

## Q3: J=13 rerun 用的 8 domains

`run_mmlu_domain_gamma_no05b.py` 使用**完全相同的 DOMAIN_MAP**（8 个域）：

1. STEM_Math (6 subjects)
2. STEM_Science (8 subjects)
3. STEM_CS_Eng (5 subjects)
4. Medical (8 subjects)
5. Humanities (9 subjects)
6. Social_Sciences (12 subjects)
7. Business_Law (7 subjects)
8. Other (2 subjects: global_facts, miscellaneous)

J=13 模型白名单 = 8× 1.5B + 5× 3B（去掉了所有 0.5B）。正在运行中（log 显示刚完成某个域的 sampling）。

---

## 三版本对比总结

| 版本 | 目录 | J | Scales | 域分组 | STEM_Math γ |
|------|------|---|--------|--------|-------------|
| N=23 (paper来源) | `results_mmlu_domain_gamma_n24/` | 23 | 0.5B+1.5B+3B | **同一 DOMAIN_MAP** | +0.97 |
| J=16 (仅1.5B) | `results_mmlu_domain_gamma/` | 16 | 仅 1.5B | **同一 DOMAIN_MAP** | -0.55 |
| J=13 rerun (no 0.5B) | `mmlu_domain_irt_no05B/` | 13 | 1.5B+3B | **同一 DOMAIN_MAP** | (running) |

**结论：三个版本的域分组定义完全一致**（同一个 DOMAIN_MAP，同样的 57 subjects → 8 domains 映射）。

γ 值差异的原因不是分组不同，而是 **respondent 组成不同**：
- N=23 包含 0.5B（ability 极低）→ scale 变异大 → IRT 能区分 ability vs exposure → γ 为正（exposure helps）
- J=16 仅 1.5B → 所有模型 ability 相似 → 无法有效分离 ability 和 exposure → γ 估计不稳定/为负

---
