# ssh gpu audit loop17

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-audit-loop17_20260516T201950_result.json`
- **Structured JSON:** [`09357151a941b9ac38fb.json`](../../sessions/09/09357151a941b9ac38fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546（全部占满，无空闲 GPU）

| GPU | PID | 实验 | 显存 | 利用率 | 状态 |
|-----|-----|------|------|--------|------|
| cuda:0 | 226878 | scalar-seed44-r2 (norm0.1) | 1923 MiB | 20% | OCCUPIED |
| cuda:1 | 295478 | reconvla-seed46 | 5146 MiB | 21% | OCCUPIED |
| cuda:2 | 306318 + 309158 | perdof-norm03-seed45 + perdof-norm01-seed45 | 11325 MiB | 99% | OCCUPIED |
| cuda:3 | 233553 | obs-only-norm02-seed45 | 1923 MiB | 22% | OCCUPIED |
| cuda:4 | 306518 + 310485 | perdof-norm02-seed46 + perdof-default-seed45 | 11325 MiB | 98% | OCCUPIED |
| cuda:5 | 229751 | obs-only-default-seed44 | 1923 MiB | 21% | OCCUPIED |

## bjb1-18228（全部占满，无空闲 GPU）

| GPU | PID | 实验 | 显存 | 利用率 | 状态 |
|-----|-----|------|------|--------|------|
| cuda:0 | 474319 | obs-only-norm01-seed45 | 3785 MiB | 21% | OCCUPIED |
| cuda:1 | 531097 + 531970 | vla-only-seed46 + perdof-norm01-seed44 | 11288 MiB | 99% | OCCUPIED |
| cuda:2 | 505419 | perdof-norm03-seed44 | 4250 MiB | 24% | OCCUPIED |
| cuda:3 | 510896 | obs-only-norm02-seed46 | 4250 MiB | 23% | OCCUPIED |

**结论：两台服务器共 10 张 GPU 全部被占用，没有空闲 GPU。** 之前认为可能空闲的 cuda:2/4（32546）和 cuda:0/1（18228）实际都已被新启动的实验占满。

---
