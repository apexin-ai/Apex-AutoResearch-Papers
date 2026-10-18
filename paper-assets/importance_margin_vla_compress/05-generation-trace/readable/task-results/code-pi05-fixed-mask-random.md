# code pi05 fixed mask random

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-fixed-mask-random_20260521T191000_result.json`
- **Structured JSON:** [`41b3f888fe10d6e82dc4.json`](../../sessions/41/41b3f888fe10d6e82dc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有改动正确。汇报如下：

## 代码改动 Diff

6 处改动，共 ~12 行新增：

| 行号 | 改动 |
|------|------|
| L32 | 新增 `_episode_mask_cache = {}` 模块级缓存 |
| L54 | 新增 `--fixed_mask` 命令行参数（`store_true`） |
| L131 | `for img, img_mask in zip(...)` → `for cam_idx, (img, img_mask) in enumerate(zip(...))` |
| L135-139 | 新增 fixed mask 逻辑：`--fixed_mask` + `random` 模式时，首次调用生成 indices 缓存到 `_episode_mask_cache[cam_idx]`，后续 replan step 复用 |
| L140-141 | `else` 分支保留原有 `prune_fn()` 调用（非 fixed_mask 或非 random 时不受影响） |
| L199 | config dict 记录 `"fixed_mask"` 字段 |
| L219 | episode 开始时 `_episode_mask_cache.clear()` 重置缓存 |
| L293-294 | 输出文件名加 `_fixmask` tag |

## Dry-run 验证

`--help` 输出确认 `--fixed_mask` 参数已注册，无语法错误。

## GPU1 状态

PID 531274 仍在运行（elapsed 1h17m）：`python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 43 --gpu 1`

## 准备好的启动命令

```bash
cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_object --n_episodes 50 --seed 42 --gpu 1 --fixed_mask
```

GPU1 当前被 k=0.9 seed43 占用，完成后可启动。

---
