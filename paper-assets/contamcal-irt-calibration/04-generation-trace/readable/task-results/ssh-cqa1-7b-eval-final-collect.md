# ssh cqa1 7b eval final collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cqa1-7b-eval-final-collect_20260519T050408_result.json`
- **Structured JSON:** [`fe587c06a146dbce1f7a.json`](../../sessions/fe/fe587c06a146dbce1f7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**10/10 Qwen2.5-7B eval 全部完成**（所有目录都有 `.done` 标记）。结果汇总：

| Adapter | MMLU | ARC |
|---------|------|-----|
| **d000_s42** | 0.6929 | 0.8959 |
| **d005_s42** | 0.6924 | 0.8968 |
| **d025_s42** | 0.7003 | 0.8985 |
| **d050_s42** | 0.7050 | 0.8993 |
| **d100_s42** | 0.7103 | 0.8933 |
| **d000_s123** | 0.6978 | 0.8985 |
| **d005_s123** | 0.6932 | 0.8985 |
| **d025_s123** | 0.7025 | 0.8993 |
| **d050_s123** | 0.7034 | 0.8993 |
| **d100_s123** | 0.7072 | 0.8968 |

趋势：
- **MMLU**：contamination dose 越高分数越高（d000 ~0.693 → d100 ~0.710），符合预期
- **ARC**：几乎不受 contamination 影响，稳定在 0.893-0.899，说明 contamination 效应具有 benchmark 特异性
- 两个 seed 间结果一致性好

PID 161500 仍在 GPU 0 上运行（d000_s123_aligned 的 4-benchmark 扩展 eval），但 MMLU+ARC 的 aligned eval 已全部完成。

---
