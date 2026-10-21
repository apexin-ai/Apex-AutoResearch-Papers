# Worker 结果输出规范

## 问题根因

Worker `worker_code_pipeline-dry-run-72b-zs_20260519T192708` 的 `result.raw` 为空字符串。

**原因**：Worker 在 Line 239 输出了完整的 dry-run 结果汇总（1136 chars），但随后在 Line 240 调用了 `TodoWrite` 标记任务完成。Claude Code 的 `result` event 取最后一个 assistant turn 的文本内容，而最后一个 turn（Line 240）只有 `tool_use`，没有 `text` block，导致 result event 的 text 字段为空字符串。

**事件序列**：
```
Line 239: assistant [text] — "## Dry-Run 结果汇总 ..." (1136 chars)  ← 有用内容在这里
Line 240: assistant [tool_use: TodoWrite]                              ← 最后一个 assistant turn
Line 241: user [tool_result]
Line 242: result {result: ""}                                          ← 空！
```

## 规范：Worker 最后一条消息必须是纯文本

Worker 在完成所有工作后，**最后一条 assistant 消息必须是纯文本总结**，不能是工具调用（包括 `TodoWrite`）。

### 正确顺序

```
1. 完成所有工作（代码、测试、分析等）
2. 调用 TodoWrite 标记所有任务完成
3. 输出纯文本总结                       ← 必须是最后一步
```

### 错误顺序（导致空 result）

```
1. 完成所有工作
2. 输出文本总结
3. 调用 TodoWrite 标记任务完成           ← 这会导致 result 为空
```

### 文本总结应包含

- **任务完成状态**：成功/部分成功/失败
- **关键结果数据**：数值、表格、文件路径等可被调用方直接使用的信息
- **异常标注**：如有问题或偏差，明确标出

### 示例

```
## 结果

3 个脚本全部 dry-run PASS。

| 脚本 | 状态 | 关键指标 |
|------|------|---------|
| compute_signals.py | PASS | LP ρ=0.081, SJ ρ=0.217, VC ρ=0.277 |
| selective_prediction.py | PASS | AUROC=0.623, Coverage@90=0.847 |
| format_for_scaling.py | PASS | 输出 3 文件，格式校验通过 |

产出文件：`/root/autodl-tmp/struct_self_consist_ie/results/dry_run/`
```

## 框架改进建议

**文件**：`/home/ubuntu/agent-ml-research/core/tools/worker.py`，Line 600

**当前逻辑**：
```python
final_text = result_event.text if result_event else output
```

**问题**：`result_event` 存在但 `.text` 为空时，不会 fallback。框架已有 `extract_last_assistant_text()` 函数（`claude_client.py:338`），但 `_monitor_worker` 中未使用。

**建议修改**：
```python
final_text = result_event.text if result_event and result_event.text.strip() else ""
if not final_text:
    final_text = backend.extract_last_assistant_text(output) or output
```

这样当 result event 的 text 为空时，会回退到最后一个包含文本的 assistant 消息（本例中就是 Line 239 的结果汇总）。
