# fix w41 cuda3 kill attn k05 deploy attn k075 s45

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_w41_cuda3_kill_attn_k05_deploy_attn_k075_s45_20260528T005155_result.json`
- **Structured JSON:** [`f575a347064acf69b635.json`](../../sessions/f5/f575a347064acf69b635.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志显示已开始加载模型，但 GPU 3 还没出现在 compute apps 中（模型加载阶段在 CPU，正常）。配置正确：`suite=libero_10, prune=attention, keep=0.75, eps=50, gpu=0`。

完成：
- **已杀** `eval_pi05_attn_k05_long_seed44_strict_w41` (PID 448236)，registry 标记 killed
- **已部署** `eval_pi05_attn_k075_long_seed45_strict_w41` (PID 459963) 到 w41:cuda:3，模型加载中

---
