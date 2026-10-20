---
loop: 2
reason: max_wall_time
updated: '2026-05-12T23:03:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:5（gpu_ids 白名单）。代码里 GPU guard 已改为默认 "5"，不要改回 "0"
- 服务器 cqa1-21977 用 conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不存在 .venv
- 模型用本地 ModelScope 下载路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/`，不要用 HF hub name
- submit_training_job 命令不要带 `> file.log 2>&1` 重定向（会覆盖 tmux pipe-pane 日志捕获）
- v3 实验使用 `HF_HUB_OFFLINE=1` 离线模式

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，用户 root，工作目录 `/root/min_necessary_circuit_css/`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/`（Qwen-2.5 0.5B，Phase 2 用）+ GPT-2 Small（auto-circuit 内置）
- 本地 artifacts：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/`
- 活跃进程：v3 实验 PID 279210, tmux=mvp_pilot_gpt2_ioi_v3, cuda:5, cron 每 120s 监控
- 日志：`~/runs/min_necessary_circuit_css/mvp_pilot_gpt2_ioi_v3.log`

### 3. 📊 当前状态
刚完成：CIRCUS deep dive（novelty 确认）、Phase 2 框架修复（4 项）、D013 non-nesting 修复、gate 逻辑审核（全 PASS）。已向 Director 汇报两轮。

registry:
- `mvp_pilot_gpt2_ioi_v3` RUNNING — GPT-2 Small / IOI / K=3, ACDC 多阈值扫描进行中（τ=0.01, 1/5, 62.8%），EAP-IG + EP 已缓存完成。**预计还需 ~5h**
- `mvp_pilot_gpt2_ioi_v2` DONE(failed) — 缓存污染被 kill
- `mvp_pilot_gpt2_ioi` DEPLOYED — 初版被 kill

等待中：v3 cron 完成回调（进程退出 → 需要人工判定）

### 4. 📋 待办
- v3 cron 回调到达（进程退出）→ spawn Worker SSH 运行 `analyze_mvp_results.py` → 读 off_diagonal_pct → gate 判定（≥10% Main / 5-10% Findings / 2-5% Marginal / <2% Kill）→ update_registry + 汇报 Director
- Gate = PASS_MAIN → 部署 Phase 2 代码到服务器（`deploy_phase2.sh`），提交 Qwen-2.5 0.5B / IOI / K=3 实验
- Gate = PASS_FINDINGS → 追加 Arithmetic 任务到 Phase 2 configs
- Gate = MARGINAL/KILL → 产出 red-section Framing 调整提案，禁止默跑下一个实验
- Phase 2 部署前：需要把 D013 修复（css.py + run_circus.py）同步到服务器

### 5. 🎯 战略上下文
- 项目目标：证明 cross-method binary consensus (CSS) 比单方法 circuit 更鲁棒，投 EMNLP 2026 Main（ARR 2026-05-25，剩 13 天）
- CIRCUS (arXiv 2603.00523) 是最大 novelty 威胁，但已确认只做 intra-method 阈值变化，不做跨方法。CSS 定位为 CIRCUS 的跨方法推广
- Mondorf et al. 是第二威胁（连续分数聚合 vs 二值共识），workshop 短文非完整方法贡献
- 决策链：D001(MVP gate 标准) → D007(GPU guard cuda:5) → D010(IFR binarization unique_score_rank) → D011(EP 架构重写) → D013(CIRCUS non-nesting 2D grid)
- 易错点 1：analyze_mvp_results.py 有两层 off-diagonal（2^K 和 CIRCUS-core×CSS），gate 用的是后者（`xtab["off_diagonal_pct"]`），不要混淆
- 易错点 2：ACDC 在 GPT-2 Small 上极慢（每 τ ~70min），5 个阈值共 ~6h，不要以为卡住了就 kill
- 易错点 3：Worker pool < 2 = 失职，v3 在跑时应该并行铺 CPU 任务（文献、代码准备、论文起草）
