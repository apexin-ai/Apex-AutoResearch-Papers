# monitor v9d save contents verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v9d_save_contents_verify_20260520T062024_result.json`
- **Structured JSON:** [`96063cb4fb5f4c3e36fb.json`](../../sessions/96/96063cb4fb5f4c3e36fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：step 10 checkpoint 会是 **~92GB**，`save_contents` 配置**没有生效**。

### 依据

**配置层级错误**：yaml 第 35 行 `save_contents: ["model", "extra"]` 在 `trainer:` 层级下，但 actor worker 的 checkpoint manager 读的是 `actor_rollout_ref.actor.checkpoint.save_contents`。

完整调用链：
1. `agent_trainer.py:1113` → `self.actor_rollout_wg.save_checkpoint(...)`
2. `fsdp_workers.py:1043` → `self.checkpoint_manager.save_checkpoint(...)`
3. `fsdp_workers.py:847` → checkpoint manager 初始化用 `checkpoint_config=self.config.actor.checkpoint`
4. yaml 中 `actor_rollout_ref.actor:` 下**没有 `checkpoint:` 子节点**，所以用了 `CheckpointConfig` 的默认值：`["model", "optimizer", "extra"]`
5. `trainer.save_contents` 在整个保存路径中**从未被任何代码读取**

**日志也确认了**：resolved config 中 actor 的 checkpoint 配置为 `'save_contents': ['model', 'optimizer', 'extra']`（包含 optimizer）。

### 修复方法

yaml 中需要把 `save_contents` 放到正确层级：

```yaml
actor_rollout_ref:
  actor:
    checkpoint:
      save_contents: ["model", "extra"]
```

**磁盘会满（91GB 可用 < 92GB checkpoint）。需要在 step 10 之前停止训练或修改配置重启。**

---
