# debug pi05 strict code sync

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_pi05_strict_code_sync_20260527T065937_result.json`
- **Structured JSON:** [`e27f086166f06b8f3261.json`](../../sessions/e2/e27f086166f06b8f3261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 关键发现：实验已完成，未 crash

两个 "strict" 实验实际上**已成功跑完**，结果已保存：

| 实验 | 状态 | SR |
|------|------|----|
| attn k=0.9 strict (GPU2) | **已完成** 11:42–14:35 (170 min) | **64.0%** |
| attn k=0.85 strict (GPU3) | **已完成** 11:42–14:47 (183 min) | **50.0%** |
| random k=0.75 strict (GPU1) | **仍在运行** pid=177597, elapsed 1h23m | 进行中 |

结果文件：
- `pi05_attention_k0.90_libero_10_seed42.json`
- `pi05_attention_k0.85_libero_10_seed42.json`

### 代码版本对比 (426 vs 464 行)

| 差异 | westd-41074 (旧) | cqa1-33015 (新) |
|------|-------------------|-----------------|
| prune modes | 4 种 | 6 种 (+zero_mask_random, zero_mask_l2norm) |
| embed_prefix fix | 仅 pruning 时覆盖 | **始终覆盖**，修复 double lang_emb scaling bug |
| episode cache | 有 `_episode_mask_cache.clear()` | 已移除 |
| filename | 含 `mask_tag` | 无 `mask_tag` |

### "strict" success condition 不存在

两个版本都用 `if done:` 作为 success 条件。`grep -c "strict"` 返回 2，仅来自 `zip(..., strict=True)`。**两个版本都没有实现 strict success checking。**

### 结论

1. 实验未 crash，已产出结果（64.0% 和 50.0%）
2. 对 attention 模式，两版代码功能等价（都 override embed_prefix）
3. 用新代码重跑 attention 实验**不会改变结果**
4. 如果需要 strict success condition，需要**新写实现**，不是同步代码能解决的

**是否仍要同步代码并重跑？还是这些结果（SR=64.0% / 50.0%）可以直接使用？**

---
