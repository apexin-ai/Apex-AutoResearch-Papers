# agent / loop_22.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_22.md`
- **Structured JSON:** [`8fe0519049d498ed714c.json`](../../sessions/8f/8fe0519049d498ed714c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-16T18:31:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单: seetacloud-westd-4x5090 的 cuda:0/1/2/3（4 张 5090）
- 模型路径必须用 /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct（HF_HUB_OFFLINE=1，不能在线下载）
- 训练脚本工作目录: /home/sonny/exec-sim-repair-verifier（不是 /root/）
- conda 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（不是 venv）
- deepseek-traj-func-v2-s123 (cuda:3) 的 registry 显示 conclusion=failed + hook on_failed，但 reconcile 确认 pid 513115 仍活着——状态不一致，下次处理时先 SSH 确认再更新 registry

### 2. 🖥️ 基础设施快照
- 服务器: seetacloud-westd-4x5090
- 工作目录: /home/sonny/exec-sim-repair-verifier
- Python: /root/miniconda3/bin/python3（conda base 环境）
- 模型: /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
- 数据: /home/sonny/exec-sim-repair-verifier/data/（traj_train.jsonl 8052条, swebench_full/ 70748条）
- Checkpoints: /root/autodl-tmp/checkpoints_deepseek_*/
- W&B: 大部分实验 --no_wandb（本地 log 为主）
- 活跃进程:
  - deepseek-cls-repo: PID 470263, cuda:0
  - deepseek-cwm-repo: PID 479953, cuda:1
  - deepseek-traj-func-v2: PID 511676, cuda:2 — **已死**
  - deepseek-traj-func-v2-s123: PID 513115, cuda:3 — reconcile 说活着

### 3. 📊 当前状态
收到 cron 回调: deepseek-traj-func-v2 (cuda:2) 进程异常退出。已派 Worker `worker_diagnose_deepseek-traj-func-v2-fixed_20260516T142001` SSH 诊断日志（读 /tmp/deepseek_traj_v2.log），Worker 尚未回调。已向 Director 汇报 cuda:2 空闲 + 正在诊断。

Registry RUNNING 实验:
- deepseek-cls-repo (cuda:0, repo-level CLS verifier, seed 42)
- deepseek-cwm-repo (cuda:1, repo-level CWM verifier, seed 42, 70k 数据)
- deepseek-traj-func-v2 (cuda:2, traj verifier seed 42) — 实际已死，待更新
- deepseek-traj-func-v2-s123 (cuda:3, traj verifier seed 123) — 状态矛盾待确认

### 4. 📋 待办
- Worker 诊断回调到达 → 读 failure_reason → update_registry(status=DONE, conclusion=failed) → 根据根因决定是否重启 cuda:2 实验
- 若 OOM → 降 batch_size 或 max_seq_length 后重提交 cuda:2
- 若代码 bug → 修复后同时重启 v2 和 v2-s123（如果 s123 也有同样问题）
- deepseek-traj-func-v2-s123 状态矛盾 → SSH 确认 pid 513115 是否真活着 + 是否在正常训练 → 修正 registry
- deepseek-cls-repo / deepseek-cwm-repo 完成回调 → 走 on-experiment-done 流程

### 5. 🎯 战略上下文
- 项目核心: 训练 execution-simulation repair verifier（CLS 分类 + CWM 连续 + Trajectory 多步验证），用 deepseek-coder-6.7b + LoRA
- 当前阶段: 大规模 repo-level 数据训练（70k swebench）+ trajectory verifier（8k 数据）
- 成功率高: 91/158 success，主要失败是早期环境/路径问题
- 易错点: registry 里有大量历史 failed/killed 实验（环境搭建期遗留），不要被吓到——当前批次的实验结构已稳定
- deepseek-traj-func (无 v2) seed 42 已 success（5/16 12:58），v2 是改进版本（可能改了数据格式或训练脚本），如果 v2 反复失败可对比 v1 的配置差异


---
