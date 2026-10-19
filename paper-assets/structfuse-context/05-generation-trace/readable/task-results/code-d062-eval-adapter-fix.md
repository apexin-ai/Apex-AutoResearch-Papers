# code d062 eval adapter fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d062_eval_adapter_fix_20260516T162002_result.json`
- **Structured JSON:** [`227294d2573b02872401.json`](../../sessions/22/227294d2573b02872401.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估进程正常运行中（PID 199480，已运行 1:41，状态 `Rl` = running）。总结：

**已完成：**
1. **修复 evaluate_pool50.py** — `load_model` 函数现在自动检测 adapter-only checkpoint（通过检查 state_dict 中 backbone keys 是否都含 `lora_`），并正确加载：adapter-only 时允许 missing keys（base model 已从 pretrained 加载），full model 时保持原有逻辑。
2. **CPU 验证通过** — adapter-only (149 keys, 33MB) 和 full model (583 keys, 6.2GB) 两种格式都能正确加载。
3. **D062 eval 任务已提交** — tmux session `d062-remaining-eval`，使用 GPU 1 (44GB free)，循环评估 8 个 checkpoints。

**运行中：**
- 第一个 checkpoint `embedding_distance_s43/best_by_val_loss` 正在评估（504 queries, pool_size=50），每个 checkpoint 预计 10-15 分钟，全部 8 个约 1.5-2 小时完成。

**StarCoder：**
- 同样存在 adapter vs full model 不一致（random=6.1GB, embedding_distance=59MB），修复是通用的，无需额外改动。

**修复核心逻辑（2行）：**
```python
is_adapter_only = all("lora_" in k for k in state_dict if k.startswith("backbone."))
# ... load_state_dict(strict=False) ...
if is_adapter_only:
    assert not result.unexpected_keys  # base model loaded from pretrained
else:
    assert not result.missing_keys     # full model covers everything
```

---
