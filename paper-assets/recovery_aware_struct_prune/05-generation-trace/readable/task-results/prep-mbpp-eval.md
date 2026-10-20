# prep mbpp eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_mbpp_eval_20260522T080533_result.json`
- **Structured JSON:** [`c2c8b153058461449c0c.json`](../../sessions/c2/c2c8b153058461449c0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

```
== 过往 MBPP 失败 ==
失败实验: 2 个（registry 中无记录，信息来自 memory.md）
主要原因:
  1. eval_mbpp_sft_rasp_20 (westb): 模型路径错误，sft_rasp_20 不存在，应为 sft_rasp_20_1p5b。37s 即崩溃。
  2. eval_mbpp_sft_standard_20 (westd-29022): SIGTERM kill，189/374 完成后被外部终止（可能因其他实验抢 GPU）。
     附加问题：westd-29022 需要 HF_DATASETS_OFFLINE=1 否则网络请求失败。
修复方案: 两个都已修复并重跑成功。

== Dry-run ==
Import: SKIPPED（westd-32935 所有 4 卡均被占用，16-19GB/卡）
参数检查: OK（已读完 eval_mbpp.py 全部源码）
  关键参数:
    --model_path (required)
    --max_samples (可选，用于小样本测试)
    --max_new_tokens (default=2048)
    --timeout (default=10, per-task sandbox 超时)
    --output_path (auto-generated if omitted)
    --dtype (default=bfloat16)
小样本测试: SKIPPED（无空闲 GPU）
代码验证: 该脚本已在 westd-32935 上成功完成 8 次 eval，依赖无问题。

== Timeout 分析 ==
per-task sandbox 超时: 10s (--timeout 参数)
job 级超时: 脚本内无，需外部 timeout 命令控制
全量 374 tasks 预估:
  - 正常速度 10-20s/task → 1-2h
  - 遇到 non-EOS 生成（max_new_tokens=2048）40-80s/task → 4-8h
  - memory 记录: sft_standard_20 平均 40s/it，部分 60-80s/it
  - 已完成的 8 个 eval 均在 max_new_tokens=2048 下完成
推荐 timeout_hours: 4（保守值，覆盖最坏情况）

== 已完成 MBPP 结果 (westd-32935) ==
| Model               | Pass@1 | Correct/Total |
|---------------------|--------|---------------|
| Dense Unpruned      | 0.5348 | 200/374       |
| SFT CKA-only 20%   | 0.1283 | 48/374        |
| SFT Standard 20%   | 0.1203 | 45/374        |
| SFT RASP 20%       | 0.1176 | 44/374        |
| GRPO Standard 20%  | 0.1310 | 49/374        |
| GRPO RASP 20%      | 0.1310 | 49/374        |
| SFT ShortGPT 20%   | 0.1043 | 39/374        |
| GRPO ShortGPT 20%  | 0.1444 | 54/374        |

== 可用 Checkpoint ==
| Method     | SFT(westd)                | GRPO(westd)               | SFT(westb)       | GRPO(westb)       |
|------------|---------------------------|---------------------------|-------------------|-------------------|
| CKA-only   | ✅ sft_cka_only_20        | ⚠️ grpo_cka_only_20_seed456 | ✅ sft_cka_only_20 | ✅ grpo_cka_only_20 |
| Standard   | ✅ sft_standard_20        | ✅ grpo_standard_20_seed123/456 | ❌             | ❌                |
| Random     | ✅ sft_random_20          | ✅ grpo_random_20          | ❌                | ✅ grpo_random_20  |
| RASP       | ⚠️ sft_rasp_20_westd      | ⚠️ grpo_rasp_20_seed456    | ❌                | ❌                |

== 缺失 MBPP 评测 (4×2 核心组合) ==
| 缺失 eval          | Checkpoint 位置                     |
|---------------------|-------------------------------------|
| SFT Random 20%     | westd: sft_random_20                |
| GRPO Random 20%    | westd: grpo_random_20               |
| GRPO CKA-only 20%  | westb: grpo_cka_only_20             |

== 阻塞项 ==
1. **westd-32935 无空闲 GPU** — 4 卡全占，无法立即跑 MBPP eval
2. **GRPO CKA-only 20% checkpoint 不在 westd** — 主 checkpoint 在 westb-23072 (grpo_cka_only_20)，westd 只有 seed456 变种。需在 westb 上跑或确认 seed456 可用
3. **westd 网络离线** — 运行时必须加 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1
```

---
