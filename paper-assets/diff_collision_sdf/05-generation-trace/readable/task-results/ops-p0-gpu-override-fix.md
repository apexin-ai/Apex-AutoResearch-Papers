# ops p0 gpu override fix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0_gpu_override_fix_20260525T195600_result.json`
- **Structured JSON:** [`fb708e2c5c07e05e5771.json`](../../sessions/fb/fb708e2c5c07e05e5771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

nvidia-smi 已确认 eval 正确落在 GPU 1（PID 142394），修复生效。

---

## 产出报告

### 1. Kill 结果
- PID 121109: SIGTERM 成功
- PID 123811: SIGKILL 成功（force killed）

### 2. 代码修改 Diff

**文��**: `/root/colliforce-vla/scripts/eval_safelibero.py` 第 1141 行

```diff
-    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
+    # Respect externally-set CUDA_VISIBLE_DEVICES (e.g. from submit_training_job)
+    if os.environ.get("CUDA_VISIBLE_DEVICES"):
+        print(f"[GPU] Using external CUDA_VISIBLE_DEVICES={os.environ['CUDA_VISIBLE_DEVICES']} (ignoring --gpu {args.gpu})")
+    else:
+        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
+        print(f"[GPU] Setting CUDA_VISIBLE_DEVICES={args.gpu} from --gpu flag")
```

### 3. 两台服务器同步
- westd-35807: ✓ 已修复
- westd-45947: �� 相同 sed 已应用，grep 确认一致

### 4. Eval 进程状态
| GPU | PID | 任务 | 显存 |
|-----|-----|------|------|
| 0 | 3717 | train_pi05_a1_spatial_bowl_s0_l005 | 27036 MiB |
| 1 | 142394 | **eval_pi05_a1_30k_s1_l005_disp** (新启动) | 8995 MiB |
| 2 | 134344 | eval_pi05_a1_best_s1_l005_16k (已在运行) | 8995 MiB |
| 3 | 75123 | eval_pi05_a1_best_s2_l005_10k | 8991 MiB |

### 5. 说明
cuda:2 的 eval（PID 134344）在 kill 前已正确运行在 GPU 2 上（它通过 `--gpu 2` 直接设置，没有外部 CUDA_VISIBLE_DEVICES 冲突），无需重启。cuda:1 上新启动的 eval 通过外部 `CUDA_VISIBLE_DEVICES=1` + 修复后代码正确绑定到 GPU 1���

---
