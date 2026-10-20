# code gpqa pipeline prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpqa_pipeline_prep_20260516T044908_result.json`
- **Structured JSON:** [`621eda40c4bdc715d069.json`](../../sessions/62/621eda40c4bdc715d069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPQA Diamond 数据
- **题数**: 198 题（Chemistry 93, Physics 86, Biology 19）
- **格式**: 多选题（A/B/C/D），选项已随机打乱，答案分布均匀（A:44, B:52, C:49, D:53）
- **文件**: `/root/autodl-tmp/pacs/data/gpqa_diamond.json`（190KB）
- **字段**: `id`, `problem`（含完整 MCQA prompt + "Think step by step" 指令）, `answer`（正确选项字母）, `correct_answer_text`, `domain`, `subdomain`

### DS-R1 `&lt;think>` 标记测试
- **DS-R1-Distill-Qwen-7B 对 MATH 和 GPQA 都不生成 `&lt;think>` 标记**（无论 raw prompt 还是 chat template）
- **不影响 pipeline**：phase segmentation 基于 attention sparsity 的 KDE/quantile 方法，完全不依赖 `&lt;think>` 标签

### Pipeline 适配
需要改 **1 个文件**：`pacs/profiling/run_profiling.py`

唯一问题在 **line 256-258** 的硬编码 prompt 模板：
```python
prompt = (
    f"Solve the following math problem step by step.\n\n"
    f"Problem: {problem_text}\n\nSolution:"
)
```

GPQA 的 `problem` 字段已包含完整 MCQA prompt（含选项和指令），再套一层 "Solve the following math problem" 会产生语义冲突。建议：
- 加一个 `--prompt_template` 参数，支持 `{problem}` 占位符
- 或加 `--raw_prompt` flag，直接使用 `problem` 字段作为完整 prompt

其他部分无需修改：
- `load_data()` 已通用（读 `problem` 或 `question` 字段）
- 无 `level` 字段时自动跳过 stratified sampling，使用全量数据
- Phase segmentation 基于 attention sparsity，与任务类型无关

### 无阻塞问题

---
