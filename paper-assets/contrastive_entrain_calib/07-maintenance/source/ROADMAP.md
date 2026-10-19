# contrastive_entrain_calib — Research Dashboard

> 最后更新: 2026-05-24 12:57 UTC | 更新原因: Round 8 审稿 + Paper Audit 后转向实验补充 (D068)

## 核心方向
Dual-layer analysis paper: "Why RL Fails for Sycophancy Calibration — and Why d_syc Makes It Worse"
- Layer 1: d_syc 方向成功判别 sycophancy (AUROC 0.827±0.028) 但所有 reward formulation 均失败
- Layer 2: ALL GRPO RL 方法都失败（R3-only 4/28 > vanilla）；唯一成功的是 SFT (ACT 31/31)
详见 paper_framing.md

## 当前阶段
**Round 8 审稿后实验补充 + 写作修复（D068）**

## Round 8 审稿回溯 · 系统性问题

### SYSTEMIC_ISSUE 1: 证据基础薄弱（6 个 CRITICAL 中 3 个）
- C1 单 seed probe trap → **实验补充：3 seeds × 2000 steps SFT (exp-008-seed2/3/4)**
- C3 gs=2 → **写作降级因果声明**（gs=8 full run ROI 太低，不做）
- C2 ACT vs GRPO confounds → **ACT-256 ablation** + **写作降级 "strongest candidate"**

### SYSTEMIC_ISSUE 2: Claim-Evidence 不匹配（3 个 CRITICAL）
- C4 Goodhart 四分类未讨论 → Paper Agent P1
- C5 Vennemeyer et al. (2025) 遗漏 → Paper Agent P2（待验证）
- C6 Framing 游移 → Paper Agent P3

### Paper Audit 关键发现
- ⚠️ 18 处 em-dash (---) = AI 写作标志 → Agent 清除
- 4/31 vs 4/28 不一致 → Agent 统一
- 内部实验编号暴露 → Agent 替换

## 冲刺计划
| 时间 | 任务 | 状态 |
|------|------|------|
| May 24 立即 | C1 多 seed SFT (3 seeds × 2000 steps, cuda:0) | 🔄 已派 Agent |
| May 24 并行 | Paper Agent 写作修复 (P1-P6) | 🔄 已派 |
| May 24 并行 | Agent 审计修复 (em-dash/4-31/exp-ID) | 🔄 已派 |
| C1 完成后 | ACT-256 ablation (cuda:0, ~8-12h) | ⏳ 待启动 |
| ~May 25-26 | 整合结果 → 重新审稿 → 提交 | ⏳ |

## 近期任务
- [ ] exp-008-seed2/3/4: C1 多 seed probe trap 验证 (cuda:0)
- [ ] ACT-256 ablation (C1 完成后, cuda:0)
- [ ] Paper Agent: Goodhart 四分类 (P1) + Vennemeyer (P2) + framing 统一 (P3) + §3 措辞 (P4) + SMART (P5) + 因果声明降级 (P6)
- [ ] Agent: em-dash 清除 + 4/31 统一 + exp-ID 替换 + 47/47 修正 + GPU 信息补充
- [ ] exp-003-len512-v3 继续运行 (cuda:1, ~36%, ETA May 27)
- [ ] 验证 Vennemeyer et al. (2025) arXiv:2509.21305 存在性

## GPU 预算
**westd-29046** (2× RTX PRO 6000 96GB):
- cuda:0 → C1 多 seed SFT (即将启动, ~6h) → 之后 ACT-256 (~8-12h)
- cuda:1 → exp-003-len512-v3 (RUNNING ~36%, ETA May 27)

## Reviewer 评估的 Findings 安全性
- 不做实验：~65-70%
- C1 replication + writing fixes：~85-90%
- 再加 ACT-256：95%+, 有机会 borderline 3.5

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D074 | 2026-05-25 | cuda:0 排序：ACT-256 → seed2 关键 checkpoint re-eval →  | exp-act-256, exp-003-s2-eval-ckpt2500, exp-002v3-gs8 |
| D073 | 2026-05-25 | 3-seed probe gaming 验证完成：pattern 一致但 ckpt-2000 方差极 | exp-008-seed2, exp-008-seed3, exp-008-seed4 |
| D072 | 2026-05-25 | 3-seed probe gaming 完全复制：S(t)→0 at step ~50, 早期 ck | exp-008-seed2, exp-008-seed3, exp-008-seed4 |
| D071 | 2026-05-25 | SFT probe penalty eval 揭示三种 temporal failure patte | exp-008-seed2, exp-008-seed3 |
| D070 | 2026-05-25 | Vanilla baseline 确认 R3 NLI hypothesis 设计缺陷（vanilla | vanilla-r3-nli-test, nli-truncation-test |
| D069 | 2026-05-24 | Truncation confound 双重排除 + R3 NLI asymmetry 新发现，归因 | exp-003-len512-v3, nli-truncation-test |
| D068 | 2026-05-24 | R8 后转向实验补充：C1 多 seed SFT (6h) + ACT-256 ablation ( | exp-008v3, exp-003-len512-v3 |
| D067 | 2026-05-24 | 不将 MMLU/GSM8K 能力保持数据加入论文 | exp-supp-mmlu-gsm8k |
| D066 | 2026-05-23 | Bootstrap CI → ± CV std: 统一 AUROC 不确定性表示 | exp-001, exp-012 |
| D065 | 2026-05-23 | Held-out 泛化数据定稿：3 checkpoint 均 SYCONScore≈0.204（+2 | exp-004-heldout, exp-004-heldout-vanilla-baseline |

