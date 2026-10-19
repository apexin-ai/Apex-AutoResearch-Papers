# reviewer / loop_14.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`3b7f9acca9e3fc45cb58.json`](../../sessions/3b/3b7f9acca9e3fc45cb58.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-25T05:40:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34887 仅 cuda:0, cuda:1。越界进程立即 CRITICAL + 要求 kill
- 论文 DDL：2026-05-25 EMNLP 2026 ARR May cycle。论文内容已冻结，待运维手动提交
- Abstract ≤ 200 words（当前 181），正文 ≤ 8 页（当前刚好 8 页）
- Reviewer 角色只读：不执行实验、不修改文件，唯一输出渠道 `reviewer_post_to_director`

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，代码根目录 /root/distill_sparse_swiglu/
- Python：/root/miniconda3/bin/python（conda base 环境，非 venv）
- 模型：LLaMA-3.1-8B, Mistral-7B-v0.3, Qwen-2.5-14B（路径在 /root/autodl-tmp/models/）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/
- 活跃进程：无。GPU 全部空闲。所有实验已完成

### 3. 📊 当前状态
论文处于可提交状态。我本轮完成了：
1. Registry↔paper 全量数据一致性独立审查（所有核心数字验证通过）
2. ROADMAP 更新审查（R29 修复全部在 LaTeX 中验证落地）
3. R29 Action Matrix 独立评估（采纳了 Diagnostic/Practical labels、CIs→directional、confirming→suggesting 等建议）
4. 补充实验评估（结论：无需）+ Claim 强度审查（合理偏保守）
5. Revision 预跑方案评估 — 发现 ste_30_s42 异常（PPL 8.41 优于 KL 8.81，需 Agent 查 eval 配置）
6. MSE LR sweep 结果审查：LR=2e-4 PPL=15.17, LR=1e-4 PPL=17.50（vs KL 8.81）— rebuttal 弹药就绪

Registry: 0 RUNNING, 0 PREPARING。最近完成：mse30_lr2e4_s42 (DONE/failed), mse30_lr1e4_s42 (DONE/failed)。
等待：无 Worker/Cron 回调。等运维手动提交 ARR。

### 4. 📋 待办（条件触发式）
- Director 回复 ste_30_s42 调查结果 → 如果是 TEAL-forced 30% 且 PPL 确实 8.41：需要确认 ablation table 是否需要补报此数据点，33.8% improvement claim 需限定为 "at 50%"
- MSE LR sweep metrics 未录入 registry → 提醒 Agent 补录（mse30_lr2e4_s42: PPL=15.17, sparsity=0.291; mse30_lr1e4_s42: PPL=17.50, sparsity=0.292），conclusion 改 "negative" 而非 "failed"
- ARR 提交后收到 reviewer feedback → 启动 rebuttal 审查模式
- Tab.1 vs Tab.3 BCE 4.8σ 偏差 → 建议加 footnote 说明不同 BCE 版本（bce_iso_v3 vs bce_30），尚未执行

### 5. 🎯 战略上下文
核心结论：KL output-distribution alignment 是 SwiGLU sparsity prediction 的主导设计维度。PPL 14.5% improvement over TEAL at 30%，cross-architecture verified (Mistral -17.3%, Qwen 14B)。知识任务回归是已知 trade-off。

易错点：
- **ste_30_s42 是个地雷**：registry 中存在未报告的 STE 30% 实验，PPL 8.41 优于 KL 8.81。eval 命令在 registry 中被截断（"..."），跑在已不可达的 westd-41718。如果 reviewer 问 "STE + TEAL at 30%?" 需要有答案。Agent 尚未回复调查结果
- **report.md 严重过时**：仍列 qwen14b v4 为"准备中"，趋势数据也过时。不要依赖 report.md 判断项目状态
- **D109 已被 supersede**：决策记录说 "Qwen GSM8K 降为 2-seed" 但 v4 后来成功，论文已用 3-seed（32.2±5.3）
- **MSE LR sweep 结果是 rebuttal 弹药不是论文修改**：tuned MSE (15.17) ≈ BCE (15.09) 但仍 72% 落后 KL (8.81)。Limitations 当前措辞准确，不需要改


---
