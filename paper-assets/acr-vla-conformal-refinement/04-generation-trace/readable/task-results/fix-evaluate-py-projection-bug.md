# fix evaluate py projection bug

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_evaluate-py-projection-bug_20260521T154742_result.json`
- **Structured JSON:** [`6c8bdd1d61e8b9293e4c.json`](../../sessions/6c/6c8bdd1d61e8b9293e4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bjb2-28827 的 evaluate.py 是旧版本，不含 pi05/obs_proj 逻辑，无需修补。

**修复完成，汇总：**

### 修改内容
`src/evaluate.py` L574-583，删除随机投影，替换为维度校验：

**原代码 (L574-579)：**
```python
# Observation feature projection for PI05 (2048D -> 960D for CRM compatibility)
obs_proj = None
if args.model == "pi05" and crm is not None:
    obs_proj = torch.nn.Linear(2048, OBS_DIM).to(device)
    obs_proj.eval()
    print(f"[eval] PI05 obs projection: 2048 -> {OBS_DIM}")
```

**修复后：**
```python
obs_proj = None
if args.model == "pi05" and crm is not None:
    pi05_feat_dim = 2048
    if args.obs_dim != pi05_feat_dim:
        raise ValueError(
            f"PI05 produces {pi05_feat_dim}D features but CRM was built with "
            f"obs_dim={args.obs_dim}. Re-train CRM with --obs_dim {pi05_feat_dim} "
            f"or pass --obs_dim {pi05_feat_dim} if checkpoint matches."
        )
    print(f"[eval] PI05 features ({pi05_feat_dim}D) passed directly to CRM (no projection)")
```

### 逻辑说明
- `obs_proj` 保持 `None` → 所有 13 处使用点已有 `if obs_proj is not None` 守卫，features 直接传递不做投影
- 如果 `--obs_dim` 与 2048 不匹配，立即报错而非静默用随机权重

### Dry-run 结果
Shape check 通过：`(1, 2048)` → `(1, 2048)` ✅

### 同步状态
| 服务器 | 状态 |
|--------|------|
| bjb1-32546 | ✅ 已修补 |
| bjb2-40593 | ✅ 已修补 |
| bjb1-18228 | ✅ 已修补 |
| bjb2-28827 | ⏭️ 旧版本，无 pi05 逻辑，无需修补 |

---
