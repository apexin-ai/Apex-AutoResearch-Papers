# symb_invariant_consensus — Research Dashboard

> 最后更新: 2026-05-24 06:20 UTC | 更新原因: o3 已解决；LLaMA 多种子完成；更新 GPU 状态和近期任务为提交冲刺

> 核心方向详见 paper_framing.md。

## 核心方向
**Symbolic Mirage**: Self-extracted logical constraints project model bias, not independent verification.

## 当前阶段
**V4 Strategic Restructure + A/D Theoretical Depth → May 25 EMNLP ARR**

## 审稿进展
- Round 12: 3.0 → Round 13: 3.5 → Round 14: 3.5 → Round 15: 3.5 (Fresh)
- Round 19 已提交，等待结果
- 目标: 4.0 Conference

## 已完成（本轮）
1. ✅ Q5/Q6/CIL/Proposition 1/Causal DAG/Paper V4/A+D 整合
2. ✅ 数据审计: tiebreaking 确认原值正确；94.4%→≥99%；Table 2 gpt-4o/Gemini 修正
3. ✅ Reviewer 一致性核查: 5/6 PASS + Check 4 (Δ bound w=3 限定) 已修
4. ✅ GPU 清理: kill 冗余实验
5. ✅ o3 数据不一致: SC=82.65%=162/196（8 API failure excluded, n=196），Table 2 已正确标注，无需修改
6. ✅ LLaMA-8B × PW 多种子: 4 seeds 全部完成，Δ −4.67 to −7.50pp，已写入附录
7. ✅ 匿名化审计 6 项 PASS + 附录可发现性 6 处引用

## 当前进行中
1. **Qwen3-14B × PW 三种子** (cuda:0/2/3): ~70%, ETA ~11:15 UTC
2. Agent 正在将 Qwen2.5-14B × PW 4-seed 数据补入附录 tab:multi-seed

## 多种子覆盖（附录 tab:multi-seed）
| Condition | Seeds | Δ Range | Direction |
|-----------|-------|---------|-----------|
| Mistral-7B × FOLIO | 3 | −2.45 to +2.94 | 不稳定 |
| Qwen2.5-14B × FOLIO | 4 | −2.01 to 0.00 | 全部 ≤0 |
| Mistral-7B × PW | 4 | −3.33 to −1.33 | 全部负 |
| LLaMA-8B × PW | 4 | −7.50 to −4.67 | 全部负 |
| Qwen2.5-14B × PW | 4 | Δ −1.63±0.76pp | 全部负 (待加入) |
| Qwen3-14B × PW | 3+1 | 运行中 | TBD |

## GPU 状态
**westd-16639** (4× RTX PRO 6000):
- cuda:0: Qwen3 seed123 (~70%)
- cuda:1: 空闲（不派新实验，聚焦提交）
- cuda:2: Qwen3 seed456 (~70%)
- cuda:3: Qwen3 seed789 (~70%)

**westd-30973**: 已释放

## 近期任务
- [x] o3 SC/n_err 修正 ✅ 无需修改
- [x] LLaMA 多种子完成 + 写入附录 ✅
- [ ] Qwen2.5-14B × PW 数据补入 tab:multi-seed ← Agent 执行中
- [ ] Qwen3 三种子完成 → 收集 → 写入附录 → push
- [ ] 最终 paper_compile_and_check + consistency check
- [ ] May 25 EMNLP ARR 投稿

## 风险管控
- ⚠️ M075: 比较实验文件与论文数据前必须确认 tiebreaking 方法一致
- ⚠️ Consistency check: 12 个 precision_mismatch warning（analysis vs experiments 小数位不一致），提交前需评估是否修正

## 关键数据
- 176 个实验，156 完成
- 已完成多种子: 5 conditions × 3-4 seeds = 19 seed-runs，绝大多数 Δ≤0
- 27 种 remediation 全部 negative
- Oracle: +13.73~+29.90pp
- Cross-arch NLI: +6.67pp zero-shot (Mistral PW)

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D156 | 2026-05-24 | R22 Action Matrix: 3 Must-Fix全部写作修复，标题改为mechanism- | — |
| D155 | 2026-05-23 | D155: CIL (Direction B) 从论文中删除。理论增强缩减为 A+D only。 | exp-d134-cil |
| D154 | 2026-05-23 | D154: V4 writing plan approved with ABCD theoretic | exp-d134-cil |
| D153 | 2026-05-22 | 废弃"两套 trace"约束，统一所有 Mistral PW 数据到 ID_FIX 后 canoni | — |
| D152 | 2026-05-22 | D152: 全面统一 D061 alphabetical tiebreaking — 所有 SC b | exp-deberta-ft-combo, exp-092-llama8b-pw-nli-combo |
| D151 | 2026-05-22 | D151: 修正 D150 — combo eval 全面使用 D061 alphabetical  | exp-deberta-ft-combo, exp-092-llama8b-pw-nli-combo |
| D150 | 2026-05-22 | D150: SC baseline 统一用 trace pre-computed sc_answer | exp-deberta-ft-combo, exp-092 |
| D149 | 2026-05-22 | Table 3 采用方案 A：统一报 w=3 + 文中补充 LLaMA w=1 显著性 | exp-092, exp-091, exp-090 |
| D148 | 2026-05-22 | D148: Diagnostic framework held-out validation — t | exp-063, exp-multi-seed-llama-folio, exp-041, exp-033 |
| D147 | 2026-05-22 | D147: Round 13 review 3.5 Borderline Conference. N | exp-013-constraint-ablation, exp-folio-2x2-crossmodel |

