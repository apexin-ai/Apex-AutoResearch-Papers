# agent / loop_10.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`b2698b66341ff715ceff.json`](../../sessions/b2/b2698b66341ff715ceff.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-14T14:55:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: westd cuda:0/1/2/3, home cuda:0。config `gpu_ids` 只列 4 张，home 是单独配置
- **D063 方法论红线**: checkpoint 选择必须在 val set (9335 样本, majority=75.88%) 上做，test set (9784, majority=72.96%) 只报最终数字。违反 = cherry-picking，论文不可投
- **D069 已知**: val set 在 2048/4096 截断下均无法做有效 checkpoint selection（截断样本全变 unparseable 默认预测 majority），这是个未解决的方法论问题
- **Apple-to-apple 对比**: CLS vs CWM 必须用 westd conda 环境（transformers 4.57.6），跨服务器对比无效（home vs westd 有 22pp 差距源于 transformers 5.8.0 vs 4.57.6）
- **CWM v11 数字已废止（D057）**: 不可引用于论文，须等 v12 全量 eval 完成

### 2. 🖥️ 基础设施快照
- **westd**: seetacloud-westd-4x5090, account=root, 项目路径 /home/sonny/exec-sim-repair-verifier
- **home**: home-1x5090, account=sonny, 同路径
- **westd conda 环境**: `/root/miniconda3/bin/python`（aml-train 镜像, `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型缓存**: westd `/root/autodl-tmp/.hf_cache`（如果是 AutoDL 实例）
- **活跃进程**: CWM seed123 eval PID 195531 (westd GPU 0), CWM v12 eval PID 195668 (westd GPU 1) — cron 仍在监控
- **Cron**: 2 个活跃 — `repo-level-cwm-seed123-conda`, `repo-level-cwm-v12`
- **wandb**: 项目应有 wandb 配置，具体 project name 需从 registry spec 中确认

### 3. 📊 当前状态
- **总计 61 实验**: success 36, negative 3, failed 15, killed 7
- **RUNNING (registry)**: 0 — 但 cron 报告 PID 195531/195668 仍活，可能是 registry 状态与实际进程不同步（registry 标 killed 但进程还在跑）。**接手后第一件事**: SSH 确认这两个 PID 是否真的在跑，如果在跑则修正 registry 回 RUNNING
- **刚失败**: `repo-level-cwm-8b-conda` 和 `repo-level-cls-8b-seed123-conda`（EXIT_CODE=1, 14:16 UTC）— 这是 D072/D073 8B 训练重启后再次失败，未诊断
- **home cuda:0**: 分配但空闲 — 违反 L1 硬约束"分配了必须跑"
- **无活跃 Worker**
- **上一轮做了什么**: 8B 训练多次重启（D070-D075），CLS/CWM eval 在跑，checkpoint sweep 发现 D063 方法论问题

### 4. 📋 待办（条件触发式）
- **CWM v12/seed123 eval 完成 cron 回调 →** 提取最终 accuracy/F1, 更新 registry, 计算 CLS-CWM gap, 做 paired bootstrap significance test, 解除 D057 论文阻塞, 汇报 Director
- **CWM eval running acc 57-58% 确认 →** gap ~20-27pp, 远超函数级 1.24pp, complexity-dependent advantage 论点极强, 准备 paper narrative patch
- **8B 训练失败诊断 →** spawn Worker SSH 查 log tail, 确定是 DataLoader 问题复发(D072/D073)还是新问题, 修复后重提交到 westd GPU 2/3
- **D063 val set sweep →** eval 脚本需 --split 参数, 所有 CLS 模型（v5, v5-conda, seed123, 8B）在 val set 上 sweep, 但 D069 说 val set 截断后无法选 checkpoint — 这个矛盾需要和 Director 讨论解决方案
- **home cuda:0 空闲 →** 立即找任务填上（D063 val sweep 或其他 eval 任务）

### 5. 🎯 战略上下文
- **核心论点**: Execution simulation 从 generation（CWM）转 classification（CLS）= task reformulation。CLS 优势随代码复杂度增长：函数级 ~1.24pp → repo-level 预估 20-27pp。EMNLP 2026 ARR May 25 截止，剩 11 天
- **决策链**: D004 P2P 率低 reframe → D007 Complexity-Dependent Advantage → D008 repo-level go/no-go → D057 等 CWM v12 全量 eval → D063 val set 方法论修复 → D069 val set 无法选 checkpoint（未解）
- **最容易判断错的事**: (1) CWM v12/seed123 的 registry 状态可能是 killed 但进程实际还在跑，不要 kill 它们——先 SSH 验证; (2) D069 和 D063 矛盾——val set 上截断样本变 unparseable 导致无法做 checkpoint selection，但 D063 又要求必须在 val set 上选，这个问题没解决; (3) 8B 训练已失败 3+ 次（OOM、DataLoader SIGTERM、原因不明），每次根因不同，不要假设之前的 fix 有效
- **容易踩的坑**: submit_training_job 命令必须自带环境激活（不要假设 .venv）; westd 是 conda 环境; home 和 westd 数据文件 md5 不同不可混用; 所有 repo-level 模型在 <10% 训练步就过拟合（best ckpt 在 step 200-600）


---
