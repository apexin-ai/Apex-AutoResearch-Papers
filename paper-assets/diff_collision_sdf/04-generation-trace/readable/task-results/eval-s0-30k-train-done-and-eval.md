# eval s0 30k train done and eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s0_30k_train_done_and_eval_20260527T090910_result.json`
- **Structured JSON:** [`4f1eb4c96d276f62a62b.json`](../../sessions/4f/4f1eb4c96d276f62a62b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

## 汇报

### s0 训练 ✅ 完成
- 30000/30000 steps，总耗时 33h54m
- Final loss: 0.0153 (action=0.0116, sdf=0.0369, ee=0.0035)
- Checkpoint: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/30000`
- Registry `train_pi05_a1_obj_s0_l01` → DONE(success)

### 30K eval ✅ 已启动
- **PID: 722752** (实际 python 进程)，cuda:0
- **`--pi05` 已确认存在** ✔
- Checkpoint 路径: `seed0_l1/30000` ✔
- 日志: `/tmp/eval_30k_s0_l1.log`
- 预计 ~30-40min 完成

### s1 训练进度
- Step 29476/30000 (98%)，ETA ~40min
- Loss 正常: 0.0200, action=0.0166, sdf=0.0335, ee=0.0038

---
