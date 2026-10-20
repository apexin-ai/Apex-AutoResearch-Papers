---
loop: 4
reason: max_wall_time
updated: '2026-05-14T10:00:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235 的 cuda:0 和 cuda:1（仅此两张，项目配置 gpu_ids）
- 355M 实验路径约定：seed=42 用 `results_medium_{method}/`，seed≠42 用 `results_medium_{method}_seed{seed}/`——脚本依赖此命名
- chain 脚本中 `CUDA_VISIBLE_DEVICES` 映射物理 GPU，脚本内部始终 `--gpu_ids 0`
- 实验无 W&B，指标全在本地 `all_results.json` / `metrics.json`——cron 检测到进程退出会报 "no W&B data"，这是正常的，需要人工 SSH 读日志判断成功/失败
- Table/正文数字必须标注 n（几个 seed 的 mean），当前 355M 是 n=2 (seed=42,123)，seed=456 完成后改 n=3

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，root@westd-11235
- 工作目录：`/root/div_cal_verify/`
- 结果目录：`/root/autodl-tmp/div_cal_verify/results_medium_*`
- 日志目录：`/root/autodl-tmp/div_cal_verify/medium_*.log`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/paper/`
- 活跃 tmux sessions：
  - `chain_cuda0_seed456`：cuda:0 跑 uncurated_seed456（完成后自动接 rgds_seed456）
  - `medium_external_seed456`：cuda:1 跑 external_seed456
  - `auto_seed456_cuda1`：轮询 external_seed456，完成后自动启动 chain_cuda1_seed456（random50_seed456）
- Crons：medium_external_seed456, medium_uncurated_seed456

### 3. 📊 当前状态
刚完成：medium_random50_seed123 DONE 确认 + registry 更新 + 论文 Table 2 更新为 2-seed mean + auto_chain_cuda1 确认正常。

**RUNNING（2 个）**：
- medium_uncurated_seed456 (cuda:0)：Gen 0/7，~19:50 CST 完成，之后 chain 自动接 rgds_seed456
- medium_external_seed456 (cuda:1)：Gen 3/7，~18:45 CST 完成，之后 auto-chain 接 random50_seed456

**PREPARING（2 个）**：
- medium_rgds_seed456：等 uncurated_seed456 完成后由 chain_cuda0_seed456 自动启动
- medium_random50_seed456：等 external_seed456 完成后由 chain_cuda1_seed456 自动启动

**等待中**：
- Worker `worker_code_enhance_355m_stat_script_20260514T095906` 正在运行（增强统计检验脚本：Bootstrap CI + 不对称 gap 模式 + LaTeX 输出）——回调到了需要读结果并汇报 Director
- Cron 回调：uncurated_seed456 和 external_seed456 完成时触发

### 4. 📋 待办
- Worker enhance_355m_stat_script 回调到 → 读结果，汇报 Director 脚本就绪状态
- external_seed456 cron 回调（进程退出）→ SSH 读日志确认完成 → update_registry DONE + 填 metrics → 确认 auto-chain 已启动 random50_seed456 → update_registry random50_seed456 RUNNING + register_cron
- uncurated_seed456 cron 回调 → 同上流程 → 确认 chain 自动接 rgds_seed456 → update_registry rgds_seed456 RUNNING + register_cron
- rgds_seed456 完成 + random50_seed456 完成 → seed=456 全部 DONE → 运行 `python analyze_355m_3seed.py` → 填论文 7 个 %TODO(355M-seeds) placeholder → 汇报 Director
- 全部 3-seed 数据就绪 → 更新 Table 2/Table 3 为 n=3 mean±SD → 更新 §5.7 百分比 → 移除所有 "pending" 标注

### 5. 🎯 战略上下文
- **核心 story**：Embedding Alignment Gap——内部嵌入的几何多样性与内容多样性在迭代自训练中系统性失对齐，RGDS 基于内部嵌入选择反而加速 collapse
- **C3 跨 2-seed 已确认**：Random 71.40 < External 78.65 < RGDS 86.55 < Uncurated 89.36（355M mean）
- **DDL**：EMNLP 2026 ARR 2026-05-25（还剩 11 天）
- **seed=456 全部完成预计 ~22:50 CST 今天**，之后跑统计检验 + 填论文数据 = 核心实验收官
- **易错点 1**：cron 报 "no W&B data" 不等于失败，这些实验都没配 W&B，必须 SSH 读日志判断
- **易错点 2**：RGDS seed=123 gen7 PPL=90.25（比 seed=42 的 82.84 高很多），这不是 bug 而是 seed variance——这正是为什么需要 3-seed 统计检验
- **易错点 3**：论文中 gap 百分比要用 mean 算（不是单 seed），当前 +21% 是基于 2-seed mean，seed=456 完成后需重算
- **Scaling narrative**：355M collapse 比 125M 更温和（双假说：表征冗余缓冲 + ceiling effect），ratio 作为鉴别指标而非因果证据（D020-D023 决策链）
