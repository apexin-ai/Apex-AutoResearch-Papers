# agent / loop_9.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`47146219fe1d4f6bdef7.json`](../../sessions/47/47146219fe1d4f6bdef7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-16T03:11:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 westd-19828 的 cuda:0 和 cuda:1，即使 Director 明确指令也不可用其他 GPU
- α=0.75 vs α=1.0 的 consensus 数字**禁止直接对比**（标准不同，D038 #27）
- Claim 措辞天花板："consistent across two transformer decoder-only model families of similar scale"——不可用 "architecture-agnostic" 或 "scale-independent"
- FNR=0 声明必须附 D017 独立证据（D041），否则循环论证
- T notation：T = generation cycles，数据点 = T+1（已修正，不要回退）
- 论文唯一真源：`docs/paper/`（D046），不是 `artifacts/`
- batch_size=32（gpt2-medium）vs 4（Pythia）差异已在 discussion.tex 注明，不要遗漏

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，pip/python 在 `/root/miniconda3/bin/`
- 模型缓存：`/root/autodl-tmp/.hf_cache`（HF_HOME），gpt2-medium 已下载
- 数据：`data/wikitext103_5k`（5000 样本，所有实验共用）
- 活跃进程：`gen_wiki_gpt2m_a025_s42`（PID 149202, tmux session, cuda:0, cron 监控中）
- cuda:1 空闲（`alpha_sweep_a025_s44` 刚完成，4.76 GPU-h）
- 环境变量必须设：`HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_DISABLE_XET=1 HF_ENDPOINT=https://hf-mirror.com`

### 3. 📊 当前状态
- **gen_wiki_gpt2m_a025_s42** RUNNING (cuda:0)——Claim 2 跨架构验证，gpt2-medium α=0.25，10 generations × 5000 steps，预计还需 ~3h（从上 session 估计，可能已接近完成）
- **alpha_sweep_a025_s44** 刚完成（DONE/success）——D026 multi-seed #3，已确认 α=0.25 三 seed 复现性好（除 ECE 外 std<1%）
- 零 GPU 分析 A/B/C 全部完成，T-notation 已修正
- Paper Agent Step 5 运行中（W1-W4 修复 + GPT-2m 整合）
- 无活跃 Worker，无 ANALYZING 实验
- Registry: 34 实验，success 14, failed 3, killed 15
- 累计 GPU ~28h

### 4. 📋 待办（条件触发式）
- **gen_wiki_gpt2m_a025_s42 cron 回调到达** → spawn worker 分析 regime-dependent pattern 跨架构复现：
  - 复现（≥2 method 一致）→ Claim 2 升 Tier 3，写入 paper cross-arch section
  - 不复现 → 降级措辞但不 panic（α=1.0 已跨架构确认），向 Director 汇报调整方案
- **alpha_sweep_a025_s44 结果** → 已完成但 report.md 未整合其 metrics（上一轮可能来不及），确认是否已写入论文
- **cuda:1 空闲** → D044 决策后无新 GPU 实验需求，剩余全部零 GPU 任务。如 Director 有新任务可立即使用
- **Paper Agent Step 5 收敛后** → 最终 proofread + compile → submit_paper_to_review

### 5. 🎯 战略上下文
- **核心叙事 D027 reframe**：方法论陷阱 + 多方法共识框架，canary prediction 为系统性 case study。Title 方向："Method Matters: Pitfalls and a Multi-Method Consensus Framework for Lead-Lag Analysis in Iterative Training Collapse"
- **投稿目标**：EMNLP 2026 main track（D043），ARR June cycle，deadline ~June 15
- **证据强度**：Claim 3（方法敏感性跨架构复现）> Claim 2（regime map，等 gpt2m_a025）> Claim 1（case study）
- **gpt2m_a025 是最后一块拼图**——跨架构 regime-dependent pattern 复现与否决定 Claim 2 最终措辞强度
- **D044 收敛决策**：已砍 a050_s44、a010_s42、plan_006_s43 等低 ROI 实验，不再追加
- **易错点**：(1) TY Granger 在 T≤10 下 underpowered 是统计限制不是 bug，不要尝试修复；(2) ECE 在小样本下噪声大（std=15.9%），跨 seed 对比需谨慎；(3) window_sensitivity.py 有已知 bug 但不影响论文数字（论文数字来自 method_ablation.py）
- **WA→Accept 路径**：步骤 1-5 已完成，剩余 6（gpt2m_a025 跨架构确认）和 7（Paper Agent 最终整合）


---
