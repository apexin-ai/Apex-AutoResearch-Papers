# diagnose pilot contrastive prompt

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pilot-contrastive-prompt_20260517T064455_result.json`
- **Structured JSON:** [`370208c327629dc5b7fd.json`](../../sessions/37/370208c327629dc5b7fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。诊断结果：

| 项目 | 结果 |
|------|------|
| **日志中的确切错误** | `bash: line 1: python: command not found` → EXIT_CODE=127 |
| **脚本是否存在** | 存在，22650 bytes，路径 `/root/symb_invariant_consensus/scripts/pilot_contrastive_constraints.py` |
| **正确的启动命令** | `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/symb_invariant_consensus && python scripts/pilot_contrastive_constraints.py` |
| **dry-run 是否通过** | 通过，Python 3.12.3 at `/root/miniconda3/bin/python` |

根因：原始命令未激活 conda 环境，裸 shell 中 `python` 不在 PATH。修复方式是在命令前加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base &&`。

---
