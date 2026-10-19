# reviewer / loop_3.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`e25a519dfb1733f26873.json`](../../sessions/e2/e25a519dfb1733f26873.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-19T08:52:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：autodl-rtx6000 (2卡)、bjb1-42106 (2卡)、cqa1-21977 (1卡)。当前全部空闲，Director 已决定释放 (D049)。**不要在这些卡上启动新实验**——四次独立评估确认无高 ROI 实验。
- R1-8B hidden states 只存 layers 12-24 (`config.py: LAYERS = list(range(12, 25))`)。layer_idx=2 → L14，不是 L2。OT-7B 存全部 28 层，32B 存全部 64 层。**E5-Mistral v1 曾因 layer indexing 错误被我标 critical**（用了 v1 的错误 layer），v2 已修正。
- 论文 `†` 标记 = n≤20 的 32B 结论。每次出现 "all four models" 必须紧跟 `†` 或 caveat。R15 已校准，不要回退。
- HarmThoughts 是唯一有 step-level CP annotation 的数据集。不要提议"换数据集验证"——不存在替代数据集。

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-rtx6000(root)`，代码根：`/root/autodl-tmp/contrastive_trace_safety`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文 tex：`docs/paper/sections/*.tex`，编译在 `home-1x5090`
- Hidden states：`/root/autodl-tmp/contrastive_trace_safety/artifacts/hidden_states*`（4 模型各一目录）
- IAA 代码：`/root/autodl-tmp/contrastive_trace_safety/src/iaa/`（5 files，已写好，等 API key，D048 降级为 future work）
- 活跃进程：无。全部实验 DONE，无 RUNNING/cron。

### 3. 📊 当前状态
**阶段**：Review — R15 修复全部完成，等用户审批后提交 R16。DDL 2026-05-25 (6天)。

**我刚完成的工作**：
- Action Matrix 独立审查（标记 4 项遗漏：BOCPD 叙事不一致、table bold 错误、Efron 引用、AI writing markers）→ 全部已在 R15 commits 中修复
- 论文三维度深度审查（Introduction story / Related Work / Table-Figure）
- 四轮 GPU 实验评估，结论一致：无高 ROI 实验
- Trajectory figure (Fig 3) 审查 PASS
- 最终写作评估：Related Work / Abstract / Limitations 均已就绪

**Registry**：39 experiments，19 success + 20 negative，全部 DONE。无 RUNNING/PREPARING。

**等待中**：用户审批 (apr_20260518T222713_5skg) → 提交 R16。

### 4. 📋 待办
- 用户审批到达 → 提交 R16（Agent 执行，Reviewer 不阻塞）
- 若 Director 要求最后一轮论文审查 → 读最新 tex diff，校验数据一致性
- 若收到新 worker_done 通知（如 writing patches）→ 审查 claim-evidence 匹配
- 若 API key 到手 + Director 决定做 IAA → 审查 IAA 结果的 kappa 值合理性（预期 Cohen's κ ≥ 0.6 为 acceptable）
- 若论文 PDF 生成 → 可用 `paper-visual-review` skill 做视觉审查（字体/图表/排版）

### 5. 🎯 战略上下文
**核心结论**：Layer selection sensitivity 是最强 contribution（审稿人给分的关键）。HS > text 是 conditional finding（encoder-quality boundary：MiniLM 4/4 HB → E5-Mistral 2/4 → BGE-large 1/4）。预估 Overall 3.5 (Borderline Conference)，Findings 概率最高 (45-50%)。

**决策链要点**：D048 IAA 降级、D049 不补实验+释放 GPU。这两个决策是我建议的，Director 采纳了。

**易错点**：
1. **不要被"跑更多实验能提分"的直觉误导**。3.5→4.0 的 gap 是 contribution framing（characterization vs solution），不是 evidence 不够。已在四轮评估中反复论证。
2. **32B claim 已经过 R15 精确校准**（"all four models†, though 32B results carry model-specific caveats"）。不要进一步软化到 "7-8B only"——那会砍掉太多贡献 scope。也不要回退到无 caveat 的 "all four models"。
3. **BOCPD 失败有两种不同机制**（OT-7B: 太陡峭 0→1 in 1-2 steps；R1-32B/QwQ: 太平滑）。commit 094d890 已修复叙事，但如果有人改动 appendix BOCPD 段，确认没有退回"统一解释"。
4. **rebuttal_prep.md 有 6 处数据不一致**（我标记过）。如果审稿后需要写 rebuttal，必须先更新该文件，不能直接使用。


---
