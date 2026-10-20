# eval capture westd all results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_capture-westd-all-results_20260515T163912_result.json`
- **Structured JSON:** [`cceb7aeb79621f2321a5.json`](../../sessions/cc/cceb7aeb79621f2321a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。汇总表：

## GSM8K Accuracy 对比 (n=100, greedy)

| 配置 | Post-Prune | Post-SFT | SFT 恢复 |
|------|-----------|----------|---------|
| α=0.0 (magnitude-only) | — | 64% | — |
| **α=0.5** | 25% | **FAIL** (checkpoint 损坏) | — |
| α=1.0 | 27% | 57% | +30pp |
| **α=2.0** | 29% | **62%** | +33pp |
| α=4.0 | 40% | 62% | +22pp |
| Standard (LLM-Pruner) | 27% | 64% | +37pp |
| RASP | 31% | 57% | +26pp |
| **GraSP-20** | **7%** (eos_rate=2%) | **41%** | +34pp |

### 关键发现

1. **α=2.0 post-SFT = 62%**，与 α=4.0 持平，但 post-prune 更低 (29% vs 40%)。SFT 恢复能力强。
2. **GraSP post-SFT = 41%**，虽然 SFT 恢复了 +34pp，但绝对值远低于其他方法。GraSP pre-SFT 仅 7% 且 eos_rate=2%（几乎全部 truncated），说明剪枝后模型结构严重受损。
3. **α=0.5 eval 失败** — safetensors 文件损坏 (`incomplete metadata, file not fully covered`)，SFT checkpoint 需要重新保存或重训。

---
