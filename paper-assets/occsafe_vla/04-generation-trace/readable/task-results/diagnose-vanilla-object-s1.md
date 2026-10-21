# diagnose vanilla object s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_vanilla_object_s1_20260528T072905_result.json`
- **Structured JSON:** [`0b0eead6240e2cc48523.json`](../../sessions/0b/0b0eead6240e2cc48523.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**判断：success** — 训练正常完成。

**日志关键行：**
```
100%|██████████| 50005/50005 [13:28:34<00:00, 7.59s/it]
Max step 50005 reached! Stopping training...
Saved merged model for Step 50000 at: /root/autodl-tmp/checkpoints/vanilla_object_s1/openvla-7b+libero_object_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_object_s1--50000_chkpt
[AUX] step=50000, occ_loss=0.0000, depth_loss=0.0000, action_loss=0.0996
```

**Checkpoint 路径：**
`/root/autodl-tmp/checkpoints/vanilla_object_s1/openvla-7b+libero_object_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_object_s1--50000_chkpt`

（另有 40000 和 45000 步的中间 checkpoint）

**Registry 更新已执行：**
- `conclusion` → `success`
- `status` → `DONE`
- `log_path` → `/root/runs/occsafe_vla/vanilla_object_s1.log`
- `checkpoint_path` → 50000 步 checkpoint 路径
- `spec` 已恢复完整对象

---
