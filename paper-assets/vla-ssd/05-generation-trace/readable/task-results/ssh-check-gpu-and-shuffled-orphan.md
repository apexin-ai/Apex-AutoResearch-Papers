# ssh check gpu and shuffled orphan

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gpu-and-shuffled-orphan_20260516T000110_result.json`
- **Structured JSON:** [`50c6a10fa4395818b303.json`](../../sessions/50/50c6a10fa4395818b303.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

| 项目 | 状态 |
|------|------|
| **GPU 0** | 16419MiB / 97887MiB, 0% util — PID 678338 (extract random s0) |
| **GPU 1** | 17106MiB / 97887MiB, 86% util — PID 677540 (untrained probe, 704MiB) + PID 678183 (extract shuffled, 16388MiB) |
| **plan008-random-s0** | **alive** — PID 678338, `extract_features_rand_inst.py --instruction_mode random --seed 0 --gpu 0`, 运行 ~3min |
| **plan008-shuffled** | **alive** — PID 678183, `extract_features_rand_inst.py --instruction_mode shuffled --gpu 1`, 运行 ~3min，不是 orphan |
| **untrained probe** | **alive** — PID 677540, `untrained_last_preaction_probe.py`, cuda:1, 运行 ~8min |

三个进程全部正常运行。GPU 1 同时跑 untrained probe 和 shuffled 特征提取，显存共占 ~17GB/98GB，空间充裕。GPU 0 利用率 0% 说明 random-s0 可能在做 I/O 或刚完成一个 batch。

---
