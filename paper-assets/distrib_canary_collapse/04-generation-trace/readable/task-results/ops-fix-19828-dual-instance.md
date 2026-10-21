# ops fix 19828 dual instance

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_19828_dual_instance_20260521T084631_result.json`
- **Structured JSON:** [`b062279812454c9730e9.json`](../../sessions/b0/b062279812454c9730e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已修复。

**结果：**
- PID 655861（多余实例）已 kill，进程不存在
- PID 656193（registry 注册的正确实例，parent session = 656188）继续运行
- cuda:1 上的 a000_s46_fp32 未受影响

**当前 GPU 状态：**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 97% | 14,239 / 97,887 MiB |
| cuda:1 | 96% | 14,239 / 97,887 MiB |

两张卡各跑一个实验，资源正常。

---
