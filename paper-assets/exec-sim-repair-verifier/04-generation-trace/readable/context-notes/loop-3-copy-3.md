# reviewer / loop_3.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`7e54ce2baf50b95c72bc.json`](../../sessions/7e/7e54ce2baf50b95c72bc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-12T19:42:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `[cuda:0, cuda:1, cuda:2, cuda:3]`（seetacloud 4x5090），home 只有 cuda:0
- seetacloud 账号 `root`，home/westd 账号 `sonny`——搞反会 SSH 失败
- seetacloud 有 cgroup memory.max = 360GB（`free -h` 显示 754GB 是宿主机，不可信），历史上导致多次 SIGKILL
- D024：禁止 kill 正常运行的训练进程。之前 prep worker 违反过（kill 了 v4 CWM PID 77816 at step 386）
- CWM repo-level 已连续失败 7 次（v1-v6 + v4 被 kill），第 8 次（当前 v6 重提交）正在跑。对 CWM 的任何操作要极度谨慎

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090** (root): 工作目录 `/home/sonny/exec-sim-repair-verifier`，Python `/root/miniconda3/bin/python`，conda base
  - 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B` (4B) / `Qwen3-8B` (8B)
  - HF cache：`/root/autodl-tmp/.hf_cache`
  - 活跃进程：CWM v6 训练 PID 84887, tmux=repo-level-cwm-v6, cuda:2, ~8s/step, 6633 总步
  - Checkpoint 路径：`/root/autodl-tmp/checkpoints_repo_cwm_v6/`
  - 日志：`~/runs/exec-sim-repair-verifier/repo-level-cwm-v6.log`
- **home-1x5090** (sonny): 工作目录 `/home/sonny/exec-sim-repair-verifier`
  - 活跃进程：CLS home PID 2840844, tmux=repo-level-cls-home, cuda:0, ~6.5s/step, 6633 总步
  - Checkpoint 路径：`/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/`
  - 日志：`~/runs/exec-sim-repair-verifier/repo-level-cls-home.log`
  - 评估脚本已就绪：`eval_repo_level.py` + `paired_bootstrap_repo.py`
- **westd-48478** (sonny): SSH 间歇性不可用，不可靠

### 3. 📊 当前状态
刚完成一轮全面核实：CWM v6 和 CLS home 两条训练线均在正常推进。

| 实验 | 状态 | 进度 | ETA (UTC) |
|------|------|------|-----------|
| repo-level-cls-home | RUNNING | step 1076/6633 (16%) | ~13:30 May 13 |
| repo-level-cwm-v6 | PREPARING→实际 RUNNING | step 10/6633 (0.2%) | ~18:20 May 13 |

**已报告的问题**：
- CWM v6 registry 仍为 PREPARING，缺 gpu/pid/log_path 字段（warning）
- Worker 声称 save_steps=50 但服务器实际 500（info，已报告）
- CWM v6 val 截断率 20.2%（info）
- Error overlap 脚本 bug：oracle_gain_over_cwm=30.05 应为 2.79（info）

**等待中**：无待处理 worker 回调。等 Director 回应或训练完成通知。

### 4. 📋 待办（条件触发式）
- CLS home 训练完成（~13:30 UTC）→ 独立核实 checkpoint 存在 + 验证 eval 命令可执行
- CWM v6 训练完成（~18:20 UTC）→ 核实 checkpoint、验证 registry 更新、检查 CWM checkpoint 是否需拷贝到 home
- CLS/CWM 双方 eval 结果出来 → 独立核实 paired_bootstrap_repo.py 结果，验证 D008 Go/No-Go 决策
- D008 判定：gap≥3pp→确认 EMNLP Main 叙事成立；1-3pp→要求追加 seeds；<1pp→确认 kill C1
- Director 转发 Paper Agent 章节或 framing 提案 → 按 §5/§6 审查
- 任何新训练提交 → 检查 GPU 边界合规 + registry 追溯完整性
- ROADMAP 更新通知 → 审查实验覆盖度、GPU 预算

### 5. 🎯 战略上下文
- **核心假说**：Task Reformulation（CLS vs CWM），CLS 在规模扩展时优势更大。function-level 4B gap=1.25pp → 8B gap=2.42pp（已验证，p=0.0039）。repo-level 是 Pillar 1（Complexity-Dependent Advantage）的关键证据。
- **D008 决策门**：repo-level gap 决定论文走向。≥3pp 全面推进，<1pp 砍 C1。
- **易错点 1**：function-level 有两套数据——seed-level 简单平均（gap=2.42pp）和 per-instance clustered bootstrap（gap=2.26pp）。两者都用了正确值（89.37），方法不同导致数字不同，不是 bug。
- **易错点 2**：seed123 的 89.52=4B accuracy，89.40=8B training eval，89.37=8B independent eval。三个值来源不同，容易混淆。
- **易错点 3**：HuggingFace Trainer 的 logging_steps 进度条重置不等于 checkpoint save。之前我误判过一次（把 logging_steps=50 当成 save_steps=50）。
- **易错点 4**：`free -h` 在 seetacloud 显示 754GB 是宿主机内存，容器实际限制 360GB（cgroup）。


---
