# analysis pi05 object baseline harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-object-baseline-harvest_20260521T114130_result.json`
- **Structured JSON:** [`3fc4c7ca75372ead1a0b.json`](../../sessions/3f/3fc4c7ca75372ead1a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**3 个 seed 全部 0.0% SR (0/600 rollouts)**，这是异常结果。

### 关键发现

| | bjb1-32546 (本次) | bjb2-40593 (quick verify) |
|---|---|---|
| Overall SR | **0.0%** | **72%** |
| 每个 task | 全 0% | 40%-100% |
| 总 rollouts | 600 | 50 |

### 排查结果
代码 (pi05_wrapper.py, evaluate.py)、模型权重 (7.47GB)、normalizer、config.json、PyTorch 2.10.0+cu128、lerobot 0.5.2、transformers 5.8.0 — **两台服务器完全一致**。SmolVLA 在 bjb1-32546 正常工作 (12% SR)，排除环境/LIBERO 问题。

Spatial benchmark 同样 0%，确认是 π0.5 在 bjb1-32546 上的系统性问题。

### 根因未知，建议紧急操作
1. **在 bjb2-40593 上重跑 π0.5 全量 eval** — 那里 72% 已验证，这是最快拿到可用数据的路径
2. 对比两台服务器的 GPU 型号（`nvidia-smi`）— 可能是 bfloat16 数值行为差异
3. 添加 action value logging，对比两台服务器的模型输出

Registry 已更新 (conclusion=failed, notes=ANOMALY)，report 已注册为 artifact。

---
