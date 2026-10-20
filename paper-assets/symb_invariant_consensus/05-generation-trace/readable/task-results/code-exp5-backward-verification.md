# code exp5 backward verification

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp5-backward-verification_20260518T180900_result.json`
- **Structured JSON:** [`2e622a812dfac99b1822.json`](../../sessions/2e/2e622a812dfac99b1822.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 验证报告

### 检查项全部通过

| 检查项 | 结果 |
|--------|------|
| python3 + z3 import | z3 v4.15.4 |
| openai import | OK |
| 数据文件 `folio_full.json` | 204 problems |
| 模型路径 `Qwen2.5-14B-Instruct` | 存在 |
| 已有 traces 目录 | 204 files |
| FOL 解析 (4 条 premise) | 4/4 parsed |
| Z3 SAT 检查 (premises satisfiable) | sat |
| Z3 UNSAT 检查 (Inactive(x)∧Students(x) 与 premises 矛盾) | unsat |
| Z3 entailment | Unknown (正确) |
| `parse_problem_text` | OK |
| `_parse_response` (含 code block) | OK |
| `normalize_logic_answer` | OK |
| SC baseline 计算 | 0.75 |
| 1-problem K=1 端到端 pipeline (Mistral-7B) | 3.5s, 得到 True=2/False=1/Unknown=-1 的区分性打分 |

### 产出文件

- **主脚本**: `/root/symb_invariant_consensus/backward_verification.py` (634 行)
- **启动脚本**: `/root/symb_invariant_consensus/scripts/run_backward_verification.sh`
- **输出目录**: `results/exp05_backward_verification/` (已创建)

### 运行命令

```bash
bash scripts/run_backward_verification.sh 0 8000
```

当前 port 8000 运行的是 Mistral-7B, 启动脚本会自动检测并启动 Qwen2.5-14B (如果端口被占用需先停掉 Mistral 或换端口)。

---
