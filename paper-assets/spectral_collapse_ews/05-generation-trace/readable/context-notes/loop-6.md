# director / loop_6.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`9a417b74e21a8f50a914.json`](../../sessions/9a/9a417b74e21a8f50a914.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-21T23:15:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 rtx6000-diagprobe 只有 2 张 GPU (cuda:0, cuda:1)，项目未配置 gpu_ids 白名单
- 数据盘 250G，之前因 checkpoint 堆积到 100% 导致 exp_014 崩溃（M013）。启动新实验前必须 `df -h /root/autodl-tmp` 确认剩余空间 > 20G
- 已完成实验的 checkpoints 在 HellaSwag eval 完成后必须及时清理，不要累积
- Table 数据必须与源文件严格对齐——之前出过 Table 3 r=0.50 混用 adaptive/fixed_mix 数据源的事故（INT-D1），以及 caption 声称 3-seed 但数据实际是 2-seed 的事故（INT-D2）
- SLV = ½ × SIGMA 的 log det(G)，论文中已诚实披露等价关系，不能再声称 metric choice 是差异化维度
- EMNLP 2026 主文严格 8 页限制，当前编译 8 页 main + limitations + references + appendix

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，用户 root
- 工作目录：`/root/spectral_collapse_ews`（远程代码）；本地论文在 `projects/spectral_collapse_ews/paper/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- Checkpoints：`/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/`
- 已清理 7 个完成的 checkpoint 目录释放 ~102G（pure_collapse_seed43/44, adaptive_k10_seed42, fixed_mix_seed42, fixed_mix_r02_seed42, fixed_mix_r03_seed42/43）
- 保留目录：fixed_mix_r025_seed42/43/44, pure_collapse_42
- 活跃进程（截至 handoff 时需要确认）：
  - exp_014b: cuda:0, PID 577216, tmux, r=0.25 seed43 gen6→10 恢复（预计 May 22 ~04:00 UTC 完成）
  - exp_015: cuda:1, PID 516824, r=0.25 seed44 完整 10 gen（预计 May 22 ~12:00 UTC 完成）
- HellaSwag eval 已全部完成（3 seeds × 11 gen），注意 seed43 JSON 格式有额外 `results` 包装层

### 3. 📊 当前状态
**刚做完**：
- 数据完整性修复全部 PASS：Table 1 全 30 cell 3-seed 替换 (94cbf2f)、Table 3 r=0.50 统一 (94cbf2f)、L163/L166 修复 (58c3536)、appendix per-gen variance 表 (98a14f5)、§4.1 "cross-seed robust" + provenance 27/27 (d577eeb)
- Rebuttal 框架完成：`artifacts/rebuttal_framework.md`（R1-W1 + C3 novelty + R1-N2 + 3 个潜在攻击面）
- review_issues.yaml 更新至 15/16 resolved（含 3 个 internal issues）

**Registry**：
- exp_014b: 可能 RUNNING 或已完成（需确认，预计 May 22 ~04:00 UTC）
- exp_015: RUNNING, cuda:1, r=0.25 seed44
- exp_016: QUEUED/ALLOCATED, r=0.3 seed44, 等 exp_014b 完成后在 cuda:0 启动

**等待**：
- Agent 新 session 启动（之前 RESET 循环问题，已报 BLOCKED + 通知 Manager）
- exp_014b 完成 → 数据集成 + 启动 exp_016
- exp_015 完成 → r=0.25 3-seed 数据集成

### 4. 📋 待办（条件触发式）
- **新 session 启动后** → 立即 SSH 检查 exp_014b/015 实际状态（GPU 利用率 + checkpoint 目录），之前派了检查指令但不确定 Agent 是否执行
- **exp_014b 完成** → (a) 确认 gen6-10 数据完整 (b) 启动 exp_016 (r=0.3 seed44, cuda:0) (c) 收集 r=0.25 seed43 spectral+downstream 数据
- **exp_015 完成** → 收集 r=0.25 seed44 数据，与 seed42 + seed43 合并计算 Table 3 r=0.25 行 3-seed mean
- **exp_016 完成** → Table 3 r=0.3 行 3-seed mean 更新；此时 r=0.25 和 r=0.3 均有 3 seeds → Abstract L5 "two random seeds" → "three random seeds"
- **P0 全部完成后** → 启动 P1 (r=0.2 seed43 + r=0.5 seed43)；更新 R1-N2 rebuttal 论点
- **全部数据集成后** → Phase E final pass（全文数字对齐 + 编译验证 ≤ 8p）→ submit_paper_to_review Round 2
- **DDL May 25** → May 24 必须完成 final pass

### 5. 🎯 战略上下文
- **核心结论**：递归合成训练中嵌入谱坍缩遵循三阶段模式，SLV 是最有效监测器（CV<1.3%），r_crit ∈ (0.25, 0.3] 是坍缩/稳定相边界，信号衰减是 spectral 反馈控制的固有限制
- **Round 1 得分 3.0**，目标 3.5 (Borderline Conference)
- **最大审稿风险**：C3 novelty（"信号衰减 trivially expected"）——防御要点在 rebuttal_framework.md，核心是 continuous quantification + τ-independence + cross-indicator generality
- **易错点**：
  1. 改论文数字后必须全文 grep 旧值确认无残留——之前多次出现 caption 和 body 数值不一致
  2. Table 3 各行数据来源必须统一（不能混 adaptive/fixed_mix）
  3. Abstract L5 的 seed 数必须与实际实验数据匹配，不能提前改
  4. exp_014b 是 gen6 恢复跑（不是从头），registry 可能没有正确记录
  5. 磁盘空间：每个 10-gen 实验 ~17G，启动前检查


---
