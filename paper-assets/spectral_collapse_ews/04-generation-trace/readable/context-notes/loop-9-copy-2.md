# reviewer / loop_9.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`41917b6f1a1cb38efeb0.json`](../../sessions/41/41917b6f1a1cb38efeb0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-22T18:33:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- exp_016 用 cuda:0, exp_017 用 cuda:1（rtx6000-diagprobe 双卡，项目独占）
- 论文 EMNLP 2026 ARR 严格 8 页主文本限制，当前 0 margin（Conclusion 结束在 page 8 约 2/3 处）。任何正文增加都有超页风险
- r=0.3 D-4 均值从 .232 (2-seed) 变为 .295 (3-seed)——这是个显著变化，Agent 更新 Table 3 后必须 grep 全文确认所有引用 D-4 at r=0.3 的位置一致
- 论文中 ">30× lower CV for SLV" claim 是关于 r=0 (不是 r=0.3)，不要因为 r=0.3 SLV s.d. 从 2.0 变 2.94 就误改这个 claim

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (root), 双卡 NVIDIA RTX PRO 6000 Blackwell (96GB each)
- 远程代码目录：/root/spectral_collapse_ews
- 结果目录：/root/spectral_collapse_ews/results/phase1_fixed_mix_r03_seed44_results.json（exp_016 完整 Gen 0-10）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/
- 论文：workspace/paper/（LaTeX，latexmk 编译）
- exp_016 已完成（cuda:0 空闲）
- exp_017 RUNNING：PID 648360, tmux=exp_017, cuda:1, r=0.2 seed43, Gen 5/10

### 3. 📊 当前状态
**刚完成**：exp_016 (r=0.3 seed44) 全部 Gen 0-10 数据到手，独立核实 PASS。已发送精确 3-seed 统计量给 Director（SLV mean=2508.2, CV=0.117%; D-4 mean=.295, s.d.=0.155）。

**已发送的审查报告**：
1. exp_016/017 中间数据核实 + GPU 利用率 ✓
2. 预提交合规检查（0 TODO, 0 overfull hbox, 0 undefined citations）✓
3. Cross-seed consistency claim 强度评估（建议不升级）✓
4. 最终品质审查（Intro/Figures/Related Work/叙事）— Figure caption 补模型名+种子数是唯一建议行动项 ✓
5. exp_016 完成后 10 处更新的预写措辞 + 精确数值清单 ✓
6. exp_016 完成核实报告 + 3-seed 精确替换值 ✓

**等待中**：
- Agent 执行论文 10 处 3-seed 更新（Abstract L5, Table 3, §3.5 L148/150/161, Limitations L5, Response letter）
- exp_017 (r=0.2 seed43) cron 完成回调

### 4. 📋 待办
- **Agent 提交 3-seed 更新后** → 核实所有 10 处替换值正确、全文 grep D-4 at r=0.3 一致性、重新编译确认页数仍 ≤8
- **exp_017 完成 (预计 ~9h)** → 读 Gen 10 数据，验证 Type II 分类（SLV dip-then-recovery），计算 2-seed r=0.2 均值，审查论文/response letter 更新
- **Figure caption 更新后** → 确认 Figure 1/2 caption 含模型名和种子数
- **最终提交前** → 再跑一次 placeholder 扫描 + overfull check + 页数确认

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR, May 25（~2 天）
- **核心结论**: r_crit ∈ (0.25, 0.3], 3-phase spectral collapse pattern, signal attenuation under mixing
- **Round 1 审稿分 3.0 (Findings)**，目标升到 3.5 (Borderline Conference)。3-seed 覆盖 + response letter 是主要升分手段
- **review_issues.yaml**: R1-N2 (seeds) 从 in_progress 可标 resolved；R1-W1 (r_crit granularity) 仍 open（用 rebuttal 回应）
- **易错点**：
  - D-4 at r=0.3 从 .232 → .295 是个大跳，所有引用 D-4 值的位置（L158, Table 3, caption, response letter）都要同步
  - Response letter 的 Q3 EMA 值 (S̃₁=2365.29, S̃₂=2364.46, Δ=-0.83) 是 seed 43 个体数据，不受 3-seed 更新影响——不要误改
  - "deterministic structural phenomenon" 在论文 §3.5 L161-162 已有两处，Abstract 用 "consistent/reproducible"，不要升级到 Conclusion


---
