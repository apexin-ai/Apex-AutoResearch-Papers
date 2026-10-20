# code plan 012 extended eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_012_extended_eval_20260517T042051_result.json`
- **Structured JSON:** [`d861f03b2f48f751cfb0.json`](../../sessions/d8/d861f03b2f48f751cfb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。总结：

---

## 完成汇报

### 1. 模型路径状态

| 模型 | 路径 | 存在 |
|------|------|------|
| RASP 20% post-SFT | `sft_rasp_20` | ✓ |
| Standard 20% post-SFT | `sft_standard_20` | ✓ |
| Unpruned post-SFT | `sft_unpruned` | ✗ 不存在 |
| RASP 20% post-GRPO | `grpo_stage2_rasp_20_v9` | ✓ |
| Standard 20% post-GRPO step-50 | `grpo_stage2_standard_20_v8/checkpoint-50` | ✓ |
| Unpruned post-GRPO | `grpo_unpruned_v2` | ✗ 不存在 |

**可评估 4 个模型**，unpruned 的 SFT/GRPO 版本不存在。

### 2. 脚本状态

| 文件 | 状态 |
|------|------|
| `src/eval_math500.py` | ✓ 就绪 |
| `src/eval_humaneval.py` | ✓ 就绪 |
| `src/run_extended_eval.sh` | ✓ 就绪（含 HF_ENDPOINT mirror） |

### 3. 依赖满足情况

- datasets 4.8.4, transformers 5.8.0, torch 2.10.0 ✓
- HuggingFace 需通过 `HF_ENDPOINT=https://hf-mirror.com`（服务器无法直连 huggingface.co）
- MATH-500 数据集 (500 problems) ✓ 可下载
- HumanEval 数据集 (164 problems) ✓ 可下载
- 代码执行环境 (subprocess sandbox) ✓ 测试通过

### 4. Dry-run 验证

- **MATH-500**: 成功跑通 3 samples（~4-6s/sample 短输出，长 CoT 问题可达 4096 tokens ~2-3min）
- **HumanEval**: 代码提取 + subprocess 执行测试通过

### 5. 预估时间

| 基准 | 每模型时间 | 4 模型总计 |
|------|-----------|-----------|
| MATH-500 (500 problems, max 4096 tokens) | ~45-90 min | 3-6 hours |
| HumanEval (164 problems, max 512 tokens) | ~15-25 min | 1-1.5 hours |

**总计约 4-7.5 小时**（取决于 CoT 长度）。建议用 `cuda:0` 和 `cuda:1` 并行跑两个模型以加速。

### 运行方式
```bash
cd /root/recovery_aware_struct_prune
export HF_ENDPOINT=https://hf-mirror.com
bash src/run_extended_eval.sh
```

---
