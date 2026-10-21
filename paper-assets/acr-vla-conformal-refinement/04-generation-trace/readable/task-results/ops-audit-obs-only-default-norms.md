# ops audit obs only default norms

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-obs-only-default-norms_20260518T061413_result.json`
- **Structured JSON:** [`9de5841d0d95a849318a.json`](../../sessions/9d/9de5841d0d95a849318a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：obs_only default 没有问题

完整代码路径分析：

### 代码追踪

| 步骤 | 文件:行 | 逻辑 |
|------|---------|------|
| CLI default | evaluate.py:78 | `--max_correction_norm` default=`None` |
| obs_only 加载 | evaluate.py:370-374 | `crm.load_state_dict(torch.load(ckpt, weights_only=True))` — 纯 state_dict |
| checkpoint 格式 | train_crm.py:494 | `torch.save(crm.state_dict(), ...)` — 只存权重，不含 max_correction_norm |
| CLI override | evaluate.py:378 | `args.max_correction_norm is None` → 不触发 |
| **最终值** | crm.py:18 | **类默认 `max_correction_norm = 1.42`** |

### 与 perdof default 的区别

perdof default 的问题来源于 checkpoint dict 中嵌入了 `max_correction_norm`（通过 `crm_k1_accg` 路径加载）。但 obs_only 走的是不同的代码路径：
- 用 `weights_only=True` 直接 load state_dict
- 训练代码只保存 `crm.state_dict()`，不含额外 key
- 实际值 = CRM 构造函数默认值 `1.42`

### 每个 seed 的结果

| Seed | Server | File | SR | actual max_correction_norm | 来源 |
|------|--------|------|------|---------------------------|------|
| 42 | bjb1-32546 | eval_object_obs_only.json | 0.19 | **1.42** | code default |
| 43 | bjb1-18228 | eval_object_obs_only_seed43.json | 0.12 | **1.42** | code default |
| 44 | bjb1-32546 | eval_object_obs_only_default_seed44.json | 0.16 | **1.42** | code default |
| 45 | bjb2-28827 | eval_object_obs_only_default_seed45.json | 0.12 | **1.42** | code default |
| 46 | bjb1-32546 | eval_object_obs_only_default_seed46.json | 0.15 | **1.42** | code default |

**1.42 远大于所有测试的 norm 值（0.03–0.3），在实践中等同于 uncapped。obs_only default 分组分类正确，无需重新归类。**

---
