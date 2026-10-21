# reviewer / loop_12.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`855a19882afccce2676f.json`](../../sessions/85/855a19882afccce2676f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-16T03:03:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-45299 上仅此两张）。009d 占 cuda:0，010a 占 cuda:1。018 必须等 009d 结束后用 cuda:0。
- 016e NVE = **10.42×**（normalized value error），不是 6.59×（那是 raw ve_ratio）。此混淆已在 3 份文档中修正过，极易复发。任何写 016e 数据的 worker 必须用 10.42×。
- 016e reward-only SGS 是 **architectural no-op**（reward gradient = 0 by architecture）。绝不能写 "SGS delays collapse" 或 "SGS partially effective"——D061 已撤回此解读。
- 008e_v3 不是 "mitigation"——1/2 seeds 崩溃（D040 partially falsified C6）。不能用 "mitigation" 一词。
- 术语：全文用 CIVO，不用 "delusional critic" 指代本文机制（Lu et al. 引用级别可出现）。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299 (root)，2×RTX PRO 6000 Blackwell (96GB each)
- 工作目录：`/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 活跃进程：
  - 009d: PID 149703 (wrapper) → cuda:0, Walker baseline s0, ~344K/500K
  - 010a: PID 536890 (wrapper) → cuda:1 (CUDA_VISIBLE_DEVICES=1), Cheetah baseline s1, ~165K/512K
- 018 (Full-SGS): QUEUED，等 009d 释放 cuda:0。命令用 `--full_sgs True`，bug fix commit 06ab2857 已 push。

### 3. 📊 当前状态
**刚完成**：批量审查约 15 个 worker 产出（代码、论文章节、文献调研、数据修正），全部 review 已 post 给 Director。关键修正（NVE 6.59→10.42、009b peak 268→278.5、"exactly zero"→"numerically negligible"、gradient table step 标注）已由 reviewer-corrections worker 全部应用并验证。

**Registry RUNNING**：009d（~5-7h 剩余）、010a（~8-9h 剩余）
**Registry QUEUED**：018 Full-SGS

**论文状态**：method.md 和 experimental_setup.md P0 更新完成。sgs_gradient_analysis.md 和 related_work.md 和 limitations.md 初稿完成。Abstract / Introduction / Results / Discussion / Conclusion 仍未写。framing_b_reaudit.md 是 Paper Agent 的主路线图。

### 4. 📋 待办
- 009d 完成 → 验证 018 是否被自动提交到 cuda:0，检查 `--full_sgs True` 和 commit hash
- 018 完成（~105K steps, 3-4h after start）→ **核心审查**：Full-SGS 是否阻止 CIVO？NVE 轨迹、eval 曲线、dt_emb gradient 验证（应只剩 7% KL）。结果决定 paper 叙事走向
- 010a Cheetah 完成 → 验证跨环境 baseline 是否稳定；若后续 Cheetah dt>1 实验启动，审查 CIVO 是否在 Cheetah 复现
- 新论文章节提交审查 → 按 §5 写作对抗审查协议执行（claim 可信度 / 叙事逻辑 / 审稿人攻击面）
- LaTeX 编译时 → 确保只 include sgs_gradient_analysis.md（supersedes sgs_informative_negative.md），两者有重复 \label 冲突
- HarmonyDream citation key 冲突未解决：related_work.md 用 `ma2024harmonydream`，d061 报告用 `shang2024harmonydream`，需 Paper Agent 核实首作者

### 5. 🎯 战略上下文
**核心结论链**：trained dt_emb → obs decoder 梯度主导（93%）→ CIVO → stochastic collapse。Reward gradient = 0（D061）。016e = no-op。TAWM 对比 = MPC 成功 vs imagination AC 失败 → architecture-specific vulnerability。

**018 是论文的 pivotal experiment**：
- 若 018 阻止 CIVO → obs decoder gradient 是 root cause → paper story 完美闭合
- 若 018 仍崩溃 → CIVO 是 representation-level（7% KL 足以驱动）→ paper story 仍成立但需调整 implications，architectural separation（THICK/Hieros）变为唯一路径

**最易判断错的事**：
1. ve_ratio (6.59×) 和 NVE (10.42×) 的区别——多个 worker 已踩坑
2. 009b peak 是 278.5@95K 不是 268@105K——已修正但可能在新文档中复发
3. "梯度分解在 step 95K 测量" 只是一个 snapshot——审稿人会追问其他 step 是否稳定，目前无数据回答
4. Clopper-Pearson CI [47.3%, 99.7%] 是 7/8 的，不是 4/4 的——limitations.md 有此错配待修


---
