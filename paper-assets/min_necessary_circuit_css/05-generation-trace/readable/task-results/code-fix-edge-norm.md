# code fix edge norm

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_edge_norm_20260512T171104_result.json`
- **Structured JSON:** [`aa2d48cddefc1a062889.json`](../../sessions/aa/aa2d48cddefc1a062889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。结果汇总：

### (1) Diff

```diff
+# 2026-05-12: Fixed _normalize_eap_edge to reuse _normalize_ac_node, ensuring consistent canonical edge names across methods.

 def _normalize_eap_edge(edge_str: str) -> str:
-    return edge_str.strip().replace('<', '.').replace('>', '')
+    parts = edge_str.strip().split('->')
+    if len(parts) == 2:
+        src = parts[0].strip().strip('<>')
+        dst = parts[1].strip().strip('<>')
+        return f'{_normalize_ac_node(src)}->{_normalize_ac_node(dst)}'
+    return edge_str.strip().strip('<>').lower()

 def _normalize_ac_node(node_str: str) -> str:
     node_str = node_str.strip()
-    if node_str in ('Resid Start', 'Resid_Start'):
+    low = node_str.lower().replace(' ', '_')
+    if low in ('resid_start', 'resid_pre', 'input', 'embed'):
         return 'input'
-    if node_str in ('Resid End', 'Resid_End'):
+    if low in ('resid_end', 'resid_post', 'logits', 'output'):
         return 'logits'
```

加上尾部 `_verify_edge_normalization()` 验证函数（6 组测试用例）。

### (2) 统一 canonical 格式

```
{src_node}->{dst_node}
```

节点格式：
- 输入节点 → `input`（匹配 `Resid Start`, `Resid_Start`, `resid_pre`, `embed`）
- 输出节点 → `logits`（匹配 `Resid End`, `Resid_End`, `resid_post`, `output`）
- 注意力头 → `a{layer}.h{head}[.{q|k|v}]`（如 `a1.h2.q`）
- MLP → `m{layer}`（如 `m3`）

### (3) Assert 验证结果

`EDGE_NORM_VERIFY: all assertions passed` — 6 组 EAP/AC 等价边名全部输出一致。

**根因**：旧 `_normalize_eap_edge` 做了 `replace('<', '.').replace('>', '')`，既没有语义解析节点名，还把 `->` 中的 `>` 一并删掉。修复后先 split on `->`，再对每个 part 剥尖括号、复用 `_normalize_ac_node` 做语义归一化。

---
