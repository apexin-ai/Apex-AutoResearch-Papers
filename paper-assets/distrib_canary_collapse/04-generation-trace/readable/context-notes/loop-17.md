# director / loop_17.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_17.md`
- **Structured JSON:** [`8e986c2260ffb92cecb3.json`](../../sessions/8e/8e986c2260ffb92cecb3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_messages
updated: '2026-05-21T23:11:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 cuda:0-5，westd-19828 cuda:0-1，共 8 张 RTX PRO 6000 Blackwell 98GB
- d102 是唯一有效分析脚本（`run_5method_analysis_d102.py`，downstream=mauve, threshold=true_3sigma_d105）。旧脚本用 perplexity+3x_sigma_drift，结果无效（M063/M064 教训）
- 所有 SSH 命令必须前缀：`export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1`
- T=15 α=0.45 PermG=6/8（不是 8/8，8/8 是旧脚本错误值，M063 修正）
- 提交实验前必须 `df -h /root/autodl-tmp` 确认 ≥30G 空闲（M065 磁盘爆满教训）
- Agent 汇报进度时要求 SSH 实际检查 gen_X 目录，不接受估算百分比（多次出现估算与实际严重不符）

### 2. 🖥️ 基础设施快照
- westd-17855：6× RTX PRO 6000 Blackwell 98GB，磁盘 ~61% used (~340G free)
- westd-19828：2× RTX PRO 6000 Blackwell 98GB，磁盘 ~40% used (~530G free)
- 工作目录：/root/autodl-tmp/distrib_canary_collapse/（两台服务器相同）
- Python/conda：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：/root/autodl-tmp/.hf_cache（TRANSFORMERS_OFFLINE=1）
- 模型：Pythia-410m（EleutherAI/pythia-410m-deduped）
- 8 个 cron 监控任务活跃（每个 RUNNING 实验一个）
- 19828 上有一个无关的 `generalize_pythia410m_wiki_a100_s42` 旧进程，未占分配 GPU

### 3. 📊 当前状态
Phase Diagram 16/20 confirmed，T=25 四格 + cross-seed 共 8 实验全部 RUNNING。

最近一次 SSH 确认（~16h 前）：
- t25_a075: gen 24/25（19828:0）→ **极可能已完成，最高优先检查**
- t25_a045_v2: gen 24/25（17855:5）→ **极可能已完成**
- t15_a060_s43: gen 12/15（17855:1）→ 大概率完成
- t15_a045_s43: gen 11/15（17855:2）→ 大概率完成
- t20_a045_s43: gen 13/20（19828:1）→ 可能完成
- t25_a060_v2★: gen 10/25（17855:3）→ 可能仍在跑
- t25_a050_v2: gen 10/25（17855:0）→ 可能仍在跑
- t20_a060_s43_v2: gen 10/20（17855:4）→ 可能仍在跑

Paper Agent 已完成 D181 claim 校准写入（约束 #57-60 全部落实到论文正文）。
D170 场景预案已写入 artifacts/D170_narrative_drafts.md（Scenario A/B for T=25 α=0.60）。

### 4. 📋 待办
- **第一优先**：Agent 启动后立即 SSH 检查 8 个实验实际完成状态 → 已完成的立即 d102 分析 → 汇报 PermG x/8
- t25_a075 完成 → d102 → 填 Phase Diagram T=25 α=0.75 格（预期 6/8）
- t25_a045_v2 完成 → d102 → 填 T=25 α=0.45 格（关键：α_c left-shift 测试）
- t25_a060_v2★ 完成 → d102 → 按 D170 场景预案选 Scenario A（>0/8）或 B（=0/8）
- T=25 四格全完成 → 20/20 heatmap 定稿 → D170 叙事定稿 → submit_paper_to_review
- cross-seed 完成 → d102 → seed robustness 验证（不影响 Phase Diagram 主格）
- GPU 释放后 → 如有需要可铺额外 cross-seed 或 ablation

### 5. 🎯 战略上下文
Phase Diagram 已确认数据：
| T\α  | 0.45 | 0.50 | 0.60     | 0.75 |
|------|------|------|----------|------|
| T=5  | 0/8  | 0/8  | 0/8      | 0/8  |
| T=10 | 0/8  | 6/8  | 0/8(dip) | 6/8  |
| T=15 | 6/8  | 6/8  | 0/8(dip) | 6/8  |
| T=20 | 5/8  | 6/8  | 0/8(dip) | 6/8  |
| T=25 | RUN  | RUN  | RUN★     | RUN  |

核心发现：(1) α_c(T) left-shift consistent with √T scaling, (2) sync-dip at α=0.60 across T=10/15/20, (3) 6/8 MAUVE ceiling, (4) predict-then-verify 2/4 within CI + systematic conservative bias

最易判断错的事：
- Agent 汇报的进度百分比经常是估算值，与 SSH 实际目录不符——必须要求 SSH 核实
- 本地 artifacts 目录可能有旧脚本残留文件（perplexity-based），d102 结果文件名含 "d102" 或用 mauve 作 downstream，看到 perplexity 就是旧数据
- T=25 α=0.60★ 结果决定 sync-dip 定性（dissolution vs permanence），场景预案已备好，不需要临场发挥
- EMNLP 2026 ARR DDL ~2026-06-15，时间充裕


---
