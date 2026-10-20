---
loop: 6
reason: max_wall_time
updated: '2026-05-14T11:17:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（westd-11235 双卡，项目 gpu_ids=[0,1]）
- selection ratio 代码实际计算 sel/rej（run_mvp.py line 294），但论文定义写的是 sel/pool——Director 已收到 WARNING，等待决策用哪种定义。**不要在修复前假设任一定义是"正确的"**
- medium_random50_seed123 的 registry 仍为 RUNNING（实验 16:29 CST 已完成），需要 Agent 补录——Reviewer 不能改 registry

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，代码 /root/div_cal_verify，数据 /root/autodl-tmp/div_cal_verify/
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：gpt2 / gpt2-medium（HuggingFace pretrained，TRANSFORMERS_OFFLINE=1）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify/
- 论文 tex：docs/paper/{introduction,results,related_work,references}.tex
- 关键脚本：analyze_355m_3seed.py（统计分析，已补 125M seed=456 数据）
- 活跃进程（截至 handoff）：
  - cuda:0: medium_uncurated_seed456（PID ~510381，tmux chain_cuda0_seed456）
  - cuda:1: medium_random50_seed456（18:42:59 启动，tmux chain_cuda1_seed456）
  - cuda:0 后续链：uncurated_seed456 完成后 → medium_rgds_seed456 自动启动（chain_cuda0_seed456.sh）

### 3. 📊 当前状态
**刚完成**：medium_external_seed456 审查（Gen7 PPL=83.00），确认 auto-chain cuda:1 触发 random50_seed456。

**Registry RUNNING**：
- medium_random50_seed123：实际已完成（PPL=72.55），registry 未更新
- medium_external_seed456：实际已完成（PPL=83.00），registry 未更新
- medium_uncurated_seed456：运行中 cuda:0
- medium_random50_seed456：刚启动 cuda:1

**PREPARING（未开始）**：
- medium_rgds_seed456：等 uncurated_seed456 完成后由 chain 自动启动 cuda:0

**待 Director 决策**：
- selection ratio 定义修复方案（sel/rej vs sel/pool）——我已推荐方案 1（改论文定义）
- scaling narrative 维持 dual-hypothesis（我已评估并建议不升级）

### 4. 📋 待办（条件触发式）
- medium_uncurated_seed456 完成 → 审查 Gen7 PPL + 确认 rgds_seed456 auto-chain 触发 + GPU 合规
- medium_random50_seed456 完成 → 审查数据 + 355M Random 50% 3-seed 统计（可与 External 3-seed 做首对 t-test）
- medium_rgds_seed456 完成 → 审查 + **此时 355M 全部 4×3 完成**，触发 analyze_355m_3seed.py 全量统计，审查输出
- 355M 全量统计完成 → 审查 results.tex Table 2/3 更新、§5.7 scaling section 全文、asymmetric gap test CI
- Director 决策 ratio 定义 → 审查对应的论文/代码修改一致性
- citation 遗留：laurent2024feature 和 karwowski2024goodhart 仍未外部验证

### 5. 🎯 战略上下文
- **核心结论**：内部 embedding 做多样性选择会加速 model collapse（C1-C3 已在 125M 3-seed 确认，p<.05, |d|>4）。355M 方向一致但等 3-seed 统计。
- **paper_framing.md 关键决策链**：D013(C3 升级) → D014(C2-revised) → D017(S3 降级) → D018(三 claim 确认) → D020(scaling dual-hypothesis)
- **易判断错的事**：
  1. 不对称 gap 模式看起来很强，但 ceiling effect 也能解释——**不要升级为 claim，保持 observation**
  2. 125M seed=456 ratio=0.868 是异常值（其他两 seed ~0.52），导致 125M ratio SD=0.20 极大——跨 scale ratio 比较无统计力，不要做 t-test
  3. RGDS vs Uncurated 在 355M 排序跨 seed 翻转（seed=42 uncurated 最差，seed=123 rgds 最差）——论文已正确处理为"ordering instability"，不要试图 claim 固定排序
  4. 论文 TODO 注释（4 处）全是等 seed=456 的占位符，不是遗漏
- **DDL**：EMNLP 2026 ARR May 25，距今 11 天。355M 全部实验预计今晚 ~22:50 CST 完成，时间充裕。
