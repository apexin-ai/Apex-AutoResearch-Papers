# check bootstrap v2 post restart

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v2_post_restart_20260523T034046_result.json`
- **Structured JSON:** [`08ed7dcbcd4ed4ab6a6a.json`](../../sessions/08/08ed7dcbcd4ed4ab6a6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**进程状态**：全部被杀。两张 GPU 均空闲（0% util, 691 MiB），tmux 无法通过 read_only 检查但从 GPU 状态判断进程已死。两份日志都停在 "fitting RidgeCV per layer..." 中途。

**已完成 11/20 JSON**：

| 条件组 | 完成情况 |
|--------|---------|
| openvla_goal | trained ✓ untrained ✓ |
| openvla_spatial | trained ✓ untrained ✓ |
| openvla_object | trained ✓ untrained ✓ |
| openvla_long | trained ✓ untrained ✓ |
| tracvla_goal | trained ✓ untrained ✓ |
| tracvla_spatial | trained ✓ (untrained 缺失) |
| tracvla_object | 缺失 |
| tracvla_long | 缺失 |
| nora_* | 全部缺失（目录都没创建） |

**待重启 9 个条件**：
- TracVLA 5 个：spatial/untrained, object/trained, object/untrained, long/trained, long/untrained
- NORA 4 个：全部

需要重新启动剩余条件的 bootstrap。是否现在重启？

---
