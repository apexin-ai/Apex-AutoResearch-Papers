# code d077 truncation fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d077-truncation-fix_20260514T154149_result.json`
- **Structured JSON:** [`cfcedf64c154f374fdf3.json`](../../sessions/cf/cfcedf64c154f374fdf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改了 westd 服务器上的两个文件：

**eval_repo_verifier.py** 和 **eval_repo_cwm.py** — `--max_seq_length` 和 `--batch_size` 默认值改为 `None`，根据 `--split` 自动设置：
- `test`: max_seq_length=2048, batch_size=16/8 (原默认值不变)
- `val`: max_seq_length=8192, batch_size=2 (truncation 从 20.2% 降到 0.1%)

用户显式指定值时覆盖自动值。所有 dry-run 验证通过。报告写入 `artifacts/d077_fix_report.md`。

---
