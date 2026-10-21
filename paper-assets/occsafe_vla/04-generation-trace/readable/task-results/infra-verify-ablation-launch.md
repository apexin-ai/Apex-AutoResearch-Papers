# infra verify ablation launch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_ablation_launch_20260521T034447_result.json`
- **Structured JSON:** [`57fc55f7f35ae1cb73a0.json`](../../sessions/57/57fc55f7f35ae1cb73a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。

## ablation_occ_detach_s0
- PID (wrapper/python): 481666 / 481746
- GPU: cuda:0, util 99%, mem 62.2GB / 97.9GB
- 参数验证: **OK** — `--occ_detach true`, `--num_images_in_input 2`, `--use_proprio True`, `--use_occ_head True` 均确认
- 速度: ~1.08-1.09 it/s（step 89）
- Loss: 尚未输出（日志仅含 progress bar，loss 可能在 step 100 或更晚的 logging interval 才打印）
- 状态: **正常**

## ablation_random_occ_s0
- PID (wrapper/python): 481813 / 481960
- GPU: cuda:1, util 99%, mem 62.2GB / 97.9GB
- 参数验证: **OK** — `--random_occ True`, `--occ_detach false`, `--num_images_in_input 2`, `--use_proprio True`, `--use_occ_head True` 均确认
- 速度: ~1.07-1.08 it/s（step 86）
- Loss: 尚未输出（同上）
- 状态: **正常**

两个实验均正常运行，参数正确，GPU 占用充分，速度与预期一致。Loss 值需要等到下一个 logging interval 才会出现在日志中。

---
