# agent / loop_1.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`bf3a293e43af10a49c03.json`](../../sessions/bf/bf3a293e43af10a49c03.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T23:31:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0, cuda:1 on westd-16980。禁止在白名单外 GPU 启动实验，即使 Director 指令也必须 push back
- submit_training_job 逐个提交，**禁止 batch script (nohup 启动多实验)**——之前 batch script 导致 GPU 1 双进程写同一文件，数据损坏
- 诊断类 Worker 只诊断+报告，**不自行重启/启动新实验**——之前诊断 Worker 越权重启导致 registry 不同步 40+ 分钟被 Director 3× CRITICAL
- grammar_only "crash" 是误报（cron 追踪 stale PID 123425），PID 126473 从未死过。不要再花时间追查 crash 根因
- Agent 自己能用 check_job_status / tail_training_logs / get_gpu_health 确认服务器状态，不需要派 Worker 做 registry 同步——Director 明确要求过 3 次

### 2. 🖥️ 基础设施快照
- 服务器: westd-16980, 2x RTX PRO 6000 96GB
- 工作目录: /root/schema_semantic_constrained_ie
- Python: /root/miniconda3/bin/python（conda base 环境，激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型: /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B
- 数据: SciERC → data/processed_data/test.json (551 samples), DocRED → data/docred/dev.json (998 docs)
- 约束文件: ontology_constraints.json (SciERC), data/docred/ontology_constraints_docred.json (DocRED)
- 输出目录: outputs/
- 活跃进程:
  - grammar_only: PID 126473, tmux=phase2_scierc_grammar_only, cuda:1, ~370/551
  - unconstrained: PID 126948, tmux session via submit_training_job, cuda:1, ~370/551
  - DocRED schema: PID 116365, cuda:0, ~700/998
- cron: grammar_only (pid=phase2_scierc_grammar_only), unconstrained (pid=126948 via reconcile)

### 3. 📊 当前状态
刚完成 registry 紧急同步——三条 registry (grammar_only→RUNNING/cuda:1, unconstrained→RUNNING/cuda:1, s2_pilot50→DONE) 已更新并向 Director 汇报。

Registry RUNNING 实验:
- **phase2_scierc_grammar_only** (P005): cuda:1, PID 126473, ~370/551, 预计 ~20min 完成
- **phase2_scierc_unconstrained** (P005a): cuda:1, PID 126948, ~370/551, 预计 ~20min 完成
- **mvp_phase0_docred_schema** (P004): cuda:0, PID 116365, ~700/998, 预计 ~1h 完成

等待中:
- Worker `analysis:s2_relation_f1_rootcause` 仍在跑（turn 28，已有初步结论: entity coverage 50% 是主因，eval 脚本无 bug，schema 无问题）。系统告警 30min 无日志更新但 verbose 显示仍在活跃
- resume 支持 Worker 已完成——`run_constrained_extraction.py` 已有 `--resume` 参数

### 4. 📋 待办
- grammar_only (P005) cron 回调完成 → 立即用 violation_checker.py 分析结果 → 更新 registry metrics → 汇报 Director
- unconstrained (P005a) cron 回调完成 → 同上分析 → 这是 Phase 2 的 F1 baseline，后续所有 constrained 实验以此为对照
- P005 + P005a 都完成 → 立即通过 submit_training_job 逐个提交 P006 (semantic_only) 和 P007 (full_s1) 到 cuda:1
- s2_relation_f1_rootcause Worker 回调 → 读结果 → 汇报 Director，由 Director 决策 P008 是否启动
- DocRED schema (P004) 完成 → 分析 + 更新 registry → 完成 C2 claim 的全部 evidence
- P007 完成后 → 提交 P008 (full_s2, 依赖 S2 root cause 解决) 和 P009 (DocRED grammar_only)

### 5. 🎯 战略上下文
- 项目: OntoCoDec — 将本体 schema 编译为解码时约束，保证 LLM IE 输出 0% 类型违规
- 目标: EMNLP 2026 ARR, deadline 2026-05-25（12 天）
- 4 个 claims: C1 violation landscape (done, strong), C2 prompt insufficiency (done, strong), C3 composable framework (Phase 2 在跑), C4 S1 vs S2 (pending P008)
- Phase 0 已证明 GO: SciERC DR=15.4%, DocRED DR=18.7%
- Phase 2 关键风险: **S2 relation_f1=0.0**。初步排查显示主因是 Pass 1 entity coverage 只有 50%（exact match），不是 eval 脚本 bug。这可能影响 C4 claim 的可行性——如果 S2 的 entity recall 太低导致 relation recall 归零，S2 strategy 的论文叙事需要调整
- 易错点: GPU 编号。submit_training_job 注入 CUDA_VISIBLE_DEVICES，脚本内 `--device cuda:0` 是逻辑设备。两个 Phase 2 实验都在物理 cuda:1 上共享（各 16.5GB），不要看到日志 "Device: cuda:0" 就以为是物理 GPU 0
- 易错点: 不要再用 batch script，每个实验单独 submit_training_job


---
