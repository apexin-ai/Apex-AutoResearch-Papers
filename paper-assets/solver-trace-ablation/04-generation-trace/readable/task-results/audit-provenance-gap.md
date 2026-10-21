# audit provenance gap

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_provenance-gap_20260515T140834_result.json`
- **Structured JSON:** [`b8acceceab81599f596e.json`](../../sessions/b8/b8acceceab81599f596e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。24 个 success 实验的 provenance 已全部补全（原 18/24 → 24/24）：

- **5 个 SFT 实验** (`plan009-sft-baseline-s43/s44/s43-1000/s44-1000/s44-1000-r3`)：从 `reproduce.command` 提取 `data_path`, `data_count`, `model_name`, `seed` 补入 spec
- **1 个 GRPO 实验** (`exp1-isr-b03-s43`)：从同系列实验推断 `log_path` 路径模式补入

报告已注册为 artifact `art_20260515_f3c732`。

---
