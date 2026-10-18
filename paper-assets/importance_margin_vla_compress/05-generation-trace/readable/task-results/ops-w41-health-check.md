# ops w41 health check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w41-health-check_20260527T130839_result.json`
- **Structured JSON:** [`bdbe96e6d8516261642d.json`](../../sessions/bd/bdbe96e6d8516261642d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**westd-41074 状态**：
- **k=0.95 v2 已完成**：78.4% (392/500)，registry 已更新为 DONE
- **4 个实验运行中**：attn k=0.5 (GPU1), attn k=0.75 (GPU0), attn k=0.7 (GPU3), random k=0.9 seed43 (GPU2)
- **cascade 等待中**：GPU3 的 attn k=0.7 完成后自动启动 L2norm k=0.95 seed43

**⚠️ 需要处理**：GPU 0 上有两个完全相同的 attn k=0.75 实验 (PID 561220 + 568159)，浪费显存且互相拖慢。建议 kill PID 568159（较晚启动的那个，tmux `eval_pi05_attn_k075_long_seed42_strict`），释放 ~10.5 GB 显存。是否执行？

---
