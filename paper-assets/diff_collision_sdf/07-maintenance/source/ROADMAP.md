# diff_collision_sdf — Research Dashboard

> 最后更新: 2026-05-30 03:56 UTC | 更新原因: D050 模拟审稿后明确 Accept 路径 + M5 引用完成

## 核心方向
VLA safety 评估 CAR 被 fake safety 污染 + SDF avoidance attribution 分析。详见 paper_framing.md。

## 当前进展
- **阶段**: Post-DDL，ICRA 2027 准备（DDL ~Sep 2026）
- **模拟审稿**: D050, 5.5/10 Borderline → 做到 3 选 2 即可升至 7/10 Accept
- **论文**: ICRA 双栏定稿，6 项 offensive 升级 + novelty framing 强化 + He2025 action memorization 引用，27 篇引用，编译 clean
- **审稿**: 已提交 Review Director（apr_20260530T002444_1cx4），等用户确认
- **代码**: 全部就绪（标注脚本 + RoboCasa eval + config + recovery checklist）
- **写作**: 全部非 GPU 工作结束——等服务器恢复执行 Accept 路径实验

## Accept 路径（D050，三选二即可 5.5→7.0）

| # | 任务 | 成本 | 效果 | 状态 |
|---|------|------|------|------|
| 1 | Pi0.5 baseline +2 seeds | 10 GPU-hrs | 封堵 W2（唯一无 error bar 的核心数字）| Recovery Phase 1 |
| 2 | Demo curation pilot 1 ratio | ~40 GPU-hrs | 从"诊断"升级为"诊断+初步验证" (W3) | Recovery Phase 2→2b |
| 3 | RoboCasa action collapse 验证 | ~50 GPU-hrs | 第二 benchmark (W1) | Recovery Phase 3+ |

**关键洞察**: Phase 2 标注输出自动包含 per-task collision-free 比例（Q3），直接验证 "avoidance from demos" 假说。标注完成后立即启动 1-ratio curation pilot（仅用 100% CF demos 训练 1 seed），~40 GPU-hrs 即可获得初步正向证据。

## 可信 Reeval 数据汇总（seed=7, 200ep, rotation-fixed v2）

| 模型 | Seeds | CAR | TSR | SSR |
|------|-------|-----|-----|-----|
| Pi0.5 baseline | 1 | 28.5% | 71.5% | 0.39 |
| LoRA-only 30K | 3 | 54.83%±2.25 | 49.7%±3.2 | 0.54 |
| SDF λ=0.005 30K | 3 | 54.5%±2.29 | 54.0%±3.0 | 0.51 |
| SDF λ=0.01 30K | 3 | 56.33%±1.61 | 53.8%±1.5 | 0.56 |
| SDF λ=0.1 30K | 3 | 57.00% | — | — |
| Pi0.5 LoRA oracle | 1 | 51.9% | 50.6% | — |

## 服务器恢复后执行计划

| Phase | 任务 | 耗时 | 目标 |
|-------|------|------|------|
| 0 | SSH + GPU + 磁盘验证 | 5min | — |
| 1 | Pi0.5 baseline eval seed42+99 | 2.5h | Accept 路径 #1 |
| 2 | Demo collision-free 标注 | 10min | per-task CF rate (Q3) |
| 2b | 100% CF demos → 1-seed curation pilot | ~40h | Accept 路径 #2 |
| 3 | RoboCasa 环境搭建 + action collapse eval | ~50h | Accept 路径 #3 |

Phase 1+2 同时启动。Phase 2b 依赖 Phase 2 标注结果。

## 基础设施
- **westd-35807/45947**: 离线
- **Feishu API**: 6/1 重置
- 137 实验：136 DONE + 1 PREPARING

## 近期任务
- [x] 论文定稿 + Reviewer 全 PASS + negative results 安全
- [x] Recovery checklist（art_20260530_cb35b7）
- [x] 引用补充（M5, 3 篇已添加：Khatib 1986 + Singletary 2022 CBF + Zhao 2020 sim2real）
- [ ] 审稿 review mode 确认 — 等用户
- [ ] 标题决策 — 等用户
- [ ] 服务器恢复后执行 Accept 路径

## GPU 预算
- 分配 2 张 — 均不可达
- Accept 路径最小投入：10 + 40 = 50 GPU-hrs（#1 + #2）
- 全部投入：10 + 40 + 50 = 100 GPU-hrs（#1 + #2 + #3）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D050 | 2026-05-30 | 模拟审稿 5.5/10 Borderline——Accept 路径明确：Pi0.5 baseline | eval_oracle_pi05_lora_s0, eval_a1_lora_object_v11_rerun |
| D049 | 2026-05-29 | Reviewer 证据链审查后调整 ICRA ablation 优先级——Pi0.5 baselin | eval_oracle_pi05_lora_s0, eval_multiseed_lora_s0_eseed0, eval_multiseed_sdf_l01_s0_eseed42 |
| D048 | 2026-05-29 | D048: ICRA 路线图重组——P1 SDF-as-obs 降级为 P3，P2 full-bod | — |
| D047 | 2026-05-29 | D047: 方法改进战略——Demo curation 为 P0 必做方向，SDF-as-obser | — |
| D046 | 2026-05-29 | D046: CoRL 2026 DDL 已过（5/28 AoE = 5/29 11:59 UTC）， | — |
| D045 | 2026-05-29 | D045: 批准 Pi0.5 LoRA Oracle-adaptive eval — 封堵 Clai | — |
| D044 | 2026-05-28 | D044: 审稿回应策略——写作级修复 + 统计重分析，Claim 3 降级，scope 收窄到 S | — |
| D043 | 2026-05-28 | D043: λ=0.1 s2 CAR=54.5% → 3-seed p_one=0.0714 → S | eval_pi05_a1_30k_s0_l01_high, eval_pi05_a1_30k_s1_l01_high, train_pi05_a1_obj_s2_l01_high |
| D042 | 2026-05-28 | D042: 全表统一用 reeval 数据——LoRA TSR=51.5±0.0, baseline | reeval_lora_s0_30k_v2, reeval_lora_s1_30k, eval_lora_s2_30k_v2 |
| D041 | 2026-05-27 | D041: 统计检验策略——正文用双尾 permutation test（保守），脚注提供单尾 +  | eval_lora_s2_30k_v2, eval_pi05_a1_30k_s0_l01_high, eval_pi05_a1_30k_s1_l01_high |


