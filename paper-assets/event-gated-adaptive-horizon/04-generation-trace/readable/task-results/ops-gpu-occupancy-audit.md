# ops gpu occupancy audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-occupancy-audit_20260519T201703_result.json`
- **Structured JSON:** [`aa904bc1528b7e54d28a.json`](../../sessions/aa/aa904bc1528b7e54d28a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**审计结果：**

| 服务器 | GPU | tmux session | 当前步数 | VRAM 占用 |
|--------|-----|-------------|---------|-----------|
| bjb1-40020 | GPU 0 (RTX 4090) | exp_025_s1 | 85,000 | 3,564 MiB / 24,564 MiB |
| bjb1-40020 | GPU 1 (RTX 4090) | exp_025_s2 | 84,000 | 2,523 MiB / 24,564 MiB |
| bjb1-45299 | GPU 0 (RTX PRO 6000) | exp_025_s3 | 85,000 | 8,576 MiB / 97,887 MiB |
| bjb1-45299 | GPU 0 (RTX PRO 6000) | exp_s3_ext | 490,000 | (共享 GPU 0) |
| bjb1-45299 | GPU 1 (RTX PRO 6000) | exp_025_s4 | 65,000 | 7,525 MiB / 97,887 MiB |
| bjb1-45299 | GPU 1 (RTX PRO 6000) | exp_s4_ext | 440,000 | (共享 GPU 1) |

**注意事项：**
- **exp_025_s4** (bjb1-45299 GPU1) 触发了 CIVO 告警：`ve_ratio=2.152, delta_ve=0.860, alert=1.0`，step 65,000
- **exp_s3_ext / exp_s4_ext** 已分别跑到 490k / 440k 步，eval_return 达 944.7 / ~920，接近收敛
- bjb1-45299 每个 GPU 跑了 2 个进程（025 + ext 共享），VRAM 占用仍很低（<9%）

---
