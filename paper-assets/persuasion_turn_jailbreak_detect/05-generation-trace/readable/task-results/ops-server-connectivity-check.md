# ops server connectivity check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server_connectivity_check_20260524T085342_result.json`
- **Structured JSON:** [`d728c63ea11131189371.json`](../../sessions/d7/d728c63ea11131189371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**autodl-5090** — 连接失败，`Unable to connect to port 33216 on 106.38.204.136`。可能实例已关机或端口变更。

**gpu-5090-4x-3** — 连接失败，同一错误、同一 IP:端口。两个名称可能指向同一台已下线的实例。

**westd-33183** — 正常：
- cuda:0: NVIDIA RTX PRO 6000 Black (98GB)，空闲，无进程
- nvidia-smi 仅显示 1 张卡，与项目配置中"9 张卡"不一致
- 磁盘 /root: 87% (仅剩 4.2G)，偏紧

报告已写入 `memory.md`。

---
