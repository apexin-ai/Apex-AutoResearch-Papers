# diagnose d051 bn v2 failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d051_bn_v2_failures_20260525T134337_result.json`
- **Structured JSON:** [`8a9628244969bf000b05.json`](../../sessions/8a/8a9628244969bf000b05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因**：westd-34685 上的代码没有同步 D051 v2 改动。三个实验传入了 `--occ_norm_type bn`，但该服务器上的 `finetune.py`（commit `bdaee754`）根本没有定义这个参数，argparse 直接报错退出（exitcode 2）。westd-10894 的代码（commit `e4287e94`）才有 `occ_norm_type`（finetune.py:98）。与 GPU 冲突无关——崩溃发生在 argparse 阶段，还没碰 CUDA。

**修复**：在 westd-34685 上 `cd /root/occsafe_vla/openvla-oft && git pull origin main` 同步代码，然后重启三个实验。

---
