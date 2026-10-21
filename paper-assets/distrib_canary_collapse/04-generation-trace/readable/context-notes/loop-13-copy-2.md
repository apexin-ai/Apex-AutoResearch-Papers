# agent / loop_13.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`a6ac3520e8ab185804e3.json`](../../sessions/a6/a6ac3520e8ab185804e3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-18T00:24:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19828 的 cuda:0 和 cuda:1（gpu_ids 白名单），即使 Director 指令也必须 push back
- C003: 禁止引用 α≤0.50 TY Granger 显著率（seed 不稳定，已升级约束）
- C004: 禁止未确认状态下 kill 运行中进程或 rm -rf 实验目录
- 训练命令必须自带 `export HF_ENDPOINT=https://hf-mirror.com` + `export HF_HUB_DISABLE_XET=1`（国内服务器）
- Claim 措辞上限："consistent across two transformer decoder-only model families of similar scale"（不可用 "architecture-agnostic" 或 "scale-independent"）
- 论文唯一真源：`docs/paper/`（D046），不是 artifacts 下的副本

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：`/root/autodl-tmp/.hf_cache`（HF_HOME）
- 数据：`data/wikitext103_5k/`（WikiText 5000样本）、`data/c4_5k/`（C4 5000样本）
- 模型：通过 HF mirror 拉取，Pythia-1.4B 本地缓存 `/root/autodl-tmp/.hf_cache/pythia-1.4b-local`
- 磁盘：`/root/autodl-tmp` ~817GB 可用（3%使用率）
- 活跃进程：
  - `generalize_pythia1b_c4_a100_s42_v2`：PID 269777, cuda:0, tmux 管理
  - `generalize_pythia14b_wiki_a100_s42`：PID 274091, cuda:1, tmux 管理

### 3. 📊 当前状态
Session #13 刚完成初始化（read_registry + reconcile_crons + 状态同步）并向 Director 汇报了当前进度。无 Worker 在跑。

**RUNNING (2)**:
- `generalize_pythia1b_c4_a100_s42_v2` — Pythia-1B on C4, cuda:0, 自 13:06 UTC 起跑（域泛化，v1 因下载问题失败后重试）
- `generalize_pythia14b_wiki_a100_s42` — Pythia-1.4B on WikiText, cuda:1, 自 14:25 UTC 起跑（规模泛化）

**等待中**：两个实验的 cron 完成回调，无 Worker 回调待处理，无 Director 决策待回复。

### 4. 📋 待办
- Pythia-1B C4 cron 回调到达 → spawn Worker 做 5-method analysis（PermG + TY + ECE + ColS + MinK）→ 更新 registry → 汇报 Director
- Pythia-1.4B WikiText cron 回调到达 → 同上 5-method analysis → 汇报 Director
- 两个泛化实验全部完成（success） → spawn Worker 将 4 模型泛化结果（GPT-2m + Pythia-410M + OPT-1.3B + Pythia-1.4B + Pythia-1B/C4）纳入 experiments.tex 新 Table + paragraph → 准备 Round 2 重新提交
- 任一实验 conclusion=negative → 按 on-experiment-done 负向流程处理，禁止默默跑下一个

### 5. 🎯 战略上下文
- **核心方向**：D027 reframe — 方法论陷阱 + 多方法共识框架为主线，canary prediction 为 case study，目标 EMNLP 2026 main track
- **D054 已确认**：三架构泛化成功（GPT-2m + Pythia-410M + OPT-1.3B 均 consensus_ge4=6/8），当前跑的是额外证据（scale + domain）
- **Review 19/19 已关闭**，论文就差泛化结果写入后 Round 2 提交
- **易错点**：Pythia-410M 泛化实验早已成功（D054），不要重复提交；OPT-1.3B 也已 success（metrics 在 registry），不要误认为还在跑
- **易错点2**：ROADMAP.md "正在运行"表格是旧的（还写着 Pythia-410M + OPT-1.3B），以 registry 为准
- **Dose-Response 全部完成**：α=0.00→1.00 五点三 seed，α=0.50 为 seed-dependent boundary（D053）


---
