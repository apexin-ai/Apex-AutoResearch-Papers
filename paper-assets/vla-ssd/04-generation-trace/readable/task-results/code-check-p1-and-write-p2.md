# code check p1 and write p2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_p1_and_write_p2_20260516T095208_result.json`
- **Structured JSON:** [`dde6b81348e83d8082f0.json`](../../sessions/dd/dde6b81348e83d8082f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。

**汇总：**

## Task 1: P1 Seed Robustness ✅ 已完成
| 指标 | 值 |
|------|-----|
| Peak layers (5 seeds) | [9, 16, 9, 10, 9] |
| Peak layer mean±std | 10.6 ± 2.7 |
| Peak R² (5 seeds) | [0.6534, 0.6549, 0.6529, 0.6531, 0.6587] |
| Peak R² mean±std | **0.6546 ± 0.0022** |

R² 跨 seed 极稳定（std < 0.003）。Peak layer 除 seed=1 (layer 16) 外均集中在 9-10。

## Task 2: P2 Demo Sensitivity 脚本 ✅ 已部署 + dry-run 通过

- 脚本路径: `/root/vla-ssd/scripts/ablations/demo_sensitivity.py`
- Dry-run (layer 0) 结果: RSA 50=0.0484 / 25=0.0198, Probe 50=0.6448 / 25=0.5709
- 单层耗时 ~51s，完整 33 层预计 ~28 min
- 运行命令: `python scripts/ablations/demo_sensitivity.py --gpu 0`

---
