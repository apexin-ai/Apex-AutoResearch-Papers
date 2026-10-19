# code fix eval determinism

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_eval_determinism_20260516T031724_result.json`
- **Structured JSON:** [`89beac29eedaa2268eea.json`](../../sessions/89/89beac29eedaa2268eea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修改摘要

- **文件**: `/root/structfuse/training/train.py`
- **改动 1** (line 86-97): 在 `ContrastiveDataset` 类中添加 `freeze_fallback_negatives(seed)` 方法 — 用独立 `random.Random(seed)` 实例为每个 sample 预计算 fallback negatives 并写入 `self._negatives`
- **改动 2** (line 326): 在 `val_ds` 创建后立即调用 `val_ds.freeze_fallback_negatives(seed=args.seed)`

```diff
+    def freeze_fallback_negatives(self, seed: int = 42):
+        """Pre-compute fallback negatives with a fixed seed for deterministic eval."""
+        rng = random.Random(seed)
+        self._negatives = {}
+        for idx, s in enumerate(self.samples):
+            fallback = list(s.get("neg_candidates", []))
+            rng.shuffle(fallback)
+            neg_pool = []
+            while len(neg_pool) < self.num_negatives and fallback:
+                cid = fallback.pop()
+                neg_pool.append({"id": cid, "tokens": s.get("candidate_tokens", {}).get(cid, "")})
+            self._negatives[idx] = neg_pool

     # after val_ds creation:
+    val_ds.freeze_fallback_negatives(seed=args.seed)
```

## 验证

- `freeze_fallback_negatives` 调用位置: line 326，`val_ds` 创建后、`DataLoader` 创建前
- `__getitem__` 走预计算路径确认: **yes** — `self._negatives[idx]` 已被填充，`len(neg_pool) >= self.num_negatives` 条件满足，不会进入 `random.shuffle` fallback
- 影响范围: **仅 val eval** — `train_ds` 不受影响，仍由 `refresh_negatives(mined)` 动态更新

---
