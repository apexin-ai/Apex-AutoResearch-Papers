# exec icl success rate 14b

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_icl-success-rate-14b_20260512T162205_result.json`
- **Structured JSON:** [`7a1315a2285a44b5ef75.json`](../../sessions/7a/7a1315a2285a44b5ef75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正在运行。模型已加载，第一个 task 完成（pick_and_place, 成功, 13.1s）。

---

**汇报：**

### 脚本内容
复用了已有的 `src/test_icl_14b.py`（417 行），核心流程：
1. 从 `alfworld_sft.json` 加载 3 种 task type（pick_and_place, pick_clean_then_place, look_at_obj）的短 expert trajectory 作为 few-shot ICL 示例
2. 用 `transformers` 加载 Qwen3-14B-AWQ（FP16，单卡）
3. 构造 instruction + ICL examples + task observation 的 multi-turn prompt
4. 每个 task 最多 30 步交互，带 action 翻译（模型输出 → ALFWorld 合法动作）
5. 输出按 task_type 分类的成功率统计

### 启动状态
- **PID**: 252942
- **GPU**: cuda:0（CUDA_VISIBLE_DEVICES=0）
- **模型**: Qwen3-14B-AWQ（非 Qwen2.5-14B-AWQ——服务器上没有 2.5 版本，只有 Qwen3）
- **参数**: `--split dev --num_tasks 50 --temperature 0`
- **日志**: `/root/autodl-tmp/error_diag_dpo_recovery/icl_14b_50tasks.log`
- **结果文件**: `data/icl_test_results/14b_awq_dev_50.json`

### 历史参考（25 task 已有结果）
总成功率 40%（10/25）：
| task_type | 成功率 |
|---|---|
| pick_and_place | 6/6 = 100% |
| look_at_obj | 4/5 = 80% |
| pick_two_obj | 0/5 = 0% |
| pick_clean_then_place | 0/4 = 0% |
| pick_heat_then_place | 0/2 = 0% |
| pick_cool_then_place | 0/3 = 0% |

50 task 的结果预计 25-50 分钟完成，可后续用 `tail` 查看日志或读取最终 JSON。

---
