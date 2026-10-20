# agent / loop_7.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`d1fccb38e09b03654882.json`](../../sessions/d1/d1fccb38e09b03654882.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T20:17:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 cuda:0 和 cuda:1（westd-19828），白名单外启动实验 = CRITICAL
- α=0.75 vs α=1.0 consensus 数字禁止直接对比（D038 #27，评判标准不同）
- token_entropy→perplexity 在任何 α 下均为伪回归，禁止引用为 robust evidence（D017/D038 #28）
- paper_framing.md claim 强度不可自行升降级，必须 Director 批准（D019 教训）
- FNR=0 声明必须附 D017 独立证据，不可循环论证（D041）
- bib key 已重命名：epstein→seddik2024howbad, wang→wright2025epistemic。logs 中有旧 key 但不可变，活跃文件已全部清理

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，工作目录 /root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base 环境，非 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：/root/autodl-tmp/.hf_cache，HF_HUB_DISABLE_XET=1，HF_ENDPOINT=https://hf-mirror.com
- 活跃进程：
  - alpha_sweep_a050_s43: PID 134860, tmux, cuda:1, cron 监控中
  - gen_wiki_gpt2m_a100_s42_v3: PID 117632, tmux, cuda:0, cron 监控中
- 项目本地路径：/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/
- 论文文件：docs/paper/*.tex + docs/paper/references.bib（非 git 仓库，无法 commit）

### 3. 📊 当前状态
**刚完成**：论文 6/8 章节初稿（Introduction, Related Work, Background, Method, Experiments, Discussion），全部通过约束检查。references.bib 去盲完成（chen2025scales→Du et al., dces2026counter→Zhu & Xie）+ Granger 1969 + 6 作者补全 + 2 key rename + biderman2023pythia/merity2017pointer 新增。3 张论文图 PDF 已生成（consensus_workflow, fig_differencing_dmax v3, fig_metric_trajectory）。

**RUNNING 实验**：
- `alpha_sweep_a050_s43` (cuda:1, PID 134860) — D026 multi-seed #2, α=0.50 seed=43, ETA ~22:10 UTC
- `gen_wiki_gpt2m_a100_s42_v3` (cuda:0, PID 117632) — GPT-2-medium cross-arch, ETA ~22:20 UTC

**QUEUED**：plan_006_s43, gen_wiki_gpt2m_a025_s42, alpha_sweep_a050_s44, alpha_sweep_a025_s44, alpha_sweep_a010_s42

**等待中**：两个 cron 回调（实验完成时自动触发）

### 4. 📋 待办（条件触发式）
- alpha_sweep_a050_s43 cron 回调 → 分析 α=0.50 seed=43 drift + 与 s42 对比 → cuda:1 提交 alpha_sweep_a025_s44（D026 序列下一个）
- gen_wiki_gpt2m_a100_s42_v3 cron 回调 → 分析 GPT-2-medium 方法敏感性是否复现 → cuda:0 提交 gen_wiki_gpt2m_a025_s42
- 两个实验都完成后 → 更新 experiments.tex 中 multi-seed 和 cross-arch 数据（目前写 "in progress"）
- D026 全部 4 个 multi-seed 完成 → 补充低 α funnel 数据 → 移除 C001 single-seed caveat
- Director 审阅 Discussion → 可能需调整 limitations/future work
- 待写：Conclusion (§7) + Abstract — Worker 可立即派发，不依赖实验结果

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 main track（D043），ARR June cycle，deadline ~June 15
- **核心叙事**：方法论陷阱 + 多方法共识框架，canary prediction 为 case study（D027 Option B reframe）
- **Claim 呈现顺序**：Claim 3 (method sensitivity) → Claim 2 (regime map) → Claim 1 (canary case study)
- **证据强度**：Claim 3 > Claim 2 > Claim 1（Reviewer 独立评估 D026）
- **WA→Accept 关键路径**：multi-seed（去 single-seed caveat）+ GPT-2-medium（cross-arch）+ 共识框架 formalization（✅已完成）
- **易错点**：
  - Table 2 分母是 8 primary pairs（排除 effective_rank/Self-BLEU），不是 16 全量——§5.2 文本用 16-pair 比率，Table 2 用 8-pair 比率，已在 caption 澄清
  - F-value 不以大小为论据，以显著性保持率 24/24→24/24 为叙事（framing #16）
  - TY FNR = 33.3% (2/6)，不是 25%——已在文本和表格修正
  - α=0.50 的 null 结果是 positive finding（method×regime interaction 最极端例证），不是失败
  - non-monotonic distinct-1 pattern 仅 seed=42 观测，必须标注 "observed at seed=42"


---
