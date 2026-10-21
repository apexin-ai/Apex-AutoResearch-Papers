# reviewer / loop_18.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_18.md`
- **Structured JSON:** [`1cbf7caaa76f17450335.json`](../../sessions/1c/1cbf7caaa76f17450335.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_wall_time
updated: '2026-05-19T11:03:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-41312 全 4 卡 + westd-30476 全 4 卡。当前全部空闲，无活跃进程，但如有新实验需确认 `execution.gpu_ids`
- 论文 tex 文件现在有两个位置：旧版 `artifacts/_project/paper/` (May 16, 已废弃) 和新版 `docs/paper/sections/` (May 19, 当前活跃)。**只审查 `docs/paper/sections/`**，不要被旧路径误导
- Table 1 per-seed 值刚从 registry 精确值完全重建（M035），绝不能再用旧的 2dp inline eval 值覆盖回去
- ForTIFAI 引用的正确 cite key 是 `zibakhsh2025fortifai`（不是 Zhang et al.），bib 已修正

### 2. 🖥️ 基础设施快照
- 服务器：westd-30476 (root) + westd-41312 (root)，各 4× RTX PRO 6000 96GB
- 远程代码根目录：`/root/provenance_weight_training`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/`
- 论文目录：`docs/paper/sections/*.tex` + `docs/paper/main.tex` + `docs/paper/references.bib`
- 全部 checkpoint 已删除，仅 seed42 adaptive_fix + uniform 存活于 westd-41312（seeds 123/456 已清理）
- 活跃进程：无。全部 GPU 空闲。无 RUNNING 实验。无 cron 任务。

### 3. 📊 当前状态
**我刚完成**：Paper Agent Phase 1-5 全部修复的独立数据审计。Table 1 重建、Checklist GPU 修正、Cohen's d 删除、W2 整合——全部核实通过（最后一份 PASS 报告已发 Director）。

**Registry 状态**：152 个实验全部 DONE/FAILED/KILLED，零 RUNNING/PREPARING。

**等待中**：
- 用户批准 Round 6 审稿（ROADMAP 标注 "等用户批准"）
- Round 6 审稿返回后 Director 可能触发 Mode B 章节对抗审查（§5 protocol）
- 最终 PDF 编译确认

### 4. 📋 待办
- Round 6 审稿返回 → Mode B 逐章节对抗审查，重点检查 claim-evidence 匹配和 overclaim
- Director 转发 Paper Agent 写作审查请求 → 按 §5.3 评分模板返回维度评分 + 具体问题
- 发现论文引用 results.tex L11 "PPL 17.693" (fixed b*=1.19 as uniform proxy) → 来源不确定，非 Table 1 数据，需确认 registry 对应实验
- paper_framing.md 中 grid b=0.3 per-seed 值仍陈旧（seed123=17.638 应为 17.579）→ 如有人依赖 framing 做决策需提醒更新
- 如触发预提交检查 → 需验证：(a) dash sweep 已完成（当前版本零 dash ✓）；(b) 编译无错误；(c) 引用完整性；(d) ARR checklist 逐项

### 5. 🎯 战略上下文
**项目核心**：D091 将论文从 method paper 转为 analytical study（Findings track）。4 个贡献：(1) Epoch confound (2) Distribution matching (3) Mechanism + detector type (4) Adaptive b* as tool。

**决策链关键节点**：D056 binding stats 修正 → D074 grid-best=b=0.3 → D090 1.7B 撤回 → D091 reframe → D093 W2 整合

**最容易判断错的事**：
- ESS-only std 从旧版 ±0.007 变为 ±0.022（因旧 per-seed 值全错），不要用旧数据判断"ESS-only 方差很小"
- W2 distribution matching 只有 seed42 单 seed（其他 checkpoint 已删），任何引用该结果的地方必须标注 single-seed caveat
- N=3 的统计限制是真的——bootstrap/permutation test 都无法达到 p<0.05，不要试图声称 statistical significance
- 论文目前 Findings 概率 ~3.0-3.25/5，最大风险不是 W2（已转化为贡献），而是 N=3 + 小效应量 + 仅 0.6B 规模


---
