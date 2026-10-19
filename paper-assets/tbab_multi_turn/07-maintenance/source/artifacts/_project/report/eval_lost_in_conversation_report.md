# Lost in Conversation 评估代码验证报告

> 数据集: `microsoft/lost_in_conversation` (HuggingFace)
> 代码仓库: https://github.com/microsoft/lost_in_conversation
> 日期: 2026-05-18

---

## 1. 数据集统计

### 1.1 总览

- **总样本数**: 627
- **Split**: 仅 `train`（评估用，不做训练）
- **任务类型**: 6 种
- **列数**: 43（union schema，不同任务使用不同列，其余为 null）

### 1.2 Per-task 样本数

| Task      | 样本数 |
|-----------|--------|
| data2text | 120    |
| database  | 107    |
| actions   | 105    |
| math      | 103    |
| code      | 100    |
| summary   | 92     |
| **合计**  | **627**|

### 1.3 Shard 数分布（per task type）

`shards` 字段为 list，shard count = `len(shards)`。

| Task      |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 12 |
|-----------|----|----|----|----|----|----|----|----|-----|
| actions   |  — | 13 | 31 | 44 | 12 |  1 |  2 |  2 |  —  |
| code      |  — |  9 | 12 | 21 | 19 | 21 |  9 |  9 |  —  |
| data2text |  — |  — |  — |102 | 18 |  — |  — |  — |  —  |
| database  |  6 | 68 | 27 |  4 |  2 |  — |  — |  — |  —  |
| math      |  — | 22 | 30 | 26 | 14 |  9 |  1 |  — |  1  |
| summary   |  — |  — |  — | 36 | 27 | 12 | 10 |  7 |  —  |

### 1.4 Shard >= 5 子集

总计 509 条样本满足 shard >= 5：

| Task      | 样本数 |
|-----------|--------|
| data2text | 120    |
| actions   | 92     |
| code      | **91** |
| summary   | 92     |
| math      | **81** |
| database  | 33     |

---

## 2. 指标计算方式

### 重要发现：P̄ / A⁹⁰ / U₁₀⁹⁰ 不在仓库代码中

这三个指标是论文级聚合指标（arXiv:2505.06120），需从实验日志 post-hoc 计算。仓库只记录 per-conversation 的 `is_correct` (bool) 和 `score` (float) 到 JSONL 文件。

**日志记录位置**: `utils_log.py:60-75` (`log_conversation`) 写入 `is_correct`, `score`, 完整 `trace`。
**日志加载**: `utils_log.py:90-128` (`load_results_from`) 按 model 分组读取。

### 2.1 P̄ (Averaged Performance)

**公式**: P̄ = mean(score) across all conversations for a given (model, condition) pair

- 对二值任务（code, database, actions, math）：score ∈ {0, 1}，P̄ = accuracy
- 对连续分数任务（summary, translation, data2text）：P̄ = mean score

### 2.2 A⁹⁰ (Accuracy at 90th percentile of turns)

**定义**: 在对话长度（turn 数）的第 90 百分位处测量的性能。衡量模型在足够多轮次后能否最终解决任务。

**计算数据来源**: 每条对话的 trace 包含完整的 user/assistant/log 消息序列，turn count = user 消息数。需要自行从 JSONL trace 中提取。

### 2.3 U₁₀⁹⁰ (Underperformance from turn 10 to 90)

**定义**: 早期（10th percentile）和晚期（90th percentile）turn 性能之间的差距，衡量模型随对话变长而"迷失"的程度。

**公式**: U₁₀⁹⁰ = Performance@10th_percentile_turns - Performance@90th_percentile_turns

需要按 turn 数分桶并比较不同桶的平均 score。

### 2.4 自行计算方法

```python
import json, numpy as np

results = []  # load from JSONL logs
scores = [r['score'] for r in results]
turns = [len([m for m in r['trace'] if m['role'] == 'user']) for r in results]

# P-bar
p_bar = np.mean(scores)

# A90: score at 90th percentile turn count
p90_turns = np.percentile(turns, 90)
a90_scores = [s for s, t in zip(scores, turns) if t >= p90_turns]
a90 = np.mean(a90_scores)

# U10_90
p10_turns = np.percentile(turns, 10)
early_scores = [s for s, t in zip(scores, turns) if t <= p10_turns]
u10_90 = np.mean(early_scores) - a90
```

---

## 3. 评估方法详细说明

### 3.1 Code 任务

**方法: pass@1 via execution（非 exact match）**

- **代码位置**: `tasks/code/task_code.py:85-115`, `tasks/code/eval_code.py`（600 行）
- **流程**:
  1. 从模型回复中用 AST 解析提取最后一个 top-level 函数定义（`task_code.py:184-217`）
  2. 执行 `check_correctness(sample, pred_code, testcases, timeout=6)`（`task_code.py:111`）
  3. 判定: `all(output is True for each test)` → score=1, 否则 score=0（`task_code.py:112-114`）
- **两种代码类型**:
  - Call-based（`eval_code.py:201-279`）: 编译代码 → 按函数名获取 → JSON 输入调用 → 比较输出
  - Standard I/O（`eval_code.py:282-397`）: patch stdin/stdout → 比较输出行 → 浮点数用 Decimal 比较
- **执行沙盒**: **无容器化沙盒**。使用 `multiprocessing.Process` fork 子进程执行（`eval_code.py:573-597`）。`reliability_guard()`（`eval_code.py:481-564`）禁用危险 OS 操作（os.kill, os.remove, subprocess.Popen 等），但代码注释明确标注"NOT a security sandbox"。超时使用 `signal.SIGALRM`（Unix only）。
- **Answer extraction**: `answer_extraction_strategy = "task_specific"`（`task_code.py:29`），用 AST 解析提取代码（`task_code.py:184-217`）

### 3.2 Math 任务

**方法: Exact string match after normalization（无数值容差）**

- **代码位置**: `tasks/math/task_math.py:33-62`
- **流程**:
  1. Gold answer: `sample["answer"].split("####")[1].strip().lower()`（GSM8K 格式）
  2. 模型回答: 由 SystemAgent 用 GPT 提取为 JSON `{"answer": "..."}`
  3. 正则提取数字: `re.findall(r"(-?[$0-9.,]{2,})|(-?[0-9]+)", answer)`
  4. 清洗: 去除 `$`, `,`, `#### ` 前缀, 末尾 `.`；`$X.00` 去尾零
  5. **严格字符串相等**: `score = 1.0 if extracted == gold else 0.0`
- **Answer extraction**: `answer_extraction_strategy = "gen"`（`task_math.py:14`），SystemAgent 调 LLM 提取答案

### 3.3 其他任务评估方法（供参考）

| Task      | 方法 | 说明 |
|-----------|------|------|
| database  | Execution match | 预测 SQL 和 gold SQL 在 SQLite 上执行，比较结果集（bag semantics） |
| actions   | AST structural match | 解析函数调用，检查函数名、参数名、类型、值 |
| summary   | LLM-based | GPT-4o 评估 insight coverage + citation F1，score = mean(coverage * citation_F1) |
| data2text | BLEU | sacrebleu.corpus_bleu / 100.0 |

---

## 4. Sharded 对话模拟方式

### 4.1 三 Agent 架构

```
User Agent (LLM)  ←→  Assistant (被测模型)  ←→  System Agent (LLM judge)
```

- **User Agent** (`user_agent.py`): LLM 模拟懒用户，每轮最多透露一个 shard
- **Assistant**: 被测模型，接收标准 chat 格式对话
- **System Agent** (`system_agent.py`): 分类 assistant 回复类型 + 提取答案

### 4.2 Sharded 模拟流程

代码位置: `simulator_sharded.py:36-116`

```
while 还有未透露的 shards:
    1. User Agent 生成回复（可能透露一个新 shard）     [line 55]
    2. Assistant 生成回复                              [line 66]
    3. System Agent 分类 assistant 回复类型            [line 73]
    4. 如果是 answer_attempt:
       - 提取答案                                      [line 82]
       - 用 task-specific evaluator 评估               [line 89]
       - 如果正确: 对话结束                            [line 103]
    5. 如果是 clarification/discussion: 继续循环       [line 109]
```

### 4.3 Prompt Template

**Shards 不是通过固定模板注入的**。User Agent 是一个 LLM，根据对话上下文和未透露的 shards 决定说什么。

**User Agent prompt** (`prompts/user_agent.txt:1-27`):
- 输入: 对话历史 + 已透露 shards + 未透露 shards
- 规则: 每轮最多透露一个 shard，用口语化方式重述，简短、可带 typo
- 输出: JSON `{"response": "...", "shard_id": N}`
- **第一轮特殊**: 直接发送 shard[0]，不经过 LLM 改写（`user_agent.py:22-26`）

**Assistant 看到的对话格式**:
- System message: task-specific prompt（如 "You are an expert Python programmer..."）
- 交替的 user/assistant 消息
- `utils.py:34-48` 的 `extract_conversation()` 过滤掉 "log" 角色条目

**Turn 分类** (`prompts/system_turn_categorization.txt:1-26`):
- 类别: answer_attempt, clarification, interrogation, discussion, hedge, refuse, missing
- 只有 answer_attempt 触发评估

---

## 5. 适配本地模型

### 5.1 当前架构

所有模型调用通过 `model_openai.py` 的 OpenAI/Azure API。三个角色（User Agent, Assistant, System Agent）都走 API。

关键代码: `model_openai.py:115-117` 的 module-level singleton `generate` 和 `generate_json` 被全局引用。

### 5.2 改动清单

| 改动项 | 范围 | 工作量 |
|--------|------|--------|
| 新增 `model_hf.py` | 新文件，实现 `generate()` 接口，用 transformers/vLLM 做推理 | ~80-100 行 |
| 修改 `model_openai.py:115-117` | 添加 dispatcher，根据 model name 路由到 API 或本地 | ~20 行 |
| JSON 结构化输出 | System/User Agent 需要可靠的 JSON 输出。方案: (a) 用 outlines/guidance 约束解码，或 (b) 保持 System/User Agent 用 API 模型 | 推荐方案 (b) |
| Chat template | 本地模型需 `tokenizer.apply_chat_template()` 转换 messages 格式 | 包含在 model_hf.py 中 |
| Cost tracking | 本地模型设 `total_usd = 0.0` | 1 行 |
| Reasoning model 检测 | `simulator_sharded.py:38`, `simulator_full.py:51` 的 o1/o3 检测逻辑需扩展 | ~5 行 |

**最小改动路径**: 只替换 assistant 模型为本地推理，System/User Agent 保持用 GPT-4o-mini（便宜）。只需改 `model_openai.py` 一个文件（~50-100 行新代码），simulator 和 task 代码零修改。

### 5.3 推理时间估算

**假设**: 600 样本 x N=10 重复 = 6000 次对话，平均每条对话 ~7 turns，每 turn 3 次 LLM 调用。

| 方案 | 推理调用数 | 估算时间（单 RTX PRO 6000） |
|------|-----------|--------------------------|
| 全部本地（7B 模型） | ~126,000 次 | ~250-350 小时 |
| 仅 assistant 本地 + system/user 用 API | ~42,000 次（本地）+ 84,000 次（API） | 本地 ~80-120 小时，API 并行 |
| 仅 assistant 本地 + vLLM 批量（跨对话并行） | ~42,000 次 | ~30-50 小时（3 GPU 并行） |

**推荐方案**: assistant 用本地 vLLM serving，system/user agent 用 GPT-4o-mini API。3 张 RTX PRO 6000 并行，7B 模型预计 **10-20 小时**可完成 600 x N=10 全量评估。

> 注意: 对话内 turns 是顺序的（必须等上一轮完成），但不同 sample 的对话可以并行。并行度取决于 vLLM 的 concurrent request 能力。

---

## 6. 样本展示

### 6.1 Code 样本（HumanEval/105, 8 shards）

```json
{
  "task_id": "sharded-HumanEval/105",
  "prompt": "def by_length(arr):\n    \"\"\"Given an array of integers, sort the integers that are between 1 and 9 inclusive, reverse the resulting array, and then replace each digit by its corresponding name...\"\"\"\n",
  "test": "def check(candidate):\n    assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == [\"Eight\", \"Five\", \"Four\", \"Three\", \"Two\", \"Two\", \"One\", \"One\"]\n    assert candidate([]) == []\n    assert candidate([1, -1, 55]) == ['One']\n    ...",
  "public_test_cases": "[{\"input\": \"[2, 1, 1, 4, 5, 8, 2, 3]\", \"output\": \"[\\\"Eight\\\", ...]\", \"testtype\": \"functional\"}, ...]",
  "metadata": {"func_name": "by_length"},
  "source": "humaneval",
  "shards": [
    {"shard_id": 1, "shard": "Turn digits into names in a list"},
    {"shard_id": 2, "shard": "Starting with a list of numbers"},
    {"shard_id": 3, "shard": "Sort numbers if they're between 1 and 9"},
    {"shard_id": 4, "shard": "Then flip the list around"},
    {"shard_id": 5, "shard": "Use the words for numbers: One to Nine"},
    {"shard_id": 6, "shard": "If the list is empty, just give back an empty list"},
    {"shard_id": 7, "shard": "Ignore any weird numbers that aren't between 1 and 9"},
    {"shard_id": 8, "shard": "For instance, from [1, -1, 55] you'll get ['One']"}
  ],
  "task": "code"
}
```

### 6.2 Math 样本（GSM8K/1166, 7 shards）

```json
{
  "task_id": "sharded-GSM8K/1166",
  "question": "Generally, a 5-year-old avocado tree produces 50 fruits, a 6-year-old one produces 3 times the initial amount of fruits, a 7-year-old one produces 7 times the initial amount, and an 8-year-old produces 200 fruits less than a 10-year-old one. During the ninth year, the avocado tree doesn't produce any fruit, and then a 10-year-old tree produces 20 times the initial amount of fruits. How many total fruits can an avocado tree produce during its 10 years of life?",
  "answer": "At 5 years it produces 50 fruits\nAt 6 years it produces 50 * 3 = 150 fruits.\nAt 7 years, it produces 50 * 7 = 350 fruits\nAt 10 years, it produces 50 * 20 = 1000 fruits\nAt 8 years, it produces 200 fewer fruits than at 10 years, so it produces 1000 - 200 = 800 fruits\nDuring 10 years, an avocado tree can produce a total of 50 + 150 + 350 + 800 + 1000 = 2350 fruits\n#### 2350",
  "shards": [
    {"shard_id": 1, "shard": "how many fruits does an avocado tree produce over 10 years?"},
    {"shard_id": 2, "shard": "a 5-year-old avocado tree produces 50 fruits normally"},
    {"shard_id": 3, "shard": "when the tree is 6 years old, it produces 3 times the initial 5-year amount"},
    {"shard_id": 4, "shard": "at age 7, it starts producing 7 times the 5-year-old amount"},
    {"shard_id": 5, "shard": "for an 8-year-old tree, it produces 200 fewer fruits than a 10-year-old tree"},
    {"shard_id": 6, "shard": "in its ninth year, the tree doesn't produce any fruit at all"},
    {"shard_id": 7, "shard": "finally, a 10-year-old tree will produce 20 times the 5-year-old amount"}
  ],
  "task": "math"
}
```

---

## 7. 关键结论

1. **数据可用**: 627 样本直接从 HuggingFace 下载，shard >= 5 的子集有 509 条（code 91, math 81）
2. **指标需自行计算**: P̄/A⁹⁰/U₁₀⁹⁰ 不在仓库中，需从 JSONL trace 日志 post-hoc 计算
3. **Code 用执行评估**: pass@1，forked subprocess 执行，非沙盒化
4. **Math 用字符串精确匹配**: GSM8K 风格，normalize 后 string equality，无数值容差
5. **对话模拟是 LLM-driven**: User Agent 是 LLM，不是固定模板。每轮最多透露一个 shard
6. **适配本地模型可行**: 最小改动路径只需修改 `model_openai.py`（~50-100 行），推荐 assistant 本地 + system/user agent 用 API
7. **全量评估预计 10-20 小时**（3 GPU 并行，7B 模型，vLLM serving）
