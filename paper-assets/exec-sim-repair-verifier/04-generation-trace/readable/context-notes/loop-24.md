# agent / loop_24.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_24.md`
- **Structured JSON:** [`68a4e2b2352695ed39af.json`](../../sessions/68/68a4e2b2352695ed39af.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: idle_timeout
updated: '2026-05-17T18:15:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud-westd-4x5090 的 GPU 分配：cuda:0 (deepseek-cls-repo-v4), cuda:1 (deepseek-cwm-repo), cuda:2 (deepseek-cls-repo-s123), cuda:3 (deepseek-cwm-repo-s123)——4/4 满载，不可抢占
- home-1x5090 只有 1 张 GPU (cuda:0)，当前无 RUNNING 实验，可用于 eval/analysis 任务
- DeepSeek repo 训练是 blocking 任务（填 Table 4 TBD + 确定 C2 narrative），不可中断/kill
- EMNLP 2026 ARR May 25 DDL，剩余 **8 天**，Abstract/Intro/Conclusion 等 DeepSeek 结果后才能统一更新到 D116 framing
- 参数修改（seq_length/bs/precision/lr）需 Director 审批（feedback memory D103）

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**: 工作目录 `/root/exec-sim-repair-verifier`，4x5090 全部 RUNNING DeepSeek repo-level 训练
  - 磁盘: `/usr/bin/nvidia-smi` 436G/879G 可用 (48%), `/autodl-pub` 5.3T/7.3T 可用
- **home-1x5090**: 工作目录 `/home/sonny/exec-sim-repair-verifier`，account=sonny，1x5090
  - 用于 Qwen TRAJ 8B 训练 + eval 任务
  - W&B project: exec-sim-repair-verifier（entity 从 project config 取）
- 活跃 cron 监控（reconcile 确认）:
  - deepseek-cwm-repo (pid=479953, cuda:1)
  - deepseek-cls-repo-v4 (pid=548885, cuda:0)
  - deepseek-cls-repo-s123 (pid=542509, cuda:2)
  - deepseek-cwm-repo-s123 (pid=542901, cuda:3)

### 3. 📊 当前状态
- **刚做的事**: 收到 qwen3-8b-traj-func-s42 完成 cron 回调，补齐了 registry 状态链 PREPARING→QUEUED→RUNNING→ANALYZING，已派 Worker `worker_analysis_qwen3-8b-traj-func-s42_20260517T141256` 去 SSH 读日志 + 查 W&B + 判定 conclusion
- **等待中的 Worker 回调**: `worker_analysis_qwen3-8b-traj-func-s42_20260517T141256`——**这是最高优先级**，回调到手后需要：更新 registry→DONE, 刷 report.md, 汇报 Director（含资源行），判断 TRAJ 8B 数据对 Table 2 scaling 分析的影响
- **RUNNING 实验** (4 个，全在 seetacloud):
  - deepseek-cls-repo-v4 (s42): DeepSeek CLS repo-level，填 Table 4
  - deepseek-cwm-repo (s42): DeepSeek CWM repo-level，填 Table 4
  - deepseek-cls-repo-s123: DeepSeek CLS repo-level seed 123, multi-seed evidence
  - deepseek-cwm-repo-s123: DeepSeek CWM repo-level seed 123, multi-seed evidence
- **PREPARING** (3 个): qwen3-8b-traj-func-s123, deepseek-traj-func-v2-s123-fixed, deepseek-traj-func-v2-fixed
- **Paper Agent 正在处理**: 6 项 Round 1 issue 修复 (R1-W4, R1-W2, R1-W5, R2-W5, R1-M3, R1-M1)

### 4. 📋 待办（条件触发式）
- Worker `worker_analysis_qwen3-8b-traj-func-s42` 回调 → 读 conclusion：
  - success (test_acc ≈ 87-88%) → 更新 Table 2 TRAJ 8B 行, 汇报 Director, 判断是否需要 s123 seed 复现
  - negative (低于 4B 86.30%) → 汇报 Director 证伪分析 + 文献联动, 不动 paper
  - failed → 读日志诊断, 修复后重提交到 home-1x5090
- qwen3-8b-traj-func-s42 成功 → 立即提交 qwen3-8b-traj-func-s123（home-1x5090 cuda:0 可用）
- deepseek-cls-repo-v4 / deepseek-cwm-repo 完成 → eval → 填 Table 4 DeepSeek TBD cells
- 4 个 DeepSeek repo 全部完成 → 确定 C2 narrative (Path A tokenizer-specific vs Path B model-agnostic) → 更新 Abstract/Intro/Conclusion 到 D116 framing
- Paper Agent 6 项修复完成 → 汇总审查一致性, 等 DeepSeek 结果后统一提交 Round 2

### 5. 🎯 战略上下文
- **核心 framing (D116)**: Design space characterization——何时用 CLS, 何时用 CWM, 取决于 tokenizer/complexity
- **C2 claim (D115)**: 放弃全局单调序 CLS≥CWM≥TRAJ, 改为 complexity-dependent divergence (tokenizer-specific, D119 已验证)
- **Re-repair (D120)**: DROPPED, genuine negative, 不再追
- **关键数字**: Qwen3-8B CLS 89.40±1.09%, CWM 86.96±0.50%; DeepSeek CLS func 86.85±0.11%, CWM func 86.83±1.49%, TRAJ func 84.16±1.30%
- **易错点**: 
  - qwen3-8b-traj-func-s42 的 Worker 分析回调是当前最紧急的——不要忽略它去做别的
  - TRAJ 8B 结果直接影响 Table 2 scaling narrative：如果 TRAJ 不 scale（与 CLS/CWM 不同），这本身也是有价值的发现（formulation-dependent scaling），需要调整 claim 措辞
  - DeepSeek repo 结果是最后的 blocking 数据点，到手前不要动 Abstract/Intro/Conclusion
  - Dream Round 1 行动项 A1-A6 已全部完成，剩余是写作修复和 DeepSeek 数据


---
