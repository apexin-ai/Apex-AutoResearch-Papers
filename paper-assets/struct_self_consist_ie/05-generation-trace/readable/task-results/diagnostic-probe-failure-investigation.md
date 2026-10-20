# diagnostic probe failure investigation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_probe_failure_investigation_20260518T123802_result.json`
- **Structured JSON:** [`2f6867ed83cdd07bd506.json`](../../sessions/2f/2f6867ed83cdd07bd506.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败根因：实验在 PREPARING 阶段就失败了，Worker 未能完成准备工作。** 具体缺失如下：

### 缺失的前置条件

1. **没有 CoNLL 版本的 hidden state 提取脚本**
   - 现有提取脚本只有 SciERC (`extract_hidden_states.py`)、FewNERD (`extract_hidden_states_fewnerd.py`) 和 exp016 版
   - 没有 `extract_hidden_states_conll.py`

2. **没有 CoNLL 版本的探针脚本**
   - `hidden_state_probe_v2.py` 硬编码指向 SciERC 数据：
     - `DATA_DIR = ".../output/hidden_state_probe"` (SciERC)
     - `SAMPLES_PATH = ".../output/exp_012_logprob/samples_with_logprobs.jsonl"` (SciERC)
   - 没有 `hidden_state_probe_conll_v2.py`

3. **没有 CoNLL 的 merged checkpoint**
   - 存在 `qwen3-8b-conll2003-lora`（LoRA adapter）
   - 但没有 `*conll*merged*` 目录，hidden state 提取需要 merged 模型

4. **没有 CoNLL hidden states 输出目录**
   - 只有 `output/hidden_state_probe/`（SciERC）、`hidden_state_probe_fewnerd/`、`hidden_state_probe_exp016/`

5. **Registry 记录本身不完整** — 没有 spec、server、log_path、error_msg 字段，说明 Worker 在写入这些元数据前就崩溃了

### 数据可用性

CoNLL 的 `samples.jsonl`（如 `exp_002_conll_n16/samples.jsonl`）已经**自带 `mean_logprob` 和 `cumulative_logprob` 字段**，探针代码的 `load_instance_data()` 可以直接使用。所以数据源不是问题。

### 修复建议

要运行这个实验，需要按顺序完成：

1. **Merge CoNLL LoRA** — 将 `checkpoints/qwen3-8b-conll2003-lora` merge 成完整模型
2. **创建 `extract_hidden_states_conll.py`** — 基于 `extract_hidden_states.py` 改写，指向 CoNLL 的 samples.jsonl 和 merged checkpoint
3. **运行提取** — 生成 `output/hidden_state_probe_conll/hidden_states.pt`
4. **创建 `hidden_state_probe_conll_v2.py`** — 基于 `hidden_state_probe_v2.py`，修改 `DATA_DIR` 和 `SAMPLES_PATH` 指向 CoNLL 数据
5. **运行探针训练+评估**

需要我执行这些修复步骤吗？

---
