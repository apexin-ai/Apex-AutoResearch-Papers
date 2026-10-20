# distrib_canary_collapse — Research Dashboard

> 最后更新: 2026-05-25 00:57 UTC | 更新原因: 修正 GPU 数量错误（1 GPU not 2）；C2-s43 改为等 s42 后串行

> 最后更新: 2026-05-25 | 更新原因: 修正 GPU 数量错误；C2-s43 failed，等 s42 完成后重跑

## 核心方向
**Title**: "Characterizing the Detectability Landscape of Iterative Model Collapse"
核心贡献：α×T 2D 相图、method sensitivity (7%-94% FPR)、cascade ordering (entropy→diversity)、cross-architecture validation。

**目标**：EMNLP 2026 ARR June（DDL ~2026-06-15，距今 21 天）
**审稿历史**：R8=3.0 → ... → R14=3.0 (Findings) → 写作修复全部完成 → 补实验中
**目标分数**：3.5 (Borderline Conference)
**升分关键**：C2 cross-arch transition region + C1 N=5 intervention

## 当前进展
- 论文编译通过 ✅（主文 8 页）
- R14 写作修复 13/13 完成 ✅（Reviewer 验证 6/6 PASS）
- FPR 数字更新 10 seeds (6.7%, 4/60) ✅ 全文一致
- C2-s42 运行中（OPT-1.3B α=0.50 seed 42，预计 ~6-7h）
- C2-s43 failed（cuda:1 不存在导致 CPU 训练）→ 等 s42 完成后用 cuda:0 重跑

## 关键实验
| ID | 描述 | 状态 | GPU | 优先级 |
|----|------|------|-----|--------|
| C2-s42 | OPT-1.3B α=0.50 seed 42 | 🏃 运行中 (PID 32378) | cuda:0 | P0 |
| C2-s43 | OPT-1.3B α=0.50 seed 43 | ⏳ 等 s42 完成后重跑 | cuda:0 | P0 |
| C1 | N=5 intervention (3 arch) | 排队（C2 后） | — | P1 |

**C2 是从 3.0→3.5 的核心证据**：验证 phase diagram 结构在 Pythia 之外泛化到 transition region。

## 近期任务
- [x] C2 s42 启动训练
- [ ] 等 C2-s42 完成 → 立即用 cuda:0 启动 C2-s43
- [ ] C2 完成后 D102 分析 → 更新论文 §4.5 + limitations
- [ ] C1: N=5 intervention（GPT-2m, OPT-1.3B, Qwen2.5-0.8B）
- [ ] 重新提交 C 群审稿

## GPU 预算
本项目：westd-19828 (**1 GPU: cuda:0 only**, RTX PRO 6000 Blackwell 98GB)
当前：**1/1 使用中**（cuda:0 → C2-s42）
⚠️ 服务器只有 1 块 GPU，不是 2 块

## 硬约束
- D102: 6-pair basis (distinct_1/2/3, MAUVE excluded); threshold=true_3sigma_d105; n_perm=5000
- α_c = 0.483±0.006; PPL reduction = 64%
- FPR: PermG 4/60=6.7% (CI [1.8%, 16.2%]), 10 seeds, 8/10 yield 0 FP
- K≥3 consensus: 6/60=10.0%
- Cross-arch at α=1.0: 11/15 forward, 4 non-confirming

## Post-C2 论文更新清单
- limitations.tex:5 "cross-architecture evaluation is limited to α=1.0" → 更新范围
- §4.5 加入 OPT-1.3B α=0.50 结果
- Abstract/Conclusion 如 C2 成功则可扩展 cross-arch claim

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D222 | 2026-05-25 | R16 Action Matrix: framing reposition (phase trans | — |
| D221 | 2026-05-24 | D221: 用 9-seed pooled FPR 数据定稿论文 FPR claim，不等 s51- | null_fpr_s42, null_fpr_s43, null_fpr_s44, null_fpr_s45, null_fpr_s46, null_fpr_s47, null_fpr_s48, null_fpr_s49, null_fpr_s50 |
| D220 | 2026-05-24 | R12 审稿报告处理：结构性修改方案（非 hedging 语言修改） | — |
| D219 | 2026-05-24 | D219: 取代 D218——FPR claim 改为 "lowest FPR among all  | null_fpr_s46, null_fpr_s48, null_fpr_s49, null_fpr_s50, null_fpr_s45, null_fpr_s47 |
| D218 | 2026-05-24 | D218: FPR claim 采用 K≥3 一致性标准——pooled 4/36 raw hits | null_fpr_s46, null_fpr_s48, null_fpr_s49, null_fpr_s50, null_fpr_s45, null_fpr_s47 |
| D217 | 2026-05-24 | D217: 撤回 D215 的"管线差异"排除理由——s45 FPR 是 seed 依赖现象；等 n | null_fpr_s45, null_fpr_s47 |
| D216 | 2026-05-24 | D216: plan_022 conditional Granger 不写入论文，保留为内部 art | plan_022 |
| D215 | 2026-05-24 | D215: s45 null FPR=2/8 暂不纳入 — 旧管线 artifact 待新 seed | null_fpr_s45 |
| D214 | 2026-05-24 | D214: Table 17 final — drop s43 T=10 column, 4-col | — |
| D213 | 2026-05-24 | D213: Unify Table 17 to 6-pair basis — re-run s42  | — |

