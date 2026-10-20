---
loop: 5
reason: max_wall_time
updated: '2026-05-14T15:14:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cqa1-38874 的 cuda:0（`get_project_status` gpu_ids 白名单）
- 实验 mvp_seed0_replication_r2 正在运行（PID 122208），**禁止修改服务器上 `/root/collapse-aware-mixing/` 的任何代码文件**，等 pipeline 结束后再动
- `analyze_seed0_vs_v7.py` 已部署在服务器上，实验完成后直接运行，不要重新部署覆盖
- seed0 r2 输出在 `/root/autodl-tmp/output_seed0/`，v7 输出在 `/root/autodl-tmp/output_v7/`——不要混淆或清理

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874，1× RTX PRO 6000 96GB
- 工作目录：`/root/collapse-aware-mixing/`
- Python：`/root/miniconda3/bin/python`（conda base，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：EleutherAI/pythia-1b（HF cache `/root/autodl-tmp/.hf_cache`）
- 数据：wikitext-103-raw-v1（HF Hub）
- 输出：v7=`/root/autodl-tmp/output_v7/`, seed0=`/root/autodl-tmp/output_seed0/`
- 活跃进程：PID 122208（tmux session，seed0 r2 pipeline），已运行 ~14h，cron 监控中
- 磁盘：134G/250G (54%)，充足

### 3. 📊 当前状态
**刚做完**：检查 seed0 r2 进度，确认 G1 metrics 完美重现 v7 上升趋势（eff_rank +1.32），已向 Director 汇报含逐代对比表。同时完成文献扫描（artifact: literature_scan_20260514.md），确认 negative result 有 novelty、Plan A 交叉空白仍在。

**Registry**：
- `mvp_seed0_replication_r2` RUNNING — G1 train+eval 完成，G1 generate 76%，预计 ~6-7h 完成 G2
- 其余 11 个实验全部 DONE（5 failed, 2 negative, 4 killed）

**等待中**：
- Cron 回调：seed0 r2 完成（PID 122208 退出时触发）
- Director 决策：Q2 vs archive 暂挂，等 G2 数据。Director 已确认 G1 重现上升趋势 → Plan A 方向成立

### 4. 📋 待办
- **seed0 r2 cron 回调（正常完成）** → 立即派 Worker SSH 运行 `python /root/collapse-aware-mixing/analyze_seed0_vs_v7.py`，产出完整 G0/G1/G2 逐代对比表 → 更新 registry（conclusion, checkpoint_path, log_path）→ 汇报 Director 附完整对比表 + Plan A/否定判断
- **seed0 r2 cron 回调（失败）** → 读 on-experiment-failed skill，诊断原因（最可能：磁盘满或 OOM），汇报 Director
- **Director 确认 Plan A** → 读 ai-time-discipline skill，准备 controlled experiment（代码已就绪），控制信号需从 eff_rank 切换到 n-gram entropy（见 memory.md 竞争格局段）
- **Director 选 Q2 negative paper** → 还需补 multi-scale (Pythia-410M/2.8B) 实验，ROADMAP 估计 ~3-4 天 GPU
- **Director 选 archive** → 释放 GPU，无后续

### 5. 🎯 战略上下文
**核心结论链**：D014 falsified C1 holdout eff_rank → D016 killed Direction C → D018 Pivot B no advantage → **三条路径全封，MVP FAIL**。但 seed0 replication 正在确认"holdout eff_rank 在 collapse 中反向上升"这一 negative result 的 seed robustness，这是 Q2 negative result paper 的基础。

**G1 中间结论**（已汇报 Director）：seed0 G1 eff_rank=678.21 vs v7 G1=678.30，差 <0.02%。上升趋势完美重现。G2 是最后一个数据点——v7 G2 eff_rank=683.44（+6.48 from G0），预期 seed0 G2 同样显著上升。

**易错点**：
- 不要混淆"Plan A = eff_rank 有用"和"Plan A = eff_rank 上升现象可复现"——这里 Plan A 指的是后者（negative result 可发表），不是 eff_rank 作为 collapse detector 有效
- 文献扫描建议 Plan A 如果继续做 controlled experiment，控制信号应换成 n-gram entropy / vocab coverage，不再用 eff_rank——**但这个决策权在 Director**
- literature_map.yaml 还差 9 篇新论文待补（详见 artifact literature_scan_20260514.md 第三节），不急但别忘
- 动态 data mixing 领域 2025H2-2026H1 论文密集，时间窗口 ~3 个月（memory.md 有记录）
