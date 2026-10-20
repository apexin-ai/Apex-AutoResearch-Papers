# director / loop_21.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_21.md`
- **Structured JSON:** [`f3f901d0f373d7bdf21a.json`](../../sessions/f3/f3f901d0f373d7bdf21a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_messages
updated: '2026-05-25T03:18:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19828 的 cuda:0（`gpu_ids: [0]`，只有 1 张卡）
- C2-s43 需要新建 registry entry，不能复用之前 failed 的 c2_opt13b_a050_s43_fp32
- OPT-1.3B 实验必须用 fp32（之前 fp16 出过 NaN 问题）
- 审稿阶段 GPU 不能空等——C2 完成后立即串行 C1 四组实验

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com)，工作目录 /root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型缓存：/root/autodl-tmp/.hf_cache
- 活跃进程：C2-s42 (c2_opt13b_a050_s42_fp32) PID 32378, cuda:0, cron 监控中
- 待处理 registry entries: 14b_t10_a060_s43, 14b_t10_a075_s43, 14b_t10_a050_s43, t15_a050_s42_fp32, qwen35_dryrun_launch

### 3. 📊 当前状态
Agent 刚完成 session 重启后的状态同步。当前等待 C2-s42 cron 回调（OPT-1.3B α=0.50 seed 42，预计还剩 ~4-5h）。

已完成：R14 写作修复 13/13、FPR 10-seed 全文更新、null_fpr_s51 抢救、C1 prep（iterative_train.py 已验证支持 --intervention_mode）。

RUNNING: c2_opt13b_a050_s42_fp32
排队: C2-s43（等 s42 完成后 cuda:0 重跑），然后 C1 四组实验（GPT-2m pred/react + OPT-1.3B pred/react）

### 4. 📋 待办
- C2-s42 cron 回调（成功）→ Agent 分析结果 + 注册 C2-s43 新 entry → 立即启动 C2-s43
- C2-s42 cron 回调（失败）→ 诊断原因，决定重跑或跳过
- C2-s43 完成 → 汇总 C2 两个 seed 结论（OPT-1.3B 是否复现 Pythia 的 phase diagram 结构）→ 启动 C1 串行
- C1 四组实验全部完成 → 汇总 intervention 效果，更新 paper framing 中 Claim 4
- 审稿报告回传 → 按 review-report-action skill 处理，逐条 Action Matrix

### 5. 🎯 战略上下文
- 项目核心：distributional canary collapse——用分布指标（PermG/SCS）做 model collapse 早期预警
- 当前处于审稿阶段，同时补充 cross-architecture (C2) 和 intervention (C1) 实验
- C2 验证 phase diagram 跨架构泛化（Pythia → OPT-1.3B），C1 验证干预方法有效性
- 论文 217 个实验，154 成功，溯源覆盖率 44/55
- 易错点：OPT-1.3B 之前 s43 因 fp16 NaN failed，必须 fp32；C1 的 iterative_train.py 已经支持 --intervention_mode 但还没实际跑过完整流程
- 只有 1 张卡，所有实验必须串行，排序优先级：C2-s42 → C2-s43 → C1 四组


---
