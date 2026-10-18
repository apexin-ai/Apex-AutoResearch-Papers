# reviewer / loop_2.md

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`75b0fc2393a2caf65e03.json`](../../sessions/75/75b0fc2393a2caf65e03.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-22T01:27:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0（westb-48145 单卡，`execution.gpu_ids=[0]`）
- 论文 α 值必须用 `alpha_pure`（3 架构 × 固定 ratio），**绝不能用** `alpha_all_15`（15 模型全局 α）——artifact 的 summary 字段用的是后者，会夸大 2 倍
- 340M eval 数据在 `/root/entrainment_gated_ft/lm_eval_clean/340m_multi/`，1.3B 在 `/root/entrainment_gated_ft/lm_eval_clean/`，两边目录命名不同（340M 用 `GDN-pure`，1.3B 用 `1.3B-100B-GatedDeltaNet-pure`）
- EMNLP 2026 ARR May deadline: **2026-05-25**，主文 ≤ 8 页

### 2. 🖥️ 基础设施快照
- 服务器：westb-48145(root)，工作目录 `/root/entrainment_gated_ft`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型 zoo：`/root/entrainment_gated_ft/models/`（Wang 2025 预训练，3 arch × 5 ratio × 2 scale）
- Eval 输出：`/root/entrainment_gated_ft/lm_eval_clean/`（1.3B）+ `340m_multi/`（340M）
- 分析脚本：`/root/entrainment_gated_ft/scripts/analyze_340m_multi.py`
- 论文本地：`projects/entrainment_gated_ft/docs/paper/`
- 活跃进程：**无**（GPU 空闲，无 RUNNING 实验）
- 无 wandb 配置，无 cron

### 3. 📊 当前状态
**全部实验完成，论文整合完毕，等用户批准 Round 6 审稿卡片后提交。**

我刚完成的工作：
1. 独立核实 340M multi-benchmark 分析（exp-340m-multi-bench）——从远程 JSON 文件逐格验证 Table 数据，全部 PASS
2. 验证 §4.3 Scenario B 整合文本（alpha_pure 口径正确，Δ=2-8pp）+ Appendix §F 新增表格
3. ROADMAP 更新审查——PASS，仅标记 info 级术语不一致（§4.3 "scale-robust" vs Appendix "scale-invariant"）

Registry: 21 个实验全部 DONE。无 RUNNING/PREPARING。无等待中的 Worker/Cron/Director 决策。

### 4. 📋 待办
- 用户批准 Round 6 → 无需 Reviewer 动作（提交流程由 Director 处理）
- Director 要求再做一轮 paper 审查 → 按 §5 审查模式 B 走，注意已 read paper-quality-lessons skill
- Director 转发 terminology fix patch → 验证 Appendix L571 "scale-invariant" 是否改为 "scale-robust"
- 任何新实验启动 → 核查 cuda:0 白名单 + alpha_pure 口径

### 5. 🎯 战略上下文
**核心结论**：Per-example multiplicity（α=0.14-0.30）是 hybrid recurrent architecture 的 structural 属性，低 Jaccard（≤0.10）跨尺度/跨任务稳定。Aggregate convergence 仅限 LAMBADA，与 multiplicity 解耦。

**决策链关键节点**：
- D014: 标题缩窄到 per-example multiplicity（不再 claim convergence/entrainment）
- D020: PIQA 入主文第 4 benchmark，WinoGrande/BoolQ 入 appendix
- D023: 340M Scenario B — "scale-robust" framing（不是 "scale-invariant"）

**易错点**：
1. artifact `340m_multi_bench_analysis.json` 的 `summary` 和 `interpretation` 用 alpha_all_15，**不是论文口径**——论文用 alpha_pure，直接引用 artifact summary 数字会写错
2. HellaSwag 用 acc_norm（不是 acc），其他 benchmark 用 acc——搞混会导致 α 计算错误
3. 论文预期 Overall 3.0-3.5，主要弱点是 single model zoo（Wang 2025）+ no seed control——这是 known limitation，不是 bug
4. Bonferroni-adjusted p=.100 for LAMBADA convergence 不过 α=0.05——论文用 CI excludes zero 作为 complementary evidence，审稿人可能攻击这一点


---
