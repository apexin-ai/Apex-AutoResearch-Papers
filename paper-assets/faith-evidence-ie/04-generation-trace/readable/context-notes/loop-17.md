# agent / loop_17.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`9f13f9314637ecf0fa91.json`](../../sessions/9f/9f13f9314637ecf0fa91.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-19T12:25:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx5090-4x cuda:0/1/2/3（共 4 张 RTX 5090）。不得用其他设备
- bjb2-12179 连接失败状态，不要尝试在该服务器操作
- 8B k=1 (53.76) < k=3 (54.33) by -0.57pp，论文不能 claim "k=1 consistently outperforms k=3"，framing 为 "methodological correction yields comparable results"
- 1.7B surpasses 8B claim 脆弱（51.22 vs 50.51 = +0.71pp，seed variance 0.95pp > gap），需更多 seeds 加固后才能写强 claim

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x，工作目录 ~/runs/faith-evidence-ie/
- 磁盘：/usr/bin/nvidia-smi 分区 431G/879G 可用（49% 已用）
- 活跃进程（reconcile 确认）：
  - plan019_8b_sft_s44: PID 567982, cuda:0
  - wave1_sft_4b_s44_eval_r2: PID 571192, cuda:1
  - wave1_sft_4b_s43_eval_r2: PID 568649, cuda:2
  - grpo_bf16_g4_ckpt200_eval: PID 571115, cuda:3
- 4 张 GPU 全部在跑，无空闲

### 3. 📊 当前状态
- **plan019_1_7b_sft_s43_r2** 刚进入 ANALYZING（进程正常退出，W&B 数据可用）。已派 Worker `worker_analyze_plan019_1_7b_sft_s43_r2_20260518T201851` 去 SSH 读日志 + 查 W&B metrics + 确认 checkpoint。**等待该 Worker 回调**
- 这是 1.7B 第三个 seed（s43），前两个：s42 ign_f1=0.4786, s44 ign_f1=0.4321。本次训练结果决定 1.7B 方差估计
- 4 个 RUNNING 实验全在跑（见上方），0 个 PREPARING/PENDING
- registry 总计：196 实验，104 success，15 negative，42 failed，28 killed

### 4. 📋 待办
- Worker analyze 回调到达 → 读结果，update_registry(conclusion=success/failed)，记录 checkpoint_path + log_path + final_train_loss → 如 success，**立即启动 1.7B s43 eval**（参考 plan019_1_7b_sft_s44_eval 的 eval 命令格式，注意用 D076 协议：--model_path=base --sft_adapter=adapter）→ 汇报 Director
- wave1_sft_4b_s43_eval_r2 完成 → 分析 4B s43 ign_f1，与 canonical 4B s42 对比
- wave1_sft_4b_s44_eval_r2 完成 → 分析 4B s44 ign_f1，与 canonical 4B s42 对比
- grpo_bf16_g4_ckpt200_eval 完成 → 与 ckpt-100 (ign_f1=0.4431) 对比，判断 GRPO 是否持续改进（D106 learning curve）
- plan019_8b_sft_s44 完成 → 启动 8B s44 eval → 8B 将有 s42+s44 两个 seed
- 当有 GPU 释放 → 排队：1.7B s43 eval > 其他 scaling seeds

### 5. 🎯 战略上下文
- 项目：FREIGE，LLM-based evidence-grounded DocRE。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax
- 目标：EMNLP 2026 Main（ARR July cycle，~58 天），从 Round 1 Overall 3.0 → 4.0
- 当前阶段：D104 进攻性扩展 + Wave 1 scaling seeds。核心任务是每个尺度 3+ seeds 的 mean±std 统计力
- D102 已完成 k=1 方法论修正。D109 确认 Random RSFT k=1 ign_f1=0.4114 远低于 CED（0.4596），CED scoring 价值已证实
- D110：GRPO bf16 ckpt-100 ign_f1=0.4431，无 catastrophic forgetting，ckpt-200 eval 正在跑
- 易错点：1.7B s44 的 ign_f1=0.4321 异常低（vs s42=0.4786），s43 结果将决定是 s44 outlier 还是 s42 outlier——这直接影响 1.7B 的 mean 和 claim 强度。如果 s43 接近 s42（~0.47+），s44 是 outlier，1.7B mean 偏高，claim 更稳；如果 s43 接近 s44（~0.43），s42 是 outlier，需要调整 framing
- eval 命令必须用 D076 协议（--model_path=base --sft_adapter=adapter），之前多次因命令格式错误导致 eval 失败


---
