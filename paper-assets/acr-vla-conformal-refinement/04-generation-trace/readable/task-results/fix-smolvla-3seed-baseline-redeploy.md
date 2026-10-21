# fix smolvla 3seed baseline redeploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_smolvla-3seed-baseline-redeploy_20260522T200919_result.json`
- **Structured JSON:** [`dc3e9c6bea64c45ff45a.json`](../../sessions/dc/dc3e9c6bea64c45ff45a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

**Phase 1 完成：**
- 残留进程已 kill（PID 725310, 725602）
- spatial_seed44 结果：**SR = 60.0%**（120/200, 10 tasks）
- Registry 已更新：spatial_seed44 → DONE/success，4 个失败实验 → DONE/failed

**Phase 2 运行中（4 个 eval 并行）：**

| 服务器 | GPU | 实验 | 状态 |
|--------|-----|------|------|
| bjb1-32546 | cuda:0 | object_seed43-v2 | 运行中 (task 0 完成, SR=60%) |
| bjb1-32546 | cuda:1 | object_seed44-v2 | 运行中 (模型已加载) |
| bjb1-18228 | cuda:0 | spatial_seed43-v2 | 运行中 (权重加载完成) |
| bjb1-18228 | cuda:1 | goal_seed43-v2 | 运行中 (权重加载完成) |

**关键修复：**
- 首次启动缺少 `--rename_map` 参数 → 已加上
- HF Hub 网络不通 → 设置 `HF_HUB_OFFLINE=1` + `HF_HOME=/root/autodl-tmp/.hf_cache`

**待办：** goal_seed44-v2 等前面任一完成后在空闲 GPU 上提交。每个 eval 预计 ~16-20 分钟。

---
