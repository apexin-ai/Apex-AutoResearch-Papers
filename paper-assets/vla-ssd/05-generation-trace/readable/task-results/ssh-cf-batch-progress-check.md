# ssh cf batch progress check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cf_batch_progress_check_20260521T231902_result.json`
- **Structured JSON:** [`90bfde413709e69fdffa.json`](../../sessions/90/90bfde413709e69fdffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`libero_long_untrained` 是旧的 MSE 方法结果（非 cosine_distance），来自之前的 openvla 实验，不可直接比较。

## 综合报告

### 1. 当前进度

**Batch 1 (cf_batch_missing_v1, cuda:0)**
| # | Task | Status |
|---|------|--------|
| 1 | openvla object untrained | ✅ 完成 (27.6 min) |
| 2 | tracvla spatial untrained | 🔄 condition "wrong" 4800/5000 (96%) |
| 3 | tracvla object untrained | ⏳ 未开始 |

**Batch 2 (cf_batch_part2_v1, cuda:1)**
| # | Task | Status |
|---|------|--------|
| 1 | tracvla goal untrained | 🔄 2/4 conditions done, "shuffled" 刚开始 |
| 2 | tracvla long untrained | ⏳ 未开始 |

Batch 2 中间结果 (tracvla goal untrained):
- wrong: cos_dist = **0.0160**
- empty: cos_dist = **0.1530**

---

### 2. 已完成结果：OpenVLA Object Untrained (cosine_distance, last layer L31)

| Condition | cos_dist | Cohen's d |
|-----------|----------|-----------|
| empty | **0.5688** | — |
| shuffled | **0.2981** | — |
| wrong | **0.2308** | 5.57 |
| paraphrased | **0.0845** | — |

排序：empty >> shuffled > wrong >> paraphrased

---

### 3. 预计剩余时间

TracVLA 每个 condition 约 **8 min**（5000 samples）。

- **Batch 1**: ~25 min (spatial 剩余 3 conditions) + ~32 min (object 4 conditions) = **~57 min**
- **Batch 2**: ~16 min (goal 剩余 2 conditions) + ~32 min (long 4 conditions) = **~48 min**

预计全部完成时间：约 **08:10 (batch 2)** / **08:17 (batch 1)**（服务器时间 UTC+8）。

---

### 4. 注意

已有的 `libero_long_untrained/counterfactual_combined.json` 使用旧的 paired_mse 方法（`model=openvla-7b-finetuned-libero-object`），不是当前 cosine_distance 方法的结果。Batch 2 会产出新的 tracvla long untrained cosine_distance 结果。

---
