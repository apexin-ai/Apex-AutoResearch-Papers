# director / loop_2.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`61270c3e05734cdf4bf3.json`](../../sessions/61/61270c3e05734cdf4bf3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T13:11:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 **1 台 AutoDL 实例**（autodl-5090），`gpu-5090-2x-2` 是同一台机器的别名（D018 已确认），只有 **cuda:0, cuda:1** 两张 RTX 5090
- outcome-bp-sensitivity 实验已被 INVALIDATED（D019，split seed 泄漏），其 holdout macro-F1=0.8593 不可引用，必须用修复后的结果
- cross-agent 分析数据 **禁止写入论文**，标签编码核查未完成（Reviewer critical：0/1 可能与 OpenHands pipeline 反转）
- Worker 池上限当前为 1（Agent 报告 spawn 第 2 个时"无可用账号"），只能串行派 Worker

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb2.seetacloud.com)，工作目录 `/root/autodl-tmp/agent_progress_probe`
- Python：aml-train 镜像，conda base 环境，`/root/miniconda3/bin/python`
- 数据：SWE-agent embeddings 在工作目录下，OpenHands 数据已下载
- 活跃进程：baseline-llm-judge (pid=27419, API-based 无 GPU)；encoder-ablation-e5-large (cuda:1)；encoder-ablation-bge-m3 (cuda:0)
- 审稿群：review_chat_id = `oc_7067491b561c6407a368c69422be7f2b`

### 3. 📊 当前状态
刚处理完 error-analysis v3 结果 + outcome-bp-sensitivity 数据泄漏发现。正在等 Agent 恢复后串行推进三个 P0 任务。

Registry RUNNING/PREPARING：
- encoder-ablation-e5-large (RUNNING, cuda:1, embedding 生成)
- encoder-ablation-bge-m3 (RUNNING, cuda:0, embedding 生成)
- baseline-llm-judge (RUNNING, API, macro-F1=0.6759 at 46%)
- openhands-fewshot-probe (PREPARING, 等 GPU)
- encoder-ablation (PREPARING, 等 embedding 完成)

等待中：
- Agent 刚 RESET，需要接收新 session 的首条指令
- outcome-bp-3seed Worker 结果（crash 前报告"即将完成"）
- 标签编码核查 Worker 未派出

### 4. 📋 待办
- Agent 新 session 启动 → 发综合指令：(1) 标签编码核查 (2) outcome-bp 修复代码 (3) LF temporal dynamics，串行优先级排列
- encoder ablation embedding 完成 → 提交 GTE-large embedding + 3 encoder probe 训练
- 标签编码核实通过 → 解冻 cross-agent 分析报告持久化；如果确认反转 → 重跑分析
- outcome-bp 修复代码完成 + GPU 空出 → 提交 holdout 重跑训练
- baseline-llm-judge 完成 → 分析 LLM vs probe 对比结果

### 5. 🎯 战略上下文
- 项目核心：用 weak supervision (LF→probe) 检测 agent 执行中的 progress/stagnation，目标 A 类会议
- 关键决策链：D017 批准 cross-agent 泛化实验 → 发现 command_repetition 是迁移失败首因（非 embedding 域偏移）→ Claim 3 精化为"LFs 有选择性地迁移"
- 成功实验：probe-001 (F1=0.9055, +6.24pp vs Repeat-3), probe-multiseed 确认稳定, error-analysis 完成
- 负向实验：cross-agent-eval (F1=0.53 直接迁移失败), baseline_flyingsquid (negative)
- 易踩坑：(1) 不要假设有 4 GPU，只有 2 张 (2) cross-agent 数据标签可能是反的，必须先核查 (3) outcome-bp 旧结论不可引用 (4) Worker 池限 1，不要尝试并行派多个
- 11 天 DDL，剩余 GPU 工作量约 20h，2 卡够用但需高效排队


---
