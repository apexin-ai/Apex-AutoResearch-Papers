# code classify no span hint

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify_no_span_hint_20260512T223926_result.json`
- **Structured JSON:** [`6d47a0dad9c65f40c0bd.json`](../../sessions/6d/6d47a0dad9c65f40c0bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行时 taxonomy 去 span hint 效果正确。所有 "Expected correction span: ..." 行已移除，错误类型核心定义完整保留。

---

### 修改汇总

**5 处修改：**

#### 1. 新增 `ERROR_TAXONOMY_NO_SPAN`（移除 span 长度描述）
```python
# 旧：只有 ERROR_TAXONOMY
# 新：在其后追加
ERROR_TAXONOMY_NO_SPAN = re.sub(
    r'\nExpected correction span:[^\n]*', '', ERROR_TAXONOMY
)
```

移除的 3 行：
- `Expected correction span: SHORT (1-3 expert steps).`
- `Expected correction span: MEDIUM (3-6 expert steps).`
- `Expected correction span: LONG (6+ expert steps).`

#### 2. 新增 `CLASSIFICATION_PROMPT_NO_SPAN`（移除 divergence 区域的 span 数值提示）
```python
CLASSIFICATION_PROMPT_NO_SPAN = CLASSIFICATION_PROMPT.replace(
    "\nExpert completes the task in {correction_span} more steps after this point.", ""
)
```

移除的行：`Expert completes the task in {correction_span} more steps after this point.`

#### 3. `build_messages()` 增加 `no_span_hint` 参数
```python
# 旧
def build_messages(task_desc, expert_actions, model_actions, div_info):
    prompt = CLASSIFICATION_PROMPT.format(
        taxonomy=ERROR_TAXONOMY,

# 新
def build_messages(task_desc, expert_actions, model_actions, div_info, no_span_hint=False):
    tmpl = CLASSIFICATION_PROMPT_NO_SPAN if no_span_hint else CLASSIFICATION_PROMPT
    taxonomy = ERROR_TAXONOMY_NO_SPAN if no_span_hint else ERROR_TAXONOMY
    prompt = tmpl.format(
        taxonomy=taxonomy,
```

#### 4. argparse 增加 `--no_span_hint`
```python
parser.add_argument("--no_span_hint", action="store_true",
                    help="Remove correction-span length hints from classification prompt")
```

#### 5. `main()` 中传参
```python
# 旧
build_messages(m["task_desc"], m["expert_actions"],
               m["model_actions"], m["divergence"])
# 新
build_messages(m["task_desc"], m["expert_actions"],
               m["model_actions"], m["divergence"],
               no_span_hint=args.no_span_hint)
```

`--help` 验证通过。`--no_span_hint` 模式下，taxonomy 保留完整的错误类型定义（策略错误 / 验证遗漏 / 计划失误的特征描述），仅移除所有 span 长度预期。

---
