# code fix eval output filename

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-output-filename_20260524T224454_result.json`
- **Structured JSON:** [`b578b73719655e47749c.json`](../../sessions/b5/b578b73719655e47749c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**Diff** (`src/evaluate.py`，main 函数底部默认文件名生成块):

```diff
         model_tag = f"_{args.model}" if args.model != "smolvla" else ""
         mode_str = f"k{args.K}mean" if args.mode == "vla_only" and args.baseline_mode == "mean" else args.mode
-        args.output_file = f"logs/eval_{args.benchmark}_{mode_str}{model_tag}{norm_tag}{adaptive_tag}_seed{args.seed}.json"
+        k_tag = "" if args.mode == "vla_only" else f"_K{args.K}"
+        args.output_file = f"logs/eval_{args.benchmark}_{mode_str}{model_tag}{k_tag}{norm_tag}{adaptive_tag}_seed{args.seed}.json"
```

**新旧文件名对比**

| mode | 旧 | 新 |
|---|---|---|
| adaptive_conformal_crm K=2 norm=0.2 tau=0.20 seed=42 spatial | `logs/eval_spatial_adaptive_conformal_crm_norm0.2_tau0.2_seed42.json` | `logs/eval_spatial_adaptive_conformal_crm_K2_norm0.2_tau0.2_seed42.json` |
| crm_perdof K=10 norm=0.1 seed=45 object | `logs/eval_object_crm_perdof_norm0.1_seed45.json` | `logs/eval_object_crm_perdof_K10_norm0.1_seed45.json` |
| vla_only seed=42 spatial | `logs/eval_spatial_vla_only_seed42.json` | `logs/eval_spatial_vla_only_seed42.json` (无变化，K 省略) |
| vla_only baseline_mode=mean K=2 seed=45 spatial | `logs/eval_spatial_k2mean_seed45.json` | `logs/eval_spatial_k2mean_seed45.json` (无变化，K 已在 mode_str 中) |

**同步状态**

- bjb2-40593：已应用 + 语法验证通过
- bjb1-32546：已应用 + 语法验证通过
- 项目无 git remote 配置，无法通过 `git pull` 同步；已直接对两台服务器分别 patch

---
