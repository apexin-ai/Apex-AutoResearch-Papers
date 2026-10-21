# agent / loop_26.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_26.md`
- **Structured JSON:** [`64b3ac10ca9d31c10c7e.json`](../../sessions/64/64b3ac10ca9d31c10c7e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 26
reason: idle_timeout
updated: '2026-05-21T13:51:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3（seetacloud-westd-4x5090），4 张 RTX 5090 32GB，无其他服务器
- train_unified.py `--task cwm` 默认加载 function-level 数据，必须显式传 `--train_file swebench_full/swebench_train.jsonl` 才是 repo-level
- `kill &lt;timeout_PID>` 会 SIGTERM 整个进程组含训练子进程——长训练必须用 submit_training_job 或 nohup，不用 timeout wrapper
- Qwen CWM eval batch=1 耗时 30-50h，会撞 DDL。必须先在 GPU 1 做 batch test 确定安全 batch size 再提交
- DeepSeek CLS s123 = 74.93 是 known outlier（NaN eval_loss），论文中已标注，不要当正常数据引用
- Qwen 训练 ETA 含 eval_steps 开销（tqdm 不计入），实际比 tqdm 显示慢 ~15-20%

### 2. 🖥️ 基础设施快照
- **服务器**: seetacloud-westd-4x5090，工作目录 `/home/sonny/exec-sim-repair-verifier`
- **Python**: 服务器用 conda（aml-train 镜像），`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**: DeepSeek → `/root/autodl-tmp/` 下；Qwen → HF cache
- **Checkpoints**: `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456_v2/`（DS s456）；`runs/exec-sim-repair-verifier/` 下各实验目录
- **活跃进程**:
  - GPU 0: qwen3-8b-cwm-repo-s123-train-v4, PID 4271, monitor PID 4871
  - GPU 1: deepseek-cwm-repo-s456-e3-eval（刚启动，cron 跳过首次 poll）
  - GPU 2: deepseek-cwm-repo-s123-train-v3, PID 28200（由 watch_s123_eval_then_resume.sh PID 817 自动启动）
  - GPU 3: qwen3-8b-cwm-repo-s456-train-v3, PID 4561, monitor PID 4883
- **Crons**: 4 个活跃，全部 still running / just created

### 3. 📊 当前状态
4 个 RUNNING 实验占满全部 GPU，0 个活跃 Worker。

| exp_id | GPU | 进度 | ETA (UTC) |
|--------|-----|------|-----------|
| qwen3-8b-cwm-repo-s123-train-v4 | 0 | ~80% | ~21:30 May 21 |
| deepseek-cwm-repo-s456-e3-eval | 1 | 刚启动 | ~12h after start |
| deepseek-cwm-repo-s123-train-v3 | 2 | ~64% | ~23:10 May 21 |
| qwen3-8b-cwm-repo-s456-train-v3 | 3 | ~81% | ~21:30 May 21 |

**等待中**: 无 Worker 回调；4 个 cron 监控中；多个 PREPARING 实验排队（包括 DS s123 eval、DS CLS resume、downsample eval、3-shot baseline 等）。

**文字打磨 + 图表修复**: 已完成。论文处于"等 CWM multi-seed 数据填 Table 3"状态。

### 4. 📋 待办（条件触发式）
- **Qwen s123/s456 训练完成（~21:30 UTC）** → 用 GPU 1 batch test 确定的 batch size 提交 Qwen CWM eval（2 个 eval 分别上 GPU 0 和 GPU 3）
- **DS s123 训练完成（~23:10 UTC）** → 提交 DS s123 3-epoch eval 上 GPU 2（使用修复后的 sort 脚本）
- **DS s456 e3 eval 完成** → 与 s42 epoch 3 (61.49%) 对比；填 Table 3 DS CWM s456 格
- **全部 6 个 CWM eval 完成** → 填充 Table 3 全部 CWM 格 → 跑 compute_supplementary_stats.py 更新统计 → scenario_a 叙事升级 → Round 7 内审
- **GPU 1 batch test 未完成** → 备选：Qwen 训练完成后在 GPU 0/3 用 `--max_samples 50` 快速测试
- **任何 CWM eval accuracy 显著偏离 s42 (61.49%)** → 汇报 Director，可能影响 CWM overfitting 叙事

### 5. 🎯 战略上下文
- **DDL**: ARR May 25（4 天），Round 7 内审 May 23
- **阶段**: D153 全力冲 accept，从 3.0 (Findings) → 3.5+
- **核心 story**: formulation 选择是 phase transition——function-level 等价（≤1.3pp），repo-level 分化 19-26pp，机制是 CWM format collapse
- **CLS/TRAJ multi-seed 全部完成**，唯一缺口是 CWM multi-seed（正在冲刺）
- **CWM 过拟合是已知风险**: train/eval loss 252x 差距，D161 已删除 "no overtraining" claim；epoch 2 vs epoch 3 数据待 s123/s456 确认
- **易错点**:
  - Qwen CWM eval 的 batch size 必须先测试，不能直接 batch=1 提交（会超 DDL）
  - DS s456 epoch 2 eval 已被 D162 kill，不要尝试恢复
  - `compute_supplementary_stats.py` / `integrate_cwm_results.py` / `plot_figure2_v2.py` 已修正过数据一致性问题（见 memory.md），新数据入 Table 3 后需重跑这些脚本
  - DeepSeek CLS vs TRAJ power=0.112，论文中必须加 exploratory caveat


---
