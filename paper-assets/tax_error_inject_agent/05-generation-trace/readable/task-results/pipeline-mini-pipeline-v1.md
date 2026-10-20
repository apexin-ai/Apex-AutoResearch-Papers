# pipeline mini pipeline v1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_mini-pipeline-v1_20260514T103649_result.json`
- **Structured JSON:** [`d535c2236f4dfaee7728.json`](../../sessions/d5/d535c2236f4dfaee7728.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Mini Pipeline Steps 1-4 完成汇报

### 1. 轨迹收集状态
- PID 11050: **仍在运行**
- PID 11045: **仍在运行**
- 当前成功轨迹: **310条**（可用 ≥4 步: 303条），成功率 73.8%

### 2. 注入 + Recovery 统计
使用已验证的注入数据（`data/mini_pipeline/`，源自 238 条轨迹）：

| 指标 | 值 |
|------|-----|
| 计划注入 | 800 |
| 成功生成 | 752 |
| 失败 | 48 |
| **注入合法率 (Gate 1)** | **94.0% ≥ 80% ✓** |

按 operator 分布:
- P1_step_order_swap: 187
- P2_sub_goal_deletion: 184
- C1_context_truncation: 190
- C4_observation_masking: 191

| Recovery 指标 | 值 |
|------|-----|
| 有效 recovery (含 think+action，无 API_ERROR/DRY_RUN) | 752/752 |
| **Recovery 质量 (Gate 2)** | **100.0% ≥ 75% ✓** |

> 注：当前 API endpoint 在并发调用下出现间歇性 422 auth 错误，无法用 310 条轨迹重新生成注入数据。单请求测试正常，疑似 API 网关并发限制。已使用此前成功生成的高质量数据。

### 3. SFT 数据
| 组别 | 条数 | MD5 |
|------|------|-----|
| **vanilla** | 303 | `0e17253b31a849a0e00733493a1f867a` |
| **taxei** | 1055 | `ab7e71b8e7ea96c8c1de762af6fe9b8f` |

- MD5 不同 ✓
- formatter 数据质量检查通过（无 DRY_RUN / API_ERROR） ✓
- 数据路径: `data/mini_pipeline_v2/`

### 4. 训练提交
| 实验 | GPU | 状态 | 总步数 | 预估时间 |
|------|-----|------|--------|----------|
| mini-taxei-sft | cuda:0, cuda:1 | **RUNNING** | 198/epoch × 3 = 594 | ~11 min |
| mini-vanilla-sft | cuda:2, cuda:3 | **RUNNING** | 57/epoch × 3 = 171 | ~5 min |

配置: Qwen3-8B + LoRA r=16, bs=1×2GPU×8acc=16 effective, max_length=4096, gradient_checkpointing=true, 3 epochs, seed=42

---
