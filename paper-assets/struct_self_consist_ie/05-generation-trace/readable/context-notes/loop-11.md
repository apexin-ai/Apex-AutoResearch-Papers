# director / loop_11.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`925e3f01db810a3ebeb7.json`](../../sessions/92/925e3f01db810a3ebeb7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-21T23:01:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0-3 + autodl-5090-c cuda:0-3，共 8 张，不得使用其他服务器/卡
- MV 统一用 strict threshold >N/2（N=8 时需 ≥5 票），整个项目一致，不得混用 inclusive ≥N/2
- FewNERD finetuned MV Δ 论文当前引用 -2.74±0.54pp（原始数据），v3 re-runs 给出 -2.44pp（s123=-2.63, s456=-2.24），s42_v3 完成前不切换数据源
- 5-epoch MV Δ 不可描述为"improvement"——26% degeneracy 使 MV≡greedy，aggregate Δ shrinkage 是稀释效应，非真实改善
- N=16 FK conditional rho 有 sign flip（mean=0.051±0.062），论文不得引用 N=16 FK conditional
- 论文已进入审稿阶段（Review Group C），Director 不参与投稿材料/格式，只管研究实验

### 2. 🖥️ 基础设施快照
- **autodl-5090**: connect.bjb1.seetacloud.com, /root/autodl-tmp/struct_self_consist_ie, 磁盘 91%⚠️ 需清理
- **autodl-5090-c**: connect.westb.seetacloud.com, /root/autodl-tmp/struct_self_consist_ie, 磁盘 72%
- Python: /root/miniconda3/bin/python（conda base）
- FewNERD finetuned model: qwen3-8b-fewnerd-exp021-merged（5090 上有嵌套子目录的 tokenizer，5090-c 环境 confirmed-working from s456_v3）
- 活跃进程：mf4v2_s42_v3 在 5090 cuda:0（~78% 进度，约 25 min 前检查），其余 7 卡空闲
- 论文源码：projects/struct_self_consist_ie/docs/paper/（本地 workspace，非远程）

### 3. 📊 当前状态
**刚做完**：
- 5-epoch s42/s123/s456 MV results 全部持久化 ✓
- Kill mf4v2_s42_v4 (5090-c cuda:0) + pretrained_s42_v2 (5090-c cuda:3) ✓
- Paper Agent per-type flip patch 完成（7/8 types direction flip 整合到 appendix + main text + discussion）✓
- Round 33 审稿已提交（approval_id: apr_20260521T220622_m50z，含 per-type flip 最完整版本）
- ROADMAP 全面更新至 final polish 阶段 ✓

**RUNNING**：mf4v2_s42_v3 (5090 cuda:0)，完成后需 MV recompute → 3-seed provenance 最后一块
**等待**：Round 33 审稿结果；mf4v2_s42_v3 worker 回调

### 4. 📋 待办
- mf4v2_s42_v3 完成 → 立即 MV recompute，保存 recompute_mv_results.txt → 3-seed provenance 验证完毕
- v3 3-seed mean 计算完毕 → 对比原始 -2.74±0.54pp，决定是否更新论文数字（差异不大可能保持原始）
- Round 33 审稿报告到达 → 按强制协议处理（Holistic Pass → Action Matrix → post_to_reviewer → 派 Agent/Paper Agent）
- 5090 磁盘 91% → v3 完成后清理临时文件降到 85% 以下
- DDL 5/25 (~3.5 days) → R33 修复完成后做 final compile + submission prep

### 5. 🎯 战略上下文
- **核心结论**：Agreement signals correlate with quality (ρ up to 0.47) but MV fails to improve selection in finetuned NER models（correlation-selection gap）。Pretrained MV works on all 3 datasets，finetuned MV fails on FewNERD/SciERC。7/8 per-type direction flip 是排除 baseline quality confound 的决定性证据。
- **叙事演变**（D232→D233）：从"finetuning-induced degeneracy"转向"finetuning decouples agreement from quality through dataset-dependent pathways"——CoNLL 是 diversity elimination，FewNERD 是 correlated error patterns
- **目标**：3.5-4.0 (Borderline Conference → Conference)，D225
- **R30 所有 weakness 已修复**：SciERC 3-seed, RE/SQL downgrade, Prop 1 repositioning, causal language, 5-epoch confound, per-type flip
- **易错点**：(1) 不要把 v3 re-run 数字和论文原始数字混用——当前论文用原始数据，s42_v3 完成前不改 (2) Conclusion 只有 1 句，R30 曾说太短但页面预算紧张，不要轻易加内容 (3) 实验程序本质完成，不要为填 GPU 发明 make-work 实验 (4) 49 页 appendix 可能被 R33 指出过长，准备精简方案


---
