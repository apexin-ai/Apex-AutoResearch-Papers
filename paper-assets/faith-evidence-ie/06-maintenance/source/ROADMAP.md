# faith-evidence-ie — Research Dashboard

> 最后更新: 2026-05-23 23:00 UTC | 更新原因: 1.7B s43 tax 数据补全，全部实验完成

> 投稿目标: **EMNLP 2026 Main** (ARR July cycle, ~54 天)

## 核心方向
FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (GRPO catastrophic > DPO gradual > RSFT none) (3) Evidence tax landscape + variance compression。详见 paper_framing.md。

## 当前进展
- **阶段**: ✅ 数据审计完成，准备 Round 3 review
- **Round 2 评分**: 3.0 (Findings)。升级路径: 3.0→3.5→4.0
- **论文状态**: 正文 8 页（3 figures + 2 tables）。所有审计发现已修复
- **数据审计**: ✅ 完成（62 项，58 PASS，3 FAIL 已修正，1 multi-seed 补全）
  - F1: DPO 1ep Rel-F1 33.38→33.37（四舍五入修正）
  - F2: method.tex EDCR 值统一为 Table 1 三-seed mean（0.6797/0.6487）
  - F3: fig_spectrum caption 轴标签已修正
  - 8B test tax: 补 error bar（3-seed, -0.91±0.74pp）
  - LLaMA test tax: 更新为 2-seed mean（-1.46±0.40pp）
- **14B RSFT s43**: ✅ 全部完成。dev with-evi=0.5815, dev no-evi=0.5713, dev tax=-1.02pp; test with-evi=0.3767, test tax=+0.08pp

## 剩余任务
- [x] **14B RSFT s43 test eval** ✅ (ign_f1=0.3767, tax=+0.08pp)
- [x] **14B RSFT s43 dev eval** ✅ (with-evi=0.5815, no-evi=0.5713, tax=-1.02pp)
- [ ] **Round 3 review** (recommended_review_mode="continue")
- [ ] **Reviewer 最终验证**：审计修复后的图表和文字

## Multi-seed Evidence Tax 汇总（RSFT test, Re-DocRED）
| Scale | s42 tax | s43 tax | s44 tax | Mean±std | 方向 |
|-------|---------|---------|---------|----------|------|
| 1.7B | -5.43pp | -4.59pp | — | -5.01±0.59 (n=2) | negative |
| 4B | +1.51pp | +1.99pp | +1.46pp | +1.65±0.29 (n=3) | positive |
| 8B | -0.34pp | -1.74pp | -0.65pp | -0.91±0.74 (n=3) | negative |
| 14B | +0.77pp | +0.08pp | — | +0.43±0.49 (n=2) | positive |
| LLaMA | -1.74pp | -1.17pp | — | -1.46±0.40 (n=2) | negative |

## GPU 预算
rtx5090-4x cuda:0-3 — 全部空闲（14B eval 全部完成）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D159 | 2026-05-25 | D159: 不纳入 1.7B seed-matched SFT variance 数据——保持 sh | d158_1_7b_rsft_s44_train |
| D158 | 2026-05-24 | D158: 补跑 1.7B s44 和 14B s44 RSFT 全流程——消除跨 scale 种子 | plan_006_qwen3_1_7b_sft, plan017_14b_rsft_s43_eval |
| D157 | 2026-05-23 | D157: 数据审计完成——3 项修正 + 8B/LLaMA multi-seed tax 补全 | data_audit |
| D156 | 2026-05-23 | D156: 批准 DPO 重建——从 RSFT generations 重新计算 CED score | — |
| D155 | 2026-05-23 | D155: Round 2 审稿 3.0 Action Matrix — 统计方法论修复 + emp | — |
| D154 | 2026-05-23 | D154: RSFT test evidence tax 5/5 完成。4B tax=+1.51pp | test_eval_4b_rsft_s42_no_evi, test_eval_1_7b_rsft_s42_no_evi, test_eval_8b_rsft_s42_no_evi, test_eval_14b_rsft_s42_no_evi, test_eval_llama_rsft_s42_no_evi |
| D153 | 2026-05-22 | D153: 预判 D150 Version A ("evidence sensitivity com | test_eval_1_7b_rsft_s42_no_evi, test_eval_8b_rsft_s42_no_evi, test_eval_14b_rsft_s42_no_evi |
| D152 | 2026-05-22 | D152: 8B RSFT variance compression 从 17× 修正为 6.5×— | plan_006_qwen3_8b_rsft_eval, d102_8b_rsft_k1_s42 |
| D151 | 2026-05-22 | D151: 采纳 Reviewer 论文加固优先级——8B RSFT s44 补全为最高优先级，堵  | plan017_14b_rsft_s43_generate |
| D150 | 2026-05-22 | D150: 采纳 Reviewer RSFT evidence tax 叙事框架——Claim 5  | test_eval_8b_rsft_s42_no_evi, test_eval_14b_rsft_s42_no_evi |

