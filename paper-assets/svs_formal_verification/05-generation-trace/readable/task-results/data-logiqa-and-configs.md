# data logiqa and configs

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_logiqa_and_configs_20260514T083300_result.json`
- **Structured JSON:** [`c15c9d4d4d812e232d86.json`](../../sessions/c1/c15c9d4d4d812e232d86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### LogiQA 数据集
- **来源**：GitHub `lgw863/LogiQA-dataset`（HF `lucasmccabe/logiqa` 因脚本格式已废弃无法使用）
- **格式**：纯文本，空行分隔块，每块 = 答案字母(a-d) + 上下文 + 问题 + 4 个选项(A-D)
- **大小**：test 651 题，train 7376 题，eval 651 题
- **存储路径**：`/root/autodl-tmp/data/logiqa/{Test,Train,Eval}.txt`

### Loader 函数
- `load_logiqa(subset, num_problems, seed)` 已添加到 `data/loader.py`
- Problem 映射：`premises=[context]`, `hypothesis=question`, `label=A/B/C/D`, `raw` 含完整 options
- `load_problems()` 统一入口已支持 `dataset="logiqa"`
- 已部署到服务器并验证 5 条样本加载正确

### 配置模板

| 文件 | dataset | num_problems | num_chains | output_dir |
|------|---------|-------------|------------|------------|
| `config_folio.yaml` | folio/validation | 204 | 10 | outputs_folio |
| `config_proofwriter_full.yaml` | proofwriter/depth-5 | 600 | 10 | outputs_proofwriter_full |
| `config_logiqa.yaml` | logiqa/test | 1000 | 10 | outputs_logiqa |

三个配置文件已写入本地 artifacts 和远程 `/root/svs_pipeline/`。

---
