# CF Fallback 代码 Diff 分析报告

**任务**: 验证 Reviewer 关于 W1 CF fallback pilot (`DR 14.78% ≈ grammar_only 14.84%`) 的根因假设
**生成时间**: 2026-05-15
**服务器**: westd-16980 `/root/schema_semantic_constrained_ie/`
**Pilot 实验**: `w1_cf_fallback_scierc_pilot` (Qwen3-8B × SciERC, 551 samples)

---

## 0. 关键前置事实

### 0.1 项目不是 git 仓库

```
$ ls /root/schema_semantic_constrained_ie/.git
ls: cannot access '...': No such file or directory
```

无 `git log` / `git diff` 可用，所有对比基于 **保存的快照文件**。

### 0.2 文件快照状态（用 md5sum 确认，2026-05-15 23:24）

| 路径 | 大小 | mtime | md5 |
|---|---:|---|---|
| `compiler/type_mask_processor.py` | 15 666 B | 2026-05-15 23:24:33 | `e957f43206…ceb594` |
| `compiler/type_mask_processor.py.bak` | 15 666 B | 2026-05-14 11:06:30 | `e957f43206…ceb594` *(同上)* |
| `compiler/type_mask_processor_cf_fallback.py` | 20 195 B | 2026-05-15 23:24:33 | `82aea5ee5c…ab2237` |

**关键事实**: 当前生产文件 `type_mask_processor.py` 与 `.bak`（CF fallback 引入之前的快照）**字节级别完全相同**。CF fallback 代码已被 `worker_code_revert_cf_fallback` (2026-05-15 15:22) 回退到 `.bak`，CF 版本被另存为 `type_mask_processor_cf_fallback.py`。

### 0.3 Pilot 实际运行的代码版本

Pilot 运行时间窗：2026-05-15 14:07 (RUNNING) → 14:57 (DONE)，**早于 15:22 的回退**。故 pilot 实际跑的是 `type_mask_processor_cf_fallback.py` 的内容（490 行）。

运行确证：`outputs/w1_cf_fallback_scierc_pilot_fallback_stats.json` 含 `cf_registry_fallback_count: 763`，而该计数器仅存在于 CF fallback 版本（`.bak` 与当前 .py 都没有 `reset_fallback_stats` / `get_fallback_stats`）。

下文所有 "CF fallback 行号" 均指 `type_mask_processor_cf_fallback.py`。

---

## 1. 代码 Diff（pilot 版本 vs 当前/.bak 基线）

完整 unified diff (`diff -u type_mask_processor.py type_mask_processor_cf_fallback.py`)，重点段落：

### 1.1 模块顶部：日志器（+2 行）

```diff
@@ L34-44 @@
 import re
+import logging
 from dataclasses import dataclass, field
 ...
 from .ontology_compiler import ConstraintSpec
+
+logger = logging.getLogger(__name__)
```

### 1.2 类属性 + 类方法：全局计数器（+22 行，cf_fallback.py L188-211）

```diff
@@ class TypeConstraintProcessor @@
+    grammar_first_fallback_count = 0
+    cf_registry_fallback_count = 0
+    total_mask_calls = 0
+
+    @classmethod
+    def reset_fallback_stats(cls): ...
+
+    @classmethod
+    def get_fallback_stats(cls):
+        return {
+            "grammar_first_fallback_count": ...,
+            "cf_registry_fallback_count":   ...,
+            "total_mask_calls":             ...,
+            "grammar_first_fallback_rate":  ...,
+            "cf_registry_fallback_rate":    ...,
+        }
```

`run_constrained_extraction.py:691, 754` 调用这两个 classmethod 写出 `*_fallback_stats.json`。

### 1.3 `__init__`：实例计数器（+2 行，cf_fallback.py L227-228）

```diff
         self._type_first_token, self._all_type_first_tokens = self._build_first_token_map()
+        self._grammar_first_skip_count = 0
+        self._cf_fallback_count = 0
```

### 1.4 `_mask_head_type`：CF 回退分支（**核心改动**，cf_fallback.py L312-337）

```diff
-        - If entity type known but NOT D/R-valid → use D/R constraint
+    - If entity type known but NOT D/R-valid → force registered type
+      (W1: registry consistency > DR compliance, prevents CF violations)
 
         rel_type = self.state.current_relation_type
         constraint = self.spec.get_constraint(rel_type) if rel_type else None
         allowed_dr = constraint.valid_head_types() if constraint else None
 
         head_text = self.state.current_head_text
         if head_text:
             actual_type = self.state.entity_registry.get_type(head_text)
             if actual_type and actual_type in self._type_first_token:
                 if allowed_dr is None or actual_type in allowed_dr:
                     return self._apply_type_mask(logits, {actual_type})
+                else:
+                    # W1 registry-consistent fallback
+                    self._cf_fallback_count += 1
+                    TypeConstraintProcessor.cf_registry_fallback_count += 1
+                    logger.debug("CF fallback (head): '%s' registered as '%s' not in dom(%s)", ...)
+                    return self._apply_type_mask(logits, {actual_type})  # <-- 强制注册类型
 
-        if allowed_dr is not None:
+        if allowed_dr is not None and allowed_dr:
             return self._apply_type_mask(logits, allowed_dr)
         return logits
```

### 1.5 `_mask_tail_type`：CF 回退分支（与 head 对称，cf_fallback.py L357-382）

```diff
         tail_text = self.state.current_tail_text
         if tail_text:
             actual_type = self.state.entity_registry.get_type(tail_text)
             if actual_type and actual_type in self._type_first_token:
                 if allowed_dr is None or actual_type in allowed_dr:
                     return self._apply_type_mask(logits, {actual_type})
+                else:
+                    # W1 registry-consistent fallback: registered type conflicts
+                    # with range(r, head_type). Force registered type to prevent CF violations.
+                    self._cf_fallback_count += 1
+                    TypeConstraintProcessor.cf_registry_fallback_count += 1
+                    return self._apply_type_mask(logits, {actual_type})
 
-        if allowed_dr is not None:
+        if allowed_dr is not None and allowed_dr:
             return self._apply_type_mask(logits, allowed_dr)
         return logits
```

注意：`allowed_dr` 计算 **未变** — pair-based `valid_tail_types_for_head(head_type)` 仍是 normal path 默认（cf_fallback.py L353）。

### 1.6 `_apply_type_mask`：Grammar-first 守卫（**核心改动**，cf_fallback.py L385-447）

```diff
+    # Grammar-First Invariant: semantic mask ⊆ grammar allowed set
+    # When XGrammar marks grammar-invalid tokens with finite negative values (e.g., -1e10)
+    # rather than -inf, and semantic masking sets all grammar-valid type tokens to -inf,
+    # argmax selects a grammar-invalid token → XGrammar accept_token assertion failure.
+    _GRAMMAR_MASK_THRESHOLD = -1e8
+
     def _apply_type_mask(self, logits, allowed_types):
+        TypeConstraintProcessor.total_mask_calls += 1
+
+        if not allowed_types:
+            return logits
+
         disallowed_first_tokens = [
             tid for etype, tid in self._type_first_token.items()
             if etype not in allowed_types
         ]
-        if disallowed_first_tokens:
-            logits[disallowed_first_tokens] = float("-inf")
+        if not disallowed_first_tokens:
+            return logits
+
+        # Verify at least one allowed type has a non-grammar-masked logit
+        any_allowed_valid = any(
+            logits[self._type_first_token[t]].item() > self._GRAMMAR_MASK_THRESHOLD
+            for t in allowed_types
+            if t in self._type_first_token
+        )
+        if not any_allowed_valid:
+            self._grammar_first_skip_count += 1
+            TypeConstraintProcessor.grammar_first_fallback_count += 1
+            logger.warning("Grammar-first fallback triggered (skip_count=%d): semantic mask would eliminate all grammar-valid tokens", ...)
+            return logits          # <-- 完全放弃 semantic mask
+
+        logits[disallowed_first_tokens] = float("-inf")
         return logits
```

### 1.7 总修改量

```
diff -u type_mask_processor.py type_mask_processor_cf_fallback.py
→ +91 行（净增），200 行 diff 输出
```

---

## 2. CF Fallback 执行流程图（文字描述）

```
每个 decoding step 进入 TypeConstraintProcessor.__call__:
    │
    ├─ PositionDetector.detect(generated_text, state)
    │   ├─ 用 _RE_ENTITY 解析 entities 段，逐条 register(text, type) 到 entity_registry
    │   ├─ 用 _RE_REL_TYPE_VAL / _RE_HEAD_TYPE_VAL / _RE_HEAD_TEXT_VAL / _RE_TAIL_TEXT_VAL
    │   │   解析最后一个 relation 对象，更新 state.current_{relation_type, head_type,
    │   │   head_text, tail_text}
    │   └─ 用 last-100-chars regex 判定 FieldPosition
    │
    ├─ position == ENTITY_TYPE:
    │       allowed_types = set(spec.entity_types)         # 全 6 种
    │       → _apply_type_mask
    │           ├─ total_mask_calls += 1
    │           ├─ disallowed_first_tokens = []            # 没有 type 被排除
    │           └─ 立即 return logits                       # ★ early return, 不计入任何 fallback
    │
    ├─ position == RELATION_HEAD_TYPE:
    │       rel = state.current_relation_type
    │       allowed_dr = constraint.valid_head_types()     # 不依赖 head_type，是 union
    │       head_text = state.current_head_text            # 来自已写出的 "head":"…"
    │       actual_type = entity_registry.get_type(head_text)
    │       ┌────────────────────────────────────────────────┐
    │       │  分支 A: actual_type ∈ allowed_dr              │
    │       │     → _apply_type_mask({actual_type})  (强制 1 种) │
    │       │                                                │
    │       │  分支 B: actual_type ∉ allowed_dr  ★CF 回退★  │
    │       │     cf_registry_fallback_count += 1            │
    │       │     → _apply_type_mask({actual_type})          │
    │       │     ※ 强制使用 registry 类型，覆盖 D/R 约束       │
    │       │     ※ 这一次 mask 一定产生 DR 违规                │
    │       │                                                │
    │       │  分支 C: head_text 未注册 / 缺失                 │
    │       │     → _apply_type_mask(allowed_dr)             │
    │       └────────────────────────────────────────────────┘
    │
    ├─ position == RELATION_TAIL_TYPE:
    │       与 HEAD 完全对称，唯一差别：
    │       allowed_dr = valid_tail_types_for_head(head_type)   # ★ pair-based, 用 head_type
    │       若 head_type 为 None (state 还没解析到) → 退化为 valid_tail_types() (union)
    │
    └─ _apply_type_mask(logits, allowed_types):
          ├─ total_mask_calls += 1
          ├─ if not allowed_types: return                        # ★ 空集守卫
          ├─ disallowed = {first_tokens of (entity_types − allowed)}
          ├─ if not disallowed: return                           # ★ 全允许时短路
          │
          ├─★ Grammar-first 守卫:
          │      any_allowed_valid = ∃ t ∈ allowed_types: logits[first_token[t]] > -1e8
          │      if not any_allowed_valid:
          │          grammar_first_fallback_count += 1
          │          return logits                               # ★ 放弃 semantic
          │
          └─ logits[disallowed] = -inf                            # 正常生效
```

**Pilot 实测（17 024 次 mask 调用，551 SciERC 样本）**:

| 通道 | 次数 | 占比 | 实际语义效果 |
|---|---:|---:|---|
| Normal mask（含 ENTITY_TYPE 全允许短路） | 10 024 | 58.85 % | 标记 disallowed first-token = -∞ |
| Grammar-first 跳过 | 6 237 | 36.64 % | **放弃 semantic mask，仅 grammar 控制** |
| CF registry 覆盖 | 763 | 4.48 % | **强制 registry 类型，覆盖 D/R 约束** |

日志直接证据（`/root/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log`）：`grep -c "Grammar-first fallback" → 6237`，等于 stats JSON 里的 count。

---

## 3. Reviewer 假设逐条验证

Reviewer 的三种候选行为：
- **(A)** 用 registry type 覆盖 constraint → semantic masking 正常但基于不同 type
- **(B)** 放弃 registry type → head_type 未知 → pair-based masking 退化为 full range
- **(C)** 跳过 semantic masking entirely → 等同 grammar-only

### 3.1 (A) **确认成立**（路径明确，频次 4.48 %）

- 代码证据: `type_mask_processor_cf_fallback.py:312-337`（head）、`:357-382`（tail）`else` 分支显式 `return self._apply_type_mask(logits, {actual_type})`。
- 运行证据: `cf_registry_fallback_count = 763 / 17 024 = 4.48 %`。
- 语义后果: 每一次都把 `state.current_relation_type` 的 D/R 约束 **覆盖** 为 `entity_registry` 里的类型，产生 763 次 token-级 DR 违规决策（折算到 triple 级数量会被多 token 类型名重复计数 + 同一 mention 多次出现稀释，可能落在 100 ~ 200 triples 的量级，但确定 > 0）。

### 3.2 (B) **不成立**

- `state.current_head_type` 来自 `_RE_HEAD_TYPE_VAL = r'"head_type"\s*:\s*"([^"]+)"'`，**只依赖已生成的 JSON 文本**，与 entity_registry **完全无关**。
- 在 RELATION_TAIL_TYPE 位置，`head_type` 字段已被模型写完闭合（紧邻 tail_type 之前），regex 一定匹配到 → `state.current_head_type` 一定非空 → `valid_tail_types_for_head(head_type)` 一定被调用，**没有"退化为 union"的代码路径**。
- 即使 `head_type` 解析失败（理论上的 None 分支），代码也只是退化为 `valid_tail_types()`（仍是 D/R 约束的 union），不是"full range / no mask"。

### 3.3 (C) **确认成立**（频次 36.64 %）

- 代码证据: `_apply_type_mask` 的 grammar-first 守卫（`type_mask_processor_cf_fallback.py:432-441`）在 `allowed_types` 全部 grammar-masked 时直接 `return logits`，**完全放弃 semantic mask**。
- 运行证据: `grammar_first_fallback_count = 6 237 / 17 024 = 36.64 %`，日志里有 6 237 行 `Grammar-first fallback triggered` 与该计数一致。
- 语义后果: 在被跳过的 36.64 % token-step 上，TypeConstraintProcessor 等价于一个 no-op，**这一步退化为 grammar_only**。

### 3.4 综合判定

Reviewer 推断的核心结论 — **"semantic 层虽被调用但无法获取 head entity type → pair-based tail masking 退化"** — 是 **部分确认 + 部分修正**:

- ✅ **现象正确**: semantic 层在 41.12 % (= 36.64 % + 4.48 %) 的 mask 调用上 **没有实际约束效果**，叠加 ENTITY_TYPE 位置的全允许短路（即便归在"Normal"通道里也是 no-op），**真正切断 token 的 mask 调用占比远低于"100 % 调用率"暗示的数值**。
- ❌ **机制误判**: 失效不来自 `head_type` 解析不到，而来自:
    1. (C) Grammar-first 守卫主动放弃 mask — 因为多 token 类型名的 token 2..N 上，所有 entity-type first-token 都已被 grammar 屏蔽，`any_allowed_valid=False` → 跳过。这条 path 大部分情况是 **无害的**（首 token 上的 mask 已经把类型锁死了，后续 token 由 grammar 强制续写），但它把"semantic mask 调用次数"打了 36.64 % 的水分。
    2. (A) CF registry 覆盖 — 主动放弃 D/R，去保 CF 一致性。**这条 path 每一次都是有害的**: 把"可能违反 CF"的 token 改成"必然违反 D/R"的 token。

**为什么 DR 14.78 % ≈ grammar_only 14.84 %**: 
- Channel (A) 直接制造 DR 违规
- Channel (C) 放弃 DR 防护
- 剩下的 58.85 % "Normal" 通道里又有相当一部分是 ENTITY_TYPE 短路 (no-op) + multi-token 类型首 token 后的 trivial 应用，能真正影响 head/tail 选择的"硬约束"调用占比远低于 58.85 %
- 三者叠加 → 端到端等价于 grammar_only

证据链补充: 已有 `artifacts/w1_cf_fallback_scierc_pilot/report/w1_cf_fallback_pilot_detailed_analysis.md` 的 Section 5.2 已独立得出相同结论 — "When the semantic mask is most restrictive, the grammar-first guard fires most often."

---

## 4. 论文叙事建议

### 4.1 推荐: **"Shared Violation Budget / Trade-off"** 框架

**不推荐** 用 "enabling mechanism" / "CF fallback enables semantic enforcement"：CF fallback 在代码层面是 **替换**（用 registry 类型覆盖 D/R）而非 **增强**（联合两种约束）。任何把它包装成"enabling"的措辞都站不住脚 — Reviewer 一旦复盘 diff (4.5 % CF 覆盖 + 36.6 % grammar 跳过)，会发现叙事与代码不一致。

**推荐叙事 (3 个 load-bearing claim, 与现有 detailed_analysis.md 一致)**:

1. **Mask-invocation count is NOT enforcement strength** 
   - 数据: 17 024 次 mask 调用中只有 58.85 % 通过 grammar-first 守卫，其中再扣除 CF 覆盖的 4.48 %，"effective semantic enforcement" 上界 ≈ 58.85 %（实际更低，因为 ENTITY_TYPE no-op 和 multi-token 续写 token 不构成硬约束）。
   - 论文建议同时报告 *coverage*（mask processor 被挂上的 token 比例）和 *effective coverage*（实际有 disallowed-token 被置 -∞ 且决定 argmax 的比例）。

2. **CF 和 DR 共享一个违规预算**
   - Baseline (full_s1): DR 0.93 % + CF 9.90 % = 10.83 %
   - CF Fallback pilot: DR 14.78 % + CF 0.04 % = 14.82 %
   - 消 CF (9.86 pp ↓) 的代价是 + DR (13.85 pp ↑)，总预算反而上升 +3.99 pp。
   - 直接证据: hierarchical fallback（先 CF 后 DR）无法同时降低两者；需要 **joint mask**（CF ∧ D/R 的交集）才能真正减小总违规预算。

3. **Tightness 是 fallback 风险的预测因子**
   - 表 2 (`detailed_analysis.md` §2) 显示 Compare (tightness 0.528) ΔDR = +36.62 pp，远高于 Used-for (tightness 0.028) ΔDR = +0.25 pp。Spearman ≈ 1.0。
   - 高 tightness 关系下，`valid_tail_types_for_head` 集合很小，越容易触发 grammar-first 跳过和 CF 覆盖。
   - 论文 implication: **联合掩码 / 回溯解码 / 训练时对齐** 是密集约束 schema 的可行路线；纯前向 fallback decoding 不行。

### 4.2 在 paper 里如何措辞

错误措辞: "CF fallback enables semantic enforcement by …"
正确措辞: "We expose a hierarchical fallback policy (CF-priority → D/R-priority) and quantify its limitation: silencing CF violations re-emerges as D/R violations because the two constraint surfaces share a single violation budget. The 4.5 % CF-override and 36.6 % grammar-first-skip rates measured on Qwen3-8B × SciERC are direct mechanism-level evidence."

把这次 pilot 写成 **negative result motivating joint masking**，比试图把它包装成 positive 更稳，也更对得起 reviewer 的预期。

---

## 5. 附录 A — 文件与时间线

```
2026-05-14 11:06  type_mask_processor.py.bak             # baseline 快照
2026-05-15 05:00  type_mask_processor.py (Birth)
2026-05-15 09:59  worker_code_w1_cf_registry_consistent_fallback   # CF fallback 实现
2026-05-15 13:34  worker_code_cf_fallback_logging                  # 加日志/计数器
2026-05-15 14:07  pilot RUNNING (CF fallback 生效)
2026-05-15 14:57  pilot DONE → fallback_stats.json
2026-05-15 15:22  worker_code_revert_cf_fallback  # 拷贝 .bak 覆盖 .py
2026-05-15 15:24  type_mask_processor.py mtime (revert 完成，与 .bak 字节同)
2026-05-15 15:42  本次分析任务启动
```

## 6. 附录 B — 关键 Stats（来自 outputs/w1_cf_fallback_scierc_pilot_fallback_stats.json）

```json
{
  "grammar_first_fallback_count": 6237,
  "cf_registry_fallback_count":   763,
  "total_mask_calls":             17024,
  "grammar_first_fallback_rate":  0.366365,
  "cf_registry_fallback_rate":    0.044819
}
```

`grep -c "Grammar-first fallback" /root/runs/schema_semantic_constrained_ie/w1_cf_fallback_scierc_pilot.log → 6237` ✓ 一致
`grep -c "CF fallback" ... → 0`（logger.debug 级别未启用，仅有计数器证据；建议未来把 CF 路径升级到 INFO 以便日志可追溯）。

## 7. 附录 C — 建议下一步代码改动（若决定继续 W1）

1. **CF fallback 日志升级**: `logger.debug` → `logger.info`，并加 `cf_break_reason` 字段，让每一次覆盖都能在 jsonl 里追溯。
2. **Per-relation 计数器**: 把 `grammar_first_fallback_by_relation: dict[str,int]` 与 `cf_registry_fallback_by_relation: dict[str,int]` 加到类属性里，~10 LOC，可以让 detailed_analysis.md §3 的"per-relation 调用归属"从估算变成直接读取。
3. **Per-doc breakdown**: 在 jsonl 输出里加 `{effective, grammar_override, cf_override}` 字段，便于离线复盘单文档。
4. **不必恢复**: 既然 W1 已被判负，主线 `type_mask_processor.py` 不需要再切回 CF fallback；但 `_cf_fallback.py` 应保留作为 reviewer 复现实验时的副本。
