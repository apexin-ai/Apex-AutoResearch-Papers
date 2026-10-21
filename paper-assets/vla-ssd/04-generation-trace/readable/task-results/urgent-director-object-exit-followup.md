# urgent director object exit followup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_director_object_exit_followup_20260521T085724_result.json`
- **Structured JSON:** [`270431f6b3ccaa108c89.json`](../../sessions/27/270431f6b3ccaa108c89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常，模型加载中。版本 warning 无害。

---

## 汇报

**任务 1 — object_pipeline_ridge_v2**: **SUCCESS**。6 phase 全部完成，耗时 96.3 min。最后输出 `counterfactual_combined.json`。

**任务 2 — object_untrained_pipeline_v1**: **已提交，运行中**。
- 原脚本不支持 untrained，已打补丁添加 `--conditions untrained` 参数（切换 CKPT → `openvla-7b`，输出 → `results/libero_object_untrained/`）
- Base model `openvla-7b` 已存在（~14GB safetensors）
- Registry 已创建（hypothesis + parent 已设置），GPU cuda:0 分配，PID 546802
- 日志: `~/runs/vla-ssd/object_untrained_pipeline_v1.log`

**任务 3 — nora_spatial_pipeline_v1**: **DEAD**。PID 543790 不存在。日志显示启动即失败：`unrecognized arguments: untrained, EXIT_CODE=2`。该脚本（`nora_spatial_full_pipeline.py`）的 `--conditions` 参数不接受 "untrained" 值。两块 GPU 当前均空闲（0% utilization, 0 MiB）。

---
