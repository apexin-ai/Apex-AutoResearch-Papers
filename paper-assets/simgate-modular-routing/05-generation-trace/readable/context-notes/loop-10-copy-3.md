# reviewer / loop_10.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`5b44df4973ed2f69d899.json`](../../sessions/5b/5b44df4973ed2f69d899.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T22:11:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（RTX 5090 32GB × 2），不可越界
- 服务器：westb-13313，account=root
- 1.7B router eval 存在 **Trainer eval vs generation-based eval 差异**：paper 中 "57.6%" 是 Trainer eval (logit-based)，generation-based nothinking 仅 41.7%。两种 pipeline 不可混用比较
- ssh_read_only 不支持 shell metacharacter（`|`, `&&`, `$()` 等），多 pattern grep 用 `-e` flag

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313(root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型缓存：`/root/autodl-tmp/models/Qwen/Qwen3-{0.6B,1.7B,4B}`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/`
- 论文 tex 文件：本地 `docs/paper/*.tex`（Paper Agent 改本地），服务器同路径（可能滞后）
- W&B：offline mode（不可检查 W&B 在线指标）
- 活跃进程：无（GPU0/GPU1 均空闲，等 Round 8 决策）
- Cron：无活跃任务

### 3. 📊 当前状态
**全部实验完成，论文终稿阶段，blocking on 用户审批 Round 8 continue review。**

我刚完成的审查：
1. **plan-008-router-size-v4**：审了 3 轮。初始发现 eval pipeline confound（CRITICAL），推动 Worker 补做 0.6B/4B nothinking eval → 再推动 1.7B nothinking eval → 最终获得真正统一的三方比较。结果：0.6B(59.1%) ≈ 4B(58.5%) >> 1.7B(41.7%)
2. **penalty-robustness**：P=50/100/200 子集 robustness 分析，数据与 plan-012 一致，PASS
3. **seed-robustness-extended**：8-seed 统计核实通过 (54.1±5.8%)
4. **plan-012-penalty-curve**：DAF 范围修正 (50%→98%)，CI 修正（script-generated 替代手动值）

Registry：77 experiments，全部 DONE。无 RUNNING/PREPARING。

**待 Director 决策**：
- 论文 experiments.tex:105 router-size ablation 段落需更新数字（当前仍用旧 Trainer eval 53.1% for 1.7B）。我已提 3 个方案给 Director（分层报告 / 全 Trainer / 仅 0.6B vs 4B）
- Round 8 continue review 需用户审批

### 4. 📋 待办
- 用户审批 Round 8 → 读最新全文做系统审查（abstract/intro/experiments/discussion/conclusion 一致性）
- Paper Agent 更新 router-size ablation 数字后 → 核实是否用了统一 pipeline 数据（registry `unified_generation_based_nothinking`），检查 "57.6%" 与 ablation 1.7B 数字的关系是否在文中解释
- 论文 local→server sync 后 → 双边核对最新版本一致性
- 任何新 worker_done 通知 → 按 audit checklist 审查
- 收到章节审查请求 → 先查 red-section skill 合规，再按 §5 对抗审查

### 5. 🎯 战略上下文
**核心结论**：ScienceWorld routing signal 主要来自 death avoidance (DAF≈90%)，router 仅是 safety critic 而非 efficiency optimizer。

**决策链关键节点**：
- D069: 统一 eval pipeline（enable_thinking=False 三方 generation eval）
- D068: plan-008-v4 router-size ablation 成功
- D066: 8-seed 更新 (54.1±5.8%)
- D062: 标题去 "90%" 数字 + Discussion pilot 数据替换

**最易判断错的事**：
1. **1.7B "57.6%" vs "41.7%"**：这两个数字是同一模型不同 eval 方法的结果，不是矛盾。Trainer eval (logit-based) = 57.6%，generation-based nothinking = 41.7%。Paper 主体用 Trainer eval，ablation 可能需要用 generation eval。关键是不能在同一段落里混用且声称 "unified pipeline"
2. **论文文件双边**：paper tex 的真源在**本地** workspace（Paper Agent 改本地），服务器可能是旧版。断言 "worker 未更新论文" 前必须两边都读
3. **seed-robustness 的 eval_loss 字段**：有 eval_loss 的 JSON = Trainer eval 产物，有 generated/clean/pred 的 JSON = generation eval 产物。这是区分两种 pipeline 的关键标志
4. **DDL 2026-05-25**：剩 10 天，不要用人类工时直觉判断来不来得及——AI 团队 + 充足 GPU 可以并行迭代，只看 GPU-hours 是否够


---
