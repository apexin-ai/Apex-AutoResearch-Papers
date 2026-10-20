# reviewer / loop_8.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`39ed175048fbb250af44.json`](../../sessions/39/39ed175048fbb250af44.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T19:30:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单: cuda:0, cuda:1, cuda:2, cuda:3（autodl-5090 全部 4 张 5090）
- SciERC 4B finetune 已崩溃 3 次（v1 step 10, v2 step 10, v3 OOM on cuda:2）。v4 在 cuda:0 首次成功跑过 step 70+。如果 v4 又崩，排查根因再重试，不要盲目换 GPU 重提
- CoNLL 4B resume 训练（PID 224639, GPU 1, train_config_conll2003_4b_resume.yaml）**未在 registry 注册**——我已报 warning，补注册或等它完成后标 DONE
- 论文 related_work.tex line 10 有 **p>0.39 与 Table 3 p=.29 的内部不一致**——Round 9 review 已报 warning，Paper Agent 尚未修复

### 2. 🖥️ 基础设施快照
- 服务器: autodl-5090(root)，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文 LaTeX: `docs/paper/sections/` (experiments.tex, discussion.tex, appendix.tex 等)
- 模型路径: `checkpoints/qwen3-8b-*-merged*`, `checkpoints/qwen3-4b-conll2003-merged`, `checkpoints/qwen3-4b-scierc-lora/`（4B SciERC 尚未 merge）
- 数据集: `data/scierc/`, `data/conll2003/`
- 无 W&B（report_to: none）
- 活跃进程（截至 handoff）:
  - PID 227128, GPU 0: SciERC 4B finetune v4 (step ~70/585, ~18min remaining)
  - PID 224639, GPU 1: CoNLL 4B resume (step ~4200/4390, <1min remaining, 未注册)
  - GPU 2-3: 空闲

### 3. 📊 当前状态
**刚完成**: Round 9 全文写作评审（已 post，Overall 7/10，8 个 Round 8 Critical 全部 resolved，3 个 warning 待修复）+ 4B CoNLL 推理审查（PASS）+ 3-seed freeform integration 审查（PASS）+ GPU 状态多轮监控。

**Registry 活跃实验**:
- `exp_qwen3_4b_scierc_finetune_v4`: PREPARING→应为 RUNNING, GPU 0, 训练中
- `exp_freeform_seed789_v3`: PREPARING, 推理已完成(samples.jsonl 存在), 缺 ablation_report
- `exp_freeform_seed123`: ANALYZING, metrics 已填充但未标 DONE
- `exp_qwen3_4b_scierc_finetune_v3`: PREPARING/failed

**等待中**: Paper Agent 可能基于 Round 9 review 提交修订版或 Round 10 审查请求。

### 4. 📋 待办（条件触发式）
- SciERC 4B v4 训练完成 → 验证 checkpoint、审查 merge + inference 流程、核对 GPU 合规
- CoNLL 4B resume 完成 → 确认 full 5-epoch model 是否改善推理指标 vs checkpoint-3800 merged（greedy_f1=0.9251 基线）
- Paper Agent 提交 Round 10 审查 → 重点验证: (a) related_work p 值已统一 (b) Table 3 的 2-seed σ 处理 (c) 3-seed freeform 数据是否纳入 appendix
- exp_freeform_seed789_v3 analysis 完成 → 与 v1 metrics 交叉验证一致性
- 任何新实验提交 → 必查 GPU 边界 + registry 注册

### 5. 🎯 战略上下文
- **核心结论**: correlation-selection gap——5 个 confidence signal 都能做 QE（ρ 最高 0.45）但全部无法做 selection（所有 p>0.05）。Gap 有两层原因: instance-level signals 定义上无法 rank candidates；LP 是唯一 per-sample signal 但 within-instance 压缩严重（median range 0.041 nats）
- **D096 scale ablation**: 4B CoNLL 推理已完成，结果 MARGINAL（SJ-FK gap 仅 0.84pp vs 8B 的 3.6pp）。4B SciERC 训练是瓶颈——v4 首次跑过 step 10，成功则补全 scale ablation 证据
- **论文状态**: DDL 2026-05-25。Paper Agent Round 9 修订中。主要剩余弱点: (1) RE 只有 SciERC 一个 benchmark (2) 只有 8B 模型（4B ablation 进行中）(3) free-form ablation 单数据集
- **易错点**: 
  - provenance 中的 p 值 (0.39, 3-seed bootstrap) 与论文 Table 3 (0.29, 2-seed Fisher) 是**不同统计方法**，不是数据错误——但论文内部必须统一
  - RE "40% zero F1" 来自 N=8 (159/397)，provenance 的 44.3% 来自 N=16——不同 N 值，不矛盾
  - exp_freeform_seed789 (v1, DONE) 和 v3 是同一 seed 的重复运行（v3 用 rm -rf 清了旧数据重跑），注意不要当成两个独立 seed


---
