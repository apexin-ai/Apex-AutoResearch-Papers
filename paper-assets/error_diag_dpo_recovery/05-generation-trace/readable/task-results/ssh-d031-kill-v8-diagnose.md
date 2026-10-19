# ssh d031 kill v8 diagnose

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d031-kill-v8-diagnose_20260513T072828_result.json`
- **Structured JSON:** [`34ece96706b0c0668d50.json`](../../sessions/34/34ece96706b0c0668d50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部进程已停。以下是诊断报告。

---

## D031 诊断报告

### 1. 失败轨迹模型行为模式

**一句话总结：模型推理逻辑正确，但 `put X in/on Y` 动作在 ALFWorld 环境中系统性返回 "Nothing happens"，导致模型进入无效动作循环（finish/finish task/end task）直到 40 步耗尽。**

v8 数据：20/20 轨迹全部 reward=False, steps=40。

典型失败链（traj 0, pick_clean_then_place, "put a clean spoon in diningtable"）：
```
[75] take spoon 1 from diningtable 1    → ✓ You pick up the spoon 1
[79] clean spoon 1 with sinkbasin 1     → ✓ You clean the spoon 1
[81] go to diningtable 1                → ✓ You arrive at diningtable 1
[83] put spoon 1 in/on diningtable 1    → ✗ Nothing happens.   ← 关键失败点
[85] put spoon 1 in/on diningtable 1    → ✗ Nothing happens.   (重试)
[89] look at diningtable 1              → ✗ Nothing happens.   (非法动作)
[93] finish                             → ✗ Nothing happens.   (非法动作)
[95-109] finish × 8                     → ✗ Nothing happens.   (死循环)
```

全局统计：
- 1157 步总量中 374 步(32.3%)返回 "Nothing happens"
- Top 无效动作：`finish`(42x), `finish task`(37x), `&lt;no_action_found>`(21x), `None (Task cannot be completed)`(15x)

### 2. 完整生成参数表

| 参数 | 值 |
|------|-----|
| temperature | 0.5 |
| top_p | 0.9 |
| top_k | 未设置 (默认) |
| repetition_penalty | **未设置 (默认)** |
| max_new_tokens | 256 |
| do_sample | True |
| stop_tokens | **未设置** |
| pad_token_id | tokenizer.pad_token_id or eos_token_id |
| enable_thinking | False |
| torch_dtype | float16 |
| device_map | cuda:{gpu} |
| num_icl_examples | 2 |
| max_steps | 40 |

**缺失参数**：无 `repetition_penalty`（导致循环 "finish"），无 stop tokens。

### 3. ICL prompt 格式

```
msg[0] user:      ALFWORLD_INSTRUCTION (系统指令 + 9 个合法动作)
msg[1] assistant:  "OK"
msg[2..N] :        ICL 示例 1 (同 task_type, user/assistant 对话轮)
msg[N+1..M]:       ICL 示例 2
msg[M+1] user:     实际 task 观测 ("You are in the middle of a room... Your task is to: ...")
```

ICL 示例来源：`data/alfworld_sft.json`，按 task_type 匹配 + n_turns ≤ 30 过滤，优先同类型，不足时补其他类型。无分隔标记。

### 4. 关键发现：`put` 动作系统性失败（跨版本一致）

| task_type | v7 成功率 | v8 成功率 | 说明 |
|-----------|----------|----------|------|
| look_at_obj | 4/8 (50%) | 0/1 (0%) | 唯一高成功类型，使用 `use desklamp` |
| pick_cool_then_place | 1/12 (8.3%) | 0/0 | 在 `cool` 步骤就判 won，不需要 put |
| pick_heat_then_place | 2/26 (7.7%) | 0/5 | 在 `heat` 步骤就判 won，不需要 put |
| pick_and_place | **0/28 (0%)** | 0/4 | 必须 put → 全部失败 |
| pick_clean_then_place | **0/33 (0%)** | 0/4 | 必须 put → 全部失败 |
| pick_two_obj | **0/31 (0%)** | 0/2 | 必须 put → 全部失败 |

**核心结论**：`put` 动作在当前 ALFWorld 环境中对所有需要 put 的任务类型系统性失败。v7 的 5.1% 成功率全部来自不需要 `put` 的任务类型。v8 的 0% 是因为采样到的 look_at_obj 恰好没找到目标物体。

**这不是模型质量问题或参数问题，而是 ALFWorld 环境层面的 `put` 动作 bug 或 action 格式不匹配。** 需要排查 env.step() 对 `put` 动作的处理逻辑。

---
