# code fix kstar theta ci lower

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_kstar_theta_ci_lower_20260515T130507_result.json`
- **Structured JSON:** [`45e82bbb5dba7cbeb662.json`](../../sessions/45/45e82bbb5dba7cbeb662.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇报：

**修改前** `compute_kstar()`：
```python
def compute_kstar(auc_values, theta):
    ...
    if auc >= theta:        # ← 用 mean AUC 判断
```

**修改后**：
```python
def compute_kstar(auc_values, ci_values, theta):
    ...
    if auc - ci >= theta:   # ← 改用 CI lower bound
```

调用处同步传入 `ci_half[name]`。

**影响**（以 θ=0.60 为例）：
| 模型 | 修改前 K*(0.60) | 修改后 K*(0.60) |
|------|:-:|:-:|
| Qwen-rewrite | 2 | 2 |
| Pythia | 2 | 2 |
| OLMo | 2 | **1** |
| Qwen-cont | 2 | **1** |

OLMo/Qwen-cont 的 1v2 CI lower bound（0.585/0.582）不过 0.60 门槛，所以 K* 从 2 降到 1。Unanimous K\*=2 区域收窄到 θ∈[0.570, 0.580]。

Reviewer 指出的 Pythia 2v3 矛盾已修正：θ=0.55 时 mean AUC=0.5515 ≥ 0.55（旧：K\*=3），但 CI lower=0.5295 < 0.55（新：K\*=2），与论文一致。

---
