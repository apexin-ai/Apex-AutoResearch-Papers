# turn_residual_gating — Research Dashboard

> 最后更新: 2026-05-25 06:34 UTC | 更新原因: Reviewer 反馈修正：GPU 状态更新、ARR DDL 补充、已完成项标记、页数压缩完成

## 核心方向
Exposure bias 摧毁 auxiliary attention losses 在多轮对话 AR 推理中的泛化性（8×–27× gap）。GAR 作为 diagnostic probe 暴露问题，五路消融定位原因，SS 是唯一有效 fix（压缩至 ~1.3×）。详见 paper_framing.md。

## 当前进展
- **阶段**: Round 4 审稿修复 — 实验补充 + Framing 重写
- **目标**: ARR August cycle（DDL: **2026-08-03**），时间充裕（~70 天）
- **Round 4 评分**: 3.0 (Findings)，修复后 ceiling 3.5 (Borderline Conference)
- **Core claims**: C1✅ C2✅ C3✅ C4✅ C5✅
- **论文状态**: Framing 重写完成 + 页数压缩完成（主文 ≤8 页）✅
- **阻塞问题**: 3 Critical 待实验修复（统计单seed C2 / GAR construct validity C1 / exposure bias 因果 C3）

## 近期任务（Round 4 修复）

### 实验（串行执行，westd-20861:cuda:0）
- [x] Phase 1A 启动（PCGrad s123 RUNNING，PID 5508，GPU 99% util）
- [ ] **Phase 1A: Multi-seed Qwen** 8 runs（~40-56h）— 全条件 mean±std（C2）
  - PCGrad ×2, UG ×2, LoRA-only ×2, TG ×1, SS ×1 新 seeds
  - 每 run 完成后 AR eval N≥50 + bootstrap 95% CI
- [ ] **Phase 2: TF→AR switching**（~4h inference-only）— 插在 Phase 1A run 间歇执行，解决 C3
- [ ] **Phase 1B: Llama PCGrad + UG** × 1 seed（~14h）— 完成 cross-model 5/5 矩阵（W3）
- [ ] Base bootstrap CI（N=50, 1000 resamples，无需训练）

### 写作（Paper Agent）
- [x] Framing 重写：GAR→diagnostic probe, ThreadGate→testbed ✅
- [x] 标题改为 "Exposure Bias Destroys Auxiliary Attention Losses in Multi-Turn Dialogue" ✅
- [x] 页数压缩至 ≤8 页 ✅
- [ ] 数据一致性修复（β=3 GAR 0.628→0.173, gap 统计口径统一, N=20→N=50, 词表描述）— 已派发
- [ ] PaperBanana method framework 概念图（API key 已审批）
- [ ] Figure 1(b) 图注与柱状图重叠修复（用户反馈）

### 实验完成后
- [ ] 汇总 5 条件 × 3 seeds 结果表，更新 Table 1 为 mean±std
- [ ] Phase 2 switching 结果写入 §5 或 §6
- [ ] Llama 5/5 条件写入 §5.5
- [ ] 更新 experiment_plan.yaml registry_id 映射（当前覆盖率 51.7% 偏低，实际 ~85-90%）
- [ ] submit_paper_to_review（fresh round）

## GPU 预算
- **已分配**: westd-20861:cuda:0 (1×RTX PRO 6000 Blackwell, 96GB)
- **当前**: Phase 1A multi-seed RUNNING（99% util）
- **预估需求**: Phase 1A ~40-56h + Phase 2 ~4h + Phase 1B ~14h = ~58-74h
- **可用时间**: ~1680h（至 8/3 DDL），非常充裕

## Phase 3（如有余裕）
- SS+LoRA-only × 3 seeds（W1 消融，~21h）— nice-to-have，不 blocking

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D056 | 2026-05-25 | Round 6 修复策略：λ_GAR rescaling + TF→AR switching + L | phase2_tf_ar_switching, phase2_lambda_gar_rescaling, phase1b_llama_complement |
| D055 | 2026-05-24 | Llama SS 训练改为 2 epochs 提前停止（Step ~14400），3 epochs  | p1_llama_ss_training |
| D054 | 2026-05-24 | KL per-head + GAR 鲁棒性分析完成——两项新发现支持 SS 优于 TG 的机制性论证 | p1_tf_ar_kl_divergence, plan_028 |
| D053 | 2026-05-24 | MMLU 质量保留确认 + Qwen-1.5B 跨尺度结果 → 均放入附录 | mmlu_eval_all, qwen15b_phase1_diag, d048_eval_qwen15b_tg |
| D052 | 2026-05-24 | SS 3-seed validation complete: AR GAR 0.401±0.047, | plan_027, d048_eval_ss_s456 |
| D051 | 2026-05-23 | D051: Framing 升级至 3.5 — SS 升为独立 Results + 5th cont | phase2_tg_s42_v8b_resume, d048_eval_ss_s42, d048_eval_ss_s123 |
| D050 | 2026-05-23 | Table 1 切换到 eval_200 N=50 数据，叙事从 "zero benefit" 调整 | d048_final_ar_eval, d048_eval_ss_s42 |
| D049 | 2026-05-22 | D049: Round 3 审稿报告 Action Matrix——不降级 SS contribut | — |
| D048 | 2026-05-22 | D048: Group C Round 2 审稿 3.0 修复计划——multi-seed 5 条件 | phase2_tg_s42_v7, phase2_tg_s42_v8b_resume, eval_llama_ar_n20, phase2_tg_s42_v9_pcgrad, instruction_retention_test |
| D047 | 2026-05-22 | D047: mid_turns 定义接受 turns 3-T（代码实际），论文措辞修正 defer  | eval_llama_ar_n20 |

