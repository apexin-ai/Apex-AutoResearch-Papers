# deploy westd41074 gpu2 random k085 spatial postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd41074-gpu2-random-k085-spatial-postfix_20260523T230853_result.json`
- **Structured JSON:** [`9200a374346225a626c1.json`](../../sessions/92/9200a374346225a626c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

- **实验**: `eval_pi05_random_k085_spatial_seed42_postfix`
- **服务器**: westd-41074 GPU 2（10614 MiB 已分配）
- **参数**: `--prune_mode random --keep_ratio 0.85 --suite libero_spatial --seed 42`
- **CPU RNG 确认**: `torch.randperm` 默认在 CPU 执行，日志显示 `first_indices=[0,1,2,3,4]`
- **tmux session**: `eval_pi05_random_k085_spatial_seed42_postfix`
- **日志**: `/tmp/eval_pi05_random_k085_spatial_seed42_postfix.log`
- **Registry**: RUNNING，spec 已更新

注意：首次启动时因缺少 `MUJOCO_GL=egl` 导致渲染挂起，第二次因 `CUDA_VISIBLE_DEVICES` 未正确传递落到 GPU 0，第三次补全所有环境变量后正常启动。GPU 0/1/3 上的实验未受影响。

---
