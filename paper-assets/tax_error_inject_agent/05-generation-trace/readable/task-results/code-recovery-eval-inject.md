# code recovery eval inject

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery-eval-inject_20260514T181829_result.json`
- **Structured JSON:** [`c684eab2dbc1a623e510.json`](../../sessions/c6/c684eab2dbc1a623e510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 张 GPU 都在训练中（18-19GB 已用，80-95% 利用率）。跳过 dry-run。

修改已完成。总结变更：

### 新增功能

**`--inject_mode {action,context}`** (默认 `action`)
- **`action` 模式（新）**：在 agent 执行第 N 步时，将其选择的动作替换为一个错误动作（same-verb-different-target 优先），实际执行到环境中，然后让 agent 自由继续。测量 agent 是否能识别错误并恢复任务。
- **`context` 模式（原有）**：在第 N 步篡改 agent 看到的历史上下文（步骤交换/删除/截断/遮蔽），保持原有行为不变。

**`--inject_step &lt;int|auto>`** (默认 `auto`)
- `auto`：随机选择 2-6 步之间注入
- 指定整数：固定在该步注入

### 新增输出指标（action 模式）

每个 episode 记录：
- `injection_step`: 实际注入步
- `injected_action` / `intended_action`: 错误动作 vs agent 原始选择
- `recovery_detected`: agent 的 thinking 中是否出现错误感知关键词
- `recovery_steps`: 注入后到 episode 结束的步数
- `final_success`: 最终任务是否完成

汇总报告 `action_injection`：
- `recovery_rate`: 注入后仍完成任务的比例
- `detection_rate`: agent 显式感知到错误的比例  
- `avg_recovery_steps`: 平均恢复步数

### 向后兼容

`--inject --inject_mode context` 完全保留原有 context-corruption 行为。`--no_inject` 不受影响。

GPU 全忙，dry-run 待 GPU 空闲后执行。备份在 `recovery.py.bak`。

---
