# reviewer / loop_4.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`f4e4dc4ab7c814c677a2.json`](../../sessions/f4/f4e4dc4ab7c814c677a2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-16T00:58:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- **C001**: count_40 子集来自 80-type pool 采样，论文必须写 "40-rel subsets sampled from the 80-relation pool"，不能暗示独立 pool
- **C002**: 3.4× amplification 仅基于 16-type vs 80-type 两个 pool size，40-rel 不是第三个独立数据点
- **GPU**: 服务器 cqa1-38874，只有 cuda:0（单卡 RTX PRO 6000 Blackwell 98GB），当前空闲
- **v1/v2 prompt 区分**: 主文 NER count curve 用 v1（0.72→0.42），cross-model table 用 v2（0.640→0.304）。两套数字不能混用，caption 已解释
- **tab:cross_model_bcs 比值**: LLaMA 效应是 Qwen3 的 **77-87%**（不是 75-87%），ROADMAP 里还是旧值 "75-87%"，尚未修正

### 2. 🖥️ 基础设施快照
- 服务器: cqa1-38874(root)，工作目录 /root/schema-dag-extraction
- 本地 workspace: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/
- 论文源文件: 本地 `docs/paper/*.tex`（Paper Agent 在本地编辑，非远程）
- 图表 PDF: 本地 `docs/paper/../../figures/paper/fig_*.pdf`（即 `figures/paper/`）
- 远程图表脚本: `/root/schema-dag-extraction/figures/paper/*.py`（已同步到 exp001 数据）
- 无 W&B 配置（本项目不查 W&B）
- 活跃进程: 无。GPU 空闲，无 tmux/cron

### 3. 📊 当前状态
- 写作迭代 3 轮收敛完成，Overall=8/10，Soundness=3/4
- Registry 31 个实验全部 DONE，无 RUNNING/PREPARING
- 刚提交了 Soundness 3→4 提分方案评估：**推荐方案 1（16-rel 100 random batches + bootstrap CI）**填 tab:bcs_controlled 的 "---"，1-2 GPU 小时，完成后做 amplification ratio bootstrap。方案 2/3 不推荐
- paper_provenance.yaml 覆盖率仍 0/32（已报 Director 两次，未被处理）
- 等待 Director 决策：是否启动 16-rel 扩展实验

### 4. 📋 待办
- Director 批准 16-rel 扩展 → 审查实验设计（batch 数量、BCS 分 bin 策略）→ 实验完成后核实数据 → 审查 tab:bcs_controlled 更新
- 16-rel 实验完成 → 审查 amplification ratio bootstrap CI 是否替代了 "range 1.9-4.7×" 的非正式估计
- Paper Agent 提交最终版审查 → 走 §5.3 模板评分，重点看 Soundness 是否因新数据提到 4
- Director 启动 reference audit / submission prep → 审查 bib 完整性、page count
- paper_provenance 被填充 → 审查 evidence 数组是否指向正确 exp_id

### 5. 🎯 战略上下文
- **核心结论**: schema-induced degradation = count channel（recall 下降）+ confusability channel（type confusion），RE 上可分离，NER 上交互。高 BCS 准确率 ≈51% 是 model-invariant floor。SDGD 是 informative negative（merge amplification）
- **决策链关键节点**: D019（放弃 SDGD positive claim）→ D026（交互效应 negative）→ D028（NER Channel 2 跨模型未复现）→ D031/D032（RE Channel 2 跨模型强复现，激活 Scenario A）
- **易踩坑**:
  - 本地 PDF 和远程 .py 脚本可能不同步（本 session 踩过 CRITICAL）——改图后两边都要验证
  - NER Channel 2 跨模型 **未复现**（floor effect + metric noise），论文只在 Limitations 提及，不要误以为双任务都复现了
  - MAVEN 方向是 **反的**（centrality confound），per-type BCS 在 same-domain schema 上不可用，只有 pairwise SCS 有效
  - 16-rel BCS 范围窄（0.78-0.89），新实验的 gap 可能比 9.1pp 小——这不是 bad news，amplification ratio 反而更大


---
