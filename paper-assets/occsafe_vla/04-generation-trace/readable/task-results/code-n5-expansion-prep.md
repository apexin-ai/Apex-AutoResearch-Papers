# code n5 expansion prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n5-expansion-prep_20260526T202905_result.json`
- **Structured JSON:** [`1213464324c9790d69ed.json`](../../sessions/12/1213464324c9790d69ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已生成并注册：`artifacts/n5_expansion_launch_commands.md`

内容包含：
- **Phase 1**: 4 个 eval 命令（vanilla_v2_s1/s2, detach_ln_s3, cutoff_25k_s1_v2），各绑定对应 GPU，MUJOCO_EGL_DEVICE_ID 已匹配
- **Phase 2**: 4 个 n=5 训练命令（seed=46），GPU 分配按任务要求：cuda:0→detach_ln_s4, cuda:1→ablation_occ_detach_s4, cuda:2→full_occ_ln_s4, cuda:3→mvp_occ_s4
- GPU 分配表、前置条件检查清单、时间估算

有一个需要确认的点：eval 脚本名在任务中是 `safelibero_eval.py`，但 registry 历史记录中是 `evaluate_safelibero.py`，启动前需确认 34685 上实际存在的文件名。

---
