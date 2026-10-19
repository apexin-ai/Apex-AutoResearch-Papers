# setup pi05 libero checkpoint — Part 2 of 2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../setup-pi05-libero-checkpoint.md) · [Structured JSON](../../../sessions/cc/cc3c9217bbd461f4591d.json)

## Before a recorded user message

### Tool result

_source line 384 · 2026-05-16T10:07:38.945Z_

<details><summary>↩ Tool result · `toolu_018siwGRKvXnZ8agGmDFKBJ7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Download Process ===\\n   PID ELAPSED COMMAND\\n637757     195 bash -c  URL=\\\"https://hf-mirror.com/lerobot/pi0_libero/resolve/main/model.safetensors\\\" DEST=\\\"/root/autodl-tmp/checkpoints/pi0_libero/model.safetensors\\\" MAX_RETRIES=100  for i in $(seq 1 $MAX_RETRIES); do     echo \\\"[$(date)] Attempt $i\\\"     wget -c --timeout=300 --tries=3 --retry-connrefused --waitretry=5 \\\"$URL\\\" -O \\\"$DEST\\\" 2>&1          if [ -f \\\"$DEST\\\" ]; then         ACTUAL_SIZE=$(stat -c%s \\\"$DEST\\\" 2>/dev/null)         EXPECTED_SIZE=7011549448         if [ \\\"$ACTUAL_SIZE\\\" -ge \\\"$EXPECTED_SIZE\\\" ]; then             echo \\\"[$(date)] DOWNLOAD COMPLETE: $ACTUAL_SIZE bytes\\\"             exit 0         fi         echo \\\"[$(date)] Incomplete: $ACTUAL_SIZE / $EXPECTED_SIZE bytes. Retrying...\\\"     fi     sleep 5 done echo \\\"[$(date)] FAILED after $MAX_RETRIES attempts\\\" \\n=== Watchdog ===\\n637861\\nRUNNING\\n=== File Progress ===\\n49 MB / 6691 MB (0.7%)\\n=== GPU Status ===\\n0, 0 %, 0 MiB\\n1, 0 %, 0 MiB\\n2, 0 %, 0 MiB\\n3, 0 %, 0 MiB\\n=== Other Processes ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6e02a838-cf45-49fa-b5cf-7558baad836b",
  "uuid": "15390930-977b-4445-b0c1-323b7dd5ebc9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"=== Download Process ===\\\\n   PID ELAPSED COMMAND\\\\n637757     195 bash -c  URL=\\\\\\\"https://hf-mirror.com/lerobot/pi0_libero/resolve/main/model.safetensors\\\\\\\" DEST=\\\\\\\"/root/autodl-tmp/checkpoints/pi0_libero/model.safetensors\\\\\\\" MAX_RETRIES=100  for i in $(seq 1 $MAX_RETRIES); do     echo \\\\\\\"[$(date)] Attempt $i\\\\\\\"     wget -c --timeout=300 --tries=3 --retry-connrefused --waitretry=5 \\\\\\\"$URL\\\\\\\" -O \\\\\\\"$DEST\\\\\\\" 2>&1          if [ -f \\\\\\\"$DEST\\\\\\\" ]; then         ACTUAL_SIZE=$(stat -c%s \\\\\\\"$DEST\\\\\\\" 2>/dev/null)         EXPECTED_SIZE=7011549448         if [ \\\\\\\"$ACTUAL_SIZE\\\\\\\" -ge \\\\\\\"$EXPECTED_SIZE\\\\\\\" ]; then             echo \\\\\\\"[$(date)] DOWNLOAD COMPLETE: $ACTUAL_SIZE bytes\\\\\\\"             exit 0         fi         echo \\\\\\\"[$(date)] Incomplete: $ACTUAL_SIZE / $EXPECTED_SIZE bytes. Retrying...\\\\\\\"     fi     sleep 5 done echo \\\\\\\"[$(date)] FAILED after $MAX_RETRIES attempts\\\\\\\" \\\\n=== Watchdog ===\\\\n637861\\\\nRUNNING\\\\n=== File Progress ===\\\\n49 MB / 6691 MB (0.7%)\\\\n=== GPU Status ===\\\\n0, 0 %, 0 MiB\\\\n1, 0 %, 0 MiB\\\\n2, 0 %, 0 MiB\\\\n3, 0 %, 0 MiB\\\\n=== Other Processes ===\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.54}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"=== Download Process ===\\n   PID ELAPSED COMMAND\\n637757     195 bash -c  URL=\\\"https://hf-mirror.com/lerobot/pi0_libero/resolve/main/model.safetensors\\\" DEST=\\\"/root/autodl-tmp/checkpoints/pi0_libero/model.safetensors\\\" MAX_RETRIES=100  for i in $(seq 1 $MAX_RETRIES); do     echo \\\"[$(date)] Attempt $i\\\"     wget -c --timeout=300 --tries=3 --retry-connrefused --waitretry=5 \\\"$URL\\\" -O \\\"$DEST\\\" 2>&1          if [ -f \\\"$DEST\\\" ]; then         ACTUAL_SIZE=$(stat -c%s \\\"$DEST\\\" 2>/dev/null)         EXPECTED_SIZE=7011549448         if [ \\\"$ACTUAL_SIZE\\\" -ge \\\"$EXPECTED_SIZE\\\" ]; then             echo \\\"[$(date)] DOWNLOAD COMPLETE: $ACTUAL_SIZE bytes\\\"             exit 0         fi         echo \\\"[$(date)] Incomplete: $ACTUAL_SIZE / $EXPECTED_SIZE bytes. Retrying...\\\"     fi     sleep 5 done echo \\\"[$(date)] FAILED after $MAX_RETRIES attempts\\\" \\n=== Watchdog ===\\n637861\\nRUNNING\\n=== File Progress ===\\n49 MB / 6691 MB (0.7%)\\n=== GPU Status ===\\n0, 0 %, 0 MiB\\n1, 0 %, 0 MiB\\n2, 0 %, 0 MiB\\n3, 0 %, 0 MiB\\n=== Other Processes ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 385_

<details><summary>Logged reasoning block</summary>

```text
OK let me give a comprehensive status report. The download is at 49MB/6.5GB after about 195 seconds. That's roughly 250KB/s average. At this rate: 6500MB / 0.25MB/s = 26,000 seconds ≈ 7.2 hours.

The situation is clear:
1. Kill: Done ✓
2. Download: In progress, limited by network speed (~250KB/s to XET CDN from China, ETA 7+ hours)
3. Architecture analysis: pi05_libero is INCOMPATIBLE (pi0.5 architecture vs pi0 MetaBrain); pi0_libero is COMPATIBLE


4. Everything else is ready to go—script, code patch, and watchdog are all prepared, so I'm just waiting for the download to finish before evaluation can start.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e02a838-cf45-49fa-b5cf-7558baad836b",
  "uuid": "6e632349-4596-4dad-9d7f-9d6983dc868b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012q1PkYZYXLgtyLYDw8RKXT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 125476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 386_

---

## 执行结果汇报

### 1. Kill 结果 ✓
所有 `evaluate_libero` 进程已终止。GPU 0-3 全部空闲。

### 2. 下载状态：进行中，受网络限制

**文件**：`lerobot/pi0_libero` (HuggingFace) → 6.5GB (bfloat16 safetensors)
**当前进度**：49MB / 6.5GB (0.7%)
**速度**：~250KB/s（XET CDN 从中国访问极慢）
**预估 ETA**：7+ 小时

已配置弹性下载脚本（PID 637757，100次重试 + wget -c 断点续传）和 watchdog（PID 637861，下载完成后自动启动 eval）。

**尝试过的下载路径**：
| 方案 | 结果 |
|------|------|
| hf-mirror.com → xethub CDN | ~100-250KB/s（当前使用） |
| ModelScope 国内CDN | ~350KB/s（但 no_proxy 导致直连极慢） |
| GCS gsutil | 大文件超时 |
| GCS HTTP API | 元数据可访问，数据流超时 |

### 3. 关键架构发现

**`pi05_libero` 与 MetaBrain 不兼容**：
- pi05 是 pi0.5 架构（`pi05=True`，含 adarms 模块，`max_token_len=200`）
- MetaBrain 用 `Pi0Config(pi05=False)`（pi0 架构，`max_token_len=48`）
- 权重 key 不匹配，无法强行加载

**`pi0_libero`（`lerobot/pi0_libero`）兼容**：
- 同为 pi0 架构（gemma_2b + gemma_300m, tokenizer_max_length=48）
- config.json 与 pi0_base 一致（仅 n_action_steps 不同：10 vs 50，不影响架构）
- bf16 safetensors 可直接加载到 MetaBrain（`Pi0Config(dtype="bfloat16")`）

### 4. 代码修改
- **evaluate_libero_plus.py line 554**: 修复 `from_dummy()` 调用，传入 `pi0_checkpoint=args.pi0_checkpoint`（原来硬编码 pi0_base）
- **run_nominal_eval.sh**: 创建 eval 脚本，用 `--perturbation_types nominal --routing none`

### 5. Nominal eval 准备就绪
一旦下载完成，watchdog 会自动执行：
```bash
CUDA_VISIBLE_DEVICES=0 python phase1/evaluate_libero_plus.py \
    --pi0_checkpoint /root/autodl-tmp/checkpoints/pi0_libero \
    --routing none --perturbation_types nominal \
    --num_episodes 5 --seeds 42 --no_wandb --gpu 0
```

### 6. 后续检查方式
```bash
# 查下载进度
ls -la /root/autodl-tmp/checkpoints/pi0_libero/model.safetensors | awk '{printf "%.0f MB / 6691 MB\n", $5/1024/1024}'

# 查 eval 结果
cat /tmp/watchdog_eval.log
```

**总结**：下载是唯一瓶颈。网络条件限制了从 XET CDN 的速度。如果有其他方式获取 `lerobot/pi0_libero` 的 model.safetensors（例如从其他机器 scp），可以大幅加速。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6e02a838-cf45-49fa-b5cf-7558baad836b",
  "uuid": "2443a6f5-2fc4-4dbe-8c2e-8f619cd1094f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012q1PkYZYXLgtyLYDw8RKXT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 125476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 387_

---

## 执行结果汇报

### 1. Kill 结果 ✓
所有 `evaluate_libero` 进程已终止。GPU 0-3 全部空闲。

### 2. 下载状态：进行中，受网络限制

**文件**：`lerobot/pi0_libero` (HuggingFace) → 6.5GB (bfloat16 safetensors)
**当前进度**：49MB / 6.5GB (0.7%)
**速度**：~250KB/s（XET CDN 从中国访问极慢）
**预估 ETA**：7+ 小时

已配置弹性下载脚本（PID 637757，100次重试 + wget -c 断点续传）和 watchdog（PID 637861，下载完成后自动启动 eval）。

**尝试过的下载路径**：
| 方案 | 结果 |
|------|------|
| hf-mirror.com → xethub CDN | ~100-250KB/s（当前使用） |
| ModelScope 国内CDN | ~350KB/s（但 no_proxy 导致直连极慢） |
| GCS gsutil | 大文件超时 |
| GCS HTTP API | 元数据可访问，数据流超时 |

### 3. 关键架构发现

**`pi05_libero` 与 MetaBrain 不兼容**：
- pi05 是 pi0.5 架构（`pi05=True`，含 adarms 模块，`max_token_len=200`）
- MetaBrain 用 `Pi0Config(pi05=False)`（pi0 架构，`max_token_len=48`）
- 权重 key 不匹配，无法强行加载

**`pi0_libero`（`lerobot/pi0_libero`）兼容**：
- 同为 pi0 架构（gemma_2b + gemma_300m, tokenizer_max_length=48）
- config.json 与 pi0_base 一致（仅 n_action_steps 不同：10 vs 50，不影响架构）
- bf16 safetensors 可直接加载到 MetaBrain（`Pi0Config(dtype="bfloat16")`）

### 4. 代码修改
- **evaluate_libero_plus.py line 554**: 修复 `from_dummy()` 调用，传入 `pi0_checkpoint=args.pi0_checkpoint`（原来硬编码 pi0_base）
- **run_nominal_eval.sh**: 创建 eval 脚本，用 `--perturbation_types nominal --routing none`

### 5. Nominal eval 准备就绪
一旦下载完成，watchdog 会自动执行：
```bash
CUDA_VISIBLE_DEVICES=0 python phase1/evaluate_libero_plus.py \
    --pi0_checkpoint /root/autodl-tmp/checkpoints/pi0_libero \
    --routing none --perturbation_types nominal \
    --num_episodes 5 --seeds 42 --no_wandb --gpu 0
```

### 6. 后续检查方式
```bash
# 查下载进度
ls -la /root/autodl-tmp/checkpoints/pi0_libero/model.safetensors | awk '{printf "%.0f MB / 6691 MB\n", $5/1024/1024}'

# 查 eval 结果
cat /tmp/watchdog_eval.log
```

**总结**：下载是唯一瓶颈。网络条件限制了从 XET CDN 的速度。如果有其他方式获取 `lerobot/pi0_libero` 的 model.safetensors（例如从其他机器 scp），可以大幅加速。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1930632,
  "duration_api_ms": 1054336,
  "num_turns": 125,
  "stop_reason": "end_turn",
  "session_id": "6e02a838-cf45-49fa-b5cf-7558baad836b",
  "total_cost_usd": 6.098830499999998,
  "usage": {
    "input_tokens": 106,
    "cache_creation_input_tokens": 114958,
    "cache_read_input_tokens": 8286900,
    "output_tokens": 49346,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 114958,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1252,
        "cache_read_input_tokens": 125476,
        "cache_creation_input_tokens": 929,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 929
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2618,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002713,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 106,
      "outputTokens": 49346,
      "cacheReadInputTokens": 8286900,
      "cacheCreationInputTokens": 114958,
      "webSearchRequests": 0,
      "costUSD": 6.096117499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c1baa5e6-2b67-4818-b49c-3d9021c94743"
}
```

</details>

---
