# director / loop_2.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`ffbd9ae45042436c4ab2.json`](../../sessions/ff/ffbd9ae45042436c4ab2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T23:45:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单: cuda:0 ~ cuda:5（6张），不可使用白名单外的卡
- evaluate.py 不接受 --gpu 参数，加了会崩溃（已有两个 eval 因此 failed）
- 所有 eval 命令必须通过 CUDA_VISIBLE_DEVICES 环境变量指定 GPU，不用 --gpu
- dosage 数据已就绪（d005/d010/d050/d100），不需要等 MMLU 或其他数据准备

### 2. 🖥️ 基础设施快照
- 服务器信息: 需从 project config / get_resource_inventory 获取（本 session 未直接 SSH）
- 项目路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/
- artifacts 目录: 上述路径下 artifacts/
- 活跃进程（截至 handoff 时刻）:
  - cuda:0: exp_001_sft_d100_05B (PID 235243, 0.5B dosage=100% SFT, ~53min)
  - cuda:1: 0.5B s42 eval
  - cuda:2: 0.5B s123 eval
  - cuda:3: 3B s123 训练
  - cuda:4: 1.5B s42 eval
  - cuda:5: exp_001_sft_d005_05B (PID 235331, 0.5B dosage=5% SFT, ~53min)
- cron 已注册监控上述 SFT 任务

### 3. 📊 当前状态
刚完成的动作:
- 标记 exp_001_eval_15B_d000_s123 为 DONE/failed（--gpu bug）
- 标记 exp_001_eval_3B_d000_s42 为 DONE/failed（同一 bug，刚派 Agent 去做）
- 启动 0.5B d100 和 d005 两个极端 dosage SFT，GPU 6/6 满载
- 预注册 exp_001_sft_d100_15B 为 PREPARING，等 cuda:3 释放

RUNNING/PREPARING 实验:
- exp_001_sft_d100_05B: RUNNING, 0.5B 100% dosage SFT
- exp_001_sft_d005_05B: RUNNING, 0.5B 5% dosage SFT
- exp_001_sft_d100_15B: PREPARING, 等 GPU 3

等待中:
- Agent 刚收到指令标记 exp_001_eval_3B_d000_s42 failed
- 多个 eval 在跑，完成后释放 GPU 给后续 dosage SFT
- cron 回调: SFT 完成后 Agent 会回报

### 4. 📋 待办
- 0.5B d100/d005 SFT 完成 → 立即派 eval（不加 --gpu），用 CUDA_VISIBLE_DEVICES
- cuda:1/2/4/5 eval 完成释放 → 优先铺 1.5B d100 SFT（已 PREPARING）、1.5B d005 SFT
- cuda:3 3B s123 训练完成 → 启动 exp_001_sft_d100_15B
- 两个 failed eval（0.5B s123 和 3B s42 的 d000 baseline eval）→ 有空 GPU 时重跑（去掉 --gpu）
- dosage grid 完成后 → 分析 contamination 剂量-效应曲线，验证 IRT calibration 核心假设

### 5. 🎯 战略上下文
- 项目核心: 用 IRT calibration 检测 LLM benchmark contamination，dosage grid 是关键实验——不同模型规模 × 不同 contamination 剂量，看 IRT 参数变化是否能量化检测
- 当前阶段: dosage grid 铺开中，0.5B 的两个极端（d005 最小、d100 最大）先跑，建立效应上下限
- 已有 d000 baseline SFT 完成（0.5B/1.5B/3B），但对应的部分 eval 因 --gpu bug 失败待重跑
- 易错点: (1) evaluate.py 绝对不能加 --gpu，这是本项目反复踩的坑 (2) dosage 数据已经就绪不需要额外准备 (3) 审稿阶段已启动（review_chat_id 存在），GPU 不能空着等审稿，继续铺 dosage grid
- 项目处于 research 阶段，paper_framing.md 和 experiment_plan.yaml 已存在


---
