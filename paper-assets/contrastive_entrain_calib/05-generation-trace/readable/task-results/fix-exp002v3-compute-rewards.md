# fix exp002v3 compute rewards

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp002v3-compute-rewards_20260519T182932_result.json`
- **Structured JSON:** [`2e113386497ba52a6c7c.json`](../../sessions/2e/2e113386497ba52a6c7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并正常运行。汇总：

## 结果

### 1. Bug 修复 diff
```diff
-    def compute_rewards(self, completions, conditions, pair_ids, batch_activations, r1_ema=None, ema_alpha=0.3):
-        rewards, components = super().compute_rewards(
-            completions, conditions, pair_ids, batch_activations, r1_ema, ema_alpha
-        )
+    def compute_rewards(self, completions, conditions, pair_ids, batch_activations):
+        rewards, components = super().compute_rewards(
+            completions, conditions, pair_ids, batch_activations
+        )
```

### 2. Import 验证
`IMPORT OK` — 通过

### 3. 进程
- DeepSpeed 主进程 PID: **153957**（GPU 0+3, master_port 29501）
- tmux session: `exp-002v3`

### 4. GPU 占用
| GPU | 显存占用 | 进程 |
|-----|---------|------|
| 0 | 22494 MiB / 32607 MiB | exp-002v3 (PID 154537) |
| 1 | 24278 MiB | exp-008v3 (未动) |
| 2 | 21484 MiB | exp-008v3 (未动) |
| 3 | 22024 MiB / 32607 MiB | exp-002v3 (PID 154538) |

### 5. 训练日志
Step 1 已完成，reward 信号正常：
- R1 mean: -0.27 → -0.01（两个 rank）
- R3 mean: ~0.998
- Combined: 0.49 / 0.59
- 速度: ~29s/step，预计 8000 steps ≈ 65h

---
