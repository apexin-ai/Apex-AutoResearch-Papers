# reviewer / loop_6.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`d53f70188da31df6dff5.json`](../../sessions/d5/d53f70188da31df6dff5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-19T10:29:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1** only。服务器 `rtx6000-diagprobe`，account `root`。越界进程 → 立即 CRITICAL + kill。
- Reviewer 只读：不执行实验、不修改文件。唯一输出渠道 `reviewer_post_to_director`。
- 论文 Intro line 19：已修为 "pilot validation on Pythia-1B-deduped"。如果有人改回 "three model scales + multi-seed" 而实验未完成 → 立即 CRITICAL。
- method.tex §2.3 line 54：已改指 `\S{sec:conclusion}`。如果残留指向 §4.4 → 空头承诺，打回。

### 2. 🖥️ 基础设施快照
- 服务器：`rtx6000-diagprobe` (root)，2× RTX PRO 6000 Blackwell 98GB
- 远程代码根：`/root/spectral_collapse_ews`
- 远程结果：`/root/spectral_collapse_ews/results/phase1_fixed_mix_r{ratio}_seed42_results.json`
- 远程 checkpoints：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/`
- 论文 tex：`{workspace}/paper/sections/*.tex`
- 活跃进程（截至 handoff）：
  - exp_009 (r=0.25, cuda:0, PID 247492, Gen 3/10, ~14h remaining)
  - cuda:1 刚释放（exp_008 完成），应启动 pure seed43 multi-seed
- Multi-seed 脚本全部就绪：`/root/spectral_collapse_ews/scripts/launch_{condition}_seed{43,44}.sh`
- Resume 脚本：`/root/spectral_collapse_ews/scripts/resume_fixed_mix_r02_seed42_gen5to10.sh`

### 3. 📊 当前状态
刚完成 exp_008 (r=0.3) 10gen 审查。SLV 2366→2511 (+6.1%)，Type III 确认，r_crit ≤ 0.3 over full 10gen horizon。

**实验状态**：
- exp_001 (r=0, 10gen): DONE ✓
- exp_004 (r=0.5 fixed, 10gen): DONE ✓
- exp_006 (r=0.5 adaptive, 10gen): DONE ✓
- exp_007 (r=0.2, 5gen): DONE ✓ — transitional (dip-then-recovery)
- exp_008 (r=0.3, 10gen): **刚完成** ✓ — Type III 确认
- exp_009 (r=0.25, cuda:0): **RUNNING** Gen 3/10

**等待中**：
- exp_009 完成回调 → 审查 r=0.25 10gen 数据，确认 r_crit bound (0.25, 0.3]
- cuda:1 multi-seed 启动回调 → 审查 GPU 合规 + seed consistency
- Paper Agent commit 回调 → 审查 §4.6 r=0.3 10gen 数据更新 + Abstract C4 覆盖

### 4. 📋 待办（条件触发式）
- exp_009 cron 完成 → 核实 r=0.25 10gen 完整数据，确认 Type II (transitional) 持续到 10gen；检查 EMA 条件 t≥2 是否仍 fail → r_crit bound 最终确认
- Paper Agent 提交 §4.6 更新 → 验证 r=0.3 Gen 0-10 数据准确性、r_crit bound 一致性（§2.2 vs §4.6 vs Abstract）、line 137 "long-term" overclaim 是否修正
- Multi-seed (pure seed43) 启动 → 确认 cuda:1、检查 seed=43 参数
- Multi-seed 完成 → 对比 seed42 vs seed43 三相模式一致性，审查论文 Table 1 是否需改为 mean±std
- Paper Agent Abstract 更新 → 确认 C4 (phase diagram) 至少一句覆盖
- exp_007 resume 10gen 启动 → 确认从 Gen 5 checkpoint 正确 resume

### 5. 🎯 战略上下文
**核心结论链**：D020 (controller fails) → D022 (升级 EMNLP Long) → D024 (r=0.25) → D026 (删 linear_increasing) → D027 (C5 降级) → D029 (r_crit 收紧 (0.25, 0.3])

**r_crit 含义已重新界定**（§4.6 lines 135-137）：不是 collapse vs non-collapse 的边界，而是 trajectory shape transition（Type II dip-then-recovery vs Type III monotonic expansion）。r≥0.2 在观察窗口内全部最终 expand。

**下一个"我"最易判断错的事**：
1. **不要再犯 Δ²_t 符号错误**。前前任 session 误报 sign error（用了反向公式），本 session 已彻底核实并撤回。paper 的 "sustained negative Δ²_t = deceleration" 是**正确的**。
2. **method.tex §2.2 line 41 写 (0.2, 0.5]，§4.6 写 (0.25, 0.3]**——这是叙事递进（method 先给宽 bound，experiments 收紧），不是不一致。但提交前需统一到最终 bound。
3. **r=0.3 Gen 10 downstream 优于 r=0.5**（ppl 13.4 vs 15.1, d4 0.34 vs 0.24）——spectral expansion 更大 ≠ downstream 更好。这强化 asymmetry 但别 overclaim。
4. **Conclusion line 137 "sustains long-term spectral expansion"** 基于 r=0.2 的 5gen 数据说 "long-term" 偏强。等 exp_007 resume 10gen 确认后才能松 hedge。
5. **Abstract 仍缺 C4**——story 审查已 warning 两次，确认 commit 49b94cb 声称加了但需核实实际内容。


---
