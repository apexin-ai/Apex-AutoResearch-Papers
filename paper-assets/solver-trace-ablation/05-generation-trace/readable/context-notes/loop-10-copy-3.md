# reviewer / loop_10.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`7aa142e3049c0b0adbcc.json`](../../sessions/7a/7aa142e3049c0b0adbcc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T19:01:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 / cuda:1（westd-39279）。无其他 GPU 可用。
- C002：训练命令必须 `export CUDA_VISIBLE_DEVICES=N`，禁止 inline 赋值。**s43-r3 已违反此条（无 CUDA_VISIBLE_DEVICES），已报 Director warning，但未造成实际损害。s44-r2 正确。**
- C008：所有 eval 必须 `--data_path data/proofwriter_fol_100.jsonl`，禁止 test_100.jsonl 或默认值。
- C013：genuine = proved − H7 − H1_exact − H8。H1-near 保留为 genuine 但标记。两侧对称。
- **D093 生效**："Random β=0.1 H7=0%" claim 已作废。不可再引用 C136/C192 原始措辞。新叙事方向："ISR amplifies H7"（待 s44-r2 确定 pooled rate）。

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，代码根 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型输出：`/root/autodl-tmp/outputs/`
- Eval 备份：`/root/autodl-tmp/eval_results_backup/`
- classify_h7.py：`/root/solver-trace-ablation/scripts/classify_h7.py`（2026-05-15 23:10 修改，当前权威版本）
- 活跃进程：plan018-additive-random-b01-s44-r2（PID 533415/533420，tmux session，cuda:1，~step 180/500 when last checked）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/`

### 3. 📊 当前状态
**刚完成**：plan018-additive-random-b01-s43-r3 完整审查 → 发现 CRITICAL：H7=36/94=38.3%（Random β=0.1 竟有大量 H7a）。已报 Director，D092/D093 已录入。β=0.3 Random 3-seed 也完成重分类（同版本 classify_h7.py）。

**Registry 关键状态**：
- plan018-additive-random-b01-s44-r2：**RUNNING**，cuda:1，seed=44，β=0.1 Random。~step 180/500，预计 ~40-50min 完成。**这是当前最关键实验——决定 Random pooled H7 rate。**
- 其余 85 个实验全 DONE。

**等待中**：
- s44-r2 on_complete cron → 触发 eval + taxonomy → 我需要审查
- s44-r2 完成后 Agent 将执行 stats_recalc_checklist.md 中的 5 项统计量重算

### 4. 📋 待办
- **s44-r2 训练完成** → 审查 eval 结果 + taxonomy（核心：H7 count 决定 Random pooled H7 rate）
  - 如果 s44 H7≈0（像 s42）→ Random pooled H7 ≈ 36/273 ≈ 13%，cross-seed variance 叙事
  - 如果 s44 H7 也高（像 s43）→ Random pooled H7 更高，H7 不再有任何 ISR 关联性
- **s44-r2 eval 完成** → 验证 Agent 的统计量重算（Fisher exact, Wilson CI, pooled genuine rate）是否与 stats_recalc_checklist.md 方案一致
- **paper_framing.md 更新后** → 审查新叙事是否诚实反映 D093 发现，检查 rationalization 风险（Agent 可能包装 H7 发现为"更 nuanced 结论"而淡化对原 claim 的冲击）
- **s44-r2 spec provenance** → 检查是否补全 data_count/model_name/seed 字段（当前 RUNNING 状态缺失）

### 5. 🎯 战略上下文
**核心发现链**：D087→D088→D089→D091（exec-only 1000步 0% genuine）+ D093（Random β=0.1 s43 H7=38.3%，"Random H7=0" 作废）

**最容易判断错的事**：
1. **不要假设 s42 的 pattern 代表 Random 条件的通用行为**。s42 H7=0/genuine=18 是异常值还是 s43 H7=36 是异常值，目前无法判断，必须等 s44。
2. **β=0.3 vs β=0.1 的 H7 比较需注意**：β=0.3 Random 重分类后 s42 H7=4（从 0 上调），s43-r4 H7=7，s44 H7=0。这些是同一 classify_h7.py 版本。β=0.1 s42 H7=0 但 s43 H7=36——β=0.1 的 cross-seed 方差反而比 β=0.3 更大。
3. **Agent 可能低估 H7 发现的冲击**：analysis.json 的 conclusion_reason 只提到 genuine_rate 低，未提 H7=36 对 paper claim 的影响。确保 Director 和 Agent 已充分理解 D093。
4. **taxonomy 版本一致性已确认**：s42 和 s43-r3 均用 2026-05-15 版 classify_h7.py，比较有效。但 s44-r2 eval 后也必须用同版本。


---
