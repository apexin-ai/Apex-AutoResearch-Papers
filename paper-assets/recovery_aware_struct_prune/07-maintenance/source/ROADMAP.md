# recovery_aware_struct_prune — Research Dashboard

> 最后更新: 2026-05-24 15:29 UTC | 更新原因: Reviewer 确认 tab_math500 + compilation + C1 inline 全部通过，checklist 大部分完成，等 git push

> 核心方向详见 paper_framing.md

## 核心方向
Pruning criterion shapes recovery capacity — CKA-only >> Standard in reward (4.4×) and accuracy (4.55pp). Reward-accuracy decoupling: SFT ≈ GRPO accuracy despite vastly different rewards. 详见 paper_framing.md.

## 当前阶段: 提交收尾 — DDL 5/25

### MATH-500 Fixed Eval ✅ 全部完成
17/17 可执行 eval 全部完成，2 "--"（checkpoint 丢失不可补）。
C1 最终验证：7 种方法配置 max |gap| = 1.8pp（α=2.0），stderr ≈ 2pp，全部在噪声范围内。

### 论文数据一致性 ✅ 全部通过
- Reviewer 独立交叉验证 tab_math500.tex 10 行数据 100% 匹配
- C1 inline claims（GSM8K fine-grained 0.61pp, dose-response 1.14pp, MATH-500 noise, 跨benchmark ≤1.8pp）全部正确
- check_paper_consistency: 0 critical, 0 warning
- 编译成功，无 undefined reference

### 收尾 Checklist
- [x] tab_math500.tex 更新全部数值 + per-section bold
- [x] C1 max |Δ| inline 数值更新
- [x] experiments.tex + appendix.tex inline MATH-500 数值
- [x] dose-response 叙事检查
- [x] paper_compile_and_check
- [x] check_paper_consistency
- [ ] git push 匿名仓库 ← Agent 执行中
- [ ] submit_paper_to_review 最终审查
- [ ] 最终提交

### Review Issues 状态
- Round 1-3: 23/23 resolved ✅

## 服务器状态
- westd-32935：4× RTX PRO 6000 — 全部空闲
- westb-23072：2× RTX PRO 6000 — 全部空闲

## 投稿目标
- EMNLP 2026 Main (ARR May 25)

## GPU 预算
- westd-32935: 4× RTX PRO 6000
- westb-23072: 2× RTX PRO 6000

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D114 | 2026-05-23 | Fix MATH-500 eval script bugs and rerun all method | eval_math500_sft_standard_20_2048_v3, eval_math500_grpo_standard_20_fair_2048_v3b |
| D113 | 2026-05-23 | Floor ablation table 改为 GRPO-only 格式；放弃 SFT eval 和 | floor_ablation_0p3_cka_only_20_v2, floor_ablation_0p5_cka_only_20_v2 |
| D112 | 2026-05-22 | D112: C1 max |Δ| 修正为 1.34pp（含 MBPP），D111 的 1.14pp  | — |
| D111 | 2026-05-22 | C1 quantified upgrade to "universal accuracy-rewar | — |
| D110 | 2026-05-22 | depth-first baseline放appendix作为sanity check，不进主表；c | eval_gsm8k_sft_depth_first_20, eval_gsm8k_grpo_depth_first_20 |
| D109 | 2026-05-22 | Dose-response narrative 修正：纯 inverted-U，α=2.0 无争议  | eval_gsm8k_grpo_rasp_alpha3p0_20_v2 |
| D108 | 2026-05-22 | Dose-response narrative: α=2.0 optimal 为主 claim，GR | eval_gsm8k_sft_alpha3p0_20, eval_gsm8k_grpo_rasp_alpha3p0_20_v2 |
| D107 | 2026-05-22 | D107: α=1.0 数据点修正——55.19%/54.43% 无 registry 溯源，替换为 | eval_gsm8k_sft_rasp_20, eval_gsm8k_grpo_rasp_20_fair, eval_gsm8k_grpo_alpha2p0_20 |
| D106 | 2026-05-22 | D106: α dose-response 揭示非单调 U 型曲线，α=2.0 (66.11%) 超 | eval_gsm8k_grpo_alpha0p5_20, eval_gsm8k_grpo_alpha4_20_v3, eval_gsm8k_grpo_alpha2p0_20 |
| D105 | 2026-05-22 | D105: MF3 Qwen-Math GRPO 启动前修复 prompt 格式——chat tem | sft_qwen_math_cka_only_20, grpo_qwen_math_cka_only_20 |






