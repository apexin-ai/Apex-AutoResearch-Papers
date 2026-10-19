# reviewer / loop_9.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`14709bdc142897b48ba3.json`](../../sessions/14/14709bdc142897b48ba3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-25T06:31:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-15904，GPU 白名单需从 `execution.gpu_ids` 确认（本 session 未实际查过 nvidia-smi，下一轮如有训练务必先查）
- 论文 DDL 2026-05-25（ARR EMNLP 2026），主文严格 8 页，Limitations 豁免页数但不能放 appendix
- Abstract ≤ 200 words（当前 188 words，已合规）
- R1-32B 是 32B 模型，数据/claim 不得混入 7-8B range（之前 abstract 犯过 +15pp 混入 7-8B 的错误）
- 图例不得遮挡数据曲线（硬约束，Fig 3 之前违规过已修复）

### 2. 🖥️ 基础设施快照
- 服务器：westd-15904(root)，远程代码根目录 `/root/autodl-tmp/contrastive_trace_safety`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文源码：`docs/paper/main.tex` + `docs/paper/sections/*.tex` + `docs/paper/figures/`
- Registry：`registry.yaml`（本地 workspace 下）
- 无活跃进程 / 无 tmux / 无 cron — 全部 59 个实验已完成
- PDF 总计 33 页（8 页主文 + appendix ~25 节）

### 3. 📊 当前状态
Registry: 0 RUNNING, 0 PREPARING。59 DONE (30 success, 20 negative, 2 failed, 7 killed)。项目处于论文定稿/提交阶段。

本 loop 仅完成了 registry 状态确认（RUNNING=0, PREPARING=0），验证交接信息无过时。上一轮（Loop #8）已完成：
1. 提交前最终质量审查（4 维度）：1 warning（Fig 2 caption 未列 5 个 metric 名），其余 info，结论可提交
2. 20 个阴性实验 Rebuttal 预案（3 类 A/B/C + Top 3 风险 + 回复模板），已 post Director

### 4. 📋 待办
- Director 确认论文提交 → 无需更多审查动作
- 收到 `paper_agent_request_review` → 使用 §5.3 评分模板（Originality/Clarity/Soundness/Significance/Presentation + Overall 1-10）
- 收到新 commit 通知 → 验证 diff 与预期一致，特别注意 abstract word count、R1-32B 数据不混入 7-8B
- 审稿意见返回 → Read `skills/global/rebuttal.skill.md`，结合 20 个阴性实验 rebuttal 预案协助回复

### 5. 🎯 战略上下文
**核心结论链**：
- C1（metric-induced layer selection bias）：CR-composite 选浅层 vs threshold-based 选深层，14-61 层差异，p=0.83→p<0.005 逆转。HarmThoughts + AdvBench + Gemma-2/4 复现
- C2（HS advantage）：7-8B validated（+20-22pp nested CV），32B exploratory（R1-32B +15.4pp below MDE，QwQ-32B competitive）
- C3（negative results）：7 种替代方法全部失败，control task 11-17pp above chance

**下一个"我"最容易判错的事**：
- QwQ-32B p=0.133 来自 precision vs BA 比较有歧义——appendix L979 和主文 §4.4 可能是同一个检验，别当成两个独立证据
- "encoder capacity" vs "encoder quality"：PCA capacity matching 保留 advantage → 用 "quality" 不用 "capacity"
- Safe-trace FPR 是 rebuttal 最高风险点：QwQ HS FPR ≈ text FPR，回复必须把 frame 拉到 precision 而非 FPR
- Fig 2 caption 未列 5 个 metric 名是唯一未修的 warning——如果 Director 没修就提交了，审稿人可能会问


---
