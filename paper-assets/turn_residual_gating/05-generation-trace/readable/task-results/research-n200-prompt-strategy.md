# research n200 prompt strategy

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_n200_prompt_strategy_20260522T102938_result.json`
- **Structured JSON:** [`179b19876aa619a7e63b.json`](../../sessions/17/179b19876aa619a7e63b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have a complete picture. Here's the analysis and strategy:

---

## 1. 现有 Prompt 分析

### 格式

每个 prompt 包含 4 个字段：
- `prompt_id`: 唯一标识
- `system_instruction`: 系统指令（要求模型遵循的约束）
- `user_messages`: 5 个 topic 不同的 user turn（用于测试跨 turn 保持）
- `check_fn`: 映射到 `CHECK_FNS` 中的 Python 函数，自动判 pass/fail

### 分类分布（18 个）

| 类别 | 数量 | 占比 | 具体 prompt |
|------|------|------|------------|
| content_constraint | 7 | 39% | mention_ai_assistant, include_certainly, no_the, include_remember, include_interesting, no_commas, no_exclamation |
| position_constraint | 5 | 28% | start_sure, end_hope, start_let_me_think, start_well, end_question |
| format_constraint | 3 | 17% | bullet_points, numbered_list, all_caps |
| count_constraint | 3 | 17% | one_emoji, three_sentences, max_two_sentences |

### 评估方式

- **全自动评估**：每个 `check_fn` 是纯 Python 函数，无 LLM judge
- **指标**：per-turn following rate、late-turn (turn 3-5) rate、per-category comparison、McNemar 显著性检验、GAR-compliance point-biserial 相关
- **check_fn 模式归纳**（这是扩展的关键）：

| 模式 | 参数化 | 现有数量 | 示例 |
|------|--------|---------|------|
| `starts_with(phrase)` | 1 参数 | 3 | start_sure, start_let_me_think, start_well |
| `ends_with(phrase)` | 1 参数 | 2 | end_hope, end_question |
| `contains(phrase)` | 1 参数 | 4 | include_certainly, include_remember, include_interesting, mention_ai_assistant |
| `not_contains(word)` | 1 参数 | 1 | no_the |
| `not_contains(char)` | 1 参数 | 2 | no_commas, no_exclamation |
| `count_X == N` | 2 参数 | 2 | one_emoji, three_sentences |
| `count_X <= N` | 2 参数 | 1 | max_two_sentences |
| `format_check` | 自定义 | 3 | bullet_points, numbered_list, all_caps |

### 难度特征

- 现有 prompt 全是**单约束**（一条指令一个要求）
- 难度主要靠约束类型区分：禁止类（no_the）比包含类（include_certainly）更难
- 无复合约束、无条件约束、无 topic-dependent 约束

---

## 2. 推荐方案

### 生成方法：参数化模板 + LLM 补充

**核心思路**：先将 check_fn 参数化为可复用的检测器工厂，再用模板批量生成 prompt，最后用 LLM 补充非模板化的创意 prompt。

**Step 1: 参数化检测器工厂（写代码，约 2h）**

将现有 18 个 check_fn 归纳为 ~10 个工厂函数：

```python
def make_starts_with(phrase):
    return lambda t: t.lstrip().startswith(phrase)

def make_ends_with(phrase):
    return lambda t: t.rstrip().endswith(phrase)

def make_contains(phrase, case_insensitive=True):
    return lambda t: phrase.lower() in t.lower() if case_insensitive else phrase in t

def make_not_contains_word(word):
    return lambda t: word.lower() not in re.findall(r"\b\w+\b", t.lower())

def make_not_contains_char(char):
    return lambda t: char not in t

def make_count_sentences(op, n):  # op: "==", "<=", ">="
    ...

def make_count_words(op, n):
    ...

def make_regex_match(pattern, should_match=True):
    ...
```

这样新增一个 prompt 只需声明参数，不需要写新函数。

**Step 2: 按类型批量生成**

| 类别 | 目标数量 | 生成方式 |
|------|---------|---------|
| content_constraint | 100 (50%) | 模板化：50 个 `contains(phrase)`（必须包含某词/短语） + 30 个 `not_contains_word(word)`（禁止某常用词） + 20 个 `not_contains_char(char)` |
| position_constraint | 40 (20%) | 模板化：20 个 `starts_with` + 20 个 `ends_with` |
| format_constraint | 30 (15%) | 10 个模板化（all_lowercase, markdown_headers, JSON format 等） + 20 个需自定义 check_fn |
| count_constraint | 20 (10%) | 模板化：sentence count, word count, paragraph count, emoji count 组合 |
| compound_constraint | 10 (5%) | LLM 生成 + 手动 check_fn（2 个约束同时满足） |

**Step 3: Topic 多样化**

每个 prompt 的 5 个 user_messages 需要 topic 多样。方案：
- 准备 30 个 topic domain（science, history, technology, health, culture, economics, ...）
- 每个 prompt 从中随机采样 5 个 domain，再用 LLM 生成具体问题
- 关键：topic 要包含容易诱导违反指令的问题（如 no_exclamation prompt 配 "What's the most amazing fact about..."）

### 分层设计细节

**content_constraint（100 个）子类型：**

| 子类型 | 数量 | 示例 |
|--------|------|------|
| must_include_word | 25 | "always use the word 'indeed'" / "include 'notably'" |
| must_include_phrase | 15 | "include 'as a matter of fact'" / "include 'in my view'" |
| must_not_use_word | 25 | "never use 'very'" / "never use 'just'" / "never use 'really'" |
| must_not_use_char | 10 | "never use semicolons" / "never use parentheses" / "never use colons" |
| must_not_use_word_category | 10 | "never use any number words" / "never use color words" |
| must_mention_topic | 10 | "always mention mathematics" / "always reference nature" |
| language_style | 5 | "never use contractions" / "always use passive voice" |

**position_constraint（40 个）子类型：**

| 子类型 | 数量 | 示例 |
|--------|------|------|
| starts_with_phrase | 20 | "start with 'Great question,'" / "start with 'To answer this,'" |
| ends_with_phrase | 15 | "end with 'Thank you for asking.'" / "end with 'That's my take.'" |
| first_word_constraint | 5 | "first word must be 'Actually'" / "first word must be a number" |

**format_constraint（30 个）- 需要更多自定义 check_fn：**
- all_lowercase, markdown_bold_key_terms, every_sentence_new_line, table_format, Q&A_format, parenthetical_asides, indented_paragraphs, AABB 韵律结构, 每段首字母递增 (A->B->C), etc.

**count_constraint（20 个）：**
- exactly N sentences (N=1,2,4,5,6)
- at most N words (50, 100, 150)
- exactly N paragraphs
- at most N bullet points
- exactly N emoji

**compound_constraint（10 个）：**
- "start with 'Sure!' AND end with a question"
- "use exactly 3 sentences AND include the word 'however'"
- "never use 'the' AND write in all caps"

---

## 3. 实施步骤

### Phase 1: 基础设施（1-2h）

1. 将 `CHECK_FNS` 重构为参数化工厂，在 `eval_instruction_retention.py` 中新增 `register_check_fn(prompt_id, factory, *args)` 机制
2. 让 prompt JSON 可以内联声明 check 参数，不用为每个 prompt 硬编码函数名：
   ```json
   {
     "prompt_id": "include_indeed",
     "system_instruction": "You must include the word 'indeed' ...",
     "user_messages": [...],
     "check_type": "contains",
     "check_args": {"phrase": "indeed", "case_insensitive": true}
   }
   ```
   向后兼容现有 `check_fn` 字段。

### Phase 2: 批量生成 content/position/count（2-3h）

1. 编写 Python 脚本 `scripts/generate_ir_prompts.py`
2. 对模板化类型：准备词表 + 短语表，自动组合生成 prompt skeleton
3. 对 user_messages：用 Claude API 批量生成 5 个多样 topic 的问题（约 800 个问题 = 160 prompt × 5 turn）
4. 对 content_constraint 中的 "诱导 turn"：针对每个约束手动设计 1-2 个容易诱导违反的 topic

### Phase 3: format/compound 类手动编写（2-3h）

1. format_constraint 中 10 个需要新 check_fn 的（如 markdown_bold, table_format 等）——手写 check 函数
2. compound_constraint 的 10 个——组合现有 check_fn + 手写 system instruction

### Phase 4: 质控（2-3h）

1. **自动可评估性验证**：对每个 prompt 生成 1 个 positive example（手写符合指令的回复）和 1 个 negative example（不符合的），确认 check_fn 判对
2. **难度校准**：用 base model（无 TG）在所有 200 prompt 上跑一轮（beta=0），筛除 compliance rate < 30% 或 > 95% 的 prompt（替换或调整指令措辞）
3. **独立性检查**：确保没有两个 prompt 的 check_fn 等价（如 "include 'certainly'" 和 "use 'certainly' in every response"）
4. **topic 重复检查**：跨 prompt 的 user_messages 不应高度重复

### Phase 5: 集成（1h）

1. 合并到 `data/instruction_retention_prompts.json`
2. 更新 `CATEGORY_MAP` 和 `CHECK_FNS`
3. 跑一次完整 eval 确认无 runtime error

**预计总工时：8-12h**（其中 LLM 生成 + API 调用 ~2h，手动编写 ~4h，质控 ~4h）

---

## 4. 参考资源

### 数据集 / Benchmark

| 资源 | 用途 | 说明 |
|------|------|------|
| **IFEval** (Zhou et al., 2023) | 约束类型参考 | 25 种 verifiable instruction 类型，含自动 check function，可直接复用约束设计 |
| **MT-Bench** (Zheng et al., 2023) | topic 多样性参考 | 8 类 topic，可作为 user_messages 的 domain 来源 |
| **AlpacaEval** | user_messages 采样源 | 805 条 diverse instruction，可用于填充 topic |
| **FLASK** (Ye et al., 2023) | 细粒度评估维度 | 12 维技能评估，参考其 instruction 设计思路 |

### IFEval 可直接复用的约束类型（与当前项目 check_fn 模式兼容）

- `keywords:existence` → `contains(word)` ✓
- `keywords:forbidden_words` → `not_contains_word(word)` ✓
- `startend:end_checker` → `ends_with(phrase)` ✓
- `length_constraints:number_sentences` → `count_sentences(op, n)` ✓
- `length_constraints:number_words` → `count_words(op, n)` ✓
- `detectable_format:number_bullet_lists` → `format_check` 需适配
- `detectable_format:title` → 新增 `has_title` check
- `change_case:english_lowercase` → 新增 `all_lowercase` check
- `punctuation:no_comma` → `not_contains_char(',')` ✓

### 关键论文

- Zhou et al. (2023) "Instruction-Following Evaluation for Large Language Models" — IFEval 原文，25 种 verifiable constraint 分类
- Qin et al. (2024) "InFoBench: Evaluating Instruction Following Ability in LLMs" — 多粒度 constraint decomposition
- Wen et al. (2024) "Benchmarking Complex Instruction Following with BenchIF" — compound constraint 设计

---

### 建议的下一步

先实施 Phase 1（重构 check_fn 为参数化工厂），这决定了后续批量生成的效率。完成后可以并行推进 Phase 2 和 Phase 3。是否开始？

---
