# code analysis scripts prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis_scripts_prep_20260514T173835_result.json`
- **Structured JSON:** [`a6f42d3d70656ad8cc8b.json`](../../sessions/a6/a6f42d3d70656ad8cc8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

目录存在但为空——s030 importance 实验还在跑。

三个脚本 dry-run 全部成功：

| 脚本 | 状态 |
|------|------|
| `validate_data_integrity.py` | 26 PASS，1 FAIL（dryrun 目录，n=3 正常） |
| `analyze_c2_n500.py --n50-only` | 成功，输出 3 个文件（_dryrun 后缀） |
| `analyze_c3_llama.py` | 成功，s015/s020/s025 已分析，s030 待数据 |

产出文件：
- `/root/autodl-tmp/pacs/analyze_c2_n500.py` — 已有，512 行
- `/root/autodl-tmp/pacs/analyze_c3_llama.py` — 已有，431 行，已生成正式结果
- `/root/autodl-tmp/pacs/validate_data_integrity.py` — 新写，分层错误/警告检测

c2_n500 的 16 个 n=500 目录目前都是空的（实验在跑），数据就绪后直接 `python analyze_c2_n500.py` 即可。c3_llama 还差 s030 importance 一个 condition。

---
