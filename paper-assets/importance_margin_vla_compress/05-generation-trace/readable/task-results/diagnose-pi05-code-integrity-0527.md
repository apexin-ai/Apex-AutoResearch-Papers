# diagnose pi05 code integrity 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05_code_integrity_0527_20260527T020052_result.json`
- **Structured JSON:** [`37d5d226526b19f7f73b.json`](../../sessions/37/37d5d226526b19f7f73b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。以下是诊断报告。

---

## 1. π0.5 Random Long 实验 × 服务器 × 代码版本

| k | SR | 结果文件服务器 | 代码行数 | success条件 | seed |
|---|---|---|---|---|---|
| 0.95 | 63.2% | westd-41074 | 426 | `if done:` | 42 |
| 0.95 | 61.2% | westd-38929 | 294 | `if done:` | 42 |
| 0.90 | 32.0% | westd-41074 | 426 | `if done:` | 42 |
| 0.90 | 31.8% | westd-38929 | 294 | `if done:` | 42 |
| 0.85 | 44.4% | cqa1-33015 | 464 | `if done or reward > 0.5:` | 42 |
| 0.75 | 62.4% | cqa1-33015 | 464 | `if done or reward > 0.5:` | 42 |
| 0.70 | 62.4% | cqa1-33015 | 464 | `if done or reward > 0.5:` | 42 |
| 0.50 | 50.2% | cqa1-33015 | 464 | `if done or reward > 0.5:` | 42 |

Registry 中对应的 exp_id（主要使用的版本）：

| exp_id | server | k | SR | status |
|--------|--------|---|---|----|
| (无注册) | westd-41074 | 0.95 | 63.2% | — |
| (无注册) | westd-41074 | 0.90 | 32.0% | — |
| eval_pi05_random_k085_long_seed42_v2 | cqa1-33015 | 0.85 | 44.4% | DONE |
| eval_pi05_random_k075_long_seed42_v2 | cqa1-33015 | 0.75 | 62.4% | DONE |
| eval_pi05_random_k07_long_seed42 | cqa1-33015 | 0.70 | 62.4% | DONE |
| eval_pi05_random_k05_long_seed42_v3 | cqa1-33015 | 0.50 | 50.2% | DONE |

## 2. 代码 diff 关键发现

### 三个版本概要

| 特性 | V-A (294行, westd-38929/27271) | V-B (426行, westd-41074) | V-C (464行, cqa1-33015) |
|------|------|------|------|
| prune_mode 选项 | none/random/l2norm | +attention | +attention/zero_mask_* |
| `--fixed_mask` | 无 | 有 | 有 |
| `_episode_mask_cache` | 无 | 有 | 有 |
| embed_prefix 覆盖 | 仅 prune 时 | 仅 prune 时 | **始终覆盖**（修复 double scaling） |
| success 条件 | `if done:` | `if done:` | **`if done or reward > 0.5:`** |
| DEVICE | 硬编码 cuda:0 | `cuda:{args.gpu}` | `cuda:{args.gpu}` |
| 文件名 tag | 无 | `_fixmask` tag | 无 |

### Random pruning 实现差异

**`prune_tokens_random()` 函数三个版本完全一致**：
```python
indices = torch.randperm(n_tokens)[:n_keep].sort().values.to(img_emb.device)
return img_emb[:, indices, :], n_keep
```
- 无固定种子，每次 inference 调用生成不同 mask
- n_keep 计算方式相同：`max(1, int(n_tokens * keep_ratio))`

### 导致非单调的两个根因

**根因 1（CRITICAL）：混合 success 条件**
- k=0.95, k=0.9 在 westd-41074 运行，用 `if done:` — 严格判定
- k=0.85 ~ k=0.5 在 cqa1-33015 运行，用 `if done or reward > 0.5:` — 宽松判定，`reward > 0.5` 会捕获部分完成状态，虚增 SR

这意味着 k≤0.85 的 SR 被系统性高估，与 k≥0.9 的结果不可直接比较。

**根因 2：k=0.9 存在真实的性能崩塌**

同台服务器 (westd-41074) 相同条件下的 per-task 对比：

| Task | k=0.95 | k=0.9 | Δ |
|------|--------|-------|---|
| T0 alphabet_soup | 70% | **10%** | -60% |
| T1 cream_cheese | 94% | 46% | -48% |
| T5 book_caddy | 82% | **26%** | -56% |
| T3 black_bowl | 84% | 44% | -40% |

仅多丢 13 个 token（243→230/256），多数 task 崩塌 30-60%。这在两台独立服务器上一致复现（westd-41074=32.0%, westd-38929=31.8%），说明 k=0.9 确实是 random pruning 的敏感阈值——但非单调曲线的"回升"部分主要是 success 条件差异造成的假象。

### Version C 的 embed_prefix 修复

cqa1-33015 版本注释：
> "Always override embed_prefix to avoid double lang_emb scaling. GemmaTextScaledWordEmbedding already applies * sqrt(hidden_size) in embed_tokens(); the default PI05Pytorch.embed_prefix applies it again, breaking the model."

但此修复对 random pruning 结果影响有限——V-A/V-B 在 prune 模式下也会覆盖 embed_prefix，只有 baseline（no pruning）模式受影响。

## 3. westd-38929 文件名不匹配

**`eval_results/openvla_l2norm_prune_k085_10.json` 实际内容：**
```json
"mode": "attention_prune",
"k_ratio": null,
"overall_success_rate": 0.458
```
- 文件名写的是 `l2norm`，实际内容是 **attention_prune** 模式
- `k_ratio` 为 null（attention mode 未记录 keep_ratio）
- SR=45.8%

**正确的 l2norm k=0.85 Long 结果在：**
`results/openvla_l2norm_prune_k085_long_seed42.json`
- `"mode": "l2norm_prune"`, `"k_ratio": 0.85`
- SR=38.8%

**影响范围：** 如果之前引用 `openvla_l2norm_prune_k085_10.json` 作为 l2norm 结果，实际拿到的是 attention 数据（45.8% vs 正确的 38.8%），差异 7%。

---

**结论：π0.5 Random Long 曲线不可用。** k≥0.9 和 k≤0.85 的实验使用了不同 success 条件，混合比较无意义。需要统一到 `if done:` 条件后重跑 k=0.85/0.75/0.7/0.5，或统一到 `if done or reward > 0.5:` 重跑 k=0.95/0.9。

---
