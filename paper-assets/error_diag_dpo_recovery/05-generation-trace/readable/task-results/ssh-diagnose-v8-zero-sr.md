# ssh diagnose v8 zero sr

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-v8-zero-sr_20260513T072151_result.json`
- **Structured JSON:** [`d773590a825a6ba0568a.json`](../../sessions/d7/d773590a825a6ba0568a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因确认

**TextWorld 1.7.0 将 `put X in/on Y` 语法改为 `move X to Y`。**

验证结果：
- `put spoon 1 in/on diningtable 1` → "Nothing happens"（不在 admissible_commands 中）
- `move spoon 1 to diningtable 1` → 成功，**Reward=1, Done=True**

所有 ALFWorld 任务最终都需要放置物品，`put` 全部失败导致 0% 成功率。与 ICL、temperature、模型行为完全无关。

### 详细发现

| 检查项 | 结果 |
|--------|------|
| temperature 实际值 | 0.5 ✅ 命令行和 argparse 均正确 |
| ICL 数据加载 | ✅ 正确加载，`from`/`value` → `role`/`content` 转换正常 |
| enable_thinking=False | ✅ 生效，无 think token 泄漏 |
| 模型行为 | ✅ 生成正确的 Thought/Action 格式，action 无隐藏字符 |
| **`put` 动作** | **❌ TextWorld 1.7.0 不再接受 `put X in/on Y`，改用 `move X to Y`** |
| 其他动作 | `take`/`go to`/`open`/`clean`/`heat` 均正常 |
| ALFWorld 版本 | 0.4.2 + TextWorld 1.7.0（不兼容） |

### 修复方案

**方案 A（最快）**：在 `env.step` 前加 action 翻译，将 `put X in/on Y` 转为 `move X to Y`：

```python
def translate_action(action: str) -> str:
    m = re.match(r"put (.+) in/on (.+)", action)
    if m:
        return f"move {m.group(1)} to {m.group(2)}"
    return action
```

同时更新 prompt 中的可用动作列表（将 `3. put {obj} in/on {recep}` 改为 `3. move {obj} to {recep}`）。

**方案 B（最稳）**：降级 TextWorld 到兼容版本：
```bash
pip install textworld==1.6.1
```

### 建议

1. 先 kill 当前 v8 进程（PID 763657, 764025），不要浪费 GPU 时间
2. 选择修复方案后重跑

---
