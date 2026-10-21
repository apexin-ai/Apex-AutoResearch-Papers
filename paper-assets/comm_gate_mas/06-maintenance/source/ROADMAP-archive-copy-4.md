# comm_gate_mas — 研究路线图

> 最后更新: 2026-04-30 07:53 UTC | 更新原因: D251: server rename + distilbert_online_e2e failed + bjb2 still blocked

> NeurIPS 2026 **Datasets & Benchmarks Track** | abstract 5/3-4, paper 5/5-6

## 核心叙事（Dissociation finding 主线）

> "Perturbation sensitivity ≠ pruning safety: ack messages show highest perturbation sensitivity yet are safe to prune in aggregate — this dissociation holds consistently across 7B-class models (Qwen2.5-7B, Llama-3.1-8B), with preliminary evidence of scale consistency at 72B."

**定位**: Empirical finding paper with reusable analysis protocol

## 当前状态

**补充实验阶段 — 带 kill switch 的有限窗口实验**

双 backbone × 双任务矩阵完成 (D243)，Provenance 79/79。Reviewer 2×PASS。
匿名仓库 zip 已就绪，待手动上传。等待 R2/R3 二审报告。

| | GSM8K | StratQA |
|--|-------|---------|
| Qwen | Δ=-0.05±0.99 (10-seed) | Δ=+0.70±0.91 (5-seed) |
| Llama | Δ=+2.20±1.44 (5-seed) | Δ=+2.81±3.94 (8-seed) |

## ⏰ Kill Switch (D248)

**硬截止: 2026-05-01 18:00 UTC**

任何未完成实验在此时间后**立即降级为 future work**，不再 debug。
论文已有 130 实验 + 2×PASS + 79/79 provenance，补充实验是锦上添花不是必要条件。
5/1 18:00 后全部精力转 paper finalization。

## DDL 倒推时间线

| 日期 | 里程碑 |
|------|--------|
| 4/30 ✅ | R1 Reviewer PASS + 匿名仓库 zip + 72B 术语修正 |
| **4/30-5/1 18:00** | **补充实验窗口（3 GPU 并行，硬截止）** |
| 5/1 18:00 | ⏰ Kill switch — 未完成实验 → future work |
| 5/1-5/2 | 补充实验结果写入论文（仅已完成的） |
| 5/1 | 二审报告 R2/R3 处理 |
| 5/3 | P0 匿名仓库上传 |
| 5/3-4 | Abstract deadline |
| 5/5-6 | Paper deadline |

## 补充实验计划（Batch 1，3 GPU 并行，优先级排序）

| 优先级 | ID | 实验 | GPU | 状态 | 假设 |
|--------|-----|------|-----|------|------|
| **P1** | EXP-A | Online DistilBERT E2E 验证 | westb-28993 cuda:1 | ❌ FAILED（待诊断+重试） | DistilBERT 在线分类 ≈ oracle pruning safety |
| **P2** | EXP-B | Gemma-2-9B-it heuristic pruning | bjb2-10838 cuda:0 | ⏸ BLOCKED（bjb2 SSH 不可达） | Dissociation 泛化到第三模型家族 |
| **P3** | EXP-C | 3-agent 拓扑 oracle 验证 | bjb2-10838 cuda:1 | ⏸ BLOCKED（bjb2 SSH 不可达） | Dissociation 在多 agent 拓扑成立 |

**阻塞项**: bjb2 SSH 端口可能变更，已通知用户查 AutoDL 控制台。

## 审稿状态

- **R1**: Borderline Accept (4/10), 2 critical + 1 major。待综合报告后统一处理
- **R2/R3**: 4/29 17:30 开始审稿，尚未返回报告（可能 session 过期）

## Finalization 任务

| 优先级 | 项目 | 状态 |
|--------|------|------|
| **P0** | 匿名仓库上传 | zip 就绪，待手动上传 |
| **P0** | 补充实验 Batch 1 | EXP-A 失败待重试，EXP-B/C blocked |
| P1 | 补充实验结果写入论文 | 待实验完成 |
| P2 | 二审报告处理 | 等待 R2/R3 |

## GPU 分配（服务器已重命名 D251）

| 服务器 | GPU | 用途 | 状态 |
|--------|-----|------|------|
| westb-28993 | cuda:1 | EXP-A: DistilBERT online E2E | 空闲（实验失败） |
| bjb2-10838 | cuda:0 | EXP-B: Gemma heuristic pruning | SSH 不可达 |
| bjb2-10838 | cuda:1 | EXP-C: 3-agent oracle | SSH 不可达 |

## 实验总结

135 个实验（125 DONE + 0 RUNNING + 10 pending）。

## 进展摘要

1. D243: 双 backbone 矩阵四格 non-inferior
2. D246: 2×Reviewer PASS
3. D247: 匿名仓库 + 72B 术语修正完成
4. D248: Reviewer WARNING 处理 — 全实验设 5/1 18:00 UTC kill switch
5. D250: EXP-B 从 DeepSeek 改为 Gemma-2-9B-it（DeepSeek 是 Qwen 蒸馏）
6. D251: Server 重命名（westb-4x6000-a→westb-28993, bjb2-4x5090-b→bjb2-10838）+ distilbert_online_e2e 失败

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D252 | 2026-04-30 | Priority reshuffle: EXP-B (Gemma) migrate to westb | gemma_heuristic_gsm8k, distilbert_online_e2e, three_agent_oracle |
| D251 | 2026-04-30 | EXP-A DistilBERT online E2E: invest 6-8h code inte | distilbert_online_e2e |
| D250 | 2026-04-30 | EXP-B 模型从 DeepSeek-R1-7B 改为 Gemma-2-9B-it — DeepSe | deepseek_r1_7b_dissociation |
| D249 | 2026-04-30 | EXP-B 模型从 DeepSeek-R1-Distill-Qwen-7B 改为 Gemma-2-9 | deepseek_r1_7b_dissociation |
| D248 | 2026-04-30 | Reviewer WARNING 处理: EXP-B 选 DeepSeek-R1-7B (非 Mis | — |
| D247 | 2026-04-30 | 用户要求继续补实验，规划 3 组并行：EXP-A DistilBERT online E2E / E | — |
| D246 | 2026-04-30 | Reviewer PASS on R1 writing modifications — 6/6 it | — |
| D245 | 2026-04-29 | Paper finalization 优先级重排：P0 匿名代码仓库（D&B programmati | — |
| D244 | 2026-04-29 | 释放 westb cuda:1，项目进入 paper finalization 等待审稿报告 | qwen_heuristic_stratqa_4seed |
| D243 | 2026-04-29 | Qwen StratQA 5-seed 完成 (Δ=+0.70±0.91pp)，论文全面更新，双 b | qwen_heuristic_stratqa_4seed, qwen_heuristic_stratqa, online_stratqa_qwen |

