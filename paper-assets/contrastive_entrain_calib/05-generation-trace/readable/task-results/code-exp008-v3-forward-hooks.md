# code exp008 v3 forward hooks

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008-v3-forward-hooks_20260518T211748_result.json`
- **Structured JSON:** [`bdef60f49e468d1455e9.json`](../../sessions/bd/bdef60f49e468d1455e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已创建，语法通过。核心变更：

1. **`ActivationCache` + `_resolve_transformer_layers`** — 从 dcgrpo_trainer.py 移植，增加 `with_grad` 参数控制是否 detach
2. **训练 loop** — 移除 `output_hidden_states=True`，改从 `act_cache.cache` 取各层 hidden states
3. **`retrain_probe_online`** — 同样改用 hook 捕获，接收 `act_cache` 参数；已在 `torch.no_grad()` 下运行所以无内存问题
4. **单 cache 方案** — 一个 `ActivationCache(with_grad=True)` 贯穿训练和 retrain，避免同层双 hook 冲突
5. **output_dir** 默认改为 `exp008v3_hook_probe`，logger 改为 `exp008v3`
6. 训练结束后 `act_cache.remove()` 清理 hooks

---
