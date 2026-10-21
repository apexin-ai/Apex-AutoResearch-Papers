# CF Fallback Code Diff 深度分析

**任务**: 验证 Reviewer 关于 W1 CF fallback pilot（DR 14.78% ≈ grammar_only 14.84%）的根因假设  
**生成时间**: 2026-05-15  
**服务器**: westd-16980 `/root/schema_semantic_constrained_ie/`

---

## 1. 代码架构

CF fallback 实现为**独立文件** `compiler/type_mask_processor_cf_fallback.py`（490行），不是对原始 `type_mask_processor.py`（399行）的修改。实验运行时临时切换 import 使用 CF 版本。

`compiler/__init__.py` 仍指向原始版本：
```python
from .type_mask_processor import TypeConstraintProcessor  # 非 CF 版本
```

服务器上无 git 仓库，无法提取 commit-level diff。以下为逐行比对两个文件的关键差异。

---

## 2. 关键代码 Diff

### 2.1 新增：Grammar-First Safety Check（`_apply_type_mask`）

**原始版本**（L345-362）— 直接 mask：
```python
def _apply_type_mask(self, logits, allowed_types):
    disallowed_first_tokens = [
        tid for etype, tid in self._type_first_token.items()
        if etype not in allowed_types
    ]
    if disallowed_first_tokens:
        logits[disallowed_first_tokens] = float("-inf")
    return logits
```

**CF 版本**（L415-445）— 增加 grammar-first 安全检查：
```python
_GRAMMAR_MASK_THRESHOLD = -1e8  # L414

def _apply_type_mask(self, logits, allowed_types):
    TypeConstraintProcessor.total_mask_calls += 1       # 新增计数

    if not allowed_types:
        return logits

    disallowed_first_tokens = [...]

    if not disallowed_first_tokens:
        return logits

    # ★ 核心变更：检查是否有 semantically-allowed type 未被 grammar mask
    any_allowed_valid = any(
        logits[self._type_first_token[t]].item() > self._GRAMMAR_MASK_THRESHOLD
        for t in allowed_types
        if t in self._type_first_token
    )
    if not any_allowed_valid:
        # 所有 semantically-valid types 已被 grammar 抑制 → 跳过 semantic mask
        self._grammar_first_skip_count += 1
        TypeConstraintProcessor.grammar_first_fallback_count += 1
        return logits  # ← 返回未修改的 logits = 等同 grammar-only
    
    logits[disallowed_first_tokens] = float("-inf")
    return logits
```

### 2.2 修改：`_mask_head_type` — registry type 覆盖 D/R

**原始版本**（L308-320）：
```python
def _mask_head_type(self, logits):
    # ... 获取 allowed_dr ...
    head_text = self.state.current_head_text
    if head_text:
        actual_type = self.state.entity_registry.get_type(head_text)
        if actual_type and actual_type in self._type_first_token:
            if allowed_dr is None or actual_type in allowed_dr:
                return self._apply_type_mask(logits, {actual_type})
            # ↑ actual_type NOT in allowed_dr 时直接 fall through

    if allowed_dr is not None:                # ← D/R 约束生效
        return self._apply_type_mask(logits, allowed_dr)
    return logits
```

**CF 版本**（L315-340）：
```python
def _mask_head_type(self, logits):
    # ... 获取 allowed_dr ...
    head_text = self.state.current_head_text
    if head_text:
        actual_type = self.state.entity_registry.get_type(head_text)
        if actual_type and actual_type in self._type_first_token:
            if allowed_dr is None or actual_type in allowed_dr:
                return self._apply_type_mask(logits, {actual_type})
            else:
                # ★ CF fallback: registry type 与 D/R 冲突时强制使用 registry type
                self._cf_fallback_count += 1
                TypeConstraintProcessor.cf_registry_fallback_count += 1
                return self._apply_type_mask(logits, {actual_type})  # ← 强制 registry type！

    if allowed_dr is not None and allowed_dr:
        return self._apply_type_mask(logits, allowed_dr)
    return logits
```

### 2.3 修改：`_mask_tail_type` — 同样的 registry 覆盖逻辑

**原始版本**（L333-347）— 当 `actual_type not in allowed_dr` 时 fall through，用 D/R 约束。

**CF 版本**（L355-385）— 当 `actual_type not in allowed_dr` 时强制 registry type：
```python
                else:
                    # ★ CF fallback: 强制 registry type 以防 CF 违规
                    self._cf_fallback_count += 1
                    TypeConstraintProcessor.cf_registry_fallback_count += 1
                    return self._apply_type_mask(logits, {actual_type})
```

### 2.4 新增：Fallback 统计机制

CF 版本新增类级别计数器和统计接口：
```python
class TypeConstraintProcessor(LogitsProcessor):
    grammar_first_fallback_count = 0   # 类级别
    cf_registry_fallback_count = 0
    total_mask_calls = 0

    @classmethod
    def reset_fallback_stats(cls): ...
    
    @classmethod
    def get_fallback_stats(cls): ...
```

---

## 3. CF Fallback 完整执行流程

```
model.generate() 每步调用 logits_processor 链：
  │
  ├─ [1] XGrammar LogitsProcessor
  │   └─ 设置 grammar-invalid tokens 的 logits 为极负值 (≈ -1e10)
  │
  └─ [2] TypeConstraintProcessor.__call__(input_ids, scores)
      │
      ├─ decode generated_text
      ├─ PositionDetector.detect() → 更新 state + 返回 FieldPosition
      │
      ├─ ENTITY_TYPE → _mask_entity_type()
      │   └─ allowed = 全部 6 种 entity type → _apply_type_mask(all_types)
      │       └─ disallowed 为空 → 直接返回（无实际约束）
      │
      ├─ RELATION_HEAD_TYPE → _mask_head_type()
      │   ├─ 获取 allowed_dr = constraint.valid_head_types()
      │   ├─ 查 entity_registry.get_type(head_text)
      │   │
      │   ├─ [Case A] registry 有 type 且 type ∈ allowed_dr
      │   │   └─ _apply_type_mask({actual_type})
      │   │       ├─ [首 token] grammar 允许该 type → mask 其他 → semantic 生效
      │   │       └─ [续 token] grammar 只允许续写 → type first-tokens 全被 grammar 抑制
      │   │           └─ grammar-first fallback → 跳过 semantic（本来也是 no-op）
      │   │
      │   ├─ [Case B] registry 有 type 但 type ∉ allowed_dr → ★ CF FALLBACK
      │   │   └─ 强制 _apply_type_mask({actual_type})  ← 忽略 D/R 约束！
      │   │       └─ 同样经过 grammar-first check
      │   │
      │   └─ [Case C] registry 无该 entity
      │       └─ _apply_type_mask(allowed_dr) → 正常 D/R 约束
      │
      ├─ RELATION_TAIL_TYPE → _mask_tail_type()
      │   └─ 逻辑同上，但约束基于 (relation_type, head_type) 对
      │
      └─ FREE_TEXT / UNKNOWN → 不做任何 masking
```

---

## 4. 实验数据对比

### 4.1 三配置结果（SciERC, 551 samples, Qwen3-8B）

| 配置 | DR violations | DR rate | CF violations | CF rate | Rel F1 |
|------|-------------|---------|---------------|---------|--------|
| **Original full_s1** | 16/1729 | **0.93%** | 245 | **9.90%** | 0.0836 |
| **CF fallback** | 255/1725 | **14.78%** | 1 | **0.04%** | 0.0823 |
| **Grammar only** | 256/1725 | **14.84%** | 2 | **0.08%** | 0.0823 |

### 4.2 Fallback 统计（CF fallback pilot）

| 指标 | 值 | 占比 |
|------|-----|------|
| Total mask calls | 17,024 | 100% |
| Grammar-first fallback | 6,237 | 36.64% |
| CF registry fallback | 763 | 4.48% |
| 正常 semantic masking | ~10,024 | ~58.88% |

### 4.3 Per-Relation DR 对比

| 关系类型 | CF fallback DR | Original full_s1 DR | valid_pairs 数/36 |
|----------|---------------|---------------------|-------------------|
| Used-for (791) | 0.25% | 0.0% | 35 (97.2%) |
| Feature-of (494) | **31.98%** | **1.21%** | ≤20 (~55%) |
| Evaluate-for (134) | **23.13%** | **5.76%** | 23 (63.9%) |
| Compare (71) | **39.44%** | **2.82%** | ≤12 (~33%) |
| Part-of (77) | **23.38%** | 0.0% | ≤15 (~42%) |
| Hyponym-of (125) | **14.40%** | 0.0% | ≤15 (~42%) |
| Conjunction (33) | 0.0% | 0.0% | 36 (100%) |

Feature-of, Compare, Evaluate-for, Part-of, Hyponym-of 的 DR 在 CF fallback 中飙升至 grammar-only 水平。这些正是约束最紧的关系类型。

---

## 5. 根因分析

### 5.1 DR ≈ grammar_only 的直接原因

**不是** entity registry 被禁用——registry 完全正常运作（register/get_type 函数未修改）。

**真正原因：CF fallback 版本改变了 D/R conflict 的处理策略。**

| 场景 | 原始版本行为 | CF 版本行为 |
|------|-------------|-------------|
| registry type ∈ allowed_dr | 强制 registry type（两者一致） | 强制 registry type（两者一致） |
| **registry type ∉ allowed_dr** | **fall through → 用 D/R 约束** | **强制 registry type → D/R 违规** |
| entity 未注册 | 用 D/R 约束 | 用 D/R 约束 |

关键差异仅在第二行：当 entity registry 的 type 与 D/R 约束冲突时，原始版本选择 D/R 约束（牺牲 entity 一致性），CF 版本选择 registry type（牺牲 D/R 合规性）。

### 5.2 为什么原始版本能达到 DR 0.93%

原始版本在冲突位置用 `allowed_dr` 覆盖 registry type：
- `head_type` / `tail_type` 字段输出 D/R-valid 的 type
- 但该 type 可能与 entity list 中该 entity 的 type 不一致
- 这就是 **245 个 CF violations** 的来源

### 5.3 Grammar-first fallback 的角色

36.64% 的 grammar-first fallback 看似很高，但**大部分发生在 type 值的续写 token**（非首 token）：
- 首 token 时：grammar 允许所有 valid type first-tokens → semantic mask 可以正常应用
- 续 token 时：grammar 只允许已选 type 的续写 → 所有 type first-tokens 被 grammar 抑制 → fallback 触发

这是**结构性 no-op**——原始版本在续 token 位置也只是多余地执行 `logits[already_masked] = -inf`。

粗略估算验证：
- entity type calls ≈ 551 × 4 × 3 ≈ 6,600（无约束力，early return）
- head/tail 续 token calls ≈ 551 × 3 × 2 × 2 ≈ 6,600（grammar-first fallback）
- 观测 grammar-first fallback = 6,237：与估算基本吻合

### 5.4 SciERC 约束松紧度的影响

Used-for 有 35/36 valid pairs → 约束几乎无效 → DR 本来就低。
DR 降低主要来自 Feature-of、Compare 等约束较紧的关系——而这些正是 CF registry fallback 最频繁触发的位置（entity type 分布导致更多 type-DR 冲突）。

---

## 6. Reviewer 假设验证

### Reviewer 原始假设
> CF fallback 代码修改可能禁用/削弱了 entity registry 的类型传播机制，导致 semantic 层虽被调用但无法获取 head entity type → pair-based tail masking 退化

### 验证结论：**(B) 部分确认**

**确认的部分：**
- ✅ semantic 层确实被调用（17,024 次 mask calls）
- ✅ pair-based tail masking 确实退化——但不是退化为 "full range"，而是被 registry type 覆盖
- ✅ 最终效果等同 grammar-only

**需要修正的部分：**
- ❌ entity registry 并未被"禁用"或"削弱"——register() 和 get_type() 完全正常
- ❌ 不是"无法获取 head entity type"——head_type 正常从 registry 获取
- ❌ 不是 pair-based masking "退化为 full range"——而是在 type conflict 时被 registry type 直接覆盖

**精确机制：**  
CF fallback 的设计意图是"entity registry 的 type 总是正确的，D/R 约束应该让步"。当 registry type 与 D/R 冲突时，选择 registry type → head_type/tail_type 与 entity list 一致 → CF 0.04%。但 D/R 约束在冲突位置不再执行 → DR 回到 grammar-only 水平。

**更准确的描述：**  
CF fallback 不是"禁用了 registry"，而是**"过度信任了 registry"**——把 registry type 视为 ground truth，在 D/R conflict 时覆盖 semantic masking 输出。这从根本上颠倒了约束优先级。

---

## 7. 对论文叙事的影响

### 推荐叙事方向：**Trade-off**（权衡）

数据展示了一个 **DR ↔ CF 的零和权衡**：

```
                     DR ↑                    CF ↑
Grammar only:    14.84%  ──────────────  0.08%
CF fallback:     14.78%  ──────────────  0.04%     (entity 一致性优先)
                    ↕ 权衡轴
Original full_s1: 0.93%  ──────────────  9.90%     (D/R 合规性优先)
```

### 不应使用的叙事

- ❌ **"Enabling mechanism"**：CF fallback 并未"启用"什么新能力，它是一种退化——与 grammar-only 数值等价
- ❌ **"Semantic layer 无效"**：原始 full_s1 证明 semantic layer 有效（DR 0.93% vs 14.84%），CF fallback 只是改变了优先级
- ❌ **"Bug in CF fallback"**：这是设计选择（registry consistency > DR compliance），不是 bug

### 推荐论文表述

> The CF fallback experiment reveals a fundamental trade-off between domain/range compliance (DR) and cross-field consistency (CF). The original semantic layer reduces DR from 14.84% to 0.93% by overriding entity registry types at conflict positions, at the cost of 9.9% CF violations. The CF-prioritized variant eliminates CF violations (0.04%) by forcing registry types, but this restores DR to grammar-only levels (14.78%). This demonstrates that DR enforcement and entity consistency are competing objectives under the current single-pass architecture, motivating future work on joint resolution strategies (e.g., two-pass generation or backtracking).

---

## 8. 附录：Fallback 触发条件总结

| Fallback 类型 | 触发条件 | 效果 | 频率 |
|--------------|---------|------|------|
| Grammar-first | `_apply_type_mask`: 所有 semantically-allowed types 的 logits < -1e8 | 跳过 semantic mask → 等同 grammar-only | 36.64% (6237/17024) |
| CF registry (head) | `_mask_head_type`: registry type ∉ allowed_dr | 强制 registry type → D/R violation | 4.48% (763/17024，含 head+tail) |
| CF registry (tail) | `_mask_tail_type`: registry type ∉ allowed_dr for (rel, head) | 强制 registry type → D/R violation | 包含在上述 763 中 |
