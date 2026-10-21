# ssh check gated isr progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gated-isr-progress_20260516T151152_result.json`
- **Structured JSON:** [`b8b08ef64ae63de550a5.json`](../../sessions/b8/b8b08ef64ae63de550a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：gated-isr-curriculum 训练状态

### 所有 4 个实验均已崩溃

| 实验 | 崩溃步数 | 原因 |
|------|---------|------|
| curriculum-t02-s42 | Step 50/500 | `No space left on device` |
| curriculum-t02-s43 | Step 50/500 | `No space left on device` |
| t03-s42 | Step 90/500 | 日志停更于 22:29，无 traceback（可能被 kill 或静默崩溃） |
| t03-s43 | Step 100/500 | `No space left on device` |

### 磁盘现状
`/root/autodl-tmp`: 129G/250G (52%)，当前有 122G 空闲——说明崩溃后已有清理。

### GPU 现状
两张 GPU 均 ~82G/97G，95-96% 利用率——**有其他实验在跑**，不是这 4 个 gated-isr 实验。

### 输出目录
- `gated_isr_curriculum_t02_s42/` — checkpoint-50, reward_log.jsonl (11KB)
- `gated_isr_curriculum_t02_s43/` — checkpoint-50, reward_log.jsonl (11KB)
- `isr_gated_curriculum/` — checkpoint-150, reward_log.jsonl (75KB)（对应某个更早的 run，非上述 4 个日志）

### Gated ISR 实验设计

**`grpo_isr_gated_curriculum.yaml`（curriculum 版本）：**
- `reward_mode: isr_gated` — ISR 奖励需通过"门控"：证明必须执行成功
- `isr_threshold: 0.2` — ISR 需超过 0.2 才有奖励
- `warmup_steps: 100` — 前 100 步处于 warmup（日志标记 `[WARMUP]`），不施加 ISR 门控
- `data_path: data/proofwriter_fol_100.jsonl` — **违反 C001**（应使用 train_500_seed42.jsonl）
- model: Qwen3-4B, 500 steps, lr=1e-6, 8 generations

**`grpo_isr_gated.yaml`（非 curriculum 版本）：**
- `isr_threshold: 0.3`（更高门槛）
- `data_path: data/train_500_seed42.jsonl`（合规）
- 无 warmup_steps

### prove_rate 趋势（t03-s42 可见范围）
- Step 1-50: 稀疏的非零 prove_rate（0.375-1.0 偶现），大量 step reward=0
- Step 50-90: 偶尔出现 prove_rate 0.625-0.875 + gate_pass=1.000 的步，但多数步仍是 reward=0
- 整体模式：模型偶尔产出可执行的证明并通过 gate，但非常不稳定

### 关键问题
1. **反复磁盘满崩溃**（C003 约束场景再现）——4 个实验中 3 个明确因 disk full 死亡
2. **curriculum config 违反 C001**——使用了 proofwriter_fol_100.jsonl 而非 train_500_seed42.jsonl
3. t03-s42 需要调查日志停更原因（可能是 GPU 被其他实验抢占或 OOM）

---
