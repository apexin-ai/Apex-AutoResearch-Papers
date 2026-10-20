# ops urgent gpu audit

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-audit_20260516T000349_result.json`
- **Structured JSON:** [`3fca875c8721904d412e.json`](../../sessions/3f/3fca875c8721904d412e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

| exp_id | GPU | tmux | 进程 PID | checkpoint-1635 | 状态 | 进度 | loss | ETA |
|--------|-----|------|----------|-----------------|------|------|------|-----|
| v4_taxei_fixed_inject50_s1 | cuda:0 (28.5G/32G, 78%) | v4-taxei-fixed-inject50-s1 ✅ | 211989 ✅ | ❌ 无 | **训练中** | 170/1635 (10.4%) | 0.642 | ~57min |
| v4_random_fixed_inject50_s1 | cuda:1 (28.5G/32G, 99%) | v4-random-fixed-inject50-s1 ✅ | 212414 ✅ | ❌ 无 | **训练中 (第2次)** | 160/1635 (9.8%) | 0.702 | ~59min |
| v4_taxei_fixed_inject50_s7 | cuda:2 (28.2G/32G, 98%) | v4-taxei-fixed-inject50-s7 ✅ | 212543 ✅ | ❌ 无 | **训练中** | 170/1635 (10.4%) | 0.639 | ~58min |
| v4_random_fixed_inject50_s7 | cuda:3 (28.2G/32G, 99%) | v4-random-fixed-inject50-s7 ✅ | 212673 ✅ | ❌ 无 | **训练中** | 170/1635 (10.4%) | 0.642 | ~58min |

### 关键发现

1. **4 块 GPU 全部活跃**，所有 4 个训练进程正常运行，约 07:57 启动，已跑约 7 分钟。

2. **没有任何 checkpoint-1635**——4 个实验都处于 epoch 1 的早期阶段（~10%），远未完成。

3. **v4_random_fixed_inject50_s1 有一个夭折的 v0 运行**（v0-20260516-065808），仅跑了 5 步就停了（loss=3.356），当前是 v1 重跑。其余 3 个都是首次运行。

4. **tmux 会话名不含 "-r2" 后缀**——实际会话名为 `v4-taxei-fixed-inject50-s1` 等，不是用户提及的 `v4-taxei-fixed-inject50-s1-r2`。

5. **无其他异常进程**——所有 python 进程均为这 4 个 swift sft 训练及其子进程。

6. **预计完成时间**：~09:05（约 1 小时后），save_strategy=epoch，checkpoint 将在 step 545/1090/1635 时保存。

### 如果 report 显示已完成——那是错的

Report 与 GPU 状态矛盾的原因：这 4 个实验刚启动不到 10 分钟，进度仅 10%，不可能有完成状态。

---
