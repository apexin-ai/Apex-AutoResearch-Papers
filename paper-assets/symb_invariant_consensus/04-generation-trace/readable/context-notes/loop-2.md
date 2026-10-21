# director / loop_2.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`56a159a6eb311dc71f25.json`](../../sessions/56/56a159a6eb311dc71f25.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-15T18:55:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只有 1 张（westd-32608），所有实验串行，不能并行跑 GPU 任务
- MVP 阶段未完成，禁止启动完整研究规划、paper_framing、experiment_plan
- Reviewer 进程已死，已与 Manager 约定 v3 完成后重启 agent-ml server（sync_ec2_code restart=true），届时通知 Manager 执行
- Agent 此前误实现 CRD（非 SICA），已纠正（D002），不要回退到 CRD 方向

### 2. 🖥️ 基础设施快照
- 服务器：westd-32608 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/symb_invariant_consensus
- Python 环境：需 SSH 探查确认（conda vs venv）
- 数据：data/proofwriter_subset.json (10题)、data/math500_subset.json (50题)
- 活跃进程：sica_aime30_v3 PID 129992，约 20/30 题完成，ETA ~111min（从 Reviewer 报告时算）
- W&B / HF cache：未配置

### 3. 📊 当前状态
- sica_aime30_v3 RUNNING：AIME 2024 30题，v3 修复了 timeout/hang bug，从 v2 P5 恢复继续，约 20/30 完成
- ProofWriter prompt 适配已完成（trace_generator.py + pipeline.py 支持 logic domain）
- MATH-500 数据+加载器+评估脚本就绪
- v4 所有 5 项代码修复（z3 parser、A+C scorer、answer extraction fallback、Int/Real sort、timeout）已在磁盘上就绪
- Agent 和我自己都在 RESET，新 session 启动后需要先确认 v3 是否已完成

### 4. 📋 待办
- v3 完成 → 分析结果（SICA vs SC@K=12 在 AIME 30 题上的对比）→ 判断 MVP 假设是否成立
- v3 完成 → 通知 Manager 执行 sync_ec2_code restart=true 重启 Reviewer
- v3 结果正面 → 启动 v4（合并 5 项修复重跑 AIME）+ 并行跑 MATH-500 50 题（如果 GPU 允许串行排）
- v3 结果负面 → 分析 P20 等低共识题的 SICA 行为，决定是否 pivot 或调整 pipeline 参数
- MVP 通过 → complete_mvp() → post-mvp-kickoff skill → paper_framing + experiment_plan + dream_simulate

### 5. 🎯 战略上下文
- 核心假设：SICA（Symbolic Invariant Consensus Aggregation）通过提取符号约束并检测跨路径矛盾，在数学推理任务上超越 SC@K
- 关键决策链：D001 立项 → D002 纠正 CRD 误实现 → D003 加固 MVP 标准 → smoke test 通过 → v1/v2 遇 timeout bug → v3 修复后重跑
- sica_smoke_5q 成功（5题小规模验证通过），但 30 题规模验证（v3）尚未出最终结果
- P20 是关键观察点：SC 仅 4/12 votes（最分散），SICA 和 SC 都答对——这类低共识题是 SICA 最可能超越 SC 的场景，v4 的 A+C scorer 可能在此类题上产生差异
- 易错：不要把 smoke test 的成功当作 MVP 通过——必须看 v3 全 30 题结果再判断


---
