# diag d176 urgent status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d176-urgent-status_20260520T092319_result.json`
- **Structured JSON:** [`c2d94e1a128d6ec182d7.json`](../../sessions/c2/c2d94e1a128d6ec182d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### Qwen-14B s123 GSM8K
- **PID 309330**: 活着，cuda:1 占 33.6GB，95% 利用率
- **d000**: 已完成，accuracy = **76.65%** (1011/1319) — 与参考值一致
- **d100**: 正在跑，**85% (141/165 batches)**，~14s/batch，预计还需 **~5-6 分钟**
- Δ(d100-d000) 待 d100 完成后计算（参考 s42: Δ=20.47pp）

### Gemma-2 d100 fixed
- **PID 307190**: 已结束（不在 nvidia-smi 中）
- 结果文件已生成（含 `.done` 标记）
- **accuracy = 3.94% (52/1319)** — 几乎全是 `pred: null`

**严重异常**: Gemma-2 d100 accuracy 仅 3.94%，绝大多数预测为 null，说明答案提取完全失败或模型输出格式不对。需要排查 evaluate.py 对 Gemma-2 的兼容性。

### GPU 总览
| GPU | 进程 | 状态 |
|-----|------|------|
| cuda:0 | PID 302132 (Phi-4 s0) | 活跃，57.3GB，75% |
| cuda:1 | PID 309330 (Qwen-14B s123 d100) | 活跃，33.6GB，95% |
| cuda:2 | PID 306129 (OLMo-2 s0) | 活跃，66.5GB，93% |
| **cuda:3** | — | **空闲** |

---
