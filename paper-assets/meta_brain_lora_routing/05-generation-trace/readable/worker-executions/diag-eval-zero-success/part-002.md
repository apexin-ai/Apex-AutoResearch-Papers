# diag eval zero success — Part 2 of 2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../diag-eval-zero-success.md) · [Structured JSON](../../../sessions/c9/c918c9bcc51c7dde6bbb.json)

## Before a recorded user message

### Task result

_source line 229_

诊断 2 确认了关键信息。现在有足够的数据给出完整诊断报告。

---

## 诊断结果

### 1. Action 输出范围

| 指标 | 值 |
|------|-----|
| Shape | `(50, 7)` ✓ |
| dtype | float32 |
| Range | min=-1.160, max=+0.895 |
| Mean | -0.143 |
| Std | 0.465 |

**逐维度统计（真实 LIBERO 观测）：**

| 维度 | mean | std | min | max |
|------|------|-----|-----|-----|
| dx | -0.136 | 0.315 | -1.068 | +0.115 |
| dy | -0.014 | 0.051 | -0.119 | +0.084 |
| dz | -0.054 | 0.129 | -0.346 | +0.131 |
| droll | **+0.363** | 0.271 | +0.040 | **+0.895** |
| dpitch | +0.077 | 0.069 | -0.164 | +0.155 |
| dyaw | -0.102 | 0.080 | -0.229 | +0.049 |
| **gripper** | **-1.134** | 0.016 | **-1.160** | **-1.106** |

**前 5 步 action：**
```
t=0: [-1.068, -0.119, -0.045, +0.566, +0.136, +0.049, -1.137]
t=1: [-0.997, -0.104, -0.042, +0.491, +0.131, +0.045, -1.143]
t=2: [-0.923, -0.091, -0.035, +0.433, +0.123, +0.040, -1.146]
t=3: [-0.843, -0.081, -0.026, +0.370, +0.110, +0.033, -1.151]
t=4: [-0.757, -0.069, -0.021, +0.302, +0.098, +0.029, -1.157]
```

### 2. LIBERO env action space

- LIBERO 期望 7D：`[dx, dy, dz, droll, dpitch, dyaw, gripper]`，范围 `[-1, 1]`
- robosuite 内部会 clip ��范围值
- MetaBrain pipeline：`model.sample_actions()` → `actions[0, :, :7]` → `env.step(action.tolist())`
- 无额外 scale/clip ���骤（openpi 官方 eval 也没有）

### 3. 图像值域

| 阶段 | dtype | 范围 | 格式 |
|------|-------|------|------|
| LIBERO env 输出 | uint8 | [5, 239] | HWC 256×256 |
| resize_with_pad 后 | uint8 | [6, 237] | HWC 224×224 |
| Observation.from_dict 后 | **float32** | **[-1.0, 0.992]** | **BCHW** ✓ |

图像预处理正确。State padding（8→32, float32）正确。Tokenization 正确（23 tokens）。

### 4. Episode 失败模式

- **所有 episode 全部跑满 max_steps (220) 后 FAIL** — 是超时不是崩溃
- 机械臂在动（action 有变化，mean abs diff=0.019/step）
- 但动作无效：**gripper 始终关闭，从不打开**
- 位移偏大（dx 初始 -1.07，被 clip 到 -1.0）

### 5. 根因判断

**最可能原因：PI0 base model 在 LIBERO 上的 zero-shot 能力不足。**

证据链：
1. `pi0_base` README 明确写 "Base model to fine tune on your specific use case"
2. norm_stats 是 identity (mean=0, std=1) — 这是未经 task-specific calibration 的标志
3. 模型输出结构化但不合理：**gripper 从不打开 (-1.13)**、旋转修正过大 (droll=0.57)
4. 排除了预处理 bug：images float32[-1,1] ✓、state pad to 32 ✓、tokenization ✓
5. eval_par_v1 日志暴露旧 bug（state 未 pad + prompt 未 tokenize），但当前代码已修复，问题仍存在 → 不是预处理 bug

**次要可能：** 如果 openpi 官方 eval 用这个 EXACT checkpoint 能在 LIBERO 上跑�� >0% 成功率，那问题出在 MetaBrain 和官方 pipeline 的细微差异上。最可疑的差异是：官方 pipeline 通过 `normalizer_processor` 对 state 做处理（虽然 stats 是 identity，但 processor 可能还做了 padding/dtype 转换），而 MetaBrain 手动处理。

**建议下一步：**
1. 用 openpi 官方 server+client 跑一次 LIBERO eval（同一 checkpoint），确认 baseline 成功率
2. 如果官方�� 0%：需要一个 fine-tuned checkpoint（如 `pi0_libero` 而非 `pi0_base`）
3. 如果官方 >0%：对比官方 pipeline 和 MetaBrain 在同一 obs 上的 action 输出差异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1004288,
  "duration_api_ms": 895547,
  "num_turns": 89,
  "stop_reason": "end_turn",
  "session_id": "6c7e90b1-b5a6-4724-aec8-27c8704556b3",
  "total_cost_usd": 3.6450720000000008,
  "usage": {
    "input_tokens": 42,
    "cache_creation_input_tokens": 131568,
    "cache_read_input_tokens": 3416394,
    "output_tokens": 44451,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 131568,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 4549,
        "cache_read_input_tokens": 141054,
        "cache_creation_input_tokens": 1961,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1961
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3000,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00309,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 42,
      "outputTokens": 44451,
      "cacheReadInputTokens": 3416394,
      "cacheCreationInputTokens": 131568,
      "webSearchRequests": 0,
      "costUSD": 3.641982000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cb54735f-be68-49ec-b5a2-cb0617745072"
}
```

</details>

---
