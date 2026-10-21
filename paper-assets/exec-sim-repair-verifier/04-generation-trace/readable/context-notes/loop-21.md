# director / loop_21.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_21.md`
- **Structured JSON:** [`c544fb0a2594587b66cd.json`](../../sessions/c5/c544fb0a2594587b66cd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_messages
updated: '2026-05-21T13:04:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配：autodl-l40s-0 的 cuda:0-3（4×L40S），autodl-5090-0 的 cuda:0-3（4×RTX 5090）。不得使用其他设备号
- Table 3 的 CWM \tbd{} 占位符：等多 seed 数据到齐后才能填，不要用单 seed 数据提前填
- Fig 2/3 内容已被用户明确要求恢复原版布局，不要再改内容/figsize/布局，只允许改字体
- 参数修改（seq_length/bs/precision/lr）必须经 Director 审批，不得自行降级（D103 教训）

### 2. 🖥️ 基础设施快照
- **autodl-5090-0**：工作目录 /root/autodl-tmp/exec-sim-repair-verifier，Python /root/miniconda3/bin/python，conda base 环境
  - 模型：/root/autodl-tmp/models/ 下 Qwen3-4B/8B, DeepSeek-Coder-6.7B-Instruct
  - HF cache：/root/autodl-tmp/.hf_cache
  - 4 个 CWM 训练在跑（截至 handoff）：DS s456-v2 ETA ~12:43 UTC, Qwen s123+s456 ETA ~21:30 UTC, DS s123-v2 ETA ~23:15 UTC
- **autodl-l40s-0**：同结构，/root/autodl-tmp/exec-sim-repair-verifier
- **本地论文**：/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/
- **artifacts**：同项目根下 artifacts/，图表脚本和输出都在这里

### 3. 📊 当前状态
- **刚完成**：导师要求的 3 张图修复（Fig1 标题上移、Fig2/3 恢复原版布局+serif 字体）、论文编译确认（仅剩 1 处 0.52pt overfull，可忽略）
- **已派 Agent**：论文文字打磨任务（Related Work/Conclusion 质量扫描、残留 placeholder 检查、编译验证），Agent 回复尚未返回
- **RUNNING 实验**：4 个 CWM 多 seed 训练（registry 中应有对应条目），用于填充 Table 3 和完善 multi-seed 统计
- **已准备好的资产**：cwm_data_fill_checklist.md（19 处待更新位置）、scenario_a_templates.md（CWM 数据到齐后的叙事模板）、W5 regression 脚本

### 4. 📋 待办
- Agent 文字打磨任务回调 → 审查修改质量，确认无过度改动
- DS s456-v2 训练完成（ETA ~12:43 UTC）→ 启动 eval，测试 Qwen eval batch=2+
- 全部 4 个 CWM 训练完成 → 跑 eval → 按 cwm_data_fill_checklist.md 填充 Table 3 + 更新 caption + 移除"in progress"措辞 → 用 scenario_a_templates.md 升级叙事
- CWM 数据到齐后 → 更新 Fig 2 error bars → W5 complete regression → Round 7 内审（目标 5月23日）
- 5月25日 ARR DDL 前完成终稿提交

### 5. 🎯 战略上下文
- **核心 story**：三种 execution-free verification formulation（CLS/CWM/TRAJ）的系统性实证比较。Core claims：CLS > CWM（尤其 repo-level gap 放大 20x）、block-correlation 模型下 per-test advantage 集中在 T≥2 实例
- **当前瓶颈**：CWM 多 seed 数据。单 seed 已有，但论文需要 multi-seed 统计才能报置信区间。Table 3 是最关键的待填表
- **易错点**：导师对图表布局很敏感，已明确要求 Fig2/3 保持原版内容不动——不要让 Agent 再"优化"这两张图的内容或尺寸。只有字体可以改
- **appendix 表格溢出已全部修复**（5 张表加了 resizebox，Table 11 拆分为 shared + model-specific 两个子表）
- **决策链**：参见 decisions.yaml，关键决策包括 CLS formulation 优先、block-correlation oracle 分析、CWM multi-seed 补充实验


---
