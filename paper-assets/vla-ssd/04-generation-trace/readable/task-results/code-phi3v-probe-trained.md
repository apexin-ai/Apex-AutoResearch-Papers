# code phi3v probe trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_probe_trained_20260519T180554_result.json`
- **Structured JSON:** [`c4f91c605478ebc5894d.json`](../../sessions/c4/c4f91c605478ebc5894d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Phi3V Trained Cross-Instruction 10-way Probe 结果

| Token Position | L0 | L1 | L2-L31 |
|---|---|---|---|
| **image_mean** | 0.10 | 0.10 | 0.095-0.103 (chance) |
| **last_preaction** | 0.10 | **0.836** | **1.000** |

**C1 readout pattern 完全确认**：
- `last_preaction`：L2 起 100%，L1 已达 83.6%
- `image_mean`：全 32 层均为 chance level (~10%)
- 与 OpenVLA (Llama-2 7B) 的 pattern 一致，跨架构泛化成立

输出文件：
- HDF5: `westd-19183:/root/autodl-tmp/vla-ssd/results/cross_instruction/phi3v_trained_cross_inst.h5` (1883 MB)
- JSON: `westd-19183:/root/autodl-tmp/vla-ssd/results/cross_instruction/phi3v_trained_probe_results.json`
- Registry: `phi3v_probe_trained` → DONE (success)

---
