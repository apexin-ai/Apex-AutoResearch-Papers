# verify d1 v3 speed and eval c

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d1_v3_speed_and_eval_c_20260513T053350_result.json`
- **Structured JSON:** [`11da4dba39cec8ff0d70.json`](../../sessions/11/11da4dba39cec8ff0d70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. D1 v3 训练状态

| 指标 | 值 |
|------|-----|
| 当前 step | **21 / 500** (4%) |
| 平均 s/it | **~113-114 s/it**（确认 ~2x 慢于 D1 v2 的 62 s/it） |
| step_time (step 10) | 113.1s |
| step_time (step 20) | 114.2s |
| reward (step 10) | 0.006714 |
| reward (step 20) | 0.01487 |
| frac_reward_zero_std | 0.9 → 0.7 |
| completions/clipped_ratio | **0.994 → 0.981** |
| completions/mean_length | 1022 → 1019（几乎全部撞 1024 上限） |
| completions/mean_terminated_length | 74.7 → 221.9 |

### 2. 速度慢的原因分析

**根因：Qwen3.5 thinking 模式导致 99% 的 completions 被截断在 max_completion_length=1024。**

- `clipped_ratio=0.994` 意味着几乎每个 completion 都生成满 1024 tokens 才被强制截断
- 模型在 thinking 阶段消耗大量 token，留给实际 JSON 输出的空间不足
- `mean_terminated_length` 只有 74-222（自然结束的极少），说明绝大部分输出未完成
- 每个 sample 生成 num_generations × 1024 tokens，generation 时间远超正常情况
- D1 v2 如果 clipped_ratio 低（即模型能在更短 token 内结束），generation 快得多

**次要因素：**
- GPU 1 上有两个进程（vLLM server PID 67223 + training PID 70714），共占 65GB，100% 利用率
- eval_C_v2 在 GPU 0（22GB, 58% util），**GPU 间无竞争**，CPU 竞争可忽略

**reward 信号极弱**：reward 仅 0.007-0.015，70-90% batch 的 reward 标准差为零 → 模型基本没有学到有效信号。

### 3. eval_C_v2 结果

**scierc_test (551 samples) — 已完成：**
| 指标 | 值 |
|------|-----|
| f1_correctness | 0.2184 |
| entity_f1 | 0.3949 |
| relation_f1 | 0.0000 |
| structural_validity | 0.9964 |
| type_conformance | 0.9537 |
| relational_constraint | 0.7191 |
| structural_completeness | 0.9543 |

**crossner_politics (651 samples) — 已完成：**
| 指标 | 值 |
|------|-----|
| f1_correctness | 0.4116 |
| entity_f1 | 0.4158 |
| relation_f1 | 0.0000 |
| structural_validity | 1.0000 |
| type_conformance | 0.9997 |
| relational_constraint | 0.0000 |
| structural_completeness | 0.9932 |

**crossner_science (543 samples) — 进行中：**
- 进度：205/543 (37.8%)，~5 s/it
- 预计剩余：~28 分钟

### 4. A checkpoint-200 路径

**已确认存在**：`/root/autodl-tmp/output/formal_A/checkpoint-200/`（创建于 May 13 00:28）。formal_A 共有 checkpoint-100 到 checkpoint-500 + merged。

---
