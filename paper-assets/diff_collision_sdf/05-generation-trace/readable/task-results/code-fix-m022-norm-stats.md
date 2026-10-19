# code fix m022 norm stats

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_m022_norm_stats_20260522T103020_result.json`
- **Structured JSON:** [`2ea25d0729b01e2b970f.json`](../../sessions/2e/2ea25d0729b01e2b970f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器语法验证通过，修复已部署。

## 结果汇总

### Diff

```diff
--- a/scripts/eval_safelibero.py
+++ b/scripts/eval_safelibero.py
@@ -485,9 +485,23 @@
     )
     a3_config = dataclasses.replace(config, model=a3_model_config)
 
-    # Load base model from pre-trained pi0 weights
+    # Load norm_stats from A3 checkpoint (not pi0_base)
+    from openpi.training import checkpoints as _checkpoints
+    sdf_ckpt = args.sdf_checkpoint or args.checkpoint
+    a3_norm_stats = None
+    a3_assets_dir = os.path.join(sdf_ckpt, "assets")
+    if os.path.isdir(a3_assets_dir):
+        for subdir in os.listdir(a3_assets_dir):
+            ns_path = os.path.join(a3_assets_dir, subdir, "norm_stats.json")
+            if os.path.isfile(ns_path):
+                a3_norm_stats = _checkpoints.load_norm_stats(a3_assets_dir, subdir)
+                logging.info("Loaded A3 norm_stats from %s/%s", a3_assets_dir, subdir)
+                break
+    if a3_norm_stats is None:
+        logging.warning("No norm_stats in A3 checkpoint %s, falling back to pi0_base", sdf_ckpt)
+
+    # Load base model from pre-trained pi0 weights, using A3 norm_stats
     policy = _policy_config.create_trained_policy(
-        a3_config, PI0_BASE_WEIGHTS, default_prompt=None
+        a3_config, PI0_BASE_WEIGHTS, default_prompt=None,
+        norm_stats=a3_norm_stats,
     )
```

### A3 checkpoint norm_stats 位置和内容

| Checkpoint | norm_stats 路径 | state.mean 前值 |
|---|---|---|
| A3 spatial | `.../a3_grad_refine_spatial_bowl/.../best/assets/safelibero_spatial/norm_stats.json` | **-0.0221...** |
| A3 object | `.../a3_grad_refine_object_pudding/.../best/assets/safelibero_object/norm_stats.json` | (同结构) |
| pi0_base (错误来源) | `.../openpi_weights/pi0_base/assets/physical-intelligence/libero/norm_stats.json` | **-0.0633...** |

### 部署状态

| 服务器 | 状态 |
|---|---|
| westd-45947 | SYNTAX OK |
| westd-35807 | SYNTAX OK |

### 修复机制

`create_trained_policy` 接受 `norm_stats` 可选参数（为 `None` 时从 `checkpoint_dir/assets/` 加载）。修复后，先扫描 A3 checkpoint 的 `assets/` 子目录找到 norm_stats，显式传入，避免从 `PI0_BASE_WEIGHTS` 加载错误的归一化统计量。

---
