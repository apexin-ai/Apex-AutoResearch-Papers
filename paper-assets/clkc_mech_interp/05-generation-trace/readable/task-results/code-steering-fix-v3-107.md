# code steering fix v3 107

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_steering-fix-v3-107_20260522T084838_result.json`
- **Structured JSON:** [`f17795b123f0ceb8b178.json`](../../sessions/f1/f17795b123f0ceb8b178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正在正常跑 baseline（136 samples），没有崩溃。

---

## 汇报

### 修复内容
**SteeringHook.__call__** 两处改动：
1. **2D case (KV cache decode)**：`h += self.alpha * d.unsqueeze(0)` → `h[-1] += self.alpha * d` — 只 steer 最后一个 position，与 3D case 的 `position="last"` 行为一致
2. **3D "all" case**：去掉冗余的 `.unsqueeze(0).unsqueeze(0)`，PyTorch broadcasting 自动处理
3. `return output` 保持不变（已经是直接返回原 output，in-place 修改生效）

其余代码无需改动：`self.applied` 初始化、`reset()` 方法、主循环中 `hook.reset()` 调用都已正确。

### Dry-run 结果
- `--dry_run` 数据验证通过：peak_layer=28, probe_acc=0.7757, 136 conflict samples
- **1-sample hook 测试全部通过**：baseline / alpha=5 / alpha=-5 三次 generate 均成功，无 IndexError 或 tuple 错误

### classify_answer 逻辑分析（不改动，报告给 Director）

当前逻辑链：
1. `extract_answer_entity(contextual)` — 用正则从全句 contextual_answer 中提取实体（匹配 "is/was/born in/located in/written by" 等模式），匹配失败则返回原句
2. `answers_match(candidate, reference)` — normalize 后做 **substring containment**（`r in c or c in r`）+ **last-word matching**
3. 分类：ctx_match ∧ ¬param → contextual；param ∧ ¬ctx → parametric；both match → both；neither match → neither

**46.3% both/neither 率的可能原因：**
- **substring containment 过于宽泛**：如果 parametric 和 contextual 答案有共同子串（如地名、人名的部分重叠），两者都匹配 → "both" 膨胀
- **extract_answer_entity 覆盖不全**：如果 contextual_answer 不匹配任何预设正则模式，回退到全句比较，substring 更容易误匹配
- **last-word matching 误报**：如果两个答案末尾恰好相同（如都以 "Smith" 结尾），可能把不同答案都判为 match
- 测试样本中 baseline response 也判为 "both"（hook test 中就出现了），说明这是 classify_answer 本身的问题，不是 steering 引入的

**建议方向**（供 Director 决策）：改用 exact entity match 或 token-level F1，去掉 substring containment 的宽松分支。

### 提交状态
完整实验已在 westd-41302 后台运行（PID=470287），136 samples × 10 alphas × (steering + control)，日志在 `/tmp/steering_107.log`。

---
