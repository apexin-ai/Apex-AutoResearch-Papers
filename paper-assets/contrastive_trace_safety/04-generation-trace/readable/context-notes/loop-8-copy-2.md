# reviewer / loop_8.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`e2095148aca71c0a7cff.json`](../../sessions/e2/e2095148aca71c0a7cff.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-24T19:14:20+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-15904，GPU 白名单需从 `execution.gpu_ids` 确认（本 session 未实际查过 nvidia-smi）
- 论文 DDL 2026-05-25（ARR EMNLP 2026），主文严格 8 页，Limitations 豁免
- Abstract ≤ 200 words（当前 188 words，已合规）
- 图例不得遮挡数据曲线（硬约束，Fig 3 之前违规过已修复）
- 一篇文章只能有一个 Limitations section，放正文，appendix 不能有
- R1-32B 是 32B 模型，不要混入 7-8B 的数据范围（之前 abstract 犯过 +15pp 混入 7-8B range 的错误）

### 2. 🖥️ 基础设施快照
- 服务器：westd-15904(root)，远程代码根目录 `/root/autodl-tmp/contrastive_trace_safety`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文源码：`docs/paper/main.tex` + `docs/paper/sections/*.tex` + `docs/paper/figures/`
- Registry：`registry.yaml`（本地 workspace 下）
- 无活跃进程 / 无 tmux / 无 cron — 全部 59 个实验已完成，项目处于论文定稿/提交阶段
- PDF 总计 33 页（8 页主文 + appendix 25 节）

### 3. 📊 当前状态
本 session 完成了两轮大审查：
1. **提交前最终质量审查**（4 维度）：Abstract 措辞、Framing 强度、Rebuttal 预判 Top 3、Figure 可读性。结论：1 个 warning（Fig 2 caption 未列出 5 个 metric 名称），其余全部 info，论文可提交。已 post 给 Director。
2. **20 个阴性实验 Rebuttal 预案**：逐条分类（A: Boundary Conditions 5个, B: Method Limitations 10个, C: Diagnostic Nulls 5个），识别 Top 3 风险（#1 Safe-trace FPR 混合, #2 AUROC 选层分歧, #3 跨模型迁移失败），为每个准备了标准回复模板。已 post 给 Director。

Registry: 0 RUNNING, 0 PREPARING。59 DONE (30 success, 20 negative, 2 failed, 7 killed)。

### 4. 📋 待办
- Director 确认论文提交 → 无需更多审查动作
- 如收到 paper_agent_request_review → 使用 §5.3 评分模板（5 维度 + Overall）
- 如收到新 commit 通知 → 验证 diff 与预期一致，无遗漏文件
- 审稿意见返回 → Read `skills/global/rebuttal.skill.md`，按 20 个阴性实验 rebuttal 预案协助回复

### 5. 🎯 战略上下文
**核心结论链**：
- C1（metric-induced layer selection bias）：CR-composite 选浅层 → threshold-based 选深层，14-61 层差异，p=0.83 vs p<0.005 逆转。已在 HarmThoughts + AdvBench + Gemma-2/Gemma-4 复现
- C2（HS advantage）：7-8B validated（+20-22pp nested CV），32B exploratory（R1-32B +15.4pp below MDE，QwQ-32B position competitive）
- C3（negative results）：7 种替代方法全部失败，control task 11-17pp above chance

**易错点**：
- QwQ-32B 的 p=0.133 来自 precision 还是 BA 比较一直有歧义——appendix L979 和主文 §4.4 都是 p=0.133，可能是同一个检验
- "encoder capacity" vs "encoder quality"：PCA capacity matching 保留 advantage 说明不是容量问题而是质量问题，所以用 "quality"
- 论文 Fig 2 caption 未列 5 个 metric 名——唯一一个 caption 不完全自包含的 figure，已标 warning
- Rebuttal 最高风险：Safe-trace FPR 混合结果（QwQ HS FPR ≈ text FPR），回复要强调核心 claim 是 precision 非 FPR


---
