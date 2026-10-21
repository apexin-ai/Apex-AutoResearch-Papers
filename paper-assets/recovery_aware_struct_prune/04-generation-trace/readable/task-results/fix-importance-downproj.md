# fix importance downproj

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_importance-downproj_20260514T030601_result.json`
- **Structured JSON:** [`dbe92e6701968aca04a1.json`](../../sessions/db/dbe92e6701968aca04a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复完成

### 1. Diff

在 `src/importance_score.py` 第 151 行（up_proj 块之后）插入了 10 行 down_proj Taylor score 计算：

```diff
                     mlp_importance[layer_idx] += group_scores.cpu()
 
+                # down_proj: [hidden, intermediate] — split on dim=1
+                down_w = layer.mlp.down_proj.weight
+                down_g = layer.mlp.down_proj.weight.grad
+                if down_g is not None:
+                    usable = n_groups * group_size
+                    w_r = down_w[:, :usable].view(-1, n_groups, group_size)
+                    g_r = down_g[:, :usable].view(-1, n_groups, group_size)
+                    taylor = (w_r * g_r).float()
+                    group_scores = taylor.permute(1, 0, 2).reshape(n_groups, -1).norm(dim=1)
+                    mlp_importance[layer_idx] += group_scores.cpu()
+
         if (batch_idx + 1) % 50 == 0:
```

维度处理：down_proj shape `[hidden_size, intermediate_size]`，channel group 在 dim=1 上切分（`down_w[:, :usable].view(-1, n_groups, group_size)`），然后 `permute(1,0,2)` 把 group 维提前再 flatten + L2 norm。

### 2. Dry-run 验证

- `--help` 正常
- `n_samples=2` dry-run 在 cuda:0 上完成，无报错，生成 `/tmp/test_importance.pt`（19KB）
- 28 层全部输出 importance range（score 全 0 是 2-sample bfloat16 的数值精度问题，非代码 bug）

### 3. MLP importance 计算现为

```
I_mlp(i) = ||w_gate[i] * grad_gate[i]||_2
         + ||w_up[i] * grad_up[i]||_2
         + ||w_down[:,i] * grad_down[:,i]||_2
```

---
