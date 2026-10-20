# ssh v7 eval extract and llama launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v7_eval_extract_and_llama_launch_20260522T002825_result.json`
- **Structured JSON:** [`76f7ae7b99e9d804785e.json`](../../sessions/76/76f7ae7b99e9d804785e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中，一切正常。

---

**全部完成。汇总：**

**eval_v7_tg_s123 结果** (raw GAR, M020):

| Metric | s123 | s42 | Delta |
|--------|------|-----|-------|
| TF GAR-ours (mid) | 0.5052 | 0.5035 | +0.0017 |
| TF GAR-dongre (mid) | 0.0119 | - | - |
| TF PPL | 2.7802 | 2.784 | -0.004 |
| AR GAR-ours (mid) | 0.0165 | 0.0157 | +0.0008 |
| AR GAR-dongre (mid) | 0.0177 | 0.0194 | -0.0017 |
| AR PPL | 1.3855 | 1.36 | +0.026 |
| **Gap ratio** | **30.6×** | **~32×** | -1.4× |

Multi-seed robustness 确认：s123 与 s42 各指标高度一致，gap ratio 30.6× 在 20-40× 范围内。

**llama_lora_only_s42** 已提交到 westd-20861 cuda:0，PID=271741，tmux session `llama_lora_only_s42`。Registry 和 plan_011 已关联。

---
