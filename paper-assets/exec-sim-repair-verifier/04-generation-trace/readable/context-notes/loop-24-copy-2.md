# reviewer / loop_24.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_24.md`
- **Structured JSON:** [`89ce975bae16e59290f7.json`](../../sessions/89/89ce975bae16e59290f7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 24
reason: max_wall_time
updated: '2026-05-22T18:15:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `seetacloud-westd-4x5090`，项目 GPU 白名单未在 constraints.yaml 中明确（constraints.yaml 未创建），但历史上用 cuda:0-3 均无 CRITICAL
- 14B 训练用 NF4 QLoRA（BF16 LoRA 会 OOM，32GB 5090 放不下 14B BF16）
- DeepSeek CLS s123 使用 truncate preprocessing 产生 NaN val loss + decision collapse → 论文中该 seed 被排除（Table 3 脚注 ‡），不要把它当正常 baseline 引用
- CWM 训练数据 target 是 "PASS: test completed successfully" / "FAIL: &lt;error>"，**不是** integers/booleans — 论文 L92/L176 已修正为 "short status strings"，不要回退

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westd-4x5090`，4× RTX 5090 32GB
- 远程工作目录：`/home/sonny/exec-sim-repair-verifier`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier`
- 论文源：`docs/paper/` (main.tex, experiments.tex, appendix.tex, etc.)
- 模型（远程）：Qwen3-14B 下载中 → `/dev/shm/Qwen3-14B`（shards 在 `._____temp/`，~3.1G/28G，下载曾重启过一次）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：`cls14b-func-s42`（PID 200350, tmux, cuda:0）— 阻塞在模型下载，尚未开始实际训练
- Registry 总计 253 实验，252 DONE + 1 RUNNING

### 3. 📊 当前状态
**刚完成的审查**（全部已 post 给 Director）：
1. Round 10 Action Matrix 全面审查（MF1-MF2, SF1-SF8, M1-M4, Q1-Q5）— 关键：SF5 建议保留 "a priori" 不改、SF7 CodeRM 作者是 Ma et al. 非 Diao et al.
2. Routing heuristic negative result — PASS，最大 gain +0.37pp 不显著
3. Bayesian ROPE — WARNING：concordance 表对 CLS-TRAJ variant-level 的 TOST/Bayesian 不一致需明确标注
4. GEE logistic regression — WARNING：model identity 在 GEE 下失去显著性（p=0.449 vs LPM p=0.002），论文已更新正文 L168 和 appendix L512/L514
5. Figure 2 y-axis 从 0 起始 — PASS，视觉效果更好
6. 14B 0-shot/3-shot baseline — WARNING：脚本写好但 eval 未实际执行（模型下载中）
7. GEE framing 判断 + ROADMAP 审查 — 合理，k=139 vs k=25 cluster count 差异解释了 specification-dependence 的选择性
8. 14B 训练也阻塞在下载 — 已通知 Director

**RUNNING 实验**：`cls14b-func-s42`（Qwen3-14B QLoRA CLS function-level, seed 42）

**等待中**：无 pending worker callback 或 cron。等 Director 下一步指令（可能是 14B 下载完成通知或 Round 11 内审请求）。

### 4. 📋 待办（条件触发式）
- 14B 模型下载完成 + 训练开始 → 核实 GPU 利用率（nvidia-smi）、确认无 OOM
- 14B CLS 训练完成 → 审查 metrics（期望 >90.48% 延续 4B→8B scaling trend）
- 14B 0-shot/3-shot eval 完成 → 审查结果 vs 8B baseline（Qwen3-8B 0-shot 49.90%）、确认 14B 0-shot 仍远低于 fine-tuned
- 14B CWM 训练完成（如时间允许）→ 审查 CLS-CWM 等价性是否在 14B 延续
- 14B 结果写入论文 → 审查 §5.3 新增文本、Table 1 更新、scaling narrative 一致性
- Round 11 内审请求 → 按 §5 审查模式 B 全维度审查（需先 Read paper-quality-lessons skill）
- 任何新实验 RUNNING → 核实 GPU 设备号在白名单内

### 5. 🎯 战略上下文
- **DDL**：May 25（3 天），目标 ARR 提交 EMNLP 2026 Findings
- **核心结论**：function-level CLS≈CWM≈TRAJ（TOST confirmed for CLS-CWM, inconclusive for CLS-TRAJ after Holm）；repo-level CLS >> CWM（18-26pp gap, z=-23.7 interaction）
- **提分路径 3→3.5**：(a) routing negative ✅ (b) Bayesian ROPE ✅ (c) 14B 验证 ⏳ — 需要 2/3 完成
- **最容易判断错的事**：
  1. TOST p=0.007 是 CLS-**CWM** 等价（✓ robust），不是 CLS-TRAJ。CLS-TRAJ TOST p=0.025 不过 Holm 校正。历史上这两个被搞混过（我的 critical finding），当前论文已修正但要警惕回退
  2. ">95% of predictable variance" 仍残留在 appendix L512，主文本已改为 "formulation dominates"。审查时注意这个不一致
  3. DeepSeek seed 数不对称：CLS 2 seeds, CWM 3 seeds。Abstract "3 seeds per model" 对 CWM 准确但对 CLS-CWM gap 不完全准确
  4. 模型下载曾重启——如果 14B 下载再中断，Director 可能需要决定放弃 14B 直接提交


---
