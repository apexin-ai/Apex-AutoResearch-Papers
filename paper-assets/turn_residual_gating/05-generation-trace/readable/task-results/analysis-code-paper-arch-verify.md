# analysis code paper arch verify

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_code_paper_arch_verify_20260519T144058_result.json`
- **Structured JSON:** [`dedb3f07321ff4b30ab9.json`](../../sessions/de/dedb3f07321ff4b30ab9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

关键代码在 `threadgate.py` 的 `_make_hook` 方法（约第 97-116 行）。核心逻辑：

```python
def hook(module, input, output):
    layer_input = input[0]
    layer_output = output[0] if isinstance(output, tuple) else output

    gate = self.gates[layer_idx](layer_input, self._current_turn_features)

    f_x = layer_output - layer_input      # f_l(x_l) = sub-layer output - input
    gated = layer_input + gate * f_x      # x_{l+1} = x_l + g_l * f_l(x_l)
```

---

```
实现方式: gate on sub-layer output
代码位置: /root/turn_residual_gating/src/threadgate.py:107-108
具体代码:
    f_x = layer_output - layer_input
    gated = layer_input + gate * f_x
与论文 Eq.3 (x_{l+1} = g_l · x_l + f_l(x_l)) 是否一致: 否
实际公式: x_{l+1} = x_l + g_l · f_l(x_l)
```

**分析：**

- 论文 Eq.3：`x_{l+1} = g_l · x_l + f_l(x_l)` — gate 缩放 residual stream（整个 identity 分支），sub-layer output 不受 gate 影响
- 代码实际：`x_{l+1} = x_l + g_l · f_l(x_l)` — identity 分支无损传递，gate 缩放 sub-layer output（即 attention/FFN 的贡献）

两者行为差异：
- **g→1 时**：两者都退化为标准 `x + f(x)`，一致
- **g→0 时**：论文公式 → `f_l(x_l)`（丢弃 residual，只保留 sub-layer output）；代码 → `x_l`（丢弃 sub-layer output，只保留 residual）。**语义完全相反**
- **对 gradient 的影响**：代码实现中 `∂x_{l+1}/∂x_l = 1 + g_l · ∂f/∂x`，identity 分支梯度始终为 1，不受 gate 影响，梯度流更稳定。论文公式中 `∂x_{l+1}/∂x_l = g_l + ∂f/∂x`，gate 直接控制 identity 分支的梯度，g→0 时梯度消失风险大

代码实现实际上是更常见、更稳定的 "gate on sub-layer output" 变体（类似 Highway Network / ReZero 的思路），与论文 Eq.3 的描述不一致。需要决定是修改代码还是修改论文公式。

---
