# fix train py adapter only checkpoint

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_train_py_adapter_only_checkpoint_20260514T193437_result.json`
- **Structured JSON:** [`20f17cb424e1cce8da2d.json`](../../sessions/20/20f17cb424e1cce8da2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两块 GPU 100% 利用率，训练正常运行。修改磁盘文件不影响当前进程。

---

**修改总结：**

### 1. `_save_checkpoint` (train.py L553-563)

**修改前：**
```python
torch.save(model.state_dict(), path / "model.pt")  # 完整 state_dict → 5.8GB
```

**修改后：**
```python
if getattr(args, 'use_lora', False):
    sd = {k: v for k, v in model.state_dict().items()
          if not k.startswith('backbone.') or 'lora_' in k}
else:
    sd = model.state_dict()
torch.save(sd, path / "model.pt")
```

LoRA 模式下只保存：
- `backbone.*.lora_A/B.*` — LoRA adapter weights (~9MB)
- `projection.*` — 投影头 (~9MB)
- `log_temperature` — 可学习温度 (4B)

预估 checkpoint 大小：**5.8GB → ~18MB**

### 2. Eval 脚本 `strict=False` (5 个文件)

| 文件 | 行号 |
|------|------|
| eval_checkpoint.py | 175 |
| evaluation/eval_swebench.py | 264 |
| evaluation/eval_retrieval.py | 188 |
| evaluation/eval_repobench.py | 216 |
| scripts/eval_swebench_e2e.py | 166 |

`strict=False` 兼容两种格式：旧的完整 checkpoint 和新的 adapter-only checkpoint。

### 3. 已有 checkpoint 格式
- s42, s43 的 `best_by_recall_at_1/` 内有 `model.pt` (5.8GB) — 完整 merged state_dict
- eval 脚本加了 `strict=False` 后加载旧格式无影响

### 4. 生效时机
当前 run (random_s44) 已加载旧 train.py 到内存 → 不受影响。chain 启动下一个 run 时读取新 train.py → 新逻辑生效。

---
