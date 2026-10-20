# director / loop_6.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`fa9e78ba36ff6bd0707d.json`](../../sessions/fa/fa9e78ba36ff6bd0707d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T18:38:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0 和 cuda:1（westd-11235 上只分配了这两张卡）
- vota_seed456 上次被错误提交到 cuda:0（与 deepseek 实验冲突），修复后路由到 cuda:1（`CUDA_VISIBLE_DEVICES=1`）。不要再犯同样的分配冲突
- Registry 中 vota_seed456 的 spec.pid 是旧值 145908，实际 wrapper PID 为 146582（Reviewer 已记录），但进程可能已退出——必须先 SSH 确认再做任何判断
- submit_training_job 的 command 中用 `export CUDA_VISIBLE_DEVICES=X` 显式指定 GPU，不要依赖默认分配

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/trace-verdict-study
- 训练日志目录：~/runs/trace-verdict-study/
- W&B：未配置（本项目实验不依赖 W&B 追踪）
- 镜像：aml-train（conda 环境，Python 在 /root/miniconda3/bin/）
- 活跃进程（需重新确认）：
  - deepseek_exception_only_seed123: PID 144507/144517, cuda:0
  - vota_seed456: PID 146582 wrapper, cuda:1（cron 报进程已退出，需验证）

### 3. 📊 当前状态
- **vota_seed456**：cron 连续报进程退出 + 无 W&B 数据，registry 仍标 RUNNING。上一轮 Agent 派了 Worker SSH 排查但 Agent 随后空转 3h 未消化 Worker 结果。**这是最高优先级：SSH 查 `~/runs/trace-verdict-study/vota_seed456.log` 尾部，判断成功/失败，update_registry + delete_cron**
- **deepseek_exception_only_seed123**：cuda:0 上 RUNNING，预计 1-2h 完成（但已过去 3h+，可能也已结束）
- Agent 上一轮还派了 Worker 准备 DeepSeek full_trace v3 代码（注释掉 load_best_model_at_end，保留 chat template truncation fix），代码可能已就绪

### 4. 📋 待办
- 立即 SSH 确认 vota_seed456 状态 → 成功则 update_registry(DONE/success) + delete_cron；失败则 update_registry(DONE/failed) + 分析原因 + cuda:1 空出后提交 DeepSeek full_trace v3
- 立即 SSH 确认 deepseek_exception_only_seed123 是否仍在跑 → 若已完成则同样更新 registry + 分析结果
- 两张卡空出后 → 提交 DeepSeek full_trace v3（代码可能已就绪）+ seed robustness 矩阵的下一组
- 两项 DeepSeek 实验落地后 → 更新 paper_framing → 启动 Paper Agent

### 5. 🎯 战略上下文
- 项目核心发现：trace 信息中 exception/error 信号是判定 verdict 的关键特征，VOTA（投票聚合）在 CodeLlama 上达 99.2% accuracy。现在做 seed robustness（plan_008）和 cross-model（DeepSeek）验证
- 已有 15 个成功实验，research 阶段 + 审稿已并行启动（Review Group C 独立运作）
- 易错点：Agent 上一轮 session 空转 3h 没消化 worker 回调，新 session 启动后先处理积压的 cron/worker 状态，不要直接派新实验
- 决策链参考 decisions.yaml（22 条记录），paper_framing.md 和 experiment_plan.yaml 是战略锚点


---
