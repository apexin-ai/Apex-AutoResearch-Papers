---
loop: 2
reason: max_messages
updated: '2026-05-16T02:42:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 rtx6000-diagprobe 的 cuda:0 / cuda:1（项目配置白名单）
- 预注册标准（D002/D003）不可修改：MVP-v2 的 pass/fail 用 ρ<0.5 + signal mean 退化 ≥15% + 2 seed 一致
- 论文/报告参数必须从实际代码读取，禁止从 IDEA_BRIEF 复制（C002 约束，已因 8 处不匹配被 Reviewer critical）
- spectral_rank 因基线 |ρ|=0.211 结构性失败，不可能贡献 pass，只做辅助观测
- Condition 2 检查的是 signal mean（entropy_mean）退化，不是 |ρ| 退化（D004 裁定）

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/prism_collapse_mixing
- Python：系统 python3（非 conda/venv）
- 模型：Pythia-410M-deduped (`EleutherAI/pythia-410m-deduped`)
- 数据：FineWeb real pool ~400M tokens，probe set 5000×256 tokens
- 关键脚本：run_pipeline.py（`--num_generations` 可配置）、generate_synthetic.py、train.py、compute_signals.py、analyze_correlation.py（含 bootstrap）、plot_collapse_trajectory.py
- 结果目录：/root/prism_collapse_mixing/results/
- 图表目录：/root/prism_collapse_mixing/figures/
- 活跃进程：run_pipeline.py 自动管道运行中（gen2 信号计算阶段），无 tmux/cron

### 3. 📊 当前状态
Gen2 训练已完成，正在做 CPU-bound 的 compute_signals（seed42 ~36%, seed137 ~31%，预计 ~02:50 UTC 完成）。信号计算完成后 pipeline 自动推进分析+可视化。

Registry：mvp_collapse_decoupling_v2 RUNNING（唯一活跃实验）；mvp_collapse_decoupling DONE(failed)。

已完成的并行任务：bootstrap CI 实现 ✓、plot_collapse_trajectory.py ✓、5 代代码适配确认 ✓、figure_layout.md ✓、paper_skeleton.md 参数修正 ✓（Reviewer 验证通过）、§3.2.4 Gram matrix 描述修正 ✓。

等待：Gen2 信号计算完成 → pipeline 自动输出 Gen2 metrics → 这是 D007 决策门的关键数据。

### 4. 📋 待办
- Gen2 metrics 出来 → 立即看 Δρ(Gen1→2)：≥0.03 = 加速信号，执行 MVP-v3（从 Gen3 续跑到 Gen5）；0.02-0.03 灰区 = 先完成 Gen3 再决定；<0.02 = 重新评估实验条件
- Gen2 bootstrap CI 不重叠 → entropy ρ 下降趋势持续，正向信号
- Gen3 完成 → 按 MVP-v2 预注册标准判定 pass/fail（ρ<0.5 + entropy_mean 退化 ≥15% + 2 seed）
- MVP-v2 判定 fail（大概率）→ 按 D006/D007 启动 MVP-v3（5 代扩展，统计检验框架）
- MVP-v3 pass 标准（新预注册）：bootstrap CI + effect size + permutation test 为主，统计检验为辅（n=6 功效不足）
- real_pool 问题：5 代时每代仅 ~80M real tokens < 100M synthetic/代，混合比偏离 1:1，可能需要扩大 real pool 到 500M+

### 5. 🎯 战略上下文
决策链：D001(MVP 方案) → D002(量化 pass/fail) → D003(entropy 为主信号) → D004(Condition 2 = signal mean) → D005(预判 3 代 fail，准备 5 代 contingency) → D006(MVP-v3 预设计：续跑+统计检验) → D007(修正：bootstrap CI 为主证据，补灰区协议)

核心判断：3 代 MVP 大概率 fail（Reviewer 预测 Gen3 ρ ≈ 0.75-0.85 vs 阈值 <0.5），但这不等于假设错误——文献支持 collapse 指数加速需要更多代。叙事方向："Decoupling has a latency period"。

易错点：
- 不要改 MVP-v2 的预注册标准（rationalize 风险，Reviewer 多次警告）
- MVP-v3 是新实验的预注册，与 MVP-v2 判定独立
- 论文写参数时必须 SSH 读代码，不要信 IDEA_BRIEF（已踩过坑）
- Gen0→1 ρ 下降 effect size=-5.8 看起来大，但这是 N=5000 bootstrap SE 很小导致的，不等于效应本身大（Δρ 只有 0.017）
