# reviewer / loop_14.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`50a12e304d3837d1c2db.json`](../../sessions/50/50a12e304d3837d1c2db.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-04-29T22:58:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-4x6000-a 本项目只分配 **cuda:1**，GPU 0/2/3 是其他项目（已验证：GPU2 跑 swin_tiny CIFAR-10，GPU3 跑 vit_small CIFAR-10）
- bjb2-4x5090-b 已释放 (D241)，**不再属于本项目**，不要在上面跑任何东西
- `online_stratqa_qwen` (registry line 1421) 是旧实验，spec 不完整（无 seed/server/gpu，log 在 /tmp 已丢失），**不可作为论文数据源**——已被 5-seed 替代 (D242)
- 论文中 `\placeholder{...}` 是红色占位符，提交前必须全部填充；forest plot `gen_fig_forest.py` 有 CI_LO=-99/CI_HI=+99 dummy 值，**运行前必须替换**

### 2. 🖥️ 基础设施快照
- 服务器：westb-4x6000-a，项目目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- vLLM 进程：PID 134958 (Qwen2.5-7B on cuda:1, 89GB)——实验已完成，应可终止释放显存
- 输出目录：`/root/autodl-tmp/comm_gate_mas/outputs/qwen_heuristic_stratqa_4seed/`（4 个 seed JSON 文件完整）
- 论文源码：本地 `artifacts/paper/`（main.tex + sections/）
- bjb2 cuda:0,1 确认 0MB/0%，已释放给 Manager

### 3. 📊 当前状态
**刚完成**：Qwen StratQA 4-seed 实验全部完成（06:35 UTC），结果独立核实通过。Paper prewrite 已审查（placeholder 结构就绪）。

**Registry**：
- `qwen_heuristic_stratqa_4seed` — 仍标 RUNNING 但实际已完成（EXIT_CODE=0），需更新为 DONE，写入 metrics：4-seed mean +1.00±0.71pp, suppress 56.5%
- 6 个 stale PREPARING（vllm_llama_8192/v2, p1_oracle ×2, oracle_qwen_gsm8k, 5run_pruned_rerun）— 全部应标 CANCELLED/FAILED

**等待中**：
- Round 2 二审报告 R2, R3 未到达
- Agent 需填充论文 placeholder（5-seed 聚合数字）并提交 commit

### 4. 📋 待办
- Registry 更新 `qwen_heuristic_stratqa_4seed` → DONE → Agent 计算 5-seed 聚合（含 seed 42 的 -0.5pp）→ 填充论文 placeholder → **审查填充后的数字是否与日志一致**
- R2/R3 审稿报告到达 → 按 review-report-action 流程审查修改方案
- 论文 placeholder 全部填充后 → 审查最终数字：5-seed Δ≈+0.70±0.91pp, CI≈[-0.43,+1.83]，确认与 registry/log 交叉一致
- Agent 若提交 "sampling noise" 措辞 → 建议改为 "superseded by 5-seed replication"（我已 warning 过，追踪是否采纳）
- westb cuda:1 vLLM 终止后 → 确认显存释放

### 5. 🎯 战略上下文
- **核心结论**：Dissociation finding——ack 消息扰动敏感性最高但可安全剪枝。双 backbone (Qwen/Llama) × 双任务 (GSM8K/StratQA) 均 non-inferior
- **D242 是本轮最大溯源事件**：论文旧 Qwen StratQA -2.4pp 来自 `online_stratqa_qwen`（4/22, 单 seed, spec 不完整），被 5-seed 彻底推翻（+0.70pp）。C22 provenance 需更新 exp_id 和 verified 状态
- **易错点**：
  1. 旧 Llama StratQA 单 seed 行 (N=250, +2.8pp) 仍在 Table 2 中与 8-seed 并存——Qwen 已升级 5-seed，Llama 一致性问题需关注
  2. Appendix 有 Version A/B 两套叙事（注释块），提交前必须删除未选版本
  3. DDL 极紧：Abstract 5/3 (3天), Paper 5/5-6 (5-6天)，R2/R3 未到是主要风险


---
