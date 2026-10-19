# diagnose exp020c log check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp020c-log-check_20260514T221700_result.json`
- **Structured JSON:** [`071ff8066bce43edabec.json`](../../sessions/07/071ff8066bce43edabec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### exp020c: 启动失败 ❌

**Hydra 配置错误**，进程已退出（tmux session DEAD）：

```
omegaconf.errors.ConfigAttributeError: Key 'enable_response_mask' is not in struct
    full_key: actor_rollout_ref.model.enable_response_mask

hydra.errors.ConfigCompositionException: Could not override 'actor_rollout_ref.model.enable_response_mask'.
To append to your config use +actor_rollout_ref.model.enable_response_mask=false
EXIT_CODE=1
```

**原因**：启动命令中用了 `actor_rollout_ref.model.enable_response_mask=false`，但该 key 在 config struct 中不存在。Hydra 要求用 `+` 前缀追加新 key。

### exp020b: 停在 step 0

最后日志显示完成了 validation eval（AlfworldSG pass@1=0.0），然后打印了：
```
Training Progress:   0%|          | 0/30 [00:00<?, ?it/s]
```
即 exp020b 在训练开始前（step 0/30）被停止。

### GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 0% | 41685 / 97887 MiB |
| cuda:1 | 0% | 41771 / 97887 MiB |

GPU 利用率 0% 但各占 ~42GB 显存——说明有残留进程占着显存但没在计算。可能是 exp020c 崩溃后的 orphan 进程。

### 修复 exp020c

启动命令中把 `actor_rollout_ref.model.enable_response_mask=false` 改为 `+actor_rollout_ref.model.enable_response_mask=false`（加 `+` 前缀），或者从启动命令中去掉这个参数。需要我修复后重新启动吗？

---
