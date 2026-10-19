# CLKC Conflict Dataset

## 数据来源

**ConflictQA** (`osunlp/ConflictQA`, Apache 2.0)
- 论文: arXiv:2305.13300
- 包含 2 个子集 × 8 个模型 = 16 个 JSON 文件

### 原始数据结构

| 子集 | 样本数 | 说明 |
|------|--------|------|
| popQA | 7947 | 基于 PopQA 的事实型问答 |
| strategyQA | 1245 | 基于 StrategyQA 的推理型问答 |

每个模型变体共享相同字段：

| 原始字段 | 说明 |
|---------|------|
| `question` | 问题 |
| `popularity` | 问题流行度 |
| `ground_truth` | 正确答案列表 |
| `memory_answer` | 模型从参数知识回答的结果 |
| `parametric_memory` | 模型对参数知识的解释 |
| `counter_answer` | 与参数知识矛盾的答案 |
| `counter_memory` | 支持矛盾答案的解释 |
| `parametric_memory_aligned_evidence` | 与参数知识一致的 evidence passage |
| `counter_memory_aligned_evidence` | 与参数知识矛盾的 evidence passage |

## 我们的数据集

### 使用的子集和筛选逻辑

- **来源**: `conflictQA-popQA-chatgpt.json`（popQA 子集，ChatGPT 生成的记忆/反记忆）
- **筛选**: 要求 `parametric_memory_aligned_evidence` 和 `counter_memory_aligned_evidence` 均非空且长度 > 20 字符
- **采样**: 从 7947 条中随机采样 500 条（seed=42）
- **划分**: 400 条用于 train，100 条用于 test

### 标签设计

每条原始样本生成 **2 条** 实例（二分类）：

| label | context 来源 | 含义 |
|-------|-------------|------|
| `conflict` | `counter_memory_aligned_evidence` | context 与模型参数知识矛盾 |
| `no_conflict` | `parametric_memory_aligned_evidence` | context 与模型参数知识一致 |

探针目标：从模型残差流激活中区分"存在知识冲突" vs "无知识冲突"。

### 字段映射

| 目标字段 | 来源 |
|---------|------|
| `question` | 原始 `question` |
| `context` | `counter_memory_aligned_evidence`（conflict）或 `parametric_memory_aligned_evidence`（no_conflict）|
| `parametric_answer` | `ground_truth[0]` |
| `contextual_answer` | `counter_answer` |
| `language` | `"en"` 或 `"zh"` |
| `label` | `"conflict"` 或 `"no_conflict"` |
| `source_subset` | `"popQA-chatgpt"` |

### 最终统计

| 文件 | 样本数 | conflict | no_conflict |
|------|--------|----------|-------------|
| `en_conflict_train.jsonl` | 800 | 400 | 400 |
| `en_conflict_test.jsonl` | 200 | 100 | 100 |
| `zh_conflict_train.jsonl` | 800 | 400 | 400 |
| `zh_conflict_test.jsonl` | 200 | 100 | 100 |

ZH 版本由 `src/translate_to_zh.py` 使用 Qwen3-8B 翻译生成（需 GPU 服务器运行）。

### 辅助文件

| 文件 | 说明 |
|------|------|
| `raw_sampled_train.jsonl` | 采样的 400 条原始 ConflictQA 数据（train） |
| `raw_sampled_test.jsonl` | 采样的 100 条原始 ConflictQA 数据（test） |
