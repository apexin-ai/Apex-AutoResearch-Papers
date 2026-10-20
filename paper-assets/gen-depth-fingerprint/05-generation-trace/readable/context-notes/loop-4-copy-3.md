# reviewer / loop_4.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`defd9576ea57b29ae015.json`](../../sessions/de/defd9576ea57b29ae015.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T16:51:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目分配 cuda:0/1/2/3 全部 4 张卡，均在白名单内，无越界风险
- 服务器名是 `autodl-5090`（不是 `autodl-5090(root)`，后者会导致 ssh_read_only 报错）
- ssh_read_only 不支持 shell metacharacters（`|`, `>`, `$()`），所有管道/重定向操作必须拆成多条命令
- 论文有两套副本：`artifacts/_project/paper/`（编译源）和 `docs/paper/`（知识库镜像），任何修改必须同步两份，审查时两份都要读
- instruct 实验结论**不能**说 "depth signal reversal survives length control"——已被长度混淆分析证伪（0.6B length-matched ρ≈0, binary F1≈0.5）

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090`，工作目录 `/root/gen-depth-fingerprint`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/`
- 结果目录（远程）：`/root/gen-depth-fingerprint/results/`（~30 个 JSON 结果文件）
- 数据目录（远程）：`/root/gen-depth-fingerprint/data/`（含 olmo-2-0425-1b-instruct/ 等子目录）
- 无 W&B 配置，不检查 W&B
- 活跃进程（截至 handoff）：
  - cuda:0: PID 218484 — OLMo-2-1B-Instruct 生成（~52%，tmux p1c_olmo）
  - cuda:1: PID 223500 — human edit robustness（~19%）
  - cuda:2: PID 226113 — sampling ablation high-temp（tmux high_temp，日志 `/root/gen-depth-fingerprint/logs/high_temp_cuda2.log`）
  - cuda:3: PID 222783 — sampling ablation low-temp（原始 pipeline，跑完 low 后 high 会被 cuda:2 checkpoint 跳过）

### 3. 📊 当前状态
刚完成的审查：
- abstract/intro binary F1 更新：PASS，但 **conclusion.tex 仍用 0.72 未更新到 0.723+CI**（已报 WARNING 给 Director）
- ordinal regression 段落扩展：PASS，数值全部与 registry 吻合
- cuda:2 并行 high-temp 拆分：PASS，总 ETA 从 11.3h→5.5h
- 之前标记的 3 个编译问题（dangling \ref, duplicate caveat, docs/ sync）均已修复

Registry 关注项（status 不准确，已报 Director）：
- `review-p1c-olmo-instruct`: ANALYZING（实际在 cuda:0 跑生成，ETA ~1h）
- `review-sampling-ablation`: PREPARING（实际在 cuda:2+3 并行，ETA ~5h）
- `plan-010-human-edit`: PREPARING（实际在 cuda:1 跑，ETA ~2h）
- `review-p1c-qwen06b-instruct`: PREPARING（已有完整 metrics+conclusion=negative，status 未更新）
- `review-p1c-instruct-logo`: PREPARING（同上，conclusion=success）

### 4. 📋 待办（条件触发式）
- OLMo instruct 完成 → 审查结果 + 独立验证长度混淆是否在第 3 个 instruct 模型上复现（预期：复现）
- plan-010 human edit 完成 → 重点审查：(a) edit 比例 5/10/20% 下 F1 衰减曲线是否单调，(b) LLM rephrase 是否比 random word replacement 更具破坏性，(c) 结果是否支持 "depth signal robust to light editing" claim
- sampling ablation 完成 → 审查：(a) low-temp vs default vs high-temp 的 F1 差异是否显著，(b) empty output 比例是否按 depth 不均匀分布，(c) 结论是否支持 "robust across decoding configs" claim
- conclusion.tex 0.72→0.723 修复 worker → 验证两份副本均已更新
- 任何新的论文章节提交审查 → 按 §5 写作对抗审查流程执行（维度评分 + 审稿人攻击面）

### 5. 🎯 战略上下文
- 核心决策链：D017 确认 gen-0 泄漏 → binary F1=0.723 替代 3-class 0.789 作为主指标 → instruct 模型方向反转被证明是长度伪影 → instruct 作为 limitation 而非 contribution
- DDL：EMNLP 2026 ARR 05-25，剩余 10 天
- Round 2 得分 Borderline 3/5，正在修 4 Critical + 6 Major + 9 Minor
- **易判断错的事**：
  1. instruct 实验的 `surface_reversal_survives_control: true` 标签具有误导性——partial ρ=0.10-0.17 方向虽"反转"但效应量骤降到无实际意义，且 binary F1≈0.5（随机水平）。不要被这个标签骗了
  2. Worker 声称 "All N files updated" 时不要信——必须独立 grep 验证每个文件（这次 conclusion.tex 就被漏掉了）
  3. Registry status 大面积不准（多个 PREPARING 实际已完成或在跑），不能依赖 status 字段判断实验进度，要 SSH 看进程


---
