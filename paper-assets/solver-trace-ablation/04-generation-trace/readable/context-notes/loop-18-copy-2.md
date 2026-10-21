# reviewer / loop_18.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`2dad25a1e829ba57fa39.json`](../../sessions/2d/2dad25a1e829ba57fa39.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-17T16:57:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-39279 上只能用 cuda:0 和 cuda:1。越界 → severity: critical + kill 进程
- 当前 GPU 已释放至 1 张（用户指令），DDL 2026-05-25 不允许新训练实验
- 论文主体 ≤8 页（ACL format），Limitations/Ethics/References 不计入。当前刚好达标，任何正文扩展需同步压缩
- fol-detailed s42 1000-step H1=100% 是 **推断值**（$^\P$ 标注），不是 text-match 结果。exec-only-1000 表对 s42 标 "---"。两表立场不同但已标注一致，不要混用

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，代码目录 /root/solver-trace-ablation
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/
- 论文目录：上述 workspace 下 paper/（main.tex, *.tex, figures/, _pdf_images/）
- 无活跃训练进程（GPU 已释放）。无 tmux session、无 cron。纯 paper-editing 阶段

### 3. 📊 当前状态
**刚完成**：Round 6 Batch 1 审查（d1af6f2）— 5 个 critical + SF1/SF7 全部 PASS。
- ISR 全文统一为 "Irreducible Solver Rate"
- Abstract 重写 ~149 words，"suggesting"/"suggestive but non-robust" 弱化到位
- Table 1 新增 exec-only 1000-step 行（PR=97±2%, H1=---, N-H≤2）
- OR framing 改为 "sensitive to classification methodology"，CMH 标注 "uncorrected classification"
- Discussion 扩展：stochastic bifurcation + "that vs how" 区分
- 页数：Section 5 完全在 page 8 内，Section 6 从 page 8 底部开始。总页 22→21

**等待中**：Round 6 Batch 2（SF3-SF8 + NF1-NF6），预计作为下一个 worker_done 到达

### 4. 📋 待办
- worker_done Batch 2 到达 → 重点检查：(1) "at all tested doses" 是否加了 500-step/trajectory 限定语（SF3，8 处出现）；(2) Table 1 N-H ≤23★ 上界标注（SF4）；(3) β 呈现顺序解释句（SF6）；(4) NF6 新引用（Amodei 2016, Geirhos 2020, DeepSeek-R1）是否添加且被 cited
- 全部 Batch 完成后 → 最终 spot check：全文数字一致性（abstract vs intro vs experiments vs appendix），特别是 97±2% 和 OR 数据链
- Director 如果要求 paper_agent_request_review → 按 §5.3 模板打维度评分（Originality/Clarity/Soundness/Significance/Presentation + Overall 1-10），Soundness ≤2 或 critical → Overall ≤4

### 5. 🎯 战略上下文
- 核心结论：ISR 作为诊断可靠，作为优化目标在所有测试剂量下均 Goodhart collapse
- 论文从 Round 1 到 Round 6 经历了：95±5%→97±2% 数据修正、"localizing"→"consistent with" SFT 弱化、OR "bound above/below"→"sensitive to methodology" 中性化、"meta-level"→删除、ISR 命名统一
- **易错点**：
  - CMH (OR=3.37) 用的是 **uncorrected** 分类，不是 H8-corrected。3-seed corrected OR=0.61 是独立分析。不要说 CMH "confirms" genuine benefit
  - fol-detailed 和 exec-only-1000 对 s42 taxonomy 的处理不同（推断 vs 不可用）。Table 1 新行用 "---" 回避了冲突，不要改回具体数字
  - Abstract "5 seeds" 已改 "three seeds"（d6812b0），97±2% 是 3-seed exec-only 1000-step 数据
  - "at all four tested doses" 目前仍未加限定语（Batch 2 SF3 待执行）。只有 β=0.1 有 trajectory confirmation，其他三个是 500-step snapshot


---
