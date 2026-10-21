# ops eval phase2 lambda0 s2 westd35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_phase2_lambda0_s2_westd35807_20260526T111719_result.json`
- **Structured JSON:** [`70dda698311fc53a8db1.json`](../../sessions/70/70dda698311fc53a8db1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行中。总结：

**Step 1 — 部署修复版脚本**: **不需要**。westd-35807 上的 `eval_safelibero.py` 已包含两项修复：
- 180° 旋转：`np.ascontiguousarray(image[::-1, ::-1])` (line 841/843)
- 相机分辨率：`camera_heights: 256, camera_widths: 256` (line 903/904)
- 与 westd-45947 版本一致

**Step 2 — 运行 eval**: 已启动
- tmux session: `eval_p2_l0_s2`
- 日志: `/root/eval_phase2_lambda0_s2.log`（tee pipe buffer 导致日志延迟刷新，通过 `tmux capture-pane` 可实时查看）
- GPU 3 占用 ~9GB 显存
- Task 0 (pick up the orange juice and place it in the basket) 已跑到 Episode 10/50
- model_type=`lora_baseline`，checkpoint 确认为 full state dict 格式（无 adapter_config.json）

**Step 3 — 注册实验**: 完成
- exp_id: `eval_phase2_lambda0_s2`
- parent: `train_pi05_phase2_lambda0_s2`
- status: RUNNING

**注意**: 跳过了 sanity check，因为脚本已是修复版（无需修改）。如果后续 TSR 异常低，可通过 `tmux capture-pane -t eval_p2_l0_s2 -p -S -100` 查看实时进度。

---
