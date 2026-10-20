# ops eval bug root cause audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-bug-root-cause-audit_20260515T213949_result.json`
- **Structured JSON:** [`483fbf36b36cc4c5d9f8.json`](../../sessions/48/483fbf36b36cc4c5d9f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。关键发现：`batch_eval.py` 的 `--sft_adapter` 是 `required=True`，但 `inference.py` 是 `default=None`（可选）。这就是根因。

---

## 根因分析

### 1. 问题机制

`inference.py` 的 adapter 加载链：
```
Qwen3-4B (base) → [merge SFT adapter if --sft_adapter given] → [load RL/RSFT adapter if model_path is adapter]
```

所有 RSFT/DPO/GRPO adapter 都是在 SFT-merged 模型上训练的（它们的权重是相对于 base+SFT 的 delta）。如果跳过 SFT merge 直接把这些 adapter 加载到 raw Qwen3-4B 上，权重错位，输出垃圾，rel_f1≈0。

### 2. 根因：inference.py 的 `--sft_adapter` 是可选参数，无缺失警告

```python
# inference.py line 264
parser.add_argument("--sft_adapter", default=None, ...)
```

而 `batch_eval.py` 做对了：
```python
# batch_eval.py line 80
parser.add_argument("--sft_adapter", required=True, ...)
```

**根因是手动提交 eval 命令时遗漏了 `--sft_adapter` 参数。** 不是代码变更，不是模板问题——是 inference.py 缺少防呆机制。

### 3. 早期 mvp2_eval_rsft_r1 (s42) 为何成功？

registry 中记录的命令是缩写描述（`python -m freige.eval.inference --no-quantize (r1 checkpoint on cuda:2)`），不是实际执行的完整命令。该实验是手动运行的，实际命令大概率包含了 --sft_adapter 或等效参数。rsft_output 确认是 LoRA adapter（有 adapter_config.json），不可能在 raw Qwen3-4B 上拿到 0.4449 的 rel_f1。

### 4. 对比证据

| 实验对 | --sft_adapter | rel_f1 |
|--------|:---:|:---:|
| eval_plan_001_flat_nli (s42) | ✓ | 0.4539 |
| eval_plan_001_flat_nli_s43 | ✗ | 0.0022 |

同一模型，不同 seed，唯一差异就是 `--sft_adapter`。铁证。

---

## 全面审计表

| exp_id | --sft_adapter | status | conclusion | rel_f1 | 受影响？ |
|--------|:---:|:---:|:---:|:---:|:---:|
| **eval_plan_001_flat_nli** | ✓ | DONE | success | 0.4539 | - |
| **eval_plan_001_flat_nli_s43** | ✗ | DONE | failed | 0.0022 | **YES** |
| **eval_plan_008_rsft_topk3** | ✗ | DONE | killed | N/A | **YES** |
| **eval_plan_008_topk3_fixed** | ✓ | PREPARING | - | N/A | fix |
| **eval_plan_012_dpo_ced_1ep** | ✗ | DONE | negative | 0.0022 | **YES** |
| **eval_plan_012_dpo_1ep_fixed** | ✓ | PREPARING | - | N/A | fix |
| **eval_plan_012_dpo_ced_ckpt400** | ✗ | DONE | failed | N/A | **YES** |
| eval_plan_014_sft_no_evidence | N/A¹ | DONE | success | 0.4893 | - |
| eval_grpo_g8_bf16 | ✓ | DONE | success | N/A | - |
| eval_sft_baseline_noquant | ✗² | DONE | success | 0.4106 | - |
| plan_011_grpo_g8_bf16_eval | ✓ | DONE | success | 0.4549 | - |
| plan_011_bf16_g8_step_eval | ✗³ | RUNNING | - | N/A | 需查脚本 |
| plan_011_eval_g8_bf16_ckpt100 | ✓ | PREPARING | killed | N/A | - |
| plan_002_test_eval_s44 | ✓ | DONE | failed | N/A | - |
| plan_009_extract_reward_eval | ✗³ | DONE | failed | N/A | 需查脚本 |
| plan_009_flatnli_reward_eval | N/A¹ | DONE | failed | N/A | - |
| plan_009_flatnli_reward_eval_r2 | ✓ | DONE | failed | N/A | - |
| mvp2_eval_rsft_r1 | ✗⁴ | DONE | success | 0.4449 | - |
| mvp2_eval_rsft_r2a | ✗⁴ | DONE | success | 0.4494 | - |
| mvp2_eval_rsft_r2b | ✗⁴ | DONE | success | 0.4493 | - |
| mvp2_eval_rsft_r2b_maxtok1536 | ✗⁴ | DONE | killed | N/A | unclear |
| mvp2_eval_rsft_r2b_maxtok1536_r2 | ✓ | DONE | negative | 0.4504 | - |
| mvp2_eval_rsft_s43 | ✓ | DONE | failed | N/A | - |
| mvp2_eval_rsft_s43_r2 | ✓ | DONE | success | 0.4683 | - |
| mvp2_eval_rsft_s44 | N/A¹ | PREPARING | killed | N/A | - |
| mvp2_eval_sft_baseline | ✗² | DONE | success | 0.4057 | - |
| mvp2_sft_eval | ✗⁴ | DONE | killed | N/A | - |
| mvp2_sft_eval_r2 | ✗² | DONE | success | 0.4057 | - |
| mvp2_sft_eval_r3 | ✗² | DONE | success | 0.4057 | - |
| mvp2_eval_ced_kl001_r4_ckpt10 | ✓ | DONE | success | 0.00296 | - |
| mvp2_eval_ced_kl001_r4_ckpt7080 | ✓ | DONE | failed | N/A | - |
| mvp2_eval_ced_kl001_r4_ckpt90 | ✗ | DONE | killed | N/A | **可能** |
| mvp2_eval_ced_kl001_r4_early | ✓ | DONE | negative | N/A | - |
| mvp2_eval_ced_kl001_r4_high | ✓ | DONE | failed | N/A | - |
| mvp2_eval_ced_kl001_r4_last | ✓ | DONE | killed | N/A | - |
| mvp2_eval_ced_kl001_r4_multi | ✓ | DONE | killed | N/A | - |
| mvp2_eval_ced_kl001_r4_step100 | ✓ | DONE | negative | 0.2167 | - |
| mvp2_eval_ced_kl001_r4_step90 | ✓ | DONE | negative | 0.2108 | - |
| mvp2_eval_lr5e6_r1_ckpt20 | ✗³ | DONE | negative | 0.0077 | 需查脚本 |
| mvp2_eval_lr5e6_r1_ckpt40 | ✗³ | DONE | failed | N/A | 需查脚本 |
| mvp2_eval_lr5e6_r1_ckpt40_r2 | ✗⁴ | DONE | negative | 0.0071 | unclear |
| mvp2_eval_lr5e6_r1_ckpt60 | ✗³ | DONE | failed | N/A | 需查脚本 |
| mvp2_eval_lr5e6_r1_ckpt60_r2 | ✓ | DONE | negative | 0.0093 | - |
| mvp2_eval_lr5e6_r1_ckpt80 | ✓ | DONE | negative | 0.0116 | - |
| mvp2_eval_lr5e6_r1_ckpt100 | ✓ | DONE | negative | 0.0138 | - |
| mvp2_eval_lr5e6_rp_r2_ckpt20 | ✗⁴ | DONE | killed | N/A | unclear |

**注释：**
- ¹ 无命令记录
- ² SFT baseline eval — model_path 本身就是 SFT adapter，不需要 --sft_adapter
- ³ 通过 bash 脚本执行，参数是否正确需检查脚本内容
- ⁴ 命令为缩写描述，非实际执行命令

### 确认受影响的实验（4个）

| exp_id | 应有的 rel_f1 参考值 | 修复状态 |
|--------|:---:|:---:|
| eval_plan_001_flat_nli_s43 | ~0.45 (参考 s42=0.4539) | **需重跑** |
| eval_plan_008_rsft_topk3 | 未知 | eval_plan_008_topk3_fixed PREPARING |
| eval_plan_012_dpo_ced_1ep | 未知 | eval_plan_012_dpo_1ep_fixed PREPARING |
| eval_plan_012_dpo_ced_ckpt400 | 未知 | **需重跑** |

---

## 修复建议

**立即修复：** 在 `inference.py` 中加入防呆逻辑 — 当 model_path 是 adapter 且未指定 --sft_adapter 时，发出警告或报错：

```python
# inference.py main() 中，adapter 检测之后加：
if adapter_path and not args.sft_adapter:
    logger.warning("model_path is a LoRA adapter but --sft_adapter not set. "
                   "Loading adapter on raw base model — this is likely wrong "
                   "for RSFT/DPO/GRPO adapters trained on SFT-merged model.")
```

**防止复发：**
1. `inference.py` 的 `--sft_adapter` 改为在有 adapter 时 required（或至少 loud warning）
2. 提交 eval 时用模板/脚本统一构造命令，不手写

---
