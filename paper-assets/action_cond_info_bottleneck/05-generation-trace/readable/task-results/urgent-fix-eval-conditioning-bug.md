# urgent fix eval conditioning bug

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_fix-eval-conditioning-bug_20260516T171938_result.json`
- **Structured JSON:** [`da82b022a4efad50309f.json`](../../sessions/da/da82b022a4efad50309f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 代码修改（diff）
```diff
69a70,71
>         if not self.training and self._cached_lang_condition is not None:
>             print(f"[EVAL] Using language conditioning, shape={self._cached_lang_condition.shape}")
202a205,206
>         if self.acib_config.condition_source == "language":
>             self._cached_lang_condition = self._compute_lang_condition(batch)
```

### 2. PID 76223 kill 确认
已 kill，进程不存在。

### 3. 修复后 eval
- **PID**: 104743
- **tmux session**: `v7_eval_fixed_seed1`
- 参数: checkpoint_step=20000, suites=spatial/object/goal/10, seed=42, GPU 1

### 4. Language conditioning 验证
```
[EVAL] Using language conditioning, shape=torch.Size([1, 960])
```
确认 scorer 现在使用 960 维 language embedding 作为 condition，而非回退到 visual_mean。

### 5. GPU 状态
| GPU | PID | 用途 | 显存 |
|-----|-----|------|------|
| 0 | 46186 | seed1 buggy eval (保留作参考) | 4.4 GB |
| 1 | 101853 | seed2 eval (libero_object) | 6.0 GB |
| 1 | 104743 | **修复后 seed1 eval** | 6.5 GB |

注意：GPU 1 上有两个 eval 进程并行（101853 是之前启动的 seed2 eval），总显存占用 ~12.5 GB / 98 GB，资源充足。

---
