# director / loop_7.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`9d59cac84027a1602615.json`](../../sessions/9d/9d59cac84027a1602615.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-16T11:52:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cqa1-22115 的 cuda:0/1/2/3（4×4090D），无其他服务器
- exp-023/024 数据已准备好在服务器上（`data/exp_023_wiki/` 和 `data/exp_024_arxiv/`），但 registry 中为 orphaned 状态（plan 有 registry_id 但未实际注册），需要先注册再启动
- Mistral K*=1 是目前唯一 non-K*=2 结果，exp-019b cross-scorer 结果出来前不要修改 paper 中关于 universality 的 claim 措辞
- θ=0.60 用户已质疑过"太 empirical"，论文 Method 已写三层 defense（Cohen's h + permutation + gap discontinuity），不要再弱化这个 defense

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-22115 (connect.cqa1.seetacloud.com)，root 账户
- 工作目录：`/root/autodl-tmp/gen-depth-contamination`
- Python：conda base (`/root/miniconda3/bin/python`)
- HF cache：`/root/autodl-tmp/.hf_cache`，需 `source /etc/network_turbo` + `HF_DATASETS_OFFLINE=1`（C4 用本地数据）
- 模型本地路径：`/root/autodl-tmp/.hf_cache/` 下各模型目录
- 活跃进程（截至 handoff）：
  - cuda:0: exp-018 LLaMA-8B depth chain (PID 10403)，运行 6h+，生成阶段，慢
  - cuda:1: exp-019b Mistral cross-scorer (PID 36365)，feature extraction，~30-40min 完成
  - cuda:2: exp-020 Pythia nuc09 (PID 27042)，evaluation 阶段，~1h
  - cuda:3: exp-021 length_512 (PID 32175)，depth 3 gen 18%，~2h

### 3. 📊 当前状态
刚完成全面 GPU 状态检查 + exp-020 重复进程修复（kill 2 个重复 PID，数据完好）。

Registry RUNNING：exp-018 (LLaMA-8B)、exp-020 (Pythia decoding)、exp-021 (length ablation)
已完成子结果：exp-021 128 tokens K*=2, 256 tokens K*=2; exp-020 greedy K*=2
Bootstrap CI 确认：exp-019 Mistral 1v2 CI=[0.5835, 0.6032]，K*=1 统计确认

等待回调：
- exp-019b (~30-40min)：**最关键**，决定 Mistral K*=1 是 self-scorer artifact 还是 genuine
- exp-020 nuc09 (~1h)
- exp-021 512 tokens (~2h) → 完成后启动 exp-022 cross-scorer matrix
- exp-018 (数小时)

### 4. 📋 待办
- exp-019b 完成 → 若 K*=2：Mistral K*=1 是 self-scorer artifact，paper 改为 "all conditions K*=2 under cross-scorer"；若仍 K*=1：调整 framing 为 "N-1/N conditions K*=2, one borderline"
- exp-021 512 完成 → 收割结果，立即启动 exp-022 (4×4 cross-scorer matrix) on cuda:3
- exp-020 全 4 config 完成 → 注册 registry 结果，cuda:2 空出后启动 exp-023 (Wikipedia domain)
- exp-018 完成 → 收割 LLaMA K*，若 K*=1 则同 Mistral 逻辑处理
- 全部 P0 完成 → exp-023/024 domain ablation 注册启动，Paper Agent patch 更新数据

### 5. 🎯 战略上下文
- 项目核心：K*=2 saturation boundary 在 20+ 条件下成立，论文 target EMNLP 2026 ARR (DDL May 25)
- 决策 D045：Mistral K*=1 优先 cross-scorer 验证（cuda:1），延后 exp-024
- 用户关注点：θ=0.60 是否太 empirical（已回复三层 defense）、K*=2 是否脆弱（已解释只是个别模型 margin 小）
- 易踩坑：exp-023/024 是 orphaned 不是 QUEUED——plan 里有 registry_id 但 registry 无 entry，需要先 `approve_experiment` + 注册才能跑
- 易判断错：exp-018 LLaMA 跑得慢≠hang，8B 模型在 4090D batch=4 确实慢，不要轻易 kill
- Paper Agent 已完成非数据依赖的写作（θ defense、claim 措辞、Figure 1 修复、appendix 占位表），等实验数据填充
- 审稿阶段已启动（review_chat_id 存在），但当前优先是把剩余实验跑完再提交 continue mode review


---
