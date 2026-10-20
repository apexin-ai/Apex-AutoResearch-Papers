# experiment mvp v2 check

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_v2_check_20260513T115322_result.json`
- **Structured JSON:** [`e8ba5d2be9aefeb0194e.json`](../../sessions/e8/e8ba5d2be9aefeb0194e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## MVP v2 实验状态：两组均已完成，Verdict 均为 KILL

GPU 空闲（0% utilization），进程已结束，80/80 traces 全部评估完成。

---

### CR70（压缩率 0.7）

| | full | uniform_ea | turnkv | diff (turnkv − uniform_ea) |
|---|---|---|---|---|
| **Standard KIRR** | 0.1676 | 0.0471 | 0.0784 | **+3.1 pp** |
| **Standard PPL** | 11.80 | 20.37 | 41.40 | **ppl_ratio = 2.03x** |
| **Adversarial KIRR** | 0.1085 | 0.0039 | 0.0 | **−0.4 pp** |
| **Adversarial PPL** | 14.05 | 25.38 | 35.21 | ppl_ratio = 1.39x |
| **Overall KIRR** | 0.144 | 0.0299 | 0.047 | **+1.7 pp** |
| **Overall PPL** | 12.70 | 22.38 | 38.92 | **ppl_ratio = 1.74x** |

MVP: KIRR pass = **false**, PPL pass = **false** → **KILL**

---

### CR85（压缩率 0.85）

| | full | uniform_ea | turnkv | diff (turnkv − uniform_ea) |
|---|---|---|---|---|
| **Standard KIRR** | 0.1676 | 0.0344 | 0.0358 | **+0.1 pp** |
| **Standard PPL** | 11.80 | 23.17 | 59.46 | **ppl_ratio = 2.57x** |
| **Adversarial KIRR** | 0.1085 | 0.0 | 0.0 | **0.0 pp** |
| **Adversarial PPL** | 14.05 | 27.65 | 58.11 | ppl_ratio = 2.10x |
| **Overall KIRR** | 0.144 | 0.0206 | 0.0215 | **+0.1 pp** |
| **Overall PPL** | 12.70 | 24.96 | 58.92 | **ppl_ratio = 2.36x** |

MVP: KIRR pass = **false**, PPL pass = **false** → **KILL**

---

### 关键发现

- **TurnKV 的 KIRR 优势微弱**：CR70 overall 仅 +1.7pp，CR85 几乎为零（+0.1pp）
- **TurnKV 的 PPL 代价巨大**：CR70 下 turnkv PPL 是 uniform_ea 的 1.74x，CR85 下是 2.36x——PPL 劣化严重
- **Adversarial 场景全面失败**：CR70 adversarial turnkv KIRR = 0（比 uniform_ea 的 0.0039 还低），CR85 两者都为 0
- 两个压缩率下 MVP verdict 均为 **KILL**，KIRR 和 PPL 两项都未通过

---
