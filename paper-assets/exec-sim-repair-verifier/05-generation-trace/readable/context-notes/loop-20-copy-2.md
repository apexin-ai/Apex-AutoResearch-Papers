# agent / loop_20.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`e97cfb49aa123e89e21e.json`](../../sessions/e9/e97cfb49aa123e89e21e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-16T10:06:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd cuda:0, cuda:1, cuda:2, cuda:3（项目已获分配 4 张 5090）
- MCP SSH 工具中服务器名必须用 `westd-48478`（不是 `westd` 或 `seetacloud-westd-4x5090`）
- D103: 任何 seq_length / batch_size / precision / lr 变更必须 Director 审批
- D112: Re-repair Phase 0 结果**不写入论文任何部分**（包括 Discussion），推翻了 D111
- D109: repo-level 不 claim "gap widens with scale"，改为 absolute magnitude + generation degradation 叙事

### 2. 🖥️ 基础设施快照
- 服务器: seetacloud-westd-4x5090 (MCP name: `westd-48478`)
- 工作目录: `/home/sonny/exec-sim-repair-verifier`
- Python: `/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型路径: `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- Checkpoints: `/root/autodl-tmp/checkpoints_deepseek_cls_repo/`, `/root/autodl-tmp/checkpoints_deepseek_cwm_repo/`
- SWE-bench metadata: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_verified_meta.jsonl`
- 活跃进程:
  - deepseek-cls-repo: PID 470263, cuda:0, cron 监控中
  - deepseek-cwm-repo: PID 479953, cuda:1, cron 监控中
  - deepseek-cls-func-s123: PID 489475, cuda:2, cron 监控中
- W&B: 上述三实验均 `--no_wandb`

### 3. 📊 当前状态
三个 DeepSeek 实验在跑:
- `deepseek-cls-repo` (repo-level CLS, cuda:0, ~27h total, started ~06:27 UTC May 16, ETA ~May 17 09:30 UTC)
- `deepseek-cwm-repo` (repo-level CWM, cuda:1, ~28h total, started ~08:05 UTC May 16, ETA ~May 17 12:00 UTC)
- 一个 PID 489475 实验在 cuda:2（可能是 deepseek-cls-func-s123，但 registry 中未找到对应条目——需要 SSH 确认是什么）

所有 func-level DeepSeek 实验已完成: CLS 86.93%, CWM 86.83±1.06%, gap 仅 0.10pp (D110)。
CWM 8B 已锁定: 65.17% acc, 73.81% unparseable (D109)。
Re-repair Phase 0: negative, 不入论文 (D112)。

等待:
- 三个 cron 回调（训练完成时自动触发）
- 无 pending Director 决策

### 4. 📋 待办（条件触发式）
- deepseek-cls-repo cron 回调 → spawn worker eval on test set (test8192) → 填主表
- deepseek-cwm-repo cron 回调 → spawn worker eval on test set → 计算 unparseable rate → 填主表
- PID 489475 完成回调 → 确认身份，处理结果
- 两个 repo-level eval 都出结果 → 更新 ROADMAP 主表 → 汇报 Director（DeepSeek generalizability claim 强度）
- Inference efficiency benchmark (cuda:3, ~30min) → 可能已完成或未启动，需确认
- 所有 DeepSeek 数据就绪 → 派 Paper Worker 更新 experiments.tex 主表 + generalizability 段落

### 5. 🎯 战略上下文
- 核心论文 claim: CLS reformulation >> CWM at repo-level（19-26pp gap Qwen3），func-level 两者相当
- DeepSeek 跨模型验证是 D108 scope 扩展的核心：证明 CLS 优势不限于 Qwen3 一个模型家族
- func-level 已确认跨模型一致 (CLS≈CWM)，repo-level 结果是最后一块拼图
- DDL: EMNLP ARR May 25, 剩 9 天。DeepSeek repo 训练 ETA ~May 17 中午 → eval ~May 17 晚 → 写入论文 ~May 18
- 易错点: deepseek-cwm-repo 的 spec 中没有 gpu/pid 字段（submit 方式可能不同于 cls），回调时需确认训练是否正常
- 易错点: 不要混淆 func-level 和 repo-level 结论——func-level gap 接近 0 是预期的（D110 confirmed），repo-level 才是核心 claim
- Registry 有大量历史 failed/killed 实验（155 total, 36 failed），不用管，都是早期迭代


---
