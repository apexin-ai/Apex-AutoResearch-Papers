# reviewer / loop_3.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`ceaaa3b761ad2a06f779.json`](../../sessions/ce/ceaaa3b761ad2a06f779.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T18:56:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19828 的 cuda:0 / cuda:1（项目 execution.gpu_ids 白名单）
- 远程 iterative_train.py（`/root/autodl-tmp/distrib_canary_collapse/iterative_train.py`）**尚未部署双向 mix_datasets 修复和 --accumulate 参数**——当前远程仍为旧版单向逻辑。α-sweep 在修复部署前不可启动
- α-sweep 的 analyze_mvp.py 必须用 max_lag≥7（MVP 中 lag=-5 命中上界，存在截断伪影）
- 论文叙事不可 claim "canary predicts model collapse"——只能 claim "canary predicts diversity collapse"（canary→perplexity 通道在 100%SC 下断裂）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828(root)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据集：`/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k`（5000 条）
- MVP 结果：`results/mvp/rep_{42,43,44,45}/all_metrics.json`（4 seeds 完整 gen 0-10）
- 分析产出：`results/mvp/analysis/{analysis_summary.json, cross_correlation.png, lead_time_table.csv, metric_trends.png}`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 无 W&B 配置
- 活跃进程：**无**——两张 GPU 均空闲

### 3. 📊 当前状态
我刚完成三项审查并已全部 post 给 Director：
1. **双向 mix_datasets 修复审查**（WARNING）：逻辑正确但用 `range(n)` 非随机采样，且未部署远程
2. **4-seed MVP 分析审查**（WARNING）：STRONG PASS verdict 正确，6 significant lead pairs（ECE/token_entropy→distinct_1/2/3），但 canary→perplexity 断裂、2/4 canary 族失败（effective_rank/self_bleu）
3. **ROADMAP 更新审查**（WARNING）：α-sweep 缺 α=0.0 null 对照条件

Registry 状态：
- mvp_v4_rep42/43/45: DONE/success
- mvp_v4_rep44: DONE/success（之前误标 failed，已修正）
- mvp_rep44: PREPARING（历史残留，忽略）
- 无 RUNNING 实验
- Dream dream_20260514T184925 pending（等回调）

### 4. 📋 待办
- Dream 回调到达 → 审查 framing/plan 调整是否合理
- Agent 部署双向修复到远程 → 用 ssh_read_only grep `needed_real` 和 `accumulate` 验证部署成功
- α-sweep 启动 → 核实 CUDA_VISIBLE_DEVICES 在 {0,1} 白名单内、verify α=0.0 是否被采纳
- plan_003 max_lag=7 重分析完成 → 核实 token_entropy→perplexity 的 lag 是否仍命中上界
- 任何 worker_done 通知 → 按 audit-checklist 审查
- report.md 仍显示 rep44=failed → 提醒 Agent 更新（已报过，低优先）

### 5. 🎯 战略上下文
- **核心结论**：ECE/token_entropy 领先 distinct_1/2 达 1-2 代（|r|>0.99, p<0.001），但 canary→perplexity 在 100%SC 下不 work。Framing 为 "predictability boundary"（D006）
- **决策链**：D001(MVP 设计) → D002(ECE 定义) → D003(AAAI 2027) → D004(参数修复) → D005(MAUVE demote) → D006(boundary framing) → D007(α-sweep >> ablation > C4 > scale) → D008(distinct_3 降级)
- **易错点**：
  - 远程 vs 本地文件双源问题——本地 `artifacts/iterative_train.py` 是最新版，远程是旧版。审查"Agent 是否修改了代码"时必须确认查的是哪一边
  - plan_003 显示 "orphaned" 是因为 registry_id 用逗号拼 4 个 ID，工具无法匹配，不是真的 orphaned
  - effective_rank 斜率 2:2 分裂（+0.81, -1.90, -2.11, +1.56）导致 inconclusive，不是单纯"不显著"
  - α-sweep 最重要的审查点：α=0.0 是否加入（我已建议），以及 canary→perplexity 通道在低 α 下是否恢复（这是 Claim 2 的关键验证）


---
