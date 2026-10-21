# ops urgent collect results and redeploy all

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-collect-results-and-redeploy-all_20260521T131119_result.json`
- **Structured JSON:** [`f73d3a9e0a1bdce13a2c.json`](../../sessions/f7/f73d3a9e0a1bdce13a2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the full status report:

---

## 完成实验结果

| 实验 | SR | 服务器/GPU |
|------|-----|-----------|
| π0.5 L2norm k=0.5 seed43 | **33.6%** (seed42=33.4%, Δ=+0.2%) | westd-41074/GPU0 |
| X-VLA l2_norm k=0.7 seed42 | **58.2%** | cqa1-33015 |
| X-VLA l2_norm k=0.7 seed43 | **59.0%** | cqa1-33015 |
| X-VLA l2_norm k=0.3 seed43 | **21.0%** | cqa1-33015 |
| X-VLA random k=0.3 seed42 | **62.8%** | cqa1-33015 |
| X-VLA random k=0.3 seed43 | **66.2%** | cqa1-33015 |
| X-VLA random k=0.5 seed43 v2 | **71.0%** | cqa1-33015 |
| X-VLA random k=0.7 seed43 v2 | **65.0%** | cqa1-33015 |
| X-VLA random k=0.7 seed44 | **65.0%** | cqa1-33015 |

**π0.5 L2norm k=0.5 valley 确认**：seed43=33.6% vs seed42=33.4%，差异仅 0.2%，valley 是系统性的。

**X-VLA 关键发现**：l2_norm pruning 对 X-VLA 灾难性 — k=0.3 仅 21%，k=0.7 约 58-59%。而 random pruning 极为 resilient — k=0.3 仍有 63-66%，k=0.7 有 65%，k=0.5 有 71%。

---

## GPU 全局状态

| 服务器 | GPU | 状态 | 实验/PID |
|--------|-----|------|----------|
| westd-41074 | GPU0 | 🟢 RUNNING | π0.5 random k=0.7 seed43 / PID 348268 |
| westd-41074 | GPU1 | 🟢 RUNNING | π0.5 L2norm k=0.7 seed43 v2 / PID 340446 (10h17m) |
| westd-41074 | GPU2 | 🟢 TRAINING | VTC M96 step 59250/100k (59.3%) / PID 68539 (1d9h) |
| westd-41074 | GPU3 | 🟢 TRAINING | VTC M64v6 step 7900/100k (7.9%) / PID 59671 (3h56m) |
| cqa1-33015 | GPU0 | 🟢 RUNNING | X-VLA l2_norm k=0.85 seed43 / PID 358232 (1h09m) |
| cqa1-33015 | GPU1 | 🟢 RUNNING | X-VLA l2_norm k=0.3 seed42 / PID 620896 (**新部署**) |
| cqa1-33015 | GPU2 | 🟢 RUNNING | X-VLA random k=0.85 seed43 / PID 358390 (1h09m) |
| cqa1-33015 | GPU3 | 🟢 RUNNING | X-VLA random k=0.7 seed42 / PID 622585 (**新部署**) |
| westd-27271 | GPU0 | 🟢 RUNNING | OpenVLA L2norm k=0.5 seed43 / PID 250599 (14m) |
| westd-27271 | GPU1 | 🟢 TRAINING | M32 resume step 59200/100k (59.2%) / PID 921279 (1d2h) |

---

## 新部署

| 实验 | 服务器/GPU | PID |
|------|-----------|-----|
| π0.5 random k=0.7 seed43 | westd-41074/GPU0 | 348268 |
| X-VLA l2_norm k=0.3 seed42 | cqa1-33015/GPU1 | 620896 |
| X-VLA random k=0.7 seed42 | cqa1-33015/GPU3 | 622585 |

全 10 GPU 满载。cqa1 无 `eval_pi05_pruning_libero.py`，故 GPU1/3 部署 X-VLA 多 seed 补充实验。

---
