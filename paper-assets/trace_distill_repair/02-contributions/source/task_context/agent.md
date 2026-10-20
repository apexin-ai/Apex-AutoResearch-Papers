---
loop: 5
reason: idle_timeout
updated: '2026-05-15T16:07:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 rtx6000-diagprobe cuda:0 + cuda:1**，不得用其他设备
- API key 加载：submit_training_job 命令必须 `source /root/trace_distill_repair/.env`，不能用 `.bashrc`（有 non-interactive guard）
- v2 进程 PID 131777 **不要 kill**——已三次误判死亡（D025/D029/D030），API retry backoff 会导致长时间静默，不等于进程挂了
- BugsInPy 测试必须在 `conda activate bugsinpy`（Python 3.8）中运行，不是 base（3.12 导致 9/13 oracle fail）
- 测试文件必须从 **fixed commit** checkout（buggy commit 缺新增 test method → ERROR 而非 FAIL）

### 2. 🖥️ 基础设施快照
- 服务器：**rtx6000-diagprobe**，工作目录 `/root/trace_distill_repair`
- Python：`/root/miniconda3/bin/python`（conda base），测试用 bugsinpy env
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- API keys：存于 `/root/trace_distill_repair/.env`（OPENROUTER_API_KEY 等）
- 数据/产出：`/root/trace_distill_repair/pipeline_output/`
- 日志目录：`~/runs/trace_distill_repair/`
- 活跃进程：
  - mvp_phase3_repair_v2: PID 131777（非 registry 里的 130226），tmux session，cuda:0，deepseek-v4-pro，10/14 完成
  - mvp_strong_model_disambig: PID 141440，tmux session，cuda:1，Claude Sonnet 4，刚启动
- Cron：mvp_strong_model_disambig 有活跃 cron 监控

### 3. 📊 当前状态
两个实验同时 RUNNING：

1. **mvp_phase3_repair_v2**（v4-pro，10/14 完成）— 剩余 tornado_2(2/4) + youtube-dl_1/5/20。已跑 2.5h+，API retry backoff 导致慢。10/14 H2H：structural vs no_trace **3-3-4 持平**，line vs no_trace 4-2-4 领先，**line 明显优于 structural（6-3-1）**。核心 claim "structural > line" 在 v4-pro 上被否定。

2. **mvp_strong_model_disambig**（Claude Sonnet 4，0/14）— 14 实例 × 4 条件，预计 ~30min。单例验证 cookiecutter_1 已通过（v4-pro 全 FAIL 的 test_pass，Sonnet 4 能 pass）。这是 C001 最终判定实验。

所有 Worker 均已完成（20 个 done），无等待中的 Worker 回调。

### 4. 📋 待办（条件触发式）
- **mvp_strong_model_disambig cron 回调到达** → spawn Worker 分析结果，计算 H2H（structural vs line vs no_trace vs full_trace），与 v4-pro 数据对比。若 structural > line → 原 claim 成立（v4-pro floor effect）；若 line > structural → 必须 pivot framing（Option B: compression narrative）
- **mvp_phase3_repair_v2 完成 14/14** → 从 checkpoint 重新计算完整 H2H（当前 10/14 是中间数据），更新 registry metrics
- **两个实验都完成** → C001 最终判定：(a) 强模型 structural > no_trace 且 test_pass > 0 → MVP PASS，进入 Research 阶段；(b) 否则 → 产出 Framing 调整提案（3 个 narrative 备选），报 Director
- **3 个 test infra 待修** → black_1, fastapi_2, tornado_2 的 oracle 需从 fixed commit checkout test 文件（修复后 oracle 14/14）。优先级低于等实验结果，但强模型完成前可并行修

### 5. 🎯 战略上下文
- **核心张力**：项目原 claim 是 "structural filtering > line filtering"，但 v4-pro 10/14 数据 H2H 1-3-6 否定了这一点。强模型实验是 tiebreaker——如果 Claude Sonnet 4 翻转结果，说明 v4-pro 能力不足（floor effect）导致无法区分；如果复现，需要 pivot framing
- **D032 修正**：之前的 "稀释假说"（structural_keep=0 实例拉低均值）不成立——Tier 1 仅 1/14 (httpie_2) structural_keep=0
- **决策链**：D018 淘汰 token efficiency narrative → D031 批准强模型消歧 → 等结果做 C001 判定
- **易踩坑**：(1) v2 进程 PID 131777 会长时间静默（API backoff），不要误判死亡；(2) registry 里 mvp_phase3_repair_v2 的 PID 是 130226（旧），实际运行的是 131777；(3) full_trace 在 v4-pro 上是唯一有 test_pass 的条件（1/9），这可能暗示 more trace > less trace，与 structural 压缩路线矛盾
- **DDL**：5/25 已放弃，瞄准 August ARR
