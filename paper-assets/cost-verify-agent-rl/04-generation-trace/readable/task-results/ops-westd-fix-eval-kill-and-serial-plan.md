# ops westd fix eval kill and serial plan

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_fix_eval_kill_and_serial_plan_20260522T092525_result.json`
- **Structured JSON:** [`2669acabe892fea45005.json`](../../sessions/26/2669acabe892fea45005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 产出报告

### 1. GPU 清理结果

| GPU | 进程 | 状态 | 显存 |
|-----|------|------|------|
| 0 | SFT baseline (PID 621890) | **运行中，已保留** | 90467 MiB |
| 1 | seed8 deadlock (PID 647219) | **已 kill** | 3 MiB ✓ |
| 2 | seed2048 残留 Ray worker (PID 691531) | **已 kill** | 3 MiB ✓ |
| 3 | intervention_c | 已自行退出 | 3 MiB ✓ |

GPU 1/2/3 全部释放，可用于串行 eval。

### 2. SFT Baseline Eval 进度

- W&B: `n6e4ylj1` ("sft-baseline-ood-eval-v2")
- 启动时间: 17:10 CST
- 当前状态: 刚完成 env 初始化（"134 games in eval_out_of_distribution"），进入首轮 rollout
- 进度: 极早期，尚未产出 episode 结果
- **ETA: 134 tasks × 最多 50 turns/task，单 GPU 预计 3-6 小时 → ~20:00-23:00 CST**

### 3. Val Seed 调查结论

| Config | val seed |
|--------|---------|
| SFT baseline | **123** |
| seed5 | **789** |
| seed6 / seed8 / seed2048 / intervention_c | **321** |

三个不同的 val seed 存在。但 **seed 差异不影响 eval 公平性**，原因：

1. ALFWorld OOD split 恰好有 **134 game files**
2. 所有 config 都用 `env_groups: 134, group_size: 1`
3. `es_manager.reset()` 中 seed 展开为 `[base_seed, base_seed+1, ..., base_seed+133]`
4. Game 选择: `game_files[seed % 134]` — 134 个连续整数 mod 134 **必然覆盖全部 0-133 索引**
5. **不同 val seed 只改变 group_id → game 的映射顺序，不改变评估的 task 集合**
6. 聚合 success rate 不受影响

### 4. 建议统一 seed

**不需要因为 seed 差异重跑任何 eval** — 数学上保证了结果等价。

为了代码一致性，后续新 eval config 统一用 `val: 42`。已完成和正在运行的结果无需修改。

### 串行 Eval 规划

SFT baseline 占 GPU 0。GPU 1/2/3 立即可用。建议：
- 在 GPU 1/2/3 上串行启动失败的 3 个 eval（seed8、seed2048、intervention_c）
- 或等 SFT baseline 完成后 4 GPU 串行跑

---
