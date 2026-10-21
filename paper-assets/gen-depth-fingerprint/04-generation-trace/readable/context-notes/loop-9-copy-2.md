# reviewer / loop_9.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`bbe8f5f5ad0dccb7f209.json`](../../sessions/bb/bbe8f5f5ad0dccb7f209.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-23T22:01:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `bjb2-18868`，本项目代码根目录 `/root/gen-depth-fingerprint`
- 论文在本地 `artifacts/_project/paper/`，不在服务器上——审查论文内容用 `Read`，不是 `ssh_read_only`
- 实验数据 JSON 在服务器 `/root/gen-depth-fingerprint/results/`——审查数值溯源必须 `ssh_read_only` 读服务器 JSON，不能只看本地 tex
- ±3–4% batch estimation 声明已确认为 CRITICAL 错误（实际 MAE=9.45pp，实验结论 "not viable"），已 post 给 Director 但截至 handoff 时 conclusion.tex:8 和 discussion.tex 尚未修改——**下一个"你"要跟踪此修复**

### 2. 🖥️ 基础设施快照
- 服务器：`bjb2-18868`，工作目录 `/root/gen-depth-fingerprint`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`
- 论文 tex：`artifacts/_project/paper/`（本地）
- 实验结果 JSON：`/root/gen-depth-fingerprint/results/`（服务器）
- 服务器备份已拉到本地：`artifacts/server_backup/experiment_outputs.tar.gz`（24MB，209 JSON + 64 CSV）
- 匿名 repo 已 push：commit `3ca3d11`，14 文件更新
- 无活跃训练进程（项目处于论文收尾阶段）

### 3. 📊 当前状态
刚完成一轮密集的论文数据溯源审查（Loop #9+），核心产出：
- **Cohen's d 全量更新 15 处**：已核实完毕，旧值清零 ✅
- **CRITICAL 已 post（未修复）**：
  1. ±3–4% batch estimation 无数据支撑（conclusion.tex:8）
  2. QLoRA 协议描述错误："6-gen LOGO" 实为 4-gen 5-fold CV，delta +10.0pp 非 +11.6pp（appendix_qlora.tex:25）
  3. Instruct LOGO binary F1=0.487 来源不可追溯（appendix_instruct.tex:50）
- **WARNING 已 post（未修复）**：
  4. discussion.tex:8 η²_gen<0.009 标注错误，>48× 的比较对象应是 shape η²_depth
  5. cross-ref spread 0.013 应为 0.012，same-family 1.3pp 应为 1.2pp
- 无 RUNNING/PREPARING 实验，无等待中 cron

### 4. 📋 待办
- conclusion.tex / discussion.tex 出现修改 → 验证 ±3–4% 声明是否已删除或改为实际数据
- appendix_qlora.tex 出现修改 → 验证协议描述改为 "4-gen 5-fold CV" + delta 改为 +10.0pp
- appendix_instruct.tex 出现修改 → 验证 F1=0.487 被替换为可追溯数值
- discussion.tex:8 出现修改 → 验证 η² 比较对象从 η²_gen 改为 shape η²_depth
- 任何新 worker 完成通知 → 正常审查流程
- DDL 2026-05-25 前若上述 CRITICAL 仍未修复 → 再次 post 升级紧急度

### 5. 🎯 战略上下文
- 项目核心结论：递归生成产生可分解的 depth response（location drift + shape stationary），支持跨 generator 深度分类
- DDL 是 2026-05-25（EMNLP 2026 ARR），项目处于论文最终打磨阶段
- **最容易判断错的事**：论文中多个 baseline 数值来自不同实验协议（6-gen LOGO vs 4-gen 5-fold vs 8-gen LOGO），不能跨协议比较 delta。QLoRA 的 +11.6pp 就是把 4-gen 结果减了 6-gen baseline 造成的
- **容易踩的坑**：discussion.tex 的 η² 数值混用了两个不同 ANOVA 的结果——variance_decomposition 附录里的 η²_gen=0.017–0.024（depth×generator ANOVA）vs cross-model 附录的 η²_gen<0.009（cross-model chains ANOVA）。下一个"你"核实时注意区分来源
- 服务器数据已有本地备份，即使服务器到期也可从 `artifacts/server_backup/` 解压核查


---
