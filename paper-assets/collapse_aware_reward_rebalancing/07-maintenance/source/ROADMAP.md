# collapse_aware_reward_rebalancing — Research Dashboard

> 最后更新: 2026-05-17 13:11 UTC

> 最后更新: 2026-05-17 13:30 UTC | 更新原因: P1 experiments launched, paper 8-page target met

## 核心方向
**Direction D: "Collapse is real but mischaracterized"**
Reward curation 不导致 semantic 或 format collapse。Format homogenization 是 iterative self-training 的固有属性，K 是放大因子。LoRA 下的表观抑制是 capacity artifact。

## 当前进展
- **阶段**: 论文完成 → P1 跨模型验证进行中
- **目标会议**: EMNLP 2026 ARR (DDL: 2026-05-25, 8 天)
- **论文进度**: 正文 8 页达标 + 4 figures 嵌入 + P0 补充指标整合完成
- **GPU**: cuda:0 C9 running, cuda:1 C10 running（P1 Qwen2.5-1.5B 实验）
- **D013**: Format collapse 因果归因修正已全面落地（iterative training 固有，非 curation 导致）

### 论文核心贡献 (5 confirmed)
1. Semantic resilience: 8 configs × 3 gens, Vendi ±1%（含 K=16 极端条件）
2. Format collapse 是 iterative training 固有属性（D013：同 K 对比 curated≈random）
3. Direction reversal: LoRA -3.4pp → Full-FT +0.63pp
4. Measurement contribution: opening_entropy + near_dup_start_rate
5. K 是 format collapse 放大因子（K=8 entropy -1.13 bits vs K=4 -0.75 bits）

## 近期任务
- [x] D013 format collapse 因果归因修正（全文 6 个 tex 文件）
- [x] Reviewer 3C5W 全部修复
- [x] 页数压缩 10→8 页 + 4 图嵌入
- [x] P0 补充指标（ArmoRM quality + self-BLEU/distinct-n → appendix）
- [x] C7 training loss 修正 + Section 4.4 quality range 修正
- [ ] P1 Qwen2.5-1.5B 实验完成 (C9 curated + C10 random, 5 gens) — ETA 6-8h
- [ ] P1 结果整合到论文（正文 1 段 + appendix 表格）
- [ ] 最终编译 + submit_paper_to_review

## GPU 预算
- cuda:0: C9 carr_qwen25_1-5b_lora_k4_curated (RUNNING)
- cuda:1: C10 carr_qwen25_1-5b_lora_k4_random (RUNNING)

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D014 | 2026-05-17 | 保留叙事顺序（semantic→format→reversal），不采纳 Reviewer 建议的  | — |
| D013 | 2026-05-17 | Format collapse 因果归因修正：从"curation causes"改为"iterat | c1-regen-v2, carr_quick_probe_k8_02 |
| D012 | 2026-05-17 | K=16 P1 FAIL (Vendi -0.19%)，确认 Outline A：8 配置全部无 s | carr_fullft_lr2e5_k16_probe_01 |
| D011 | 2026-05-17 | Direction C FAIL (CARR dry-run 99.3% overlap)，切 Di | carr_fullft_lr2e5_k16_probe_01, carr_fullft_lr2e5_probe_01 |
| D010 | 2026-05-17 | 采用 C→D fallback pipeline: 24h 内验证 CARR Pareto opti | carr_fullft_lr2e5_probe_01, carr_fullft_lr2e5_k16_probe_01 |
| D009 | 2026-05-17 | P1 5/5 全部 FAIL，核心假设证伪：curation 不导致 diversity colla | carr_quick_probe_03, carr_quick_probe_k8_02, carr_fullft_k4_probe_03, carr_fullft_lr2e5_probe_01, carr_baseline_no_curation_01 |
| D008 | 2026-05-16 | Full-FT K=4 P1 FAIL (Vendi +0.9%)，LR underfitting  | carr_fullft_k4_probe_03 |
| D007 | 2026-05-16 | K=8 P1 FAIL，与 K=4 收敛到相同 Vendi (107.25)。确认 LoRA 是 c | carr_quick_probe_k8_02, carr_quick_probe_03, carr_baseline_no_curation_01 |
| D006 | 2026-05-16 | 重新定义 P1: 从 Vendi 绝对下降 ≥5% 改为 baseline-relative gap | carr_baseline_no_curation_01, carr_quick_probe_03 |
| D005 | 2026-05-16 | Baseline 显示 curation 抑制 diversity 增长 (relative gap | carr_baseline_no_curation_01, carr_quick_probe_03 |

