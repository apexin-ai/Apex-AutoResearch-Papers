# code eval pipeline check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_pipeline_check_20260514T003024_result.json`
- **Structured JSON:** [`547447a2ff4c42f61c29.json`](../../sessions/54/547447a2ff4c42f61c29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出总结

### 现状

| 能力 | 状态 |
|------|------|
| 4 benchmarks (MMLU/GSM8K/ARC/HumanEval) | ✅ 已有 |
| item-level 输出 (`per_item` in `eval_results.json`) | ✅ 已有 |
| IRT 用 correctness matrix | ✅ 已有 (`correctness_matrix.json`) |
| 批量链式触发 (train all → eval all) | ✅ 已有 (`run_exp001.sh --phase all`) |
| 单 job train→eval 链式触发 | ❌ 缺失 → **已补** |
| `--max-samples` dry-run 参数 | ❌ 缺失 → **已补** |
| 结构化 `item_responses.json` | ❌ 缺失 → **已补** |

### 修改文件

1. **`evaluate.py`** (575→600 行)
   - 新增 `--max-samples` 参数，截断每个 benchmark 的样本数
   - 新增 `item_responses.json` 输出：`{item_id, benchmark, correct, model_answer, gold_answer}`

2. **`train_and_eval.sh`** (新建)
   - 单 job 链式执行：SFT train → eval(original）→ eval（paraphrased）
   - 用法：`bash train_and_eval.sh --model Qwen/Qwen2.5-0.5B --dosage 5 --seed 42 --gpu 0`
   - 支持 `--eval-only`（只跑 eval）、`--max-samples N`（dry-run）
   - 内置 skip 逻辑（已有结果自动跳过）

### 输出路径规范

```
/root/autodl-tmp/exp001/eval_results/{Model}_d{dosage:03d}_s{seed}/
├── eval_results.json        # 完整结果（含 per_item）
├── correctness_matrix.json  # IRT 用二值矩阵
└── item_responses.json      # 结构化 item-level 响应
```

### Dry-run 验证

用 `Qwen2.5-0.5B_d000_s42` + `--max-samples 5` + `arc_challenge` 验证通过，3 个输出文件格式正确。

### 注意事项
- AutoDL 上跑 eval 需要 `HF_HUB_OFFLINE=1`（模型/数据集已缓存）或先 `source /etc/network_turbo`
- paraphrased eval 有一个预存 bug（`load_paraphrased_benchmark` 中 `'list' object has no attribute 'get'`），与本次修改无关，需后续修复
- bitsandbytes 的 `libnvJitLink.so.13` 警告不影响功能

---
