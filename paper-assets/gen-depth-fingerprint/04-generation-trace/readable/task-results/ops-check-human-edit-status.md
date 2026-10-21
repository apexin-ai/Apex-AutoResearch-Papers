# ops check human edit status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-human-edit-status_20260515T211920_result.json`
- **Structured JSON:** [`34641c1a75459a5b34a0.json`](../../sessions/34/34641c1a75459a5b34a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。汇总：

## plan-010 human-edit 实验结果

**状态：已完成** (总耗时 167 分钟，结果写入于 2026-05-16 02:51)

| Condition | 3-class LOGO F1 | Binary F1 | Δ LOGO F1 | Δ Binary F1 |
|-----------|:-:|:-:|:-:|:-:|
| baseline | **0.7889** [.787, .798] | **0.7241** [.719, .734] | — | — |
| random_5pct | 0.7538 [.750, .764] | 0.7182 [.713, .729] | −0.0351 | −0.0059 |
| random_10pct | 0.7425 [.735, .752] | 0.7168 [.711, .729] | −0.0464 | −0.0073 |
| random_20pct | 0.7292 [.722, .739] | 0.7165 [.711, .727] | −0.0597 | −0.0076 |
| llm_rephrase | 0.7549 [.750, .762] | 0.6615 [.655, .672] | −0.0340 | −0.0626 |

**结论：**
- **degradation_curve = robust** — 随机替换 5%→20% token，3-class F1 从 0.789 graceful 降到 0.729（−7.6%），没有断崖式下跌
- **llm_rephrase_robust = True** — LLM 改写后 3-class F1 仅降 0.034，depth fingerprint 在表面文本改写下保持鲁棒
- Binary F1 在 random 条件下几乎不受影响（−0.006~−0.008），但 llm_rephrase 下降较多（−0.063），说明 LLM 改写对 human-vs-machine 二分类的影响大于对 generator attribution 的影响

**进程状态：**
- PID 223500 (human_edit_robustness.py) — 已退出
- PID 228872 (wait_and_rerun.sh) — 仍在运行（已跑 4h8m），可能在等待某个条件或已完成主任务在空转

**cuda:1 状态：空闲** — 利用率 0%，显存占用仅 627 MiB / 32607 MiB

---
