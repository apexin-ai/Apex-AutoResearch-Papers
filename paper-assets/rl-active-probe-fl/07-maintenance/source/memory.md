# 实验进度报告 — 2026-05-14 19:40

## 1. GRPO v2 训练（最高优先级）

| 项目 | 值 |
|------|-----|
| 进程 | PID 30171, State: R (running), cuda:0 |
| 当前 step | **4/73** (5.5%) |
| 每 step 耗时 | ~10 min |
| 预估剩余时间 | **~11h 50min**（约明早 07:30 完成） |
| reward_mean | **尚不可知** — logging_steps=5，step 5 时才会输出第一条 reward 指标 |
| checkpoint 输出 | 空（save_steps=50，尚未触发） |

**注意事项**：
- 当前跑的是**第二次启动**（18:57:53 启动）。第一次运行（15:14→15:55）已崩溃（wandb EOF，无 checkpoint）
- 第二次运行的 wandb 可能未正确初始化（wandb/ 目录下最新 run 仍是第一次的 v93btbiu）
- 需要等 step 5（约 10min 后）才能看到 reward 信号
- **stdout 全缓冲问题**：nohup 重定向导致 TRL PrinterCallback 的 metrics 卡在内存 buffer，日志文件看不到 reward/loss。可能需要等 buffer 填满或 checkpoint 的 trainer_state.json 才能确认

**行动建议**：等 step 10+ 或 step 50 checkpoint 时读 trainer_state.json 确认 reward > 0。

## 2. eval-sft-v2-ckpt ✅ 已完成

202/202 样本全部评估完成，结果已保存到 `results/eval_sft_v2_ckpt.json`。

| 指标 | SFT v1 ckpt (eval-sft-v2) | SFT v2 ckpt (eval-sft-v2-ckpt) | Base (v3) |
|------|-----|-----------|------|
| debug_accuracy | **0.767** [0.713, 0.822] | 0.762 [0.713, 0.812] | 0.748 [0.688, 0.807] |
| probe_executed | 0.594 [0.530, 0.658] | 0.584 [0.525, 0.644] | 0.599 [0.535, 0.658] |
| probe_diagnostic | **0.129** [0.084, 0.173] | 0.134 [0.094, 0.173] | 0.104 [0.064, 0.149] |
| probe_dependent | 0.149 [0.104, 0.198] | 0.144 [0.104, 0.183] | 0.153 [0.109, 0.203] |
| probe_generation_rate | 0.990 | 0.985 | 1.000 |

**小结**：SFT v1 与 v2 checkpoint 在 eval 上无显著差异（76.7% vs 76.2%），训练时禁用 thinking 对 SFT 没有影响。SFT 比 Base 在 debug_accuracy 上提升 +1.9pp，probe_diagnostic +2.5pp，但幅度小且 CI 重叠。

## 3. Qwen3-30B-A3B 下载

| 项目 | 值 |
|------|-----|
| 已下载 | 50GB，14/16 个 .safetensors 文件 |
| 缺失文件 | model-00013-of-00016, model-00015-of-00016 |
| 完成度 | **~87%**（差 ~7.6GB） |
| 状态 | 仍在下载中（最新文件修改时间 18:39） |

**注意**：最新文件修改时间为 18:39，距现在已过约 1 小时。可能下载已停滞，需确认下载进程是否存活。

## 4. 经验教训

- **eval 脚本 cron 误报**：evaluate.py 完成后没有写 sentinel 文件或注册 W&B run，导致 cron 误判为 failed。后续应给 eval 脚本加 `touch ~/runs/{project}/{exp_id}.done` sentinel 输出。
- **nohup stdout 缓冲**：Python 通过 nohup 运行时 stdout 全缓冲，TRL metrics 不会实时 flush 到日志。应使用 `PYTHONUNBUFFERED=1` 或 `python -u` 启动训练。
