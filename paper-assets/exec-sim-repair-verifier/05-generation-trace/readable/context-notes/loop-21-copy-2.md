# agent / loop_21.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`48a68ea55d686c27f204.json`](../../sessions/48/48a68ea55d686c27f204.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: idle_timeout
updated: '2026-05-16T14:12:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd cuda:0, cuda:1, cuda:2, cuda:3（项目已获分配 4 张 5090）
- MCP SSH 工具中服务器名必须用 `westd-48478`（不是 `westd` 或 `seetacloud-westd-4x5090`）
- D103: 任何 seq_length / batch_size / precision / lr 变更必须 Director 审批
- D112: Re-repair Phase 0 结果**不写入论文任何部分**（包括 Discussion）
- D109: repo-level 不 claim "gap widens with scale"，改为 absolute magnitude + generation degradation 叙事

### 2. 🖥️ 基础设施快照
- 服务器: seetacloud-westd-4x5090 (MCP name: `westd-48478`)
- 工作目录: `/home/sonny/exec-sim-repair-verifier`
- Python: `/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型路径: `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- Checkpoints: `/root/autodl-tmp/checkpoints_deepseek_cls_repo/`, `/root/autodl-tmp/checkpoints_deepseek_cwm_repo/`, `/root/autodl-tmp/checkpoints_deepseek_cls_func_s123/`
- SWE-bench metadata: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_test.jsonl` (9784 instances)
- 活跃进程:
  - deepseek-cls-repo: PID 470263, cuda:0, cron 监控中
  - deepseek-cwm-repo: PID 479953, cuda:1, cron 监控中
  - deepseek-cls-func-s123: PID 489475, cuda:2, cron 监控中
- W&B: 上述三实验均 `--no_wandb`

### 3. 📊 当前状态
Session #21 刚启动，完成了初始化：
- reconcile_crons 确认三个进程全部在跑
- 修复了 `deepseek-cls-func-s123` 缺失的 registry 条目（补建 RUNNING + spec + hypothesis）
- 已派 2 个 Worker：(1) GPU 状态全面检查（确认 cuda:3 用途）(2) DeepSeek repo-level eval 代码就绪性验证
- 已向 Director 汇报 session start 状态
- **两个 Worker 尚未回调**——下一轮需要处理它们的结果

### 4. 📋 待办（条件触发式）
- Worker `check:gpu-status-all` 回调 → 确认 cuda:3 空闲 → 启动 inference efficiency benchmark
- Worker `code:deepseek-repo-eval-prep` 回调 → 确认 eval 脚本是否兼容 DeepSeek（如需改动则派 Worker 修）
- `deepseek-cls-func-s123` cron 回调 → spawn worker eval on test set (n=1890) → 更新 func-level 主表第二个 seed
- `deepseek-cls-repo` cron 回调 (ETA ~May 17 09:30 UTC) → spawn worker eval on test8192 → 填 repo-level 主表
- `deepseek-cwm-repo` cron 回调 (ETA ~May 17 12:00 UTC) → spawn worker eval → 计算 unparseable rate → 填主表
- 两个 repo-level eval 都出结果 → 汇报 Director（DeepSeek generalizability claim 强度）→ 派 Paper Worker 更新 experiments.tex

### 5. 🎯 战略上下文
- 核心论文 claim: CLS reformulation >> CWM at repo-level（Qwen3 gap 19-26pp），func-level 两者相当
- DeepSeek 跨模型验证是最后一块拼图：证明 CLS 优势不限于 Qwen3
- func-level 已确认跨模型一致 (DeepSeek CLS 86.93% ≈ CWM 86.83±1.06%, gap 0.10pp, D110)
- DDL: EMNLP ARR May 25, 剩 9 天。DeepSeek repo 训练 ETA ~May 17 中午 → eval ~May 17 晚 → 写入论文 ~May 18
- 易错点: deepseek-cwm-repo 的 spec 中没有 gpu/pid 字段（是通过非 submit_training_job 方式启动的），回调时需 SSH 确认训练状态
- 易错点: 不要混淆 func-level 和 repo-level 结论——func-level gap ≈ 0 是预期的（D110），repo-level 才是核心 claim
- 易错点: read_registry 的 exp_id filter 似乎对最近追加的实验不生效（返回空），需要用 limit 或直接读 YAML 文件确认


---
