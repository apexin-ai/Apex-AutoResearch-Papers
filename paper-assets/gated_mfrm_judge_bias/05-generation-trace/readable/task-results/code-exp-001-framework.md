# code exp 001 framework

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001_framework_20260521T231703_result.json`
- **Structured JSON:** [`d374ee897567ffdc3985.json`](../../sessions/d3/d374ee897567ffdc3985.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 结果

| 文件 | 行数 | 说明 |
|------|------|------|
| `judge_interface.py` | 229 | 统一 judge 接口 + 6 个 judge 实现 + factory |
| `collect.py` | 186 | 主收集脚本（resume/swap/retry/rate-limit） |
| `data_loader.py` | 74 | Benchmark 数据加载器 |
| `config.yaml` | 23 | 配置文件 |

验证结果：
- 语法检查：✓ 全部通过
- `from judge_interface import get_judge` ：✓ OK

依赖安装：openai、anthropic、google-generativeai 已装入 conda base。

待后续补充：`data/` 目录下的 benchmark prompts 和 model responses JSONL 文件。

---
