# ops submit mistral docred westd21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_mistral_docred_westd21461_20260516T052351_result.json`
- **Structured JSON:** [`6e91c2050f9dc64436fc.json`](../../sessions/6e/6e91c2050f9dc64436fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已提交并确认运行中。

## 提交状态汇报

| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| w6_mistral_docred_unconstrained | 5576 | cuda:0 (15.3GB/98GB) | 22/998 samples | RUNNING ✓ |
| w6_mistral_docred_constrained | 6794 | cuda:1 (15.3GB/98GB) | 6/998 samples | RUNNING ✓ |

- 服务器: westd-21461, 2x NVIDIA RTX PRO 6000 Blackwell (98GB each)
- GPU 利用率: GPU0 89%, GPU1 86%
- 输出文件: `outputs/w6_mistral_docred_unconstrained.jsonl` (152KB), `outputs/w6_mistral_docred_constrained.jsonl` (40KB)
- Constrained 实验比 unconstrained 慢属正常（grammar 编译 96 relation types）
- Registry 已更新为 RUNNING

注意: tmux sessions 已不存在（清理冲突时丢失），但两个 python 进程均通过 nohup 后台运行，不受 SSH 断连影响。日志: unconstrained → `/tmp/w6_mistral_docred_unconstrained.log`, constrained → `/tmp/w6_mistral_docred_constrained.log`。

---
