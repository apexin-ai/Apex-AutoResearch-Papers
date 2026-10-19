# director / loop_2.md

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`aa0be6bc460a4963103e.json`](../../sessions/aa/aa0be6bc460a4963103e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T19:26:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-42106 cuda:0, cuda:1 **仅此两张**，历史上有两次越界事故（D005, D012）
- 训练脚本路径：`/root/structfuse/run_m2_full_qwen.sh` 和 `/root/structfuse/run_m2_full_starcoder.sh`（在项目根目录，**不是** `scripts/` 下——第 4 次启动失败就是路径写错）
- **禁止任何 Worker kill GPU 训练进程**——除非 Director 明确指令。诊断 Worker 曾误杀正在运行的训练导致双卡空闲 50 分钟
- **禁止绕过 run_m2_full_*.sh 脚本直接用 python 命令启动训练**——fix Worker 曾跳过脚本用错超参导致第 3 次失败
- 目录 `/root/structfuse` 未重命名（训练脚本硬编码该路径），**等 18 runs 全部完成后才能重命名为 `/root/structfuse-context`**
- D019/D020 go/no-go 阈值已锁定，**结果出来前不允许修改**

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-42106 (connect.bjb1.seetacloud.com:42106)，2× RTX PRO 6000 96GB
- 工作目录：`/root/structfuse`（代码），`/root/autodl-tmp/structfuse/`（数据/checkpoints）
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- M2 训练数据：`/root/autodl-tmp/structfuse/full_m2_training_data/`（9 train + 9 val + dataflow_graph.json，14,288 inst/seed）
- Checkpoints 输出：`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 和 `m2_full_starcoder/`
- 活跃进程：
  - cuda:0: m2_full_qwen（PID 73558, tmux=m2_qwen, random_s42 epoch 1 ~step 300）
  - cuda:1: m2_full_starcoder（PID 76627, tmux=m2_starcoder, 数据构建已完成 → random_s42 训练中）
- SWE-bench eval 脚本已就绪：`/root/structfuse/evaluation/eval_swebench.py`
- Artifacts 目录：`/root/autodl-tmp/structfuse/artifacts/`（negative_difficulty 图表、plan006 JSON、Z% JSON）

### 3. 📊 当前状态
双卡满载运行 full M2 训练（18 runs = 3 strategies × 3 seeds × 2 encoders），每卡 9 runs 顺序执行。

- **m2_full_qwen**: RUNNING，random_s42 epoch 1 进行中。首次 eval@500 预计很快到达。单 run ~12-24h，9 runs ~3-7 天
- **m2_full_starcoder**: RUNNING，random_s42 刚开始（StarCoder 数据构建完成后自动启动）

等待中：
- Qwen eval@500 cron 回调（最关键的下一事件）
- Worker: negative_difficulty_margin（补跑 query-positive similarity）
- Agent 已收到 M1 重提取准备指令（D022），尚未汇报

### 4. 📋 待办（条件触发式）
- eval@500 到达 → 检查 Qwen random_s42 的 R@1 和 val_loss，对比 pilot baseline（pilot random R@1=0.5357）。这是 full M2 首个信号
- negative_difficulty_margin 完成 → 检查 Qwen margin vs StarCoder margin。如果 margin 相近 → D021 "StarCoder 已经懂了" 结论需修正
- 单个 encoder 9 runs 完成 → 立即启动 plan_003 SWE-bench eval（不等另一个 encoder），脚本已就绪
- 18 runs 全部完成 → 按 D019/D020 阈值执行 go/no-go 判定（bootstrap 95% CI + paired t-test）
- go/no-go 后如需更多数据 → 启动 M1 重提取（D022，28K instances 可恢复，2.8x 数据增长）
- 18 runs 完成 + 训练进程结束 → 执行目录重命名 + update_project_config
- Full M2 完成后优先启动 plan_014 temperature ablation (~10h)

### 5. 🎯 战略上下文
- **决策链**：D008 MVP通过 → D015 Z%=78% Best Framing → D016/D17 pilot 完成 → D018 不做预判 pivot → D019/D020 量化阈值锁定 → D021 negative difficulty 解释 encoder capacity 差异 → D022 28K instances 可恢复
- **核心结论到目前为止**：embedding > random 跨编码器一致（+2.0pp/+1.6pp）是最稳健发现；dataflow mixed（Qwen +0.8pp, StarCoder -0.5pp）；原 Claim 2 "embedding harms" 在 true embedding mining 下不复现
- **最容易判断错的事**：(1) pilot 差异 <2pp 且 n=1，不要基于 pilot 做强结论——full M2 (3 seeds) 是唯一可信判据；(2) StarCoder dataflow 无效不是方法失败，是 encoder pretrained separability 已经很高（D021）；(3) 不要改 D019/D020 阈值来适配结果
- **Reviewer 路径推荐**：如果落入 (B) Conditional Go，Path A "Negative Mining Methodology Analysis" 是 Reviewer 和 Agent 独立共识的最佳叙事方向，目标降为 EMNLP Findings
- **DDL**: ARR May 25（~11 天）。GPU-hours 充足（~140h needed / 576h available），瓶颈是实验依赖链


---
