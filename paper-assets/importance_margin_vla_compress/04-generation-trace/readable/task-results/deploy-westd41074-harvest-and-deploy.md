# deploy westd41074 harvest and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_harvest_and_deploy_20260522T172317_result.json`
- **Structured JSON:** [`b0f55f56add4b743e809.json`](../../sessions/b0/b0f55f56add4b743e809.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正在运行 — torch.compile 正在编译模型（可以看到大量 compile_worker 进程，parent=872802）。编译完成后 cuda:0 VRAM 会上升。进程状态正常。

### 汇报

**任务 A — Goal L2norm k=0.5 结果**
- **SR = 59.2%**（296/500），conclusion: **negative**
- 远低于 baseline 96.4%，50% token pruning 对 Goal suite 造成严重退化
- 任务方差大：turn_on_stove 100%, put_wine_bottle_on_cabinet 92%, 但 put_bowl_on_stove 仅 2%
- Registry 已更新为 DONE

**任务 B — cuda:0 新实验部署**
- `eval_pi05_l2norm_k03_goal_seed42` 已启动（PID 872802）
- 当前处于 torch.compile 阶段，编译完成后 cuda:0 VRAM 将上升
- Registry 已更新为 RUNNING

**四卡状态**

| GPU | VRAM | 任务 |
|-----|------|------|
| cuda:0 | 4 MiB (编译中) | **新部署** L2norm k=0.3 Goal |
| cuda:1 | 10786 MiB | eval 任务运行中 |
| cuda:2 | 10686 MiB | attention pruning eval 链 |
| cuda:3 | 27535 MiB | OpenVLA Smart Compress m64 训练 |

---
