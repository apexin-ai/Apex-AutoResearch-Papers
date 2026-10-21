# m103 verify spatial baseline westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_m103_verify_spatial_baseline_westd27271_20260525T012523_result.json`
- **Structured JSON:** [`8378c2506a428e3e4d19.json`](../../sessions/83/8378c2506a428e3e4d19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. Spatial Baseline ✓ 已确认
- **SR: 80.0% (400/500)**
- 模型路径: `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial` — 正确的 suite-specific finetuned 模型
- seed=42, 10 tasks × 50 episodes
- Registry 已更新

### 2. L2norm k=0.9 实验（进行中）
两个 GPU 都在跑（74%/65% utilization, ~16GB each）：

| 实验 | 进度 | 已完成 tasks 累计 SR | ETA |
|------|------|---------------------|-----|
| **Spatial** | 7/10 tasks done, Task 8 running | 263/350 (75.1%) | ~60 min |
| **Goal** | 6/10 tasks done, Task 7 running | 208/300 (69.3%) | ~80 min |

模型加载确认：
- Spatial: `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial` + `[*] L2 norm pruning: k=0.9`
- Goal: `/root/autodl-tmp/openvla-7b-finetuned-libero-goal` + `[*] L2 norm pruning: k=0.9`

### 3. Attn k=0.9 实验 ✓ 已完成
| Suite | SR | 模型 |
|-------|-----|------|
| **Goal** | 73.2% (366/500) | `openvla-7b-finetuned-libero-goal` ✓ |
| **Spatial** | 80.4% (402/500) | `openvla-7b-finetuned-libero-spatial` ✓ |

两个 Attn 实验均使用正确的 suite-specific 模型，`[*] Attention pruning: k=0.9` 确认了方法。

### 对比速览（Spatial suite）
| Method | SR |
|--------|-----|
| Baseline | **80.0%** |
| Attn k=0.9 | **80.4%** (+0.4%) |
| L2norm k=0.9 | ~75% (预估，待完成) |

---
