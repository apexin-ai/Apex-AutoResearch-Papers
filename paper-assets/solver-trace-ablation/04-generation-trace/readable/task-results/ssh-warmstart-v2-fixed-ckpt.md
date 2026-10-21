# ssh warmstart v2 fixed ckpt

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_warmstart-v2-fixed-ckpt_20260516T153415_result.json`
- **Structured JSON:** [`dab75c64338917370b18.json`](../../sessions/da/dab75c64338917370b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：500 步 exec-only checkpoint 不存在

**磁盘搜索结果：**

| 路径 | 状态 | 原因不可用 |
|------|------|-----------|
| `plan001_exec_only_s42` | 不存在 | 已清理 |
| `plan001_exec_only_s43_1000_r2` | 有模型文件 | 是 1000 步最终模型，无中间 checkpoint |
| `plan001_exec_only_s44_1000_r2` | 有模型文件 | 同��� |
| `sweep-exec-only-s45-r2` | 目录已删 | 磁盘清理时移除（registry 有记录但文件不在） |
| `w2_1.7b_exec_only_s42/checkpoint-500` | 存在 | 架构不兼容（Qwen3-1.7B vs 项目用 Qwen3-4B） |

**结论：没有任何 Qwen3-4B 的 500 步 exec-only checkpoint 存活在磁盘上。**

---

**可行替代方案：从 base model 重训 500 步 exec-only**

- Base model: `/root/autodl-tmp/models/Qwen3-4B`
- 参考: `sweep-exec-only-s45-r2` 历史记录显示 500 步训练耗时 ~55 min
- 两张 GPU 完全空闲（RTX PRO 6000 Blackwell, 98GB × 2）

**风险提示：** `sweep-exec-only-s45-r2` 的 500 步数据显示 entropy_final=0.045 且 H7a=93.9%。即使只训 500 步，模型可能已经高度 peaked。1000 步 collapse 更严重，但 500 步的 diversity 是否足以支撑 K=8 下产生 reward variance 需要验证。

---

**按任务要求，不提交训练任务。** 等待 Director 指示：
1. 是否从 base model 重训 500 步 exec-only（~55min）然后继续本方案
2. 是否尝试更早步数（如 200-300 步）以确保更多 diversity
3. 是否改用 `isr_gated_curriculum/checkpoint-150`（已在 gated-ISR 训练中存活 190+ 步，prove_rate=0.5-0.75，未 collapse）

---
