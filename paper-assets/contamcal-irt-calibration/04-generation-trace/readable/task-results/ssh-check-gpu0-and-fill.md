# ssh check gpu0 and fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gpu0-and-fill_20260513T222425_result.json`
- **Structured JSON:** [`ffe3dd831fd7646e2d7d.json`](../../sessions/ff/ffe3dd831fd7646e2d7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## 全部 6 GPU 状态

| GPU | Util | 显存 (used/total) | 实验 / PID | 运行时间 |
|-----|------|--------------------|-----------|---------|
| **0** | **100%** | **23890/24564 MiB** | MMLU paraphrase gen (PID 204472 + vLLM 223768) | 3h10m |
| **1** | 0% | 0/24564 MiB | **空闲** | — |
| **2** | 0% | 0/24564 MiB | **空闲** | — |
| **3** | 46% | 17327/24564 MiB | 3B d000 s123 训练 (PID 216254) | 1h43m |
| **4** | 53% | 5829/24564 MiB | 1.5B d000 s42 评估 (PID 221376) | 54m |
| **5** | 30% | 18665/24564 MiB | 3B d000 s42 训练 (PID 210671) | 2h40m |

## GPU 0 状态

**GPU 0 被占用**——MMLU paraphrase 生成进度 **58% (304/526)**，预计还需 ~20 分钟。vLLM 引擎占 22832 MiB。

## d005 数据状态

- `sft_dosage_005.jsonl` 存在（50124 行，88MB，生成于 04:17）
- **mmlu_paraphrases.json 不存在**（正在生成中）
- 已有 paraphrases：arc_challenge、gsm8k、humaneval
- d005 内容为通用 SFT 数据，**缺 MMLU contamination 数据**

## 操作结果

**采取情况 C**：GPU 0 仍被 MMLU paraphrase 占用，不做任何操作。

MMLU paraphrase 完成后（~20min），GPU 0 将释放。届时需要：
1. 用 MMLU paraphrases 重新生成 d005 数据
2. 再启动 0.5B d005 s42 训练

---
