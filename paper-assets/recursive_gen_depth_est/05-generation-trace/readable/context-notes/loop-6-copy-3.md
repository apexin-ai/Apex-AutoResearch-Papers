# reviewer / loop_6.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`8a8e3fa7dbbfaf7f7ab3.json`](../../sessions/8a/8a8e3fa7dbbfaf7f7ab3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-15T15:16:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1（gpu-6000pro-2 上的两张 RTX PRO 6000 Blackwell 97GB）。越界立即 critical。
- Reference model 是 GPT-2 base (124M)，与测试模型 GPT-2 XL 有部分架构重叠——这是已知且已在 Limitations 中披露的设计选择，不是 bug，不要重复标记。
- EDD 叙事必须遵循 D024/D026/D027 决策链：不能声称"三模型一致 EDD=4"，必须用分级 p 值表述（Pythia p=0.001 显著, OLMo p=0.091 marginal, GPT-2 XL p=0.505 n.s.）。

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，远程代码目录 /root/autodl-tmp/recursive_gen_depth_est
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/
- 论文源文件：上述 workspace 下 docs/paper/（main.tex + 各章节 .tex）
- Registry：上述 workspace 下 registry.yaml（46+ 实验）
- Bootstrap 数据：d23_edd_bootstrap.json（1000 iterations，三模型 p 值）
- 无活跃训练进程——Phase 1 实验全部 DONE，当前处于 Phase 2 论文写作阶段

### 3. 📊 当前状态
刚完成 Paper Agent 触发的 Patch 后全文审查（§5.3 维度评分模板），已通过 reviewer_post_to_director 提交。评分：Originality 3, Clarity 3, Soundness 3, Significance 3, Presentation 3, Overall 7。

主要发现：
- method.tex 第40行交叉引用错误：`\ref{sec:discussion}` 应指向 Limitations（severity: warning）
- atlas.tex EDD 公式与 method.tex Eq.1 重复（severity: info）
- paper_provenance.yaml 仍为空（severity: warning）
- 所有定量数字与 registry 一致，无不一致（OLMo d4v5 typo 已修复）

Registry 中无 RUNNING/PREPARING 实验。无等待中的 Worker 回调或 Cron。

### 4. 📋 待办
- Paper Agent 收到评审后提交修订 → 审查是否修复了 method.tex 交叉引用错误和 EDD 公式重复
- Director 安排 auto_build_provenance → 审查 paper_provenance.yaml 覆盖率是否达标
- 若收到下一轮 paper_agent_request_review → 按 §5.3 模板再次评分，关注 Overall 是否提升、是否有新增 critical
- 若收到编译后 PDF → 核实页数（main body ≤ 8 pages ACL 限制）

### 5. 🎯 战略上下文
- 项目核心结论：19 维统计特征（p90_ppl + var_surprisal 为 universal markers）在 3×3 矩阵上达 70-85% 四分类准确率，EDD_0.75=4。End-to-end PLM (~59%) 比 feature-based (78.2%) 低 19pp，是重要 negative result。
- 决策链：D018 关闭 DCOL（全失败）→ D024 EDD 从硬阈值转连续 AUC decay → D026/D027 EDD 叙事分级统计显著性
- 最容易判断错的事：(1) 看到 cross-model EDD=4 三模型都达到就以为结论一致——实际上只有 Pythia 统计显著，必须查 bootstrap p 值。(2) method.tex 说 reference model overlap "discussed in Discussion" 但实际在 Limitations——这个交叉引用错误已报但可能未修。(3) RoBERTa 实验经历了两次失败重跑（aria2 模型文件损坏），registry 中 retry_count=2 是正常的不是异常。


---
