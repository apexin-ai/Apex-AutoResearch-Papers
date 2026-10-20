# analysis diff apply diagnosis

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diff_apply_diagnosis_20260515T144951_result.json`
- **Structured JSON:** [`df8da347b465f7924d77.json`](../../sessions/df/df8da347b465f7924d77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完毕。

## 结果

### 失败分类表（14/28 = 50% 的结果中 diff apply 失败）

更正：7 instances × 4 conditions = 28 results, 其中 24 已完成（7 instances 的 checkpoint 包含 `luigi_5` 只有4条中有些也在数据中），11 fail / 13 success (among the 24 completed)。

| Instance | Condition | 失败原因 | patch stderr |
|----------|-----------|----------|-------------|
| black_1 | full_trace | **C: hunk count** (old: 8→应为9) | malformed patch at line 15 |
| black_1 | structural_filtered | **C: hunk count** (old: 7→应为6) | malformed patch at line 13 |
| black_1 | line_filtered | **C: hunk count** (old: 7→应为8) | malformed patch at line 11 |
| cookiecutter_1 | no_trace | **C: hunk count** (old: 7→10, new: 9→12) | silent fail |
| cookiecutter_3 | no_trace | **C: hunk count** | malformed patch at line 16 |
| cookiecutter_3 | structural_filtered | **C: hunk count** | silent fail |
| cookiecutter_3 | line_filtered | **C: hunk count** (old: 22→20, new: 27→25) | silent fail |
| fastapi_2 | full_trace | **C: hunk count** (multi-hunk, 2nd hunk counts wrong) | malformed at line 15 |
| httpie_2 | no_trace | **C: hunk count** (old: 11→10, new: 12→11) | silent fail |
| httpie_2 | full_trace | **C: hunk count** (old: 7→6, new: 11→9) | malformed at line 12 |
| httpie_2 | structural_filtered | **C: hunk count** (new: 13→10) | unexpected EOF |

### 根因：**100% 系统性 prompt 问题（可修复）**

**11/11 失败全部是 hunk line count 不匹配** — LLM 在 `@@ -X,N +Y,M @@` 中写错了 N 或 M 的值，但 diff 内容本身是正确的。

关键证据：**成功的 13 个 case 中有 8 个也有 hunk count 不匹配**，只是 `patch -p1` 容忍了较小的偏差（off-by-one）。当偏差较大（off-by-2+）或出现在 multi-hunk diff 中时，`patch` 就报错了。

这不是 LLM 能力问题。LLM 能正确生成 diff 内容（增删改行），但不能可靠地数行数。

### 修复建议

在 `apply_diff_in_dir()` 调用 `patch -p1` 之前，加一个 `recount_diff_hunks()` 后处理函数，重新计算每个 hunk 的实际行数：

```python
def recount_diff_hunks(diff_text: str) -> str:
    """Recalculate @@ line counts from actual hunk body."""
    lines = diff_text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r'^@@ -(\d+),\d+ \+(\d+),\d+ @@(.*)', lines[i])
        if m:
            old_start, new_start, rest = int(m.group(1)), int(m.group(2)), m.group(3)
            hunk_lines = []
            j = i + 1
            while j < len(lines):
                if lines[j].startswith('@@') or lines[j].startswith('--- ') or lines[j].startswith('+++ '):
                    break
                hunk_lines.append(lines[j])
                j += 1
            while hunk_lines and hunk_lines[-1] == '':
                hunk_lines.pop()
            old_count = sum(1 for l in hunk_lines if not l.startswith('+'))
            new_count = sum(1 for l in hunk_lines if not l.startswith('-'))
            result.append(f'@@ -{old_start},{old_count} +{new_start},{new_count} @@{rest}')
            result.extend(hunk_lines)
            i = j
        else:
            result.append(lines[i])
            i += 1
    return '\n'.join(result) + '\n'
```

修改 `apply_diff_in_dir` 第 213 行之前加一行：`diff_text = recount_diff_hunks(diff_text)`。

这一个修复预期能把 diff apply 成功率从 54%（13/24）提升到接近 100%。

---
