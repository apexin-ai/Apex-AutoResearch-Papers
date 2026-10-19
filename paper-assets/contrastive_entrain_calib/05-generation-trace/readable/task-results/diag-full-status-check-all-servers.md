# diag full status check all servers

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_full-status-check-all-servers_20260519T062307_result.json`
- **Structured JSON:** [`8df935a37a2158d57813.json`](../../sessions/8d/8df935a37a2158d57813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

---

### westd-29046 (2× RTX PRO 6000 Black, 98GB each)

| 实验 | GPU | PID | Step | 进度 | 速度 | VRAM | GPU% |
|------|-----|-----|------|------|------|------|------|
| **exp-002v2** | 0 | 130467 | 521/8000 | 6.5% | ~30s/step | 63.6/97.9 GB | 98% |
| **exp-003** | 1 | 70649 | 1714/8000 | 21.4% | ~30s/step | 38.2/97.9 GB | 95% |

**exp-002v2 (DC-GRPO cosine)**
- R1 持续在零附近波动，无学习趋势（最近10步: -0.06 ~ +0.003）
- Per-strength R1 (step 519): weak=0.011, medium=-0.063, strong=-0.046 → 三个强度全部接近零
- R3 波动较大 (0.44~0.86)，combined 0.32~0.64
- checkpoint-500 已保存（LoRA adapter 245MB）
- 预计完成：~May 22 凌晨（~62h）

**exp-003 (R3-only)**
- `d_syc not loaded` 警告持续出现，仅 R3 reward 生效
- R3 波动 (0.35~0.87)，step 1710 统计: mean=0.87, std=0.34
- 预计完成：~May 21 下午（~51h）

---

### westd-28034 (4× RTX 5090, 32GB each)

| 实验 | GPU | PID | Step | 进度 | 速度 | VRAM | GPU% |
|------|-----|-----|------|------|------|------|------|
| **exp-004** | 0 | 18204 | 5700/8000 | 71.3% | ~88s/10step | 21.8/32.6 GB | 45% |
| **exp-014** | 1+2 | 40314/40315 | 3243/8000 | 40.5% | ~10s/step | 31.4+30.6 GB | 71%+77% |
| — | 3 | — | — | — | — | 4 MB | 0% (idle) |

**exp-004 (ACT baseline)**
- 稳定训练中，sft=0.0, l2≈0.001, lr 从 1.65e-5 缓降
- checkpoint-5500 已保存
- 预计完成：**~今晚 20:00**（~5.6h）

**exp-014 (continuous probe, DeepSpeed 2-GPU)**
- R1 波动极大 (0.25~0.999)，R2 恒为 0，R3 几乎饱和 (~0.999)
- Combined 0.81~0.999
- 已有 checkpoint: 500/1000/1500/2000/2500/3000
- 预计完成：~May 20 03:30（~13h）

**GPU 3**: 空闲，exp-016 已结束，无进程占用。

---

### 关注点
1. **exp-002v2 R1 不学习**：520步了 R1 仍在零附近，per-strength 三类全无提升，可能需要诊断
2. **exp-003 d_syc 未加载**：一直是 R3-only 模式，确认是否符合预期
3. **exp-014 R2 恒为 0**：R2 reward 完全不起作用
4. **GPU 3 空闲**：可安排新实验

---
