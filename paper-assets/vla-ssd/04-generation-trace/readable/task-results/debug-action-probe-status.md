# debug action probe status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_action_probe_status_20260517T155241_result.json`
- **Structured JSON:** [`06057b269ffa8610ea16.json`](../../sessions/06/06057b269ffa8610ea16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是完整报告：

---

## 1. 进程状态
`l1_ablation_action_probe` **无运行进程**（已结束）。

## 2. 结果文件
`action_probe_results.json` — 9213 bytes，生成于 **May 17 23:08**。

## 3. Action Probe R² 完整结果

### 汇总（mean_R²）

| Condition | L1 | L8 | L13 |
|---|---|---|---|
| **baseline** | 0.2558 | 0.4401 | 0.5240 |
| **ablate_all24** | 0.3627 (+0.107) | 0.4496 (+0.010) | 0.5194 (−0.005) |
| **ablate_all32** | 0.3747 (+0.119) | 0.4449 (+0.005) | 0.5184 (−0.006) |

### Detailed — baseline

**L1** (mean=0.2558, overall=0.3857, epochs=50):
- per_dim: [0.4238, 0.3276, 0.2074, 0.2759, 0.3123, 0.5627, 0.4338]
- per_task: open middle drawer 0.1971, open top drawer+bowl 0.2649, push plate 0.1901, bowl on plate 0.3754, bowl on stove 0.2352, bowl on cabinet 0.2561, cream cheese in bowl 0.1860, wine on rack 0.1894, wine on cabinet 0.2789, turn on stove 0.3854

**L8** (mean=0.4401, overall=0.5241, epochs=27):
- per_dim: [0.5479, 0.5721, 0.3590, 0.5499, 0.2719, 0.6670, 0.5588]
- per_task: open middle drawer 0.4532, open top drawer+bowl 0.3757, push plate 0.3358, bowl on plate 0.4371, bowl on stove 0.3960, bowl on cabinet 0.4519, cream cheese in bowl 0.3797, wine on rack 0.3917, wine on cabinet 0.4624, turn on stove 0.7171

**L13** (mean=0.5240, overall=0.6061, epochs=18):
- per_dim: [0.5870, 0.6881, 0.4503, 0.5939, 0.2486, 0.6611, 0.6437]
- per_task: open middle drawer 0.5686, open top drawer+bowl 0.5466, push plate 0.4092, bowl on plate 0.3887, bowl on stove 0.5352, bowl on cabinet 0.6587, cream cheese in bowl 0.5835, wine on rack 0.4304, wine on cabinet 0.3856, turn on stove 0.7336

### Detailed — ablate_all24

**L1** (mean=0.3627, overall=0.4805, epochs=50):
- per_dim: [0.4962, 0.4212, 0.3563, 0.3820, 0.3174, 0.6372, 0.5189]
- per_task: open middle drawer 0.2211, open top drawer+bowl 0.3403, push plate 0.1968, bowl on plate 0.4740, bowl on stove 0.3950, bowl on cabinet 0.4567, cream cheese in bowl 0.3454, wine on rack 0.4240, wine on cabinet 0.3529, turn on stove 0.4213

**L8** (mean=0.4496, overall=0.5364, epochs=33):
- per_dim: [0.5406, 0.5977, 0.3770, 0.5583, 0.2681, 0.6702, 0.5718]
- per_task: open middle drawer 0.3808, open top drawer+bowl 0.3880, push plate 0.3505, bowl on plate 0.4295, bowl on stove 0.4430, bowl on cabinet 0.4702, cream cheese in bowl 0.4111, wine on rack 0.3958, wine on cabinet 0.4901, turn on stove 0.7365

**L13** (mean=0.5194, overall=0.6053, epochs=16):
- per_dim: [0.6025, 0.6668, 0.4552, 0.5792, 0.2541, 0.6685, 0.6408]
- per_task: open middle drawer 0.4178, open top drawer+bowl 0.5401, push plate 0.4578, bowl on plate 0.3919, bowl on stove 0.5135, bowl on cabinet 0.6405, cream cheese in bowl 0.5285, wine on rack 0.3943, wine on cabinet 0.4917, turn on stove 0.8184

### Detailed — ablate_all32

**L1** (mean=0.3747, overall=0.4920, epochs=50):
- per_dim: [0.5003, 0.4346, 0.3441, 0.3893, 0.2718, 0.6236, 0.5387]
- per_task: open middle drawer 0.1426, open top drawer+bowl 0.3482, push plate 0.2116, bowl on plate 0.4781, bowl on stove 0.3982, bowl on cabinet 0.4722, cream cheese in bowl 0.3489, wine on rack 0.4197, wine on cabinet 0.3900, turn on stove 0.5379

**L8** (mean=0.4449, overall=0.5301, epochs=33):
- per_dim: [0.5404, 0.6055, 0.3632, 0.5476, 0.2741, 0.6614, 0.5644]
- per_task: open middle drawer 0.3953, open top drawer+bowl 0.3704, push plate 0.3693, bowl on plate 0.4327, bowl on stove 0.4237, bowl on cabinet 0.4573, cream cheese in bowl 0.4089, wine on rack 0.4087, wine on cabinet 0.4746, turn on stove 0.7081

**L13** (mean=0.5184, overall=0.6029, epochs=18):
- per_dim: [0.5884, 0.6840, 0.4604, 0.5730, 0.2161, 0.6815, 0.6361]
- per_task: open middle drawer 0.5962, open top drawer+bowl 0.5647, push plate 0.4236, bowl on plate 0.3524, bowl on stove 0.5306, bowl on cabinet 0.6513, cream cheese in bowl 0.5582, wine on rack 0.4244, wine on cabinet 0.3537, turn on stove 0.7290

### Metadata
- Probe: MLP(4096, 256, 7)
- Optimizer: Adam lr=0.001, epochs=50, patience=5, batch=256, seed=42
- Target: next_action a_{t+1} from feature at time t
- Normalization: z-score (train mean/std)
- Split: 80/20 per-task by demo index (n_train=5312, n_val=1294)
- Readout layers: [1, 8, 13], demos_per_task=5, n_tasks=10
- Checkpoint: openvla-7b
- instruction_heads_24: [0,1,2,4,7,8,10,11,12,14,15,16,17,18,19,20,22,23,25,26,27,29,30,31]

## 5. GPU 状态
2× NVIDIA RTX PRO 6000 Black (98GB each), 均空闲（0% util, 0MiB memory, 28-29°C）。

---

**关键发现**：ablation 后 L1 的 action R² 显著上升（+0.107/+0.119），但 L8 和 L13 几乎不变。移除 instruction heads 后 L1 的 action 信息反而增加，说明这些 heads 在 L1 主要承载 instruction 信息而非 action 信息，ablation 释放了 capacity 给 action 编码。深层 action 表征不受影响。

---
