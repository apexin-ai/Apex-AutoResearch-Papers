# reviewer / loop_14.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`6fc4168fba251ccdf0a5.json`](../../sessions/6f/6fc4168fba251ccdf0a5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-27T12:14:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU: westd-19183 的 2× RTX PRO 6000，`gpu_ids` 需查 constraints.yaml 确认白名单（全部实验已完成，GPU 空闲待释放）
- 论文页面限制：CoRL 2026 = 8 页正文 + references。当前 §5 Discussion 已在第 9 页顶部（与 References 同页），**零空间可用**，任何正文新增必须等量删除
- 不要建议"降级 venue"——venue 决策不在 Reviewer 职责范围内
- 审"未改"类结论前必须双边核对源：论文在本地 workspace `projects/vla-ssd/docs/paper/`，训练代码/数据在远程 `/root/vla-ssd/`

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183，远程代码根 `/root/vla-ssd/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/`
- 论文源码：`projects/vla-ssd/docs/paper/`（main.tex + 7 个 .tex + figures/）
- 编译 PDF：`docs/paper/main.pdf`（最新 2026-05-27 06:54 UTC，43 页含 appendix）
- Rebuttal：`artifacts/submission_package/anticipated_rebuttal_v2.md`（Q1-Q12）
- 无活跃进程、无 tmux session、无 cron。全部 107 success 实验已完成。GPU 空闲，释放请求已提 Manager 5 次未批。
- W&B 项目存在但本轮未用（核查指标直接读 registry）

### 3. 📊 当前状态
**全部审查完成，论文提交就绪，等待用户操作 OpenReview 提交（DDL 5/29）。**

本轮（Loop #14）完成的审查：
1. Type 3 字体最终验证 → ✅ 零 Type 3（38 CID TrueType + 26 Type 1）
2. Q11 rebuttal 强化确认 → ✅ 已含 "Scientific validation of the metric" 段
3. 布局检查 → ✅ 0 critical, 8 warning（均无害）
4. 进攻性实验评估（Director 触发）→ 结论：107 实验中无值得跑的新实验，核心弱点（venue fit）不可通过实验解决
5. 纯写作层面进攻评估（Director 触发）→ 结论：写作接近该 scope 极限，总边际提升 ~1.5-2pp（55%→57%），仅 Abstract 加 NLP controls 和 Discussion staged pipeline 微调值得考虑

Registry: 0 RUNNING, 0 PREPARING。154 total (107 success / 19 negative / 12 killed / 7 failed)。无等待中的回调。

### 4. 📋 待办
- Director 批准 Abstract/Discussion 微调 → 验证修改后叙事一致性 + 重新确认页面未溢出
- 用户提交论文 → 无需 Reviewer 动作
- 审稿意见返回 → 加载 `rebuttal` skill，对照 `anticipated_rebuttal_v2.md` 逐条评估覆盖率
- Manager 批准 GPU 释放 → 无需 Reviewer 动作
- Director 转发新 framing 提案 → 加载 `negative-framing-review` skill 四维度审

### 5. 🎯 战略上下文
**核心结论**：VLM→VLA fine-tuning 引发 exit collapse（ΔR²=0.156-0.455, 6/6 cells），VLA→VLA 不引发（0/4 cells, ΔR²<0.10），NLP controls 确认 specificity（3/3, ΔR²=0.000）。L1 instruction attention 是 inherited 而非 trained。

**中稿率估计**：53-58%，median 55%。主要风险是 venue fit（analysis paper at robotics venue）。

**关键决策链**：D105（Qwen NLP control 闭合 stated limitation）→ D107（n=9 behavioral correlation 为设计硬约束，终结扩展讨论）→ D108/D110（无可跑实验，GPU 空置）→ D112（关闭 action-head decoding 实验线）

**易错点**：
1. 不要被 19 个 negative 实验吓到——已逐条审查（D110），均为 honest negative，无一值得重试
2. specificity control 只有 8% gap（d=0.65 vs 0.60）——这是 distributed routing 的证据，不是 specificity 失败。论文已正确 frame 为"instruction information woven into general residual stream"
3. NORA-Goal ΔR²=0.455 的 bootstrap CI 不可靠（exit R²≈-0.006 artifact）——论文用 footnote b 标注，核心结论不依赖此 cell（排除后 VLM→VLA range 仍 0.156-0.362）
4. 不要把 Cohen's d（action-space）和 cosine distance（representation-space）跨指标比较——论文 §4.4 已明确标注 incommensurability


---
