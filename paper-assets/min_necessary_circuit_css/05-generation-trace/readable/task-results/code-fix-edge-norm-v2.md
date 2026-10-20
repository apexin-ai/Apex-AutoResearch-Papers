# code fix edge norm v2

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_edge_norm_v2_20260512T172249_result.json`
- **Structured JSON:** [`37dea32c07c1eccb9fc7.json`](../../sessions/37/37dea32c07c1eccb9fc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新增了 `torch_dtype` 的 deprecation warning（正常）。模型仍在加载中，进程正常运行。

---

**汇报：**

### 1. 修复 diff

**Bug 1 — `_normalize_eap_edge` QKV 角括号解析：**
```diff
 def _normalize_eap_edge(edge_str: str) -> str:
     parts = edge_str.strip().split('->')
     if len(parts) == 2:
-        src = parts[0].strip().strip('<>')
-        dst = parts[1].strip().strip('<>')
-        return f'{_normalize_ac_node(src)}->{_normalize_ac_node(dst)}'
+        src_raw = parts[0].strip().strip('<>')
+        dst_raw = parts[1].strip()
+        m = re.match(r'(.+)<([qkvQKV])>$', dst_raw)
+        if m:
+            dst_node, qkv = m.groups()
+            dst_node = dst_node.strip('<>')
+            return f'{_normalize_ac_node(src_raw)}->{_normalize_ac_node(dst_node)}.{qkv.lower()}'
+        dst_raw = dst_raw.strip('<>')
+        return f'{_normalize_ac_node(src_raw)}->{_normalize_ac_node(dst_raw)}'
     return edge_str.strip().strip('<>').lower()
```

**Bug 2 — `_normalize_ac_node` MLP 命名扩展 + 前移：**
```diff
     if low in ('resid_end', 'resid_post', 'logits', 'output'):
         return 'logits'
+    m = re.match(r'(?:mlp[\s_]*|m)(\d+)$', node_str, re.IGNORECASE)
+    if m:
+        return f'm{m.group(1)}'
     m = re.match(r'A(\d+)\.(\d+)(?:\.([QKV]))?', node_str)
     if m:
         l, h, qkv = m.groups()
         ...
         return r
-    m = re.match(r'M(\d+)', node_str)
-    if m:
-        return f'm{m.group(1)}'
     return node_str.lower()
```

**Bug 3 — 测试用例替换：**
```diff
-    test_pairs = [
-        ('&lt;A0.0>->&lt;M0>', 'A0.0->M0'),
-        ('&lt;Resid Start>->&lt;A0.0>', 'Resid Start->A0.0'),
-        ('&lt;A1.2.Q>->&lt;A1.2.K>', 'A1.2.Q->A1.2.K'),
-        ('&lt;M3>->&lt;Resid End>', 'M3->Resid End'),
-        ('&lt;resid_pre>->&lt;A0.0>', 'Resid_Start->A0.0'),
-        ('&lt;resid_post>->&lt;M0>', 'Resid_End->M0'),
-    ]
+    test_pairs = [
+        ('input->a0.h0&lt;q>', 'Resid Start->A0.0.Q'),
+        ('a0.h0->m0',       'A0.0->MLP 0'),
+        ('m0->a1.h3&lt;k>',    'MLP 0->A1.3.K'),
+        ('a9.h9->logits',   'A9.9->Resid End'),
+    ]
```

### 2. 验证输出

4 组全部 OK：
```
[OK] EAP 'input->a0.h0&lt;q>'    -> 'input->a0.h0.q'
     AC  'Resid Start->A0.0.Q' -> 'input->a0.h0.q'
[OK] EAP 'a0.h0->m0'          -> 'a0.h0->m0'
     AC  'A0.0->MLP 0'        -> 'a0.h0->m0'
[OK] EAP 'm0->a1.h3&lt;k>'       -> 'm0->a1.h3.k'
     AC  'MLP 0->A1.3.K'      -> 'm0->a1.h3.k'
[OK] EAP 'a9.h9->logits'      -> 'a9.h9->logits'
     AC  'A9.9->Resid End'    -> 'a9.h9->logits'
```

### 3. 新 PID
**275600** (tmux session: `mvp_pilot_gpt2_ioi`, GPU cuda:5)

### 4. 日志状态
前几行为正常的 deprecation warnings（`TRANSFORMERS_CACHE`、`torch_dtype`），无报错，模型正在加载中。

---
