# ScienceWorld SFT Eval 诊断报告

**日期**: 2026-05-19
**问题**: SFT eval valid action rate 0-2%, 训练 loss 0.003

## 根因

### 1. 训练数据用了 gold action（环境不接受）

训练数据来自 ScienceWorld 内部 gold action sequence，格式与环境 player parser 不兼容：

| Gold action (训练数据) | 环境响应 | 正确 action |
|---|---|---|
| `open door to kitchen` | "No known action matches" | `open door` |
| `go to kitchen` | "No known action matches" | — (需先 open door 再用别的命令) |

验证：
```python
env.step("open door to kitchen")  # → "No known action matches that input."
env.step("open door")             # → "The door is now open."  ✓
```

### 2. Admissible actions 被 "connect" 淹没

`get_valid_action_object_combinations()` 对 boil v14 返回 939 个 action：

| Action type | Count | % |
|---|---|---|
| connect X to Y | 506 | 54% |
| pour | 154 | 16% |
| move | 113 | 12% |
| dunk | 42 | 4% |
| look | 35 | 4% |
| disconnect | 23 | 2% |
| **open** | **3** | **0.3%** |
| pick up | 10 | 1% |
| 其他 | ~53 | 6% |

Eval 只展示前 50 个（全是 connect），模型从不在 prompt 中看到有用 action。

### 3. valid_action_rate metric 误导

```python
shown = valid_actions[:50]          # 全是 connect
action_is_valid = action in shown   # 模型生成 "open cupboard" → False
```

模型生成的 action 可能在全量 939 个中存在，但不在 shown[:50] 中 → metric 报 0%。

### 4. fmt rate 53-74%

约 30-40% 的步骤格式解析失败，`env.step("")` 浪费回合。

## 修复方案

### A. Eval 修复（无需重训）

1. **过滤/排序 admissible actions**：useful verbs 优先，connect 限量
2. **valid_action_rate 用全量 list**
3. **增大 MAX_VALID_ACTIONS**

### B. 重新生成数据 + 重训（根治）

1. 用 `get_valid_action_object_combinations()` 中的 action（非 gold path）
2. 过滤 connect flood
3. 确保 expert action ∈ shown admissible list
