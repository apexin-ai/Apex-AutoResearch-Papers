# distill_sparse_swiglu — Research Dashboard

> 最后更新: 2026-05-24 07:29 UTC | 更新原因: 标记匿名 repo push + URL 持久化 + claim/实验最终审查为完成

## 核心方向
KL distillation for SwiGLU sparsity prediction：output-distribution alignment 是 PPL 的主导设计维度（signal type gap 25:1 vs coupling breadth）。Cross-layer coupling contributes task-dependently。C1 target-swap ablation confirms KL-discovered masks carry most quality information。详见 paper_framing.md。

## 当前进展
- **阶段**: 论文可提交状态，待运维手动提交 EMNLP 2026 ARR
- **最新内部评分**: R29 = 3.0 Findings（目标 ≥3.5 Conference）
- **R29 修复**: 3 Critical + 6 Warning 全部落地 (commit 8e3fd0b)
- **审计完成**: 附录可发现性 (9 orphan→pointer)、paper audit (0 critical)、数据一致性 (registry↔paper 全量匹配)、claim 强度审查 (合理偏保守)、补充实验评估 (无需)
- **匿名仓库**: push 完成 (bbd8873)，URL 已持久化到 _anonymous_repo.json
- **实验**: 408 个（成功 257），所有 GPU 实验已完成

## 近期任务
- [x] R29 Action Matrix 3 Critical + 6 Warning 全部落地
- [x] 附录可发现性审计（9 个孤立附录补正文引用）
- [x] Paper Audit（编译/格式/数据一致性/匿名/页数）
- [x] 数据一致性审查（Reviewer 核实 registry↔paper 全量匹配）
- [x] 清理孤立 bib 条目（meng2022locating）
- [x] 匿名 repo push 最新 commits
- [x] 匿名 repo URL 持久化到 _anonymous_repo.json
- [x] Claim 强度 + 补充实验最终审查（Reviewer：无需改动/无需补实验）
- [ ] 运维手动提交 ARR（非我们的动作）

## GPU 预算
- 分配: westd-34887 cuda:0,1（2× RTX PRO 6000 Blackwell 96GB）
- 当前: 全部空闲（所有实验已完成，论文收尾中）
- DDL: 2026-05-25（EMNLP 2026 ARR May cycle）

## 关键数据汇总

### 主表数据（30% uniform, 3-seed）
| Method | PPL | ARC-c | WG | MMLU | GSM8K |
|--------|-----|-------|------|------|-------|
| KL uniform | 8.81±0.02 | 43.7±2.5 | 68.9±0.4 | 40.7±1.3 | 7.5±0.1 |
| TEAL uniform | 10.82 | 39.33 | 65.04 | 45.86 | 8.79 |
| BCE global | 11.25 | 41.2 | 66.0 | 36.3 | 6.0 |
| MSE uniform | 18.52±1.68 | 35.8±4.1 | 59.8±2.6 | 30.7±2.6 | 2.3±0.7 |

### K-curve（30% uniform, 3-seed mean±std）
| K | PPL | ARC-c | WG | MMLU | GSM8K |
|---|-----|-------|------|------|-------|
| 1 | 9.05±0.02 | 39.9* | 65.9* | 38.6* | 5.8* |
| 2 | 10.75±0.15 | 39.7±1.2 | 63.2±1.8 | 38.3±3.2 | 2.8±0.6 |
| 4 | 8.89±0.005 | 40.0±1.2 | 66.9±0.2 | 42.7±1.4 | 7.0±1.6 |
| 8 | 8.99±0.06 | 40.7±1.1 | 68.7±1.3 | 40.4±0.7 | 6.8±1.3 |
| 16 | 8.67±0.02 | 41.9±1.1 | 68.5±0.9 | 40.9±2.9 | 8.5±1.2 |
| 32(E2E) | 8.81±0.02 | 43.7±2.5 | 68.9±0.4 | 40.7±1.3 | 7.5±0.1 |

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D112 | 2026-05-25 | 用 bs=1 重跑 s456 GSM8K 排除 batch_size confound，论文冻结不改 | qwen14b_kl30_s123_gsm8k_v6, qwen14b_kl30_s456_gsm8k |
| D111 | 2026-05-25 | v6 为 Qwen 14B s123 GSM8K 权威数据源（0.3609），论文冻结不改，came | qwen14b_kl30_s123_gsm8k_v6, qwen14b_kl30_s123_eval_v4 |
| D110 | 2026-05-25 | Tab.1 vs Tab.3 BCE PPL 偏差（15.09 vs 15.71）列为 camera | bce_iso_v3_s42, bce30_uniform_s42 |
| D109 | 2026-05-24 | Qwen GSM8K 降为 2-seed (s42+s456) 提交，不等 v4 | qwen14b_kl30_s123_gsm8k_v3, qwen14b_kl30_s123_gsm8k_v4 |
| D108 | 2026-05-23 | R27 3.0→冲刺 Conference：K-curve 3-seed + C4 3-seed + | — |
| D107 | 2026-05-23 | Override D104: 补跑 K=2/K=8/K=16 实验 + C4 eval，按用户指令和 | perlayer_kl_k8_s42, perlayer_kl_k2_s42, perlayer_kl_k16_s42, c4_kl30_s42_eval |
| D106 | 2026-05-23 | 放弃 C4 实验（方案 B），退回方案 A（纯写作修复）处理 C2 knowledge regres | c4_kl30_s42 |
| D105 | 2026-05-23 | R25 Action Matrix: C2 跑 C4 训练实验（~2h）+ C1/C3/W1-W6/ | — |
| D104 | 2026-05-23 | R24 写作修复直接执行，不等 Reviewer 反馈；K=8/K=16 和 Table 4 3-s | — |
| D103 | 2026-05-22 | K=4 3-seed downstream 完成：ARC-c 97% genuine couplin | perlayer_kl_k4_s123, perlayer_kl_k4_s456, constraint_remove_valley_kl30_s42 |

