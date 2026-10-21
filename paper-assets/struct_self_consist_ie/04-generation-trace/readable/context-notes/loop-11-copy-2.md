# agent / loop_11.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`479895babc4e64dfe803.json`](../../sessions/47/479895babc4e64dfe803.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-16T00:57:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 上 cuda:0, cuda:1, cuda:2, cuda:3（config 已确认）
- 论文数据必须来自 gold-filtered 管道（排除 gold-empty 实例）。CoNLL n=2756, SciERC n=551/529。**不要用 registry metrics 中来自 report.json 的 EM/VC 值**——必须用分析脚本输出（与 Qwen 同一套管道），已知两者存在系统性差异（memory.md D066）
- Table 4 SciERC 8B 数据已统一为 Table 1 的 v2 checkpoint 值（D100），不要再用旧值
- unified_rho_full.json 中 LLaMA SciERC 数据已修复污染（D092-D094），canonical 数据在 artifacts/analysis_unified_rho.json
- 论文 ε 默认=0.05，有 sweep 实证支撑（D095），不要随意改
- DDL: **2026-05-25**，9 天，无 buffer

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（别名 bjb1-21071），4× RTX 5090 32GB，**全部空闲**
- 工作目录：/root/autodl-tmp/struct_self_consist_ie/
- Python：/root/miniconda3/bin/python（conda base）
- 环境激活：`source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 基座模型：/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/
- 8B merged checkpoint: checkpoints/qwen3-8b-scierc-merged-v2/
- 4B merged checkpoints: checkpoints/qwen3-4b-conll2003-merged-ckpt4200, checkpoints/qwen3-4b-scierc-merged（推测，需确认）
- ε sweep CSV: analysis_round8/epsilon_sweep.csv
- 活跃进程：无（0 running workers, 0 active crons, 0 RUNNING experiments）

### 3. 📊 当前状态
Registry 104 实验全部 DONE（58 success / 22 negative / 4 failed / 其余 killed/superseded）。无 RUNNING/PREPARING。

上一轮 session（5/15-5/16）完成了：
- 4B scale ablation 2×2 矩阵全部跑完并分析（D098），结论：gap 与 model capacity 无关
- Table 1 vs Table 4 rho 不一致分析（worker_analysis_table1_vs_table4_rho_discrepancy, done）→ D100 统一数据
- Round 8 内容修补（worker_paper_r8-content-patch, done）+ 压缩（worker_paper_r8-framing-compress, done）
- FK independence TOST 修复（worker_analysis_fk-independence-tost-fix, done）
- **worker_paper_round8-fixes 失败**——需要调查原因并重新派发
- Round 8 审稿任务 1-4 分析 + thinking tokens + RE multiseed 分析全部完成

**关键路径现在在论文写作修复上**，不在实验上。ROADMAP 列出的待办：
1. ~~Registry desync 清理~~ → 大部分完成
2. Paper Agent: 4B scale ablation Patch（compact table ≤0.5 页）
3. Paper Agent Phase 1: 页数压缩至 ≤8 页（含 4B table）
4. Paper Agent: ε robustness 写入
5. Paper Agent Phase 2-5: 标题/Abstract/RE标注/次要修复
6. Round 9 审稿
7. Final polish + 提交

### 4. 📋 待办（条件触发式）
- 启动即刻 → 调查 worker_paper_round8-fixes 失败原因，重新派发或拆分任务
- 启动即刻 → 派 Paper Worker 执行 4B compact table 写入 + 页数压缩（Phase 1，最高优先级）
- Phase 1 完成 → 派 Paper Worker 做 Phase 2-5（标题去 overclaim、Abstract 精简、RE "preliminary" 标注、次要修复）
- Phase 2-5 完成 → 启动 Round 9 审稿（continue mode）
- Round 9 审稿若发现需要补充实验 → 4 块 5090 待命，立即提交
- Round 9 审稿通过 → Final polish → 提交（DDL 5/25）
- Director 任何时候问进展 → 汇报带 `[资源] GPU 分配 4 / 实际跑 0 | Worker 池 0 (全部论文写作阶段)`

### 5. 🎯 战略上下文
**核心结论**：Structured IE 中 confidence signals 的 correlation-selection gap 是 universal 的——controlled free-form ablation 证明 score compression 是 model/task intrinsic，非 constrained decoding artifact。4B scale ablation 进一步证明与 model capacity 无关，task difficulty 是主驱动。

**决策链关键节点**：
- D098: 4B 2×2 矩阵完成，R14 reviewer concern RESOLVED
- D095: ε=0.05 robustness 有实证，BLOCKING #2 已解决
- D100: Table 4 SciERC 8B 数据统一为 v2 checkpoint 值
- D073: RE signal effectiveness 是 task-dependent（LP > structural in RE），已纳入 framing

**易踩的坑**：
- 不要把 GC4-par 和 GC4-seq 直接对比（不同 decoding regime）
- 不要从 registry metrics 引用 EM/VC 到论文（report.json vs 分析脚本有系统性差异）
- Round 8 还有 2 个 HIGH issue 未解决：标题 overclaim + Abstract 过载（Phase 2 任务）
- worker_paper_round8-fixes 失败了但后续的 r8-content-patch 和 r8-framing-compress 成功了——可能部分修复已完成，查清楚再派新 worker 避免重复工作
- 9 个 PREPARING+killed 的老实验因状态机限制无法推到 DONE，不影响任何事，忽略即可
- 论文当前可能超页数限制（≤8 页），压缩是 Phase 1 的核心任务


---
