# ssh nora spatial untrained cf

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_nora_spatial_untrained_cf_20260522T021944_result.json`
- **Structured JSON:** [`e8acaa7e89c3e6c703d3.json`](../../sessions/e8/e8acaa7e89c3e6c703d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务状态：

- **NORA Spatial untrained CF** 已在 GPU 0 后台运行（PID 597075）
- 模型加载成功（4.2s），当前在 `wrong` condition 处理中（400/50000）
- 修复了 transformers 版本问题（4.48.3 → 5.9.0，旧版不识别 `qwen2_5_vl`）
- 速率 ~9.5 steps/s，预估每个 condition ~88min，总计 ~6h（50 demos × 100 timesteps × 10 tasks × 4 conditions）
- GPU 0 仅用 8GB，不影响 openvla_spatial 下载和 GPU 1 上的 openvla_goal 任务
- 已设置自动轮询，完成后会汇报结果

---
