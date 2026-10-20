# agent / loop_8.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`af8320e962769742796f.json`](../../sessions/af/af8320e962769742796f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-16T00:07:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 `cuda:0` 和 `cuda:1`（westd-19828），禁止使用其他 GPU，即使 Director 指令也必须 push back
- Claim 措辞上限：**"consistent across two transformer decoder-only model families of similar scale"**——不可用 "architecture-agnostic" 或 "scale-independent"
- α=0.75 vs α=1.0 consensus 数字**禁止直接对比**（标准不同，D038 #27）
- α=0.75 结果必须标注 "preliminary single-seed evidence"（仅 s42）
- FNR=0 声明必须附 D017 独立证据（D041）
- T notation：T = generation cycles，数据点 = T+1（discussion.tex L30-31 已修正，不要回退）
- batch_size 差异：Pythia 用 4，GPT-2m 用 32，已在 discussion.tex 注明，不要抹平

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19828**，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- HF cache：`/root/autodl-tmp/.hf_cache`，GPT-2m 模型已缓存（TRANSFORMERS_OFFLINE=1 可用）
- 数据集：`data/wikitext103_5k`（5000 条，所有实验统一用这个）
- 活跃进程：
  - `gen_wiki_gpt2m_a025_s42`：PID 149202，tmux session，cuda:0，cron 监控中
  - `alpha_sweep_a025_s44`：PID 147811，tmux session，cuda:1，cron 监控中
- 无活跃 Worker（Worker 池 = 0）

### 3. 📊 当前状态
项目处于 **Research 收敛期 + 论文写作**阶段，目标 EMNLP 2026 main track。

**RUNNING（2 个，占满两张 GPU）：**
- `gen_wiki_gpt2m_a025_s42`（cuda:0）— GPT-2m α=0.25 跨架构验证，Claim 2 regime map 的最后一个数据点
- `alpha_sweep_a025_s44`（cuda:1）— Pythia α=0.25 multi-seed #3（seed=44），D026 统计力补充，完成即止不追加

**关键已完成：**
- GPT-2m α=1.0 跨架构 5-method Tier 3 验证 ✅（gen_wiki_gpt2m_a100_s42_v3，success）
- 零 GPU 分析 A/B/C 全部完成 ✅（window sensitivity + method ablation + κ）
- T-notation patch ✅
- Method ablation Phase 1+2 ✅（56 panel rows，4 alphas，核心发现：naive 100% sig vs PermG 75% sig at α=1.0 only）
- Pythia 全 alpha sweep 完成（α=0/0.25/0.50/0.75/1.0，14 success / 0 negative）

**等待中：**
- 两个 RUNNING 实验的 cron 完成回调（预计各 ~3-8h）
- Paper Agent Step 5 收敛（W1-W4 修复 + GPT-2m 结果整合）
- 无待处理 Director 决策

### 4. 📋 待办（条件触发式）
- `gen_wiki_gpt2m_a025_s42` cron 回调到达 → spawn Worker 做 5-method lead-lag 分析 → 与 Pythia α=0.25 对比 regime-dependent pattern → 写入论文 Claim 2 跨架构段落 → 汇报 Director
- `alpha_sweep_a025_s44` cron 回调到达 → spawn Worker 提取 metrics + 与 s42/s43 cross-seed 比较 → 更新 registry + report.md → 若 deviation <10% 则确认 reproducibility，标记 D026 multi-seed 完成
- 两个实验都完成后 → 推进 Paper Agent Step 5 收敛：最终 proofread + compile → submit_paper_to_review
- 如果 gpt2m_a025 结果与 Pythia α=0.25 regime pattern **不一致** → 按 red-section 规范产 Framing 调整提案（Claim 2 scope 可能需缩窄），禁止默默跳过

### 5. 🎯 战略上下文
**核心 narrative（D027 reframe）：** 论文主线是方法论陷阱 + 多方法共识框架。三个 Claims 按证据强度排序：Claim 3（方法敏感性，最强，跨架构复现 + 4/5 唯一最优 + κ 跨架构一致）> Claim 2（regime map，待 gpt2m_a025 确认）> Claim 1（case study，跨架构复现）。

**决策链关键节点：** D043（EMNLP target）→ D044（砍低 ROI 实验，转零 GPU 分析）→ 当前只剩 gpt2m_a025 一个 GPU 实验需求。

**最容易判断错的事：**
- gpt2m_a025 是 α=0.25（低污染 regime），预期 Granger FDR 不 sig——这不是 negative，是 regime-dependent validity 的正面证据（与 Pythia α=0.25 一致 = Claim 2 confirmed）
- 不要把 α=0.25 的 "0/4 FDR-sig" 误判为实验失败——这正是 regime map 的一部分
- PREPARING 状态的 4 个旧实验（alpha_sweep_a025_s42, v2, mvp_rep44, mvp_v2_rep44）是历史遗留，已被后续实验替代，不要尝试恢复
- 累计 GPU ~23h，D044 后剩余 GPU 需求极低（仅 gpt2m_a025 ~8-10h），其余全是零 GPU 分析 + 论文写作


---
