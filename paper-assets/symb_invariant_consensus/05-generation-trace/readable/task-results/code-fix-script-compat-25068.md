# code fix script compat 25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-script-compat-25068_20260518T080607_result.json`
- **Structured JSON:** [`97378f560b27fe4a31d9.json`](../../sessions/97/97378f560b27fe4a31d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。总结：

### 修改的文件
**`/root/symb_invariant_consensus/run_full_mvp.py`** (服务器 westd-25068)

### 新增的 5 个 argparse 参数
| 参数 | 类型 | 默认值 | 作用 |
|------|------|--------|------|
| `--temperature` | float | 0.7 | 传递给 VLLMGenerator/APIGenerator |
| `--max-tokens` | int | 4096 | 传递给 VLLMGenerator/APIGenerator |
| `--seed` | int | None | 设置 Python random seed |
| `--folio-data` | str | None | FOLIO 数据集路径 |
| `--save-intermediates` | flag | False | 保存每题的 sica_result 到 intermediates/ |

### 其他修改
- `load_all_problems()` 增加可选 `folio_path` 参数，加载 FOLIO 数据并标记 `dataset="folio"`
- `build_generator()` 将 temperature/max_tokens 从 args 传递给生成器（之前硬编码为默认值）
- **新增 per-problem domain 切换**：proofwriter/folio 使用 `domain="logic"`（逻辑约束提取 prompt），math 使用 `domain="math"`

### dry-run 验证结果
- `--help` 输出包含全部新参数
- 两个实验脚本 (`run_exp024_llama70b.sh`, `run_exp025_qwen72b.sh`) 语法检查通过
- mock 模式端到端运行：成功加载 0 MATH + 600 ProofWriter + 204 FOLIO = 804 题
- intermediates 目录正常创建

### 数据加载方式
实验脚本用 `--math-data data/empty.json`（空数组）跳过 MATH，`--pw-data data/proofwriter_full.json` 加载 600 题，`--folio-data data/folio_full.json` 加载 204 题，合计 804 题在一次运行中处理。

---
