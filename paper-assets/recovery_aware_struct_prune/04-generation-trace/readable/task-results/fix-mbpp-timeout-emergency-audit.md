# fix mbpp timeout emergency audit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mbpp_timeout_emergency_audit_20260519T203035_result.json`
- **Structured JSON:** [`9930b0d896bfe17e61ff.json`](../../sessions/99/9930b0d896bfe17e61ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 已占用 12497 MiB，数据集正在加载。eval_mbpp_sft_standard_20 成功启动。

---

## E. 汇总表格

### westd-29022

| GPU | 实验 | timeout wrapper | timeout 值 | 操作 | Python PID 状态 |
|-----|------|----------------|-----------|------|----------------|
| cuda:0 | **eval_mbpp_sft_standard_20** (新) | ❌ 无 | — | 已重新提交，无 timeout | 模型已加载 12.5GB，数据集加载中 ✅ |
| cuda:0 | eval_mbpp_grpo_standard_20 (旧) | ❌ 无 | — | 已杀掉（与 cuda:2 的 v2 重复，同一输出路径） | Dead |
| cuda:1 | eval_mbpp_grpo_rasp_20 | ❌ 无 | — | 安全，无需操作 | PID 127964, 222/374 运行中 ✅ |
| cuda:2 | eval_mbpp_grpo_standard_20_v2 | ✅ 有 | 21600s (6h) | ⚠️ **附带伤亡**：kill timeout 时 SIGTERM 被转发给子进程，python 也死了 | Dead (仅 5/374，损失极小) |
| cuda:3 | eval_mbpp_sft_rasp_20 | ✅ 有 | 86400s (24h) | 安全（>8h），未动 | PID 133679, 213/374 运行中 ✅ |

### westb-23072

| GPU | 实验 | timeout wrapper | timeout 值 | 操作 | Python PID 状态 |
|-----|------|----------------|-----------|------|----------------|
| cuda:0 | eval_mbpp_sft_standard_20_1p5b | ❌ 无 | — | 安全 | PID 917409 运行中 ✅ |
| cuda:1 | eval_mbpp_sft_cka_only_20_1p5b | ❌ 无 | — | 安全 | PID 916225 运行中 ✅ |

### 关键发现

1. **eval_mbpp_sft_standard_20** — 已在 westd cuda:0 重新提交，**无 timeout wrapper**，registry 已更新为 RUNNING
2. **eval_mbpp_grpo_standard_20_v2** (cuda:2) — 附带伤亡。GNU `timeout` 收到 SIGTERM 时会转发给子进程组，无法单独杀 wrapper 保留 python。仅 5/374，损失极小。**cuda:2 现已空闲，需要重新提交此实验**
3. **eval_mbpp_sft_rasp_20** (cuda:3) — 24h timeout 充足，未触碰
4. **westb 两个实验均无 timeout wrapper**，全部安全

### 教训

`kill &lt;timeout_PID>` 无法安全解除 timeout wrapper——`timeout` 会将收到的信号转发给子进程组。正确做法是：要么一开始就不用 timeout，要么接受它直到自然过期。

---
