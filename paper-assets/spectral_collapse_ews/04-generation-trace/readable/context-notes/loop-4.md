# director / loop_4.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`c9a6dda17a2cfd816c05.json`](../../sessions/c9/c9a6dda17a2cfd816c05.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-19T10:29:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0** 和 **cuda:1**（rtx6000-diagprobe 上的两张 RTX PRO 6000 Blackwell 98GB）
- 论文 **8 pages 上限**（ACL format），新增内容必须同步压缩其他部分
- r_crit bound 全文必须一致：当前 **(0.25, 0.3]**（§2.2/abstract/conclusion 已同步，§4.3 保留初步 bound (0.2, 0.5] 作叙事递进）
- cron 回调不可靠——实验完成后 Agent 可能不自动接力，**必须主动 check + 手动启动下一个实验**
- exp_007 (r=0.2) 只有 5gen 数据，论文中关于 r=0.2 的 claim 必须 hedge "observed five generations"

### 2. 🖥️ 基础设施快照
- 服务器：**rtx6000-diagprobe** (connect.westd.seetacloud.com)，user root
- 工作目录：远程 `/root/spectral_collapse_ews`，本地 `/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews`
- 论文：`paper/` 目录，latest commit `d7052de`
- Launch scripts 全就绪：`/root/spectral_collapse_ews/scripts/launch_*.sh` + `resume_*.sh`（7 个脚本覆盖 Phase 2 全部实验）
- 活跃进程：
  - exp_009 (r=0.25, 10gen): cuda:0, tmux=exp_009, Gen ~3-4/10
  - exp_010 (pure seed43, 10gen): cuda:1, tmux=exp_010, 刚启动 ~Gen 0-1
- 分析输出：`/root/spectral_collapse_ews/results/second_order_analysis.json` + `controller_activation_analysis.json`

### 3. 📊 当前状态
刚完成 r_crit bound 级联更新 (0.25, 0.3] 全文同步（commit d7052de）。exp_008 (r=0.3) 10gen 完成（SLV=2511.1, Type III confirmed），exp_010 (pure seed43) 已在 cuda:1 接力启动。

- **exp_009** (r=0.25, cuda:0): RUNNING, Gen 3/10, ~14h remaining. Gen 3 SLV=2380.9, Type II confirmed.
- **exp_010** (pure seed43, cuda:1): RUNNING, 刚启动, ~20h. Phase 2 multi-seed 第一个实验。
- 等待：exp_009 Gen 5+ 数据 → 更新 §4.5 r=0.25 描述；exp_010 完成 → 验证 C1 multi-seed

### 4. 📋 待办
- exp_009 Gen 5+ 数据到 → 更新 §4.5 r=0.25 完整描述 + 确认 10gen trajectory 是否持续 expand
- exp_010 完成 → 验证三阶段 pattern seed 一致性 → cuda:1 启动 `launch_pure_collapse_seed44.sh 1`
- exp_009 完成 → cuda:0 启动 `resume_fixed_mix_r02_seed42_gen5to10.sh 0`（exp_007 resume 10gen）
- exp_007 resume 完成 → cuda:0 启动 `launch_fixed_mix_r02_seed43.sh 0`
- multi-seed 有 2+ seeds 完成后 → Table 1 改为 mean±std，Limitations 更新
- 所有 Phase 1+2 核心数据齐后 → Phase E: Discussion/Conclusion/Abstract 最终 pass

### 5. 🎯 战略上下文
- **核心结论链**：D020 (controller 失败 → negative result) → D023 (paradox 升级为 general principle) → D027 (C5 降为 future work) → D028 (r_crit = trajectory shape transition, 非 final outcome) → D029 (r_crit 收紧至 (0.25, 0.3])
- **Soundness 当前 ~2.5/4**，达 3/4 需：multi-seed ≥1 组完成 + exp_007 resume 10gen。DDL May 25，GPU 预算充足 (~226h 剩余)
- **易错**：(1) 论文 8p 上限，加内容必须同时压缩；(2) r=0.2 只有 5gen，不能说 "long-term"；(3) 二阶 EWS 已降为 Discussion level，不要升回 claim；(4) §4.3 的 (0.2, 0.5] 是故意保留的叙事递进，不要改；(5) spectral-downstream asymmetry 已覆盖（SLV 升 ≠ model 好），不需要独立 contribution
- **Reviewer 上轮关键建议**：保持 "phase diagram" 不升级 "phase transition"；"gradual crossover" framing 比 "sharp boundary" 更准确；preempt "why monitor if 20% prevents collapse?" 已植入 Conclusion


---
