# agent / loop_25.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_25.md`
- **Structured JSON:** [`61289dead9769844e55a.json`](../../sessions/61/61289dead9769844e55a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 25
reason: idle_timeout
updated: '2026-05-17T22:38:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配必须查 `get_project_resource_usage` 的 `allocated_gpus`，当前显示 0 张分配——意味着所有 GPU 使用需要先确认 Director 分配
- seq_length / batch_size / precision / lr 修改需 Director 审批（D103 教训，见 feedback memory）
- seetacloud 无 Docker，SWE-bench eval 只能在 home-1x5090 跑
- DeepSeek eval 必须用独立脚本 `eval_deepseek_repo.py`（非 eval_repo_cls.py），因为 tokenizer 差异（LlamaTokenizerFast vs Qwen2TokenizerFast）
- CWM repo 报告策略已锁定方案 B（D125）：epoch 3 为主数字 + checkpoint sensitivity 作 fragility 证据。不要擅自改回方案 A

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**：4× RTX 5090，工作目录 `/home/sonny/exec-sim-repair-verifier`
  - Python：`/root/miniconda3/bin/python`（conda base）
  - HF cache：`/root/autodl-tmp/.hf_cache/`
  - Qwen3-8B：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
  - DeepSeek：`/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
  - Checkpoints 前缀：`/root/autodl-tmp/checkpoints_*`
  - 磁盘：`/usr/bin/nvidia-smi` 分区 436G/879G 可用（48% 已用）
- **home-1x5090**：工作目录 `/home/sonny/exec-sim-repair-verifier`，Docker 可用（SWE-bench harness v4.1.0）
- **活跃 cron**：3 个——`deepseek-cls-repo-v4` (pid=664774)、`deepseek-cwm-repo-s42-epoch2-eval` (pid=662946)、`deepseek-cwm-repo-s123` (pid=668680)
- **活跃 Worker**：1 个——`worker_prepare_home-next-task-plan_20260517T223515`（CPU 任务）

### 3. 📊 当前状态
我刚完成 session-start 初始化。项目整体：182 实验，104 success / 7 negative / 41 failed / 26 killed。

**ROADMAP 记录的 GPU 进度**（来自上一轮 Agent 更新，需 SSH 确认是否仍准确）：
- cuda:0: CLS v4 eval (ckpt-4422) ~40%, running_acc 70.9%, ETA ~6h
- cuda:1: CWM s42 eval (epoch 3, ckpt-13266) ~12%, running_acc 58.2%, ETA ~28h
- cuda:2: CLS s123 eval (best ckpt) ~35%, running_acc 74.5%, ETA ~7h
- cuda:3: CWM s123 eval (epoch 2, ckpt-8844) ~9%, running_acc 62.6%, ETA ~30h
- home: 3-shot repo baseline running

**注意**：report.md auto-facts 显示 deepseek-cls-repo-v4 [failed] 和 deepseek-cwm-repo-s123 [failed]，但 reconcile_crons 报告对应 PID 仍活跃。可能是 report 过期或实验被重启。**下一个"你"首要任务是 SSH 确认这 4 个 GPU 上的进程真实状态**。

**最近重要结果**：
- deepseek-cwm-repo (s42) SUCCESS：~58% accuracy，73.8% unparseable——确认 CWM 在 DeepSeek 上同样 repo-level 崩塌
- deepseek-traj-repo：s42 和 s123 均 77.1%（negative，16.7% unparseable）
- Qwen3-8B TRAJ func: s42=87.98%, s123=87.42%——SUCCESS，确认 8B scaling

**DDL**：EMNLP 2026 ARR May 25，剩余 **8 天**。Round 1 weak reject，15/18 issues resolved，3 blocked on DeepSeek repo results。

### 4. 📋 待办（条件触发式）
- CLS v4 eval (cuda:0) 完成 → 记录 s42 accuracy → **立即启动 CLS v5 retrain**（解决 R1-N1 multi-seed）
- CLS s123 eval (cuda:2) 完成 → 记录 s123 accuracy → **立即启动 CWM s42 epoch 2 eval**（D124 判定实验：过拟合 vs seed variance）
- D124 结果到手 → epoch 2 ≈ epoch 3 → seed variance，保持 epoch 3 为主；epoch 2 >> epoch 3 → 过拟合确认，epoch 2 为主
- CWM s42 + s123 eval 全部完成 → Table 4 定稿 → DeepSeek 行填入
- 所有 eval 完成 → Paper Agent 最终 Patch（替换 preliminary 标记 + CWM narrative + checkpoint sensitivity section）→ Round 2 提交（目标 May 20-21）
- `worker_prepare_home-next-task-plan` 回调到达 → 处理 home 5090 下一步任务安排

### 5. 🎯 战略上下文
- **核心 framing（D116+D122）**：设计空间特征化——CLS vs CWM vs TRAJ 的最优选择取决于 task complexity × model family 交互。Path AB = formulation-inherent（CWM 生成式格式天然脆弱）× model-contingent（tokenizer 差异放大/缩小 gap）
- **CLS 是赢家**：所有模型、所有粒度上 CLS 最稳定。CWM 在 func-level 接近但 repo-level 崩塌（Qwen 65%/58%、DeepSeek ~58%）。TRAJ 居中
- **D125 方案 B**：CWM 报 epoch 3 数字 + checkpoint sensitivity 曲线（CLS 单调递增 vs CWM 加速退化）作为第三维 fragility 证据
- **Re-repair 已 drop（D120）**：genuine negative，8B 模型无法利用 per-test 诊断信息
- **易错点**：
  - 不要混淆 func-level 和 repo-level 数字——func-level CWM≈CLS（差 1-2pp），repo-level CWM 崩塌（差 20+pp）
  - DeepSeek CWM repo 的 epoch 2 vs epoch 3 gap（~5pp）是真实的（D124），不是噪声
  - TRAJ repo 的 16.7% unparseable 是 DeepSeek 特有问题（Qwen TRAJ repo 未跑，不可类推）
  - `get_project_resource_usage` 显示 0 allocated GPUs，但实际有 cron 监控的进程在跑——GPU 分配记录可能 stale，以 SSH 实际状态为准


---
