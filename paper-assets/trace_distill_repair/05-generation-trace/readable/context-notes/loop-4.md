# agent / loop_4.md

**trace distill repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`3faa938936978f6cd446.json`](../../sessions/3f/3faa938936978f6cd446.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-15T12:45:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：只能用 rtx6000-diagprobe 上的 cuda:0 和 cuda:1（config gpu_ids）
- **API key 加载**：submit_training_job 命令必须 `source /root/trace_distill_repair/.env`，不能用 `source /root/.bashrc`（有 non-interactive guard 会 return）
- **mvp_phase3_repair（v1）已 INVALIDATED**（D021）：三重 confound 使全部 132 个评估无效，不可引用其 metrics 做任何结论
- **get_buggy_code() 已确认 33/33 全错**：之前估计 ~14 个是低估，实际 100% fallback 到字母序第一个 .py 文件。修复方案是从 bug_patch.txt 的 diff header 提取
- **DDL: EMNLP 2026 ARR May = 5/25**，剩 10 天

### 2. 🖥️ 基础设施快照
- **服务器**：rtx6000-diagprobe，账号 root
- **工作目录**：/root/trace_distill_repair
- **Python**：/root/miniconda3/bin/python（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **API keys**：持久化在 /root/trace_distill_repair/.env（OPENROUTER_API_KEY / DEEPSEEK_API_KEY）
- **数据**：/root/trace_distill_repair/pipeline_output/（Phase 1 v2 traces 33 实例 + Phase 2 v3 scoring 结果 + Phase 3 v1 repair outputs）
- **Phase 3 v1 结果**：/root/trace_distill_repair/pipeline_output/phase3_results/
- **活跃 Worker**：`worker_validate_intermediate_v2_20260515T123833`（running，turn 16，正在做 D022 要求的中间验证——修复后 pipeline 在 2-3 个已知实例上验证 buggy_code 提取 + prompt 格式 + 输出非截断）
- **活跃 cron**：无（reconcile 返回 0）
- **活跃 tmux**：无实验在跑（GPU 空闲）

### 3. 📊 当前状态
**刚完成**：
- D021/D022 决策落地——Reviewer 核实三重 confound 后，mvp_phase3_repair 标记 invalidated
- Worker `fix_three_confounds` 已完成 pipeline 修复（diff-based repair prompt + buggy_code 从 bug_patch.txt 提取 + max_tokens=8192）
- Worker `tier_classification_v2` 已完成 Tier 分类：Tier 1 = 14 实例（含 httpie_2，D022 纳入），Tier 2 = 17 实例（keep=0），Exclude = 2（fastapi_1 多文件）

**正在做**：
- `worker_validate_intermediate_v2` 运行中（中间验证步骤，D022 要求）——在 httpie_2 + 2-3 个已知实例上验证修复后 pipeline 的 buggy_code/prompt/输出

**Registry 待处理**：
- `mvp_phase3_repair_v2`：PREPARING 状态，等中间验证通过后重跑 Tier 1 clean subset（14 实例 × 4 条件 + test execution）
- `mvp_structural_scoring_v2`：PREPARING 但已 CANCELLED by D013（历史残留，不用管）

**等待中**：
- 中间验证 Worker 回调 → 验证通过则提交 mvp_phase3_repair_v2
- 无 Director 决策 pending（D022 已是最新指令）

### 4. 📋 待办（条件触发式）
- **intermediate_v2 Worker 回调 success** → 立即提交 mvp_phase3_repair_v2（Tier 1 14 实例 × 4 条件，diff output + test execution eval），用 `submit_training_job` 在 rtx6000-diagprobe cuda:0 上跑
- **intermediate_v2 Worker 回调 fail** → 分析失败原因，继续修 pipeline，再验证
- **mvp_phase3_repair_v2 完成 + conclusion=success**（structural > no_trace on test pass rate）→ 按 on-experiment-done 流程汇报 Director，推进 Research 阶段（student distillation、扩大到 SWE-bench）
- **mvp_phase3_repair_v2 完成 + conclusion=negative** → 按 D018/D019 启动强模型消歧（Claude Sonnet 4 / GPT-4o 重跑 4 条件 × Tier 1 实例）；kill criteria: (1) 强模型 no_trace judge ≥3.0 (2) structural > no_trace (3) ≥1 条件 test pass >0%；三条全满足=PASS 否则 MVP FAIL
- **clean subset < 8 实例**（中间验证发现更多问题缩小 Tier 1）→ 评估是否需修 structural segment cap (MAX_SEGMENTS=20→40-50) 扩大 Tier 1

### 5. 🎯 战略上下文
**项目核心问题**：execution trace 经结构化过滤后能否提升 LLM 程序修复质量？

**决策链关键节点**：
- D013/D014: Phase 1 trace 未覆盖 failing test（根本 bug），全部重跑后 v2 成功
- D021: Phase 3 v1 三重 confound invalidated（buggy_code 100% 错 + prompt 退化 + 输出截断）
- D022: 修 pipeline → 中间验证 → 重跑 clean subset → test-based eval
- D018/D019: 如果 clean run 仍 negative，启动强模型消歧（有操作化的 kill criteria，不允许无限消歧）

**最容易判断错的事**：
1. **不要引用 mvp_phase3_repair 的任何 metrics**——那些数据全部无效，包括 judge 分数和 h2h 比较
2. **Tier 1 是 14 实例不是 15**——D022 将 httpie_2 纳入但 fastapi_1（5 文件）排除
3. **55% 实例 structural_keep=0**——这些在 Phase 3 中 structural_filtered ≡ no_trace，只有 Tier 1 的 14 个实例能区分条件
4. **test execution 依赖每个 BugsInPy 项目的独立环境**——conda base 不够，需要项目级 venv + 依赖安装；测试函数可能不在 buggy 版本中需要 git diff 注入
5. **Option C (token efficiency pivot) 已被 D018 否决**——不要再提


---
