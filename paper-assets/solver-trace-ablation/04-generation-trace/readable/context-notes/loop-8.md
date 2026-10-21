# director / loop_8.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`0c5ff138059eaee2a07b.json`](../../sessions/0c/0c5ff138059eaee2a07b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-17T21:07:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-39279 **仅 1 张 GPU** (cuda:0)，cuda:1 不存在。ROADMAP 此前误记为 2 张，已修正。
- nvidia-smi 显示 utilization=100% / memory=0 MiB 是 driver 状态缓存，非真实负载。无需排查。
- 论文 ACL long paper 8 页正文限制：§5 Discussion and Conclusion 必须在 page 8 内结束，§6 Limitations 起于 page 9。每次修改后用 `pdftotext main.pdf - | grep -n "Discussion and Conclusion"` 验证。
- GPU 分配仅 cuda:0，不可使用其他设备。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279 (connect.westd.seetacloud.com), user=root
- 工作目录：/root/solver-trace-ablation
- 论文本地路径：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/
- GPU：1 × RTX PRO 6000 96GB (cuda:0)，当前空闲
- 实验输出：/root/solver-trace-ablation/outputs/
- 1.7B 已有配置参考：d113-1.7b-isr-b01-s42, d113-1.7b-random-b01-s42, d113-1.7b-isr-b03-s42
- 无活跃进程，无 tmux session

### 3. 📊 当前状态
**刚完成**：Round 9 论文修改全部落地（commits 698f48b + f3c25a6 + 4550e71），Reviewer 12 项 PASS + Figure 3 更新为 5-seed + Provenance v13。Uesato 引用格式修复 + C2 "genuine windows"→"transient genuine phases" 统一。

**刚批准派出**：D129 — 1.7B cross-scale +2 seeds (s43/s44) 实验，共 6 runs。Agent 已收到指令但尚未回复确认开始执行。这是当前最重要的待跟踪项。

**Registry**: 140 experiments, 0 RUNNING（D129 的 6 runs 待 Agent 启动）。sweep-isr-b005-s42 已从 PREPARING 修复为 DONE。

### 4. 📋 待办
- Agent 回复 D129 实验启动确认 → 确认 registry 注册正确、GPU 分配 cuda:0、训练开始
- D129 每个 run 完成 → 检查 eval 结果，特别关注：任何 seed >10% genuine 需暂停讨论；不同 hacking mode 正常记录
- D129 全部 6 runs 完成 → 更新 experiments.tex §4.5（删 "Preliminary"/"exploratory"/"single-seed"，改为 3-seed 数据）+ Table 1 1.7B 行更新 + Figure 重生成 + Provenance 更新
- 论文更新后 → 提交 Round 10 内审或直接提交外审（submit_paper_to_review）
- review_issues.yaml 中 v3-R12-NI-1 → D129 完成后标 resolved

### 5. 🎯 战略上下文
**核心结论**：ISR reliable as diagnostic, unreliable as optimizer at any dose. 论文经 9 轮内审得分 3.0 Findings。

**D129 是提分关键**：1.7B 单 seed 是连续 9 轮最持久 critical concern (v3-R12-NI-1)。+2 seeds 预计 ~15 hrs，风险极低（4B 5/5 seeds 全 hack，1.7B s42 三条件全 0% genuine）。成功后预期 Overall 3.0→3.5。

**易错点**：
- 不要被 ROADMAP 中旧的 "Round 4 提交" 任务迷惑——论文已经过 Round 9，那些是历史遗留已完成项
- review_issues.yaml 有大量 in_progress/open issues，但多数是 text-level 已通过 Round 9 修复，只是 status 未更新。核心 open experiment concern 只剩 v3-R12-NI-1（D129 正在解决）和 v8-R12-N2（scope mismatch，8 天内不可能加新模型族，靠 hedging 处理）
- DDL 2026-05-25 (ARR May)，剩 8 天。D129 完成后还有充裕时间做论文更新和最终审稿提交
- 论文外审通过 submit_paper_to_review 提交给 Review Director (Group C)，研究侧不参与投稿材料准备


---
