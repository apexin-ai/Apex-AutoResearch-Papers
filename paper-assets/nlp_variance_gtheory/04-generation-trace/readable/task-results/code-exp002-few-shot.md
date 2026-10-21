# code exp002 few shot

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_few_shot_20260521T083523_result.json`
- **Structured JSON:** [`6e72363349b36ecf136f.json`](../../sessions/6e/6e72363349b36ecf136f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

**完成内容：**

1. **`scripts/prepare_few_shot_exp002.py`** — 从 HuggingFace train split 采样 few-shot 示例
   - GSM8K: 5 例覆盖 easy/medium/hard/very_hard 难度，含完整 CoT + `#### answer`
   - ARC: 5 例覆盖 A/B/C/D 不同答案位置
   - HellaSwag: 5 例覆盖 5 个不同 activity label

2. **生成的数据文件：**
   - `data/few_shot_gsm8k.json`
   - `data/few_shot_arc.json`
   - `data/few_shot_hellaswag.json`

3. **`src/inference/run_experiment.py` 修改：**
   - 新增 `DEFAULT_FEW_SHOT` 字典，每个 benchmark 自动映射对应 few-shot 文件
   - `_build_prompt()` 现在将 `few_shot` 传递给所有 benchmark 的 prompt builder
   - 数据加载逻辑移除了 MMLU-only 限制
   - 新增 `--zero-shot` 标志禁用 few-shot；`--few-shot` 默认自动选择

4. **验证结果：**
   - 三个 benchmark 的 5-shot prompt 格式正确，CoT/选项/答案标注清晰
   - few-shot 示例与 test items 零重叠
   - zero-shot 路径（`few_shot=None`）保持兼容

---
