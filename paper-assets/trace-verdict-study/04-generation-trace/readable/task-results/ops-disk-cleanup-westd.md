# ops disk cleanup westd

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_westd_20260521T210601_result.json`
- **Structured JSON:** [`04e2889fe22beaabfb52.json`](../../sessions/04/04e2889fe22beaabfb52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 清理前后对比

| 分区 | 清理前 | 清理后 | 释放空间 |
|------|--------|--------|----------|
| 根分区 (/) | 21G/30G (69%) | 21G/30G (68%) | ~0.3G |
| 数据盘 (/root/autodl-tmp) | 208G/250G (84%) | 174G/250G (70%) | **~34G** |

## 清理内容

| 项目 | 释放空间 |
|------|----------|
| CodeLlama-7b-Instruct-hf（项目未使用） | ~26G |
| ModelScope cache（CodeLlama-13b 副本） | ~9.3G |
| 3 个失败实验空目录 | <1M |
| pip/apt cache | <0.3G |
| **总计** | **~35G** |

## 未删除（需注意）

- `/root/models/Qwen/`（12G，Qwen3 模型，根分区）— 非本项目使用，属于其他项目
- `/root/autodl-tmp/div_cal_verify/`（34G）— 其他项目
- 所有中间 checkpoint — 全部在 May 19 之后，按 3 天规则保留

**当前可用空间：根分区 9.8G，数据盘 77G。** 足够跑补实验。

---
