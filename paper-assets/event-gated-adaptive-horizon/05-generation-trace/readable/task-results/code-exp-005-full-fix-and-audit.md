# code exp 005 full fix and audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_005_full_fix_and_audit_20260513T155111_result.json`
- **Structured JSON:** [`e5080b87960a594d4480.json`](../../sessions/e5/e5080b87960a594d4480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结如下：

---

## 产出

### 1. 代码当前状态评估
前一个 Worker 已完成大部分框架代码（EventGate、variable-dt subsampling、lambda_return_variable_dt），但留下了核心 bug：`compute_gate_targets` 调用使用 `gate_max_dt`（固定=8）而非 `effective_max_dt`（curriculum 动态值），且 gate_scale/effective_max_dt 计算在 3 处重复。

### 2. 架构改进（8 个 edit）
- **单一来源**：`WorldModel._update_gate_schedule()` 集中计算 `_gate_scale` 和 `_effective_max_dt`
- **关键修复**：`compute_gate_targets` 新增 `effective_max_dt` 参数，masked bins 的概率质量=0
- **消除重复**：3 处独立计算 → 1 处计算 + 属性访问

### 3. 完整审计表格
18 处 `gate_max_dt`/`effective_max_dt` 使用已逐一审查，8 处需修改均已完成。`EventGate.entropy()` 在 masked logits 上数值安全（IEEE 754 下 `0*(-1e9)=0`），无需修改。

### 4. 验证结果
- **Import**: OK
- **Unit tests**: gate_loss ∈ [0, 2.08]（修复前 3e8），entropy 无 NaN，target masking 正确
- **dry-run**: 进程启动成功（model init OK, 16.9M params），评估阶段通过

### 5. exp_005 提交确认
- **PID**: 51721
- **tmux session**: `exp_005_event_gated_v4`
- **GPU**: cuda:1
- **logdir**: `logdir/event_gated_v5_s1`
- **log**: `~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log`

---
