---
loop: 2
reason: max_wall_time
updated: '2026-05-13T23:20:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（seetacloud-westb-2xpro6000）。不得用其他设备号
- MVP 已判定 FAIL（D012）。**禁止启动新训练实验**，等用户方向决策
- eval 脚本必须注入 `{%- set enable_thinking = false -%}` 禁用 Qwen3.5 thinking mode，否则 eval 结果不可比
- model_name 必须用本地磁盘路径（如 `/root/autodl-tmp/output/formal_A/merged`），不能用 HF hub 名
- submit_training_job 的 command 如果用 `source`/`conda activate`，必须包在 `bash -c "..."` 里

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westb-2xpro6000（2x RTX PRO 6000 96GB）
- 工作目录：/root/schema-conform-ie-training
- Python：/root/miniconda3/bin/python（conda base 环境，非 venv）
- 数据：/root/autodl-tmp/data（scierc_test 551, crossner_politics 651, crossner_science 543）
- HF cache：/root/autodl-tmp/.hf_cache
- 模型 checkpoints：
  - A merged: /root/autodl-tmp/output/formal_A/merged
  - B merged: /root/autodl-tmp/output/formal_B/merged
  - D1 v4 merged: /root/autodl-tmp/output/formal_D1_v4/merged
  - D2 ckpt400 merged: /root/autodl-tmp/output/formal_D2/checkpoint-400-merged
  - D2 final merged: /root/autodl-tmp/output/formal_D2/merged
  - A-continued ckpt400: /root/autodl-tmp/output/formal_A_continued/checkpoint-400-merged
  - A-continued final: /root/autodl-tmp/output/formal_A_continued/merged
- 活跃进程：eval_A_continued_final 可能刚完成（PID 118930, tmux=train_a_continued, cuda:0）
- Cron：eval_A_continued_final（interval 300s）——Worker 正在检查是否完成

### 3. 📊 当前状态
**刚做完**：向 Director 汇报 7/8 组对比表 + ablation 分析。确认 GPU 1 空闲。

**等待中**：
- Worker `worker_eval_collect_a_continued_final_v2_20260513T231858` 正在检查 eval_A_continued_final 是否完成并收集 metrics
- 收到结果后需要：推 registry 到 DONE、删 cron、汇报完整 8/8 表给 Director
- Director 等用户方向决策（MVP FAIL 后下一步）

**Registry RUNNING**：eval_A_continued_final（唯一）
**Registry PREPARING**：exp_004_d1_v3, exp_004_d1_v2, exp_004_d1_f1_dominant（历史残留，已 killed/failed）

### 4. 📋 待办
- Worker eval_collect_a_continued_final_v2 回调 → 检查 metrics 是否已写入 registry → 如未写则手动补 → 推 DONE → 删 cron → 汇报完整 8/8 表给 Director
- 如果 eval_A_continued_final 仍在跑（cron 误判） → 等下一轮 cron 触发
- Director/用户给出方向决策 → 按指令启动新实验或调整 narrative
- 8/8 表完成后 → 更新 report.md + memory.md

### 5. 🎯 战略上下文
**核心结论**：Conformance reward 不提升零样本迁移。A-cont ckpt400（F1-only, 900步）vs D2 ckpt400（F1+conf, 900步）在 CrossNER 零样本上差距 <0.5pp。D2 观察到的零样本提升归因于"更多训练步数"，非 conformance reward。

**决策链**：D005（MVP 首轮未达标 B<A）→ D006（D1/D2 调参）→ D009（D2 初步 PASS）→ D010（Reviewer CONDITIONAL PASS，要求 ablation）→ D011（A relation_f1 基线修正）→ D012（MVP 翻转 FAIL）

**易错点**：
- D2 step 460 出现 mode collapse（frac_reward_zero_std=0.55, grad_norm=0），导致 relation_f1 下降。不要把 D2 relation_f1 低归因于"conformance reward 有害"——可能是训练不稳定
- D1 v4（500步 F1-dominant 75:25）是最高效单步配置，entity_f1=0.4966, relation_f1=0.2913。如果用户想 pivot，D1 v4 的 reward weighting 是有价值的方向
- 串行 eval 在同一 tmux session 中运行时，cron PID 监控会在第一个 eval 完成时误触发——上次就出现过这个问题
- 7/8 表已汇报 Director，只差 A-cont final 一行。数据齐全后立即补发
