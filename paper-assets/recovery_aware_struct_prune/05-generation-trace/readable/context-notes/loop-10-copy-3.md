# reviewer / loop_10.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`54509b515fc897edb8b9.json`](../../sessions/54/54509b515fc897edb8b9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-16T10:11:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-23072 只能用 cuda:0, cuda:1（C001 约束）
- westd-11672 只能用 cuda:0, cuda:1（C003 约束）
- DeepSeek 系列剪枝 calibration=512，Qwen-Math 系列 calibration=256——混用会导致 ~5% group selection 差异，论文需一致报告
- 服务器全名必须带端口后缀：westb-23072, westd-11672（ssh 工具不接受简写）
- Reviewer 只读：只用 ssh_read_only / read_registry / tail_logs / fetch_wandb_metrics，唯一输出渠道 reviewer_post_to_director

### 2. 🖥️ 基础设施快照
- **westb-23072**: root, /root/recovery_aware_struct_prune (代码), /root/autodl-tmp/recovery_aware_struct_prune (数据/模型/结果)
  - Python: /root/miniconda3/bin/python, conda base
  - 磁盘: 179G/250G (72%), 清理后有 72GB 余量
  - 结果文件: /root/autodl-tmp/recovery_aware_struct_prune/results/
  - 30% 剪枝模型: pruned_rasp_30/, pruned_standard_30/
- **westd-11672**: root, 同上路径结构
  - Qwen-Math 模型: /root/autodl-tmp/models/Qwen2.5-Math-7B
  - 剪枝模型: pruned_qwen_math_rasp_20/, pruned_qwen_math_standard_20/
  - SFT 完成: sft_qwen_math_rasp_20/ (12.34GB), sft_qwen_math_standard_20/ (12.29GB)
  - CKA/importance scores: cka_scores_qwen_math.pt, importance_scores_qwen_math.pt
- **本地 workspace**: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/
- **W&B**: 未确认是否配置（之前检查跳过了 W&B）
- **活跃进程（截至 handoff 前）**:
  - westb GPU 0: eval_sft_rasp_25 (PID 602990, ~1h 运行中)
  - westb GPU 1: eval_sft_standard_25 (PID 598084, ~2.5h 运行中)
  - westd: 双卡空闲（Qwen-Math SFT 已完成）

### 3. 📊 当前状态
**刚完成的审查**:
- fig2_reward_accuracy.pdf: PASS，数据与 registry 精确匹配
- fig3_collapse_dynamics.pdf: PASS，标注值验证通过
- method.tex: **CRITICAL**——RLVR 动机与实验结论矛盾（RASP "优化 RLVR 可恢复性"但实验证明 RASP 对 RLVR 有害）
- introduction.tex: **CRITICAL**——"Redundancy Paradox" 定义与 RASP 公式行为相反（intro 说保留高 overlap，公式说剪除高 overlap）；Self-Healing 引用与 C1 矛盾
- prune.py rasp-rlvr 模式代码: PASS，S=I×F^α 实现正确
- 30% 剪枝 (RASP+Standard): PASS

**Registry RUNNING/PREPARING/QUEUED**:
- eval_sft_rasp_25: RUNNING, westb cuda:0 — C3 关键数据点（25% RASP SFT accuracy）
- eval_sft_standard_25: RUNNING, westb cuda:1 — C3 关键数据点
- eval_postprune_standard_25: RUNNING（但进程已死 PID 601607，westd 有旧结果 16%，需决定是否重跑）
- sft_rasp_20_qwen_math: RUNNING（实际已完成，registry 未更新）
- sft_standard_20_qwen_math: RUNNING（实际已完成，registry 未更新）
- eval_sft_rasp_qwen_math: PREPARING
- eval_sft_standard_qwen_math: PREPARING
- grpo_rasp_25 / grpo_standard_25: PREPARING
- grpo_rasp_qwen_math / grpo_standard_qwen_math: PREPARING
- prune_rasp_25_qwen_math: QUEUED
- prune_rasp_rlvr_20: QUEUED → sft_rasp_rlvr_20: PREPARING

### 4. 📋 待办（条件触发式）
- eval_sft_rasp_25 完成 → 核实 accuracy（旧 westd 中间值 ~56.67% at 150/1319），与 eval_sft_standard_25 对比计算 25% SFT gap，验证 C3
- eval_sft_standard_25 完成 → 同上，两个结果凑齐后做 z-test 看 25% gap 是否比 20% (2.2pp, p=0.25) 更显著
- Qwen-Math eval 启动 → 检查 GPU 合规 (westd cuda:0/1)，核实模型路径指向已完成的 SFT 输出
- GRPO 25% 启动 → 重点监控 collapse 时间点，与 20% 数据对比（RASP 预期更早 collapse）
- prune_rasp_rlvr_20 完成 → 核实 pruning_metadata，检查 F≈0 结构是否被不当剪除（edge case）
- method.tex / introduction.tex 修订版提交 → 重审 RLVR framing 是否已修正
- Director 转发 Framing 调整提案 → 立即 Read negative-framing-review skill，四维度审查

### 5. 🎯 战略上下文
**核心叙事（D044/D045 pivot 后）**: Redundancy-Stability Tradeoff——SFT 和 RLVR 对结构冗余有相反需求。RASP 不是万能方法而是诊断工具。

**三个 Core Claims**:
- C1: GRPO reward-accuracy decoupling 是 universal（所有模型 Δ≤0.84pp n.s.）——最强
- C2: Collapse severity gradient（RASP step10 < Standard step60 < Unpruned stable）——强
- C3: Recovery method conditions optimal pruning（SFT gap 2.2pp p=0.25）——最弱，25% 数据是救命稻草

**最容易判断错的事**:
1. **Introduction/Method 的 RLVR framing 是错的**——当前写的是"RASP 优化 RLVR 可恢复性"，实际实验证明相反。如果修订版提交审查，必须验证这个矛盾是否已修正，不能只看文字流畅度就 PASS
2. **Registry 大面积过时**——多个实验实际完成但 registry 仍 RUNNING。审查前必须 ssh 独立核实进程状态，不能信 registry status
3. **RASP-RLVR 是新增第四种剪枝条件**——如果 RASP-RLVR + GRPO 不 collapse，这将大幅强化论文 story；如果也 collapse，则 tradeoff 叙事需要调整
4. **eval_postprune_standard_25 处于薛定谔状态**——registry RUNNING 但进程死了，westd 有旧结果 (16%)，westb 无结果。需要 Director 决策


---
