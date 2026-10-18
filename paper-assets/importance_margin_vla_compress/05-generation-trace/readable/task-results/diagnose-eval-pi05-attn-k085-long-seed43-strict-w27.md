# diagnose eval pi05 attn k085 long seed43 strict w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_attn_k085_long_seed43_strict_w27_20260527T175301_result.json`
- **Structured JSON:** [`c9df3db6b0c0d026eccf.json`](../../sessions/c9/c9df3db6b0c0d026eccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。426 行（从 294 行增长），包含 `compute_attention_importance_probe` 函数（2处引用：定义+调用）和 `pruned_embed_prefix_attn`（4处引用：定义+赋值+logged+log）。

```json
{"root_cause":"w27 上的 eval_pi05_pruning_libero.py 是旧版本(294行)，argparse choices 只有 [none, random, l2norm]，缺少 attention/zero_mask 模式的所有代码","error_type":"infrastructure","fix_steps":["备份原文件为 .bak","Python patch 1: argparse choices 加 attention/zero_mask_random/zero_mask_l2norm, 加 --fixed_mask 参数, 加 _episode_mask_cache, 修 DEVICE=f'cuda:{args.gpu}', 加 zero_mask 函数, 加 compute_attention_importance_probe 函数, 加 zero_mask dispatch","Python patch 2: 在 prune_fn 块之后插入 attention 模式的 pruned_embed_prefix_attn 及 embed_prefix hookup","验证 --prune_mode attention --help 正常输出"],"can_auto_fix":true,"fixed":true,"correct_prune_mode":"attention"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "w27 上的 eval_pi05_pruning_libero.py 是旧版本(294行)，argparse choices 只有 [none, random, l2norm]，缺少 attention/zero_mask 模式的所有代码",
    "error_type": "infrastructure",
    "fix_steps": [
      "备份原文件为 .bak",
      "Python patch 1: argparse choices 加 attention/zero_mask_random/zero_mask_l2norm, 加 --fixed_mask 参数, 加 _episode_mask_cache, 修 DEVICE=f'cuda:{args.gpu}', 加 zero_mask 函数, 加 compute_attention_importance_probe 函数, 加 zero_mask dispatch",
      "Python patch 2: 在 prune_fn 块之后插入 attention 模式的 pruned_embed_prefix_attn 及 embed_prefix hookup",
      "验证 --prune_mode attention --help 正常输出"
    ],
    "can_auto_fix": true,
    "fixed": true,
    "correct_prune_mode": "attention"
  }
}
```

</details>

---
