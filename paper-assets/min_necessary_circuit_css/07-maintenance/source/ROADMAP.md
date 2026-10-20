# min_necessary_circuit_css — Research Dashboard

> 最后更新: 2026-05-13 16:14 UTC | 更新原因: Size-controlled bootstrap CI 完成 (PASS)，所有实验数据齐全

## 核心方向
跨方法二值共识（CSS）在电路发现中的系统性失败分析。详见 paper_framing.md。

核心发现：CSS=1.0 在所有 6 个 task×model 配置上均未超越最佳单方法（控制电路大小后），失败归因于三个结构性模式。

## 当前进展
- **阶段**: Writing（Paper Agent 活跃，Step 2 figures 完成，Step 3 正文写作中）
- **投稿目标**: EMNLP 2026 Findings (ARR DDL 2026-05-25，剩余 12 天)
- **配置覆盖**: 6/6 完成
- **核心 claims**: 4 个（ACDC isinf ★★★★★, universal failure ★★★★★, scaling failure ★★★★, CIRCUS ablation ★★★）
- **Bootstrap CI 全部完成**: SVA (p=0.099), FR (p=0.000 neg), IOI non-size-ctrl (p=0.342), IOI size-ctrl (all p>0.1, CSS≡ACDC delta=0)
- **Figures**: fig1_overview ✓, fig2_size_controlled ✓, fig3_jaccard_heatmap ✓
- **服务器**: westd-39279 (cuda:0, cuda:1), 路径已规范化

## 近期任务
- [x] size-controlled baseline 实验 (NEGATIVE)
- [x] paper_framing.md 更新 (D036)
- [x] experiment_plan.yaml 同步
- [x] IOI Bootstrap CI 修复 (p=0.342, registry 已更新)
- [x] **size-controlled Bootstrap CI** (CSS≡ACDC delta=0 p=1.0, 所有比较 p>0.1)
- [x] 服务器路径规范化完成
- [x] Figures 1-3 生成完成
- [ ] **Paper Agent 正文写作中**（Step 3）
- [ ] (nice-to-have) Arithmetic Bootstrap CI
- [ ] (nice-to-have) 扩展 random baselines

## GPU 预算
- 已分配: 2× GPU (westd-39279: cuda:0, cuda:1)
- 所有实验完成，GPU 当前空闲
- **瓶颈在写作速度**

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D036 | 2026-05-13 | D036: IOI 正例死亡确认——size-controlled baseline 证明 CSS= | ioi_size_controlled_baseline, bootstrap_ci_sva_fr, mvp_pilot_gpt2_ioi_v3 |
| D035 | 2026-05-13 | D035: Reframe 为分析论文 Route A — "When Does Cross-Met | mvp_pilot_gpt2_ioi_v3, phase2_qwen05b_ioi_acdc_k3, mvp_arithmetic_gpt2_k3 |
| D034 | 2026-05-13 | D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择 | phase2_qwen05b_ioi_acdc_k3, phase2_qwen05b_ioi_k3, mvp_pilot_gpt2_ioi_v3 |
| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |
| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |
| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |
| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |
| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |





