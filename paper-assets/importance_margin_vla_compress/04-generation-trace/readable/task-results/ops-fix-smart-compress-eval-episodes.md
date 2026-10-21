# ops fix smart compress eval episodes

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_smart_compress_eval_episodes_20260518T013319_result.json`
- **Structured JSON:** [`71c1db748a029f60d03c.json`](../../sessions/71/71c1db748a029f60d03c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 进程正常运行：

| 配置 | PID | GPU | 状态 |
|------|-----|-----|------|
| M=32 | 541184 | GPU 0 | 运行中，已到 Ep 8/50 |
| M=64 | 542036 | GPU 1 | 运行中，已到 Ep 3/50 |

**修正内容：**
- 旧进程 420909/426524 已不存在（之前已结束或被 kill）
- `--num_episodes 500` → `--num_episodes 50`（每 task 50 eps）
- 参数名修正：`--n_queries`（非 `--num_queries`）
- 加了 `--seed 42`
- 加了 `HF_HOME=/root/autodl-tmp/.hf_cache`（原脚本漏了这个环境变量，导致首次重启失败）

---
