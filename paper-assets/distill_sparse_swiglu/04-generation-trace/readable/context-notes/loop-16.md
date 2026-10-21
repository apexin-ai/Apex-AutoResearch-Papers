# agent / loop_16.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`06e1ce1dd459e37fc2ca.json`](../../sessions/06/06e1ce1dd459e37fc2ca.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-24T00:40:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-34887 cuda:0,1（2× RTX PRO 6000 Blackwell 96GB）。westd-41718 已由用户释放，不可使用
- DDL 2026-05-25 EMNLP 2026 ARR May cycle，当前阶段是 R24 写作修复，不需要新实验（D104/D106 已决策）
- D107 override: 用户指令补跑 K=2/K=8/K=16 + C4 eval，这批是最后的实验补充
- perlayer_kl_k2_s42_train 是 perlayer_kl_k2_s42 的重复条目，Worker 应将其标记为 killed/duplicate

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887，工作目录 /root/distill_sparse_swiglu
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- 模型：llama-3.1-8b（具体路径在服务器 /root/distill_sparse_swiglu/ 下）
- Checkpoint 目录：/root/distill_sparse_swiglu/checkpoints/
- 日志目录：~/runs/distill_sparse_swiglu/
- WANDB_MODE=disabled（K-curve 实验均禁用 W&B，指标从训练日志读取）
- 活跃进程：perlayer_kl_k16_eval_final2 (PID 114997, RUNNING, reconcile 确认存活)

### 3. 📊 当前状态
- perlayer_kl_k2_s42 刚完成训练，CRON 已转 ANALYZING。我派了 Worker `worker_analysis_perlayer_kl_k2_s42_20260523T055755` 去读日志、提取指标、更新 registry。**Worker 回调尚未到达**
- perlayer_kl_k16_eval_final2：RUNNING（K=16 downstream eval，用 Reviewer-verified command，前几次 eval 均 failed）
- Paper Agent 正在执行 R24 写作修复（C1/C2/W3/W6/Minor 项）
- K-curve 已有数据：K=1 PPL=9.0568, K=8 PPL=8.9704, K=32(joint) PPL=8.8157。K=4 PPL 未在 registry 中（需从日志补录）

### 4. 📋 待办
- Worker `worker_analysis_perlayer_kl_k2_s42` 回调到达 → 读取 K=2 PPL/KL/sparsity 指标 → 更新 registry → 汇报 Director K-curve 进展
- perlayer_kl_k16_eval_final2 cron 回调 → 分析 K=16 downstream eval 结果（前 3 次 eval 都 failed，这是最后尝试）
- K=2 训练完成后需要跑 downstream eval（ARC-c/WG/MMLU/GSM8K/HS/PIQA），与 K=1/K=4/K=8 对齐
- Paper Agent R24 写作修复完成 → submit_paper_to_review continue mode 验证 → R25 通过后提交最终版本
- K-curve 全部数据收集完成后 → 更新 paper Table/Figure（K-curve 趋势图）

### 5. 🎯 战略上下文
- 核心结论：KL distillation 是 PPL 的主导设计维度；cross-layer coupling 贡献 task-dependent（commonsense 任务 coupling-dominated，reasoning 任务 mismatch-dominated）
- K-curve 是 D107 的核心产出：{K=1,2,4,8,16,32} 量化 coupling scope 对质量的影响。预期趋势是 K↑ → PPL↓（更多 cross-layer 信息），但可能存在饱和点
- 易错点：K=4 的 PPL 数据不在 registry metrics 中（metrics 为空），需要从服务器日志补录才能画完整 K-curve
- K=16 eval 已连续 failed 3 次（EXIT_CODE=127/1），perlayer_kl_k16_eval_final2 是第 4 次尝试，如果再 fail 需要向 Director 汇报放弃
- perlayer_kl_k2_s42_train 是重复条目，必须清理（标记 killed + duplicate 备注），否则 report.md 会显示两个 ANALYZING 的 K=2 实验造成混乱


---
