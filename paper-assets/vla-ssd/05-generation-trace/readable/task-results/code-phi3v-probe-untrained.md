# code phi3v probe untrained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phi3v_probe_untrained_20260519T182430_result.json`
- **Structured JSON:** [`ba5120319f5830282bcc.json`](../../sessions/ba/ba5120319f5830282bcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

**Untrained (base Phi-3-instruct) vs Trained 对比：**

| Position | Layer | Untrained | Trained |
|---|---|---|---|
| **last_preaction** | L0 | 10% | 10% |
| | L1 | **98.1%** | 83.6% |
| | L2-L31 | **100%** | 100% |
| **image_mean** | L0-L31 | ~10% | ~10% |

关键发现：
- **last_preaction**: untrained 从 L1 就达到 98.1%（甚至高于 trained 的 83.6%），L2+ 完全 100%。instruction routing 完全继承自 base Phi-3 的 instruction tuning，VLA 训练未创造此能力。
- **image_mean**: 两个条件均为 chance（~10%），instruction 信息从未写入 image token 均值。
- **Untrained L1 > Trained L1**: 这暗示 VLA 训练轻微扰动了 L1 的 instruction routing（83.6% vs 98.1%），但 L2+ 不受影响。

输出文件：
- HDF5: `/root/autodl-tmp/vla-ssd/results/cross_instruction/phi3v_untrained_cross_inst.h5` (1.9 GB)
- JSON: `/root/autodl-tmp/vla-ssd/results/cross_instruction/phi3v_untrained_probe_results.json`
- Registry: `phi3v_probe_untrained` → DONE (success)

---
