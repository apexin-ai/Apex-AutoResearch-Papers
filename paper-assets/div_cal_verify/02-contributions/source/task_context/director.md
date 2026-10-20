---
loop: 3
reason: max_messages
updated: '2026-05-14T07:15:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（2×RTX PRO 6000 98GB），不可用其他服务器或 GPU
- 355M 数据统一用 3-seed 均值（125M）对比 seed=42/123/456（355M），不可混用单 seed 值当主效应量
- S3（random pruning as regularizer）已被 D017 降级为 directional observation，论文中不可做因果推断
- 50% vs 100% 对比混淆数据量效应，只有 within-budget 对比（RGDS vs Random, 同 50%）无混淆——论文表述必须区分

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 `/root/div_cal_verify/`（远程代码/脚本/数据）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/`（论文/framing/registry/ROADMAP）
- 结果目录：`/root/autodl-tmp/div_cal_verify/results_medium_*/`
- 统计分析脚本：`/root/div_cal_verify/analyze_355m_3seed.py`（已就绪，3 seed 完成后重跑出完整统计）
- seed=456 chain 脚本：`chain_cuda0_seed456.sh`（uncurated→rgds→random50）、`run_medium_external_seed456.sh`（cuda:1）
- 活跃进程（截至 handoff）：
  - cuda:0: random50_seed123（chain 尾部）
  - cuda:1: external_seed456（刚启动，Worker 确认中）
  - tmux sessions: chain_cuda0_s123, auto_cuda1（衔接机制）, medium_external_seed456（可能）

### 3. 📊 当前状态
**刚做完**：seed=123 三个实验完成（uncurated/rgds/external），registry 已更新 DONE。发现 RGDS vs Uncurated 跨 seed 排序翻转（重要）。Paper Agent 已修正 §5.7 + Table 3。paper_framing.md 已同步所有发现（D017 S3 降级 + D020 scaling narrative + 排序翻转 + ratio 数据）。

**RUNNING**：
- medium_random50_seed123 (cuda:0, Gen 0/7) — seed=123 最后一个
- medium_external_seed456 (cuda:1, 刚启动) — seed=456 第一个

**PREPARING/QUEUED**：
- medium_uncurated_seed456 / medium_rgds_seed456 / medium_random50_seed456 — 脚本就绪，等 cuda 空出

**等待中**：random50_seed123 完成 → cuda:0 启动 chain_cuda0_seed456

### 4. 📋 待办
- random50_seed123 完成 → 更新 registry + cuda:0 启动 chain_cuda0_seed456（uncurated→rgds→random50 串行）
- random50_seed123 数据到手 → 确认 C3 在 355M seed=123 成立（RGDS > Random same budget）
- seed=456 全部完成 → 运行 analyze_355m_3seed.py → 3-seed t-test + Cohen's d + ratio 汇总
- 355M 3-seed ratio 均值 >0.8 且 SD<0.05 → 加强 genuine attenuation 表述；ratio 方差大 → 两假说等权
- 不对称 gap 3-seed 验证（External/Uncurated gap 扩大 vs RGDS gap 缩小）→ 如果 robust，考虑升级到 Abstract/Intro
- 统计分析完成 → 派 Paper Agent 最终 patch：填入 3-seed 数据替换所有 %TODO(355M-seeds)
- 全部完成 → 提交 Group C 审稿（submit_paper_to_review）

### 5. 🎯 战略上下文
- **核心决策链**：D009(MVP pass) → D014(framing revised) → D017(S3 降级) → D018(3 claim 跨 seed 稳健) → D019(追加 seed=456) → D020(scaling narrative 双假说共存)
- **论文最强点**：C3 RGDS vs Random +74%(125M) 是最 clean 的 ablation；不对称 gap 模式是 ceiling effect 的有力反驳
- **易判断错的事**：
  1. 355M RGDS vs Uncurated 排序不稳定（跨 seed 翻转），不要对此做定性结论——只有 RGDS vs Random（same budget）是稳定的
  2. paper_framing.md 中 125M 数值必须用 3-seed 均值（+7.4%/+8.9%），不是 seed=42 单值（+5.3%/+16.4%）
  3. Discussion §6.3 "绝对差缩小"不能用来排除 ceiling effect（逻辑有误，已修正为 "consistent with but not diagnostic of"），不对称方向分析才是真正的论证
  4. Paper Agent 声称修改了不等于真改了——上轮 Table 3 External-only 声称已补但 Reviewer 发现未生效，需要验证交付
- **DDL**：EMNLP 2026 ARR 2026-05-25（还有 11 天），时间充裕
