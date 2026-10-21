# check llama ss progress v2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama_ss_progress_v2_20260524T095011_result.json`
- **Structured JSON:** [`faf50054589dfefe319b.json`](../../sessions/fa/faf50054589dfefe319b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Llama SS 训练状态：RUNNING**

| 项目 | 值 |
|------|-----|
| PID | 158507 (GPU 进程 158516) |
| 运行时长 | 2h 32m |
| 当前 step | **6550** / epoch 0 |
| 配置 total steps | 3000（日志记录，可能是 optimizer steps，数据 step 有 grad accum） |
| GPU | RTX PRO 6000 Blackwell, 90.4/97.9 GB, 79% util, 285W |
| Loss | L_NTP≈1.03, L_GAR≈0.0002, total≈1.03 |
| Gate mean | 0.94 (std=0.056, range 0.79–1.00) |
| SS ratio | 0.273 / max 0.30 (接近上限，warmup 已完成) |
| Gate profile | 浅层高(L0-L5 ≈0.97-0.99)，深层低(L25=0.789 最低) |

Gate 分布合理：浅层近 1（保留残差），深层更低（更多门控干预）。SS ratio 接近 max=0.3，训练已进入稳态阶段。

按 2.5h 完成 6550 data steps 的速率，若 total optimizer steps=3000 对应 ~24000 data steps (grad_accum=8)，剩余约 **6.6h**。

---
