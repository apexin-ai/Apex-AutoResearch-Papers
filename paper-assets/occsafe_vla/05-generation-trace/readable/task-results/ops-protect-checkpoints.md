# ops protect checkpoints

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_protect_checkpoints_20260523T060338_result.json`
- **Structured JSON:** [`9239b0cc98586dfef8d0.json`](../../sessions/92/9239b0cc98586dfef8d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论清晰了。

## 检查结果

### 1. 训练代码 checkpoint 策略

`finetune.py` 第 119-121 行：
- `save_freq = 10_000`
- `save_latest_checkpoint_only = False`（默认值）

当 `save_latest_checkpoint_only=False` 时，每次保存都创建独立目录 `run_dir--{log_step}_chkpt`（第 673 行）。**代码中没有任何自动清理旧 checkpoint 的逻辑**（无 `rm`/`rmtree`/`unlink` 调用）。

### 2. 外部清理脚本

发现两个相关脚本：

- **`checkpoint_rotation.sh`** — 每 10 分钟扫描，保留最新 2 个 checkpoint，删除更旧的。但**只监控 `occ_s0`、`occ_s1`、`occ_s2` 三个目录**，不涉及 `vanilla_retrain_s0` 和 `full_occ_retrain_s0`。
- **`kill_on_50000_chkpt.sh`** — 检测到 50000 checkpoint 后杀进程。同样**只针对 `occ_s0` 和 `occ_s2`**，不影响 retrain 实验。

### 3. 当前 checkpoint 状态

两个 retrain 目录目前都只有 `dataset_statistics.json`，step 10000 的 checkpoint 尚未生成，训练还没到 10K 步。

### 结论

**retrain 实验的 checkpoint 是安全的。** `save_latest_checkpoint_only=False` 意味着 step 10000、20000、30000、40000、50000 的 checkpoint 都会保留在独立目录中，不会被覆盖或清理。现有的 rotation 脚本不监控 retrain 目录。无需额外操作。

---
