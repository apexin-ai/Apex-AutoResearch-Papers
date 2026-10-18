# code c5 roboflamingo action head fix — Part 2 of 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-c5-roboflamingo-action-head-fix.md) · [Structured JSON](../../../sessions/8b/8becddca45f4d13d1819.json)

## Before a recorded user message

### Tool call

_source line 212_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Dp5movgs6yVEpSCqwPnAKk`</summary>

```json
{
  "server": "westd-41074",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nwith open('/root/autodl-tmp/RoboFlamingo/test_fwd_libero.py','r') as f:\n    content = f.read()\n\n# Fix assertion 1: arm_pred is (B, W, 6) not (B, 1, 6) since multi_step_action=1 and last_action=False\ncontent = content.replace(\n    \\\"assert arm_pred.shape == (B, 1, 6), 'Expected (B=%d, 1, 6), got %s' % (B, str(arm_pred.shape))\\\",\n    \\\"assert arm_pred.shape == (B, WINDOW_SIZE, 6), 'Expected (B=%d, W=%d, 6), got %s' % (B, WINDOW_SIZE, str(arm_pred.shape))\\\"\n)\n\n# Fix assertion 2\ncontent = content.replace(\n    \\\"assert arm2.shape == (1, 1, 6), 'Expected (1, 1, 6), got %s' % str(arm2.shape)\\\",\n    \\\"assert arm2.shape == (1, WINDOW_SIZE, 6), 'Expected (1, W=%d, 6), got %s' % (WINDOW_SIZE, str(arm2.shape))\\\"\n)\n\nwith open('/root/autodl-tmp/RoboFlamingo/test_fwd_libero.py','w') as f:\n    f.write(content)\nprint('OK: assertions fixed')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5a34fd0-1027-4aad-b69f-a3a69423a6ca",
  "uuid": "fb9d233c-44bc-42b4-9e32-44d4906d764e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgAPWHbyhtCpo5HRN11f5y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2575,
      "cache_read_input_tokens": 127019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2575
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-19T19:04:56.194Z_

<details><summary>↩ Tool result · `toolu_01Dp5movgs6yVEpSCqwPnAKk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK: assertions fixed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.39}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5a34fd0-1027-4aad-b69f-a3a69423a6ca",
  "uuid": "4176ea34-eb0b-4044-846e-33a79471a4ba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"OK: assertions fixed\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.39}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"OK: assertions fixed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.39}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 214_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01DQtQSv7anZJyPNifs8cNhf`</summary>

```json
{
  "server": "westd-41074",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/RoboFlamingo && CUDA_VISIBLE_DEVICES=1 python test_fwd_libero.py 2>&1",
  "account": "root",
  "timeout": 180000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5a34fd0-1027-4aad-b69f-a3a69423a6ca",
  "uuid": "c9882d6a-0af4-4078-b8d0-c76886a72758",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ccq3pMbQYzqv8woQ4foQ22",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 129594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 898
      },
      "output_tokens": 73,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-19T19:05:22.995Z_

<details><summary>↩ Tool result · `toolu_01DQtQSv7anZJyPNifs8cNhf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/.cache/huggingface/modules/transformers_modules/mpt_hyphen_1b_hyphen_redpajama_hyphen_200b_hyphen_dolly/5cd5ddc98d606e91/attention.py:289: UserWarning: Using `attn_impl: torch`. If your model does not use `alibi` or `prefix_lm` we recommend using `attn_impl: flash` otherwise we recommend using `attn_impl: triton`.\\n  warnings.warn(\\n/root/.cache/huggingface/modules/transformers_modules/mpt_hyphen_1b_hyphen_redpajama_hyphen_200b_hyphen_dolly/5cd5ddc98d606e91/param_init_fns.py:45: UserWarning: Using a non-tuple sequence for multidimensional indexing is deprecated and will be changed in pytorch 2.9; use x[tuple(seq)] instead of x[seq]. In pytorch 2.9 this will be interpreted as tensor index, x[torch.tensor(seq)], which will result either in an error or a different result (Triggered internally at /pytorch/torch/csrc/autograd/python_variable_indexing.cpp:306.)\\n  init_fn_(module.weight[slice_indices])  # type: ignore\\nWARNING:root:No pretrained weights loaded for model 'ViT-L-14'. Model initialized randomly.\\nCompatibility patches applied.\\n[1] Loading tokenizer...\\n[2] Building model with window_size=12 (random weights)...\\nYou are using config.init_device='cpu', but you can also use config.init_device=\\\"meta\\\" with Composer + FSDP for fast initialization.\\n----------------------------------------------------------------------------------------------------\\ntransformer.blocks\\nwindow size: 12\\n1024 2048\\nMosaicGPTConfig {\\n  \\\"alibi\\\": true,\\n  \\\"alibi_bias_max\\\": 8,\\n  \\\"architectures\\\": [\\n    \\\"MosaicGPT\\\"\\n  ],\\n  \\\"attn_clip_qkv\\\": null,\\n  \\\"attn_impl\\\": \\\"torch\\\",\\n  \\\"attn_pdrop\\\": 0,\\n  \\\"attn_qk_ln\\\": true,\\n  \\\"attn_uses_sequence_id\\\": false,\\n  \\\"auto_map\\\": {\\n    \\\"AutoConfig\\\": \\\"configuration_mosaic_gpt.MosaicGPTConfig\\\",\\n    \\\"AutoModelForCausalLM\\\": \\\"mosaic_gpt.MosaicGPT\\\"\\n  },\\n  \\\"d_model\\\": 2048,\\n  \\\"dtype\\\": \\\"float32\\\",\\n  \\\"emb_init_std\\\": null,\\n  \\\"emb_init_uniform_lim\\\": null,\\n  \\\"emb_pdrop\\\": 0,\\n  \\\"embedding_fraction\\\": 1.0,\\n  \\\"fan_mode\\\": \\\"fan_in\\\",\\n  \\\"init_device\\\": \\\"cpu\\\",\\n  \\\"init_div_is_residual\\\": true,\\n  \\\"init_gain\\\": 0,\\n  \\\"init_nonlinearity\\\": \\\"relu\\\",\\n  \\\"init_std\\\": 0.02,\\n  \\\"logit_scale\\\": null,\\n  \\\"low_precision_layernorm\\\": true,\\n  \\\"max_seq_len\\\": 2048,\\n  \\\"mlp_ratio\\\": 4,\\n  \\\"model_type\\\": \\\"mosaic_gpt\\\",\\n  \\\"n_heads\\\": 16,\\n  \\\"n_layers\\\": 24,\\n  \\\"no_bias\\\": true,\\n  \\\"param_init_fn\\\": \\\"kaiming_normal_\\\",\\n  \\\"prefix_lm\\\": false,\\n  \\\"resid_pdrop\\\": 0,\\n  \\\"softmax_scale\\\": null,\\n  \\\"tokenizer_name\\\": \\\"EleutherAI/gpt-neox-20b\\\",\\n  \\\"transformers_version\\\": \\\"5.8.1\\\",\\n  \\\"use_cache\\\": false,\\n  \\\"verbose\\\": 0,\\n  \\\"vocab_size\\\": 50279\\n}\\n\\n  Model: 2724.0M params, time=17.5s\\n[3] Test 1: Flattened format (B=2, W=12 -> 24 frames)...\\n  arm_pred: torch.Size([2, 12, 6])\\n  grip_pred: torch.Size([2, 12, 1])\\n  feat: torch.Size([24, 2048])\\n  PASS!\\n[4] Test 2: Eval mode (W=12 frames, single batch)...\\n  arm_pred: torch.Size([1, 12, 6])\\n  grip_pred: torch.Size([1, 12, 1])\\n  PASS!\\n[5] Test 3: Single frame (B=1, T=1)...\\n  Expected error with single frame: shape '[-1, 12, 2048]' is invalid for input of size 2048\\n  This is correct - eval must pad to window_size!\\n\\nGPU mem: 11.27 GB\\nTotal time: 18.1s\\n=== ALL CRITICAL TESTS PASSED ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 23.54}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5a34fd0-1027-4aad-b69f-a3a69423a6ca",
  "uuid": "f7f24c42-e06a-4294-b839-d315447ae7c8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/.cache/huggingface/modules/transformers_modules/mpt_hyphen_1b_hyphen_redpajama_hyphen_200b_hyphen_dolly/5cd5ddc98d606e91/attention.py:289: UserWarning: Using `attn_impl: torch`. If your model does not use `alibi` or `prefix_lm` we recommend using `attn_impl: flash` otherwise we recommend using `attn_impl: triton`.\\\\n  warnings.warn(\\\\n/root/.cache/huggingface/modules/transformers_modules/mpt_hyphen_1b_hyphen_redpajama_hyphen_200b_hyphen_dolly/5cd5ddc98d606e91/param_init_fns.py:45: UserWarning: Using a non-tuple sequence for multidimensional indexing is deprecated and will be changed in pytorch 2.9; use x[tuple(seq)] instead of x[seq]. In pytorch 2.9 this will be interpreted as tensor index, x[torch.tensor(seq)], which will result either in an error or a different result (Triggered internally at /pytorch/torch/csrc/autograd/python_variable_indexing.cpp:306.)\\\\n  init_fn_(module.weight[slice_indices])  # type: ignore\\\\nWARNING:root:No pretrained weights loaded for model 'ViT-L-14'. Model initialized randomly.\\\\nCompatibility patches applied.\\\\n[1] Loading tokenizer...\\\\n[2] Building model with window_size=12 (random weights)...\\\\nYou are using config.init_device='cpu', but you can also use config.init_device=\\\\\\\"meta\\\\\\\" with Composer + FSDP for fast initialization.\\\\n----------------------------------------------------------------------------------------------------\\\\ntransformer.blocks\\\\nwindow size: 12\\\\n1024 2048\\\\nMosaicGPTConfig {\\\\n  \\\\\\\"alibi\\\\\\\": true,\\\\n  \\\\\\\"alibi_bias_max\\\\\\\": 8,\\\\n  \\\\\\\"architectures\\\\\\\": [\\\\n    \\\\\\\"MosaicGPT\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"attn_clip_qkv\\\\\\\": null,\\\\n  \\\\\\\"attn_impl\\\\\\\": \\\\\\\"torch\\\\\\\",\\\\n  \\\\\\\"attn_pdrop\\\\\\\": 0,\\\\n  \\\\\\\"attn_qk_ln\\\\\\\": true,\\\\n  \\\\\\\"attn_uses_sequence_id\\\\\\\": false,\\\\n  \\\\\\\"auto_map\\\\\\\": {\\\\n    \\\\\\\"AutoConfig\\\\\\\": \\\\\\\"configuration_mosaic_gpt.MosaicGPTConfig\\\\\\\",\\\\n    \\\\\\\"AutoModelForCausalLM\\\\\\\": \\\\\\\"mosaic_gpt.MosaicGPT\\\\\\\"\\\\n  },\\\\n  \\\\\\\"d_model\\\\\\\": 2048,\\\\n  \\\\\\\"dtype\\\\\\\": \\\\\\\"float32\\\\\\\",\\\\n  \\\\\\\"emb_init_std\\\\\\\": null,\\\\n  \\\\\\\"emb_init_uniform_lim\\\\\\\": null,\\\\n  \\\\\\\"emb_pdrop\\\\\\\": 0,\\\\n  \\\\\\\"embedding_fraction\\\\\\\": 1.0,\\\\n  \\\\\\\"fan_mode\\\\\\\": \\\\\\\"fan_in\\\\\\\",\\\\n  \\\\\\\"init_device\\\\\\\": \\\\\\\"cpu\\\\\\\",\\\\n  \\\\\\\"init_div_is_residual\\\\\\\": true,\\\\n  \\\\\\\"init_gain\\\\\\\": 0,\\\\n  \\\\\\\"init_nonlinearity\\\\\\\": \\\\\\\"relu\\\\\\\",\\\\n  \\\\\\\"init_std\\\\\\\": 0.02,\\\\n  \\\\\\\"logit_scale\\\\\\\": null,\\\\n  \\\\\\\"low_precision_layernorm\\\\\\\": true,\\\\n  \\\\\\\"max_seq_len\\\\\\\": 2048,\\\\n  \\\\\\\"mlp_ratio\\\\\\\": 4,\\\\n  \\\\\\\"model_type\\\\\\\": \\\\\\\"mosaic_gpt\\\\\\\",\\\\n  \\\\\\\"n_heads\\\\\\\": 16,\\\\n  \\\\\\\"n_layers\\\\\\\": 24,\\\\n  \\\\\\\"no_bias\\\\\\\": true,\\\\n  \\\\\\\"param_init_fn\\\\\\\": \\\\\\\"kaiming_normal_\\\\\\\",\\\\n  \\\\\\\"prefix_lm\\\\\\\": false,\\\\n  \\\\\\\"resid_pdrop\\\\\\\": 0,\\\\n  \\\\\\\"softmax_scale\\\\\\\": null,\\\\n  \\\\\\\"tokenizer_name\\\\\\\": \\\\\\\"EleutherAI/gpt-neox-20b\\\\\\\",\\\\n  \\\\\\\"transformers_version\\\\\\\": \\\\\\\"5.8.1\\\\\\\",\\\\n  \\\\\\\"use_cache\\\\\\\": false,\\\\n  \\\\\\\"verbose\\\\\\\": 0,\\\\n  \\\\\\\"vocab_size\\\\\\\": 50279\\\\n}\\\\n\\\\n  Model: 2724.0M params, time=17.5s\\\\n[3] Test 1: Flattened format (B=2, W=12 -> 24 frames)...\\\\n  arm_pred: torch.Size([2, 12, 6])\\\\n  grip_pred: torch.Size([2, 12, 1])\\\\n  feat: torch.Size([24, 2048])\\\\n  PASS!\\\\n[4] Test 2: Eval mode (W=12 frames, single batch)...\\\\n  arm_pred: torch.Size([1, 12, 6])\\\\n  grip_pred: torch.Size([1, 12, 1])\\\\n  PASS!\\\\n[5] Test 3: Single frame (B=1, T=1)...\\\\n  Expected error with single frame: shape '[-1, 12, 2048]' is invalid for input of size 2048\\\\n  This is correct - eval must pad to window_size!\\\\n\\\\nGPU mem: 11.27 GB\\\\nTotal time: 18.1s\\\\n=== ALL CRITICAL TESTS PASSED ===\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 23.54}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/.cache/huggingface/modules/transformers_modules/mpt_hyphen_1b_hyphen_redpajama_hyphen_200b_hyphen_dolly/5cd5ddc98d606e91/attention.py:289: UserWarning: Using `attn_impl: torch`. If your model does not use `alibi` or `prefix_lm` we recommend using `attn_impl: flash` otherwise we recommend using `attn_impl: triton`.\\n  warnings.warn(\\n/root/.cache/huggingface/modules/transformers_modules/mpt_hyphen_1b_hyphen_redpajama_hyphen_200b_hyphen_dolly/5cd5ddc98d606e91/param_init_fns.py:45: UserWarning: Using a non-tuple sequence for multidimensional indexing is deprecated and will be changed in pytorch 2.9; use x[tuple(seq)] instead of x[seq]. In pytorch 2.9 this will be interpreted as tensor index, x[torch.tensor(seq)], which will result either in an error or a different result (Triggered internally at /pytorch/torch/csrc/autograd/python_variable_indexing.cpp:306.)\\n  init_fn_(module.weight[slice_indices])  # type: ignore\\nWARNING:root:No pretrained weights loaded for model 'ViT-L-14'. Model initialized randomly.\\nCompatibility patches applied.\\n[1] Loading tokenizer...\\n[2] Building model with window_size=12 (random weights)...\\nYou are using config.init_device='cpu', but you can also use config.init_device=\\\"meta\\\" with Composer + FSDP for fast initialization.\\n----------------------------------------------------------------------------------------------------\\ntransformer.blocks\\nwindow size: 12\\n1024 2048\\nMosaicGPTConfig {\\n  \\\"alibi\\\": true,\\n  \\\"alibi_bias_max\\\": 8,\\n  \\\"architectures\\\": [\\n    \\\"MosaicGPT\\\"\\n  ],\\n  \\\"attn_clip_qkv\\\": null,\\n  \\\"attn_impl\\\": \\\"torch\\\",\\n  \\\"attn_pdrop\\\": 0,\\n  \\\"attn_qk_ln\\\": true,\\n  \\\"attn_uses_sequence_id\\\": false,\\n  \\\"auto_map\\\": {\\n    \\\"AutoConfig\\\": \\\"configuration_mosaic_gpt.MosaicGPTConfig\\\",\\n    \\\"AutoModelForCausalLM\\\": \\\"mosaic_gpt.MosaicGPT\\\"\\n  },\\n  \\\"d_model\\\": 2048,\\n  \\\"dtype\\\": \\\"float32\\\",\\n  \\\"emb_init_std\\\": null,\\n  \\\"emb_init_uniform_lim\\\": null,\\n  \\\"emb_pdrop\\\": 0,\\n  \\\"embedding_fraction\\\": 1.0,\\n  \\\"fan_mode\\\": \\\"fan_in\\\",\\n  \\\"init_device\\\": \\\"cpu\\\",\\n  \\\"init_div_is_residual\\\": true,\\n  \\\"init_gain\\\": 0,\\n  \\\"init_nonlinearity\\\": \\\"relu\\\",\\n  \\\"init_std\\\": 0.02,\\n  \\\"logit_scale\\\": null,\\n  \\\"low_precision_layernorm\\\": true,\\n  \\\"max_seq_len\\\": 2048,\\n  \\\"mlp_ratio\\\": 4,\\n  \\\"model_type\\\": \\\"mosaic_gpt\\\",\\n  \\\"n_heads\\\": 16,\\n  \\\"n_layers\\\": 24,\\n  \\\"no_bias\\\": true,\\n  \\\"param_init_fn\\\": \\\"kaiming_normal_\\\",\\n  \\\"prefix_lm\\\": false,\\n  \\\"resid_pdrop\\\": 0,\\n  \\\"softmax_scale\\\": null,\\n  \\\"tokenizer_name\\\": \\\"EleutherAI/gpt-neox-20b\\\",\\n  \\\"transformers_version\\\": \\\"5.8.1\\\",\\n  \\\"use_cache\\\": false,\\n  \\\"verbose\\\": 0,\\n  \\\"vocab_size\\\": 50279\\n}\\n\\n  Model: 2724.0M params, time=17.5s\\n[3] Test 1: Flattened format (B=2, W=12 -> 24 frames)...\\n  arm_pred: torch.Size([2, 12, 6])\\n  grip_pred: torch.Size([2, 12, 1])\\n  feat: torch.Size([24, 2048])\\n  PASS!\\n[4] Test 2: Eval mode (W=12 frames, single batch)...\\n  arm_pred: torch.Size([1, 12, 6])\\n  grip_pred: torch.Size([1, 12, 1])\\n  PASS!\\n[5] Test 3: Single frame (B=1, T=1)...\\n  Expected error with single frame: shape '[-1, 12, 2048]' is invalid for input of size 2048\\n  This is correct - eval must pad to window_size!\\n\\nGPU mem: 11.27 GB\\nTotal time: 18.1s\\n=== ALL CRITICAL TESTS PASSED ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 23.54}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 216_

所有测试通过！总结修复内容：

## 修复汇报

### 修改了 3 个文件：

1. **`robot_flamingo/models/action_head.py` (line 339)**  
   - Bug: `org_feat.view(self.window_size, dim)` 假设 batch_size=1
   - Fix: `org_feat.reshape(-1, dim)` 支持任意 batch size

2. **`train_libero.py` `compute_loss()`**  
   - Bug: 直接传 `(B, W, 1, C, H, W)` 多帧格式给模型。LLM 输出 `(B, text_len, dim)` 池化后 `(B, dim)`，action_head reshape `(-1, W, dim)` 需要 `B % W == 0` 但 batch_size 和 window_size 通常不满足
   - Fix: 匹配 CALVIN 训练格式 — flatten batch+window 维度到 `(B*W, 1, 1, C, H, W)` 独立帧，text repeat+flatten 到 `(B*W, text_len)`。action_head reshape `(B*W, dim)` → `(B, W, dim)` 正确工作

3. **`eval_libero.py` `get_action()`**  
   - Bug: 不做 padding，early timesteps 帧数 < window_size 导致 reshape 失败；且使用多帧格式
   - Fix: pad 到 window_size（复制首帧）；使用 flatten 格式（每帧独立处理），text repeat 到每帧

### 测试结果
- Test 1 (B=2, W=12 flattened): `arm_pred (2,12,6)` ✓
- Test 2 (B=1, W=12 eval mode): `arm_pred (1,12,6)` ✓  
- Test 3 (单帧不 pad): 预期失败 ✓
- GPU 内存: 11.27 GB

### 注意事项
- `factory.py` 的 `from_pretrained` 需要 MPT 权重文件（当前目录只有 config）。训练时需要下载 MPT 权重或改用 `from_config` + OpenFlamingo checkpoint 加载
- 当前测试用随机权重，实际训练需要 OpenFlamingo checkpoint（已有 `/root/autodl-tmp/models/OpenFlamingo-3B-vitl-mpt1b-langinstruct/checkpoint.pt`）
- `train_libero.py` 的 `create_roboflamingo_model` 需要修复 factory 调用（加 `debug=True` 或下载 MPT 权重），否则训练启动会卡在 trust_remote_code 提示

**不启动训练**，等 Director 批准。是否需要同时修复 factory 的 MPT 权重加载问题？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5a34fd0-1027-4aad-b69f-a3a69423a6ca",
  "uuid": "74385691-b5a1-4d8b-b382-6389c6df9d54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q7WViDgkVEXFd19tLm6tD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 130492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1764
      },
      "output_tokens": 1,
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

_source line 217_

所有测试通过！总结修复内容：

## 修复汇报

### 修改了 3 个文件：

1. **`robot_flamingo/models/action_head.py` (line 339)**  
   - Bug: `org_feat.view(self.window_size, dim)` 假设 batch_size=1
   - Fix: `org_feat.reshape(-1, dim)` 支持任意 batch size

2. **`train_libero.py` `compute_loss()`**  
   - Bug: 直接传 `(B, W, 1, C, H, W)` 多帧格式给模型。LLM 输出 `(B, text_len, dim)` 池化后 `(B, dim)`，action_head reshape `(-1, W, dim)` 需要 `B % W == 0` 但 batch_size 和 window_size 通常不满足
   - Fix: 匹配 CALVIN 训练格式 — flatten batch+window 维度到 `(B*W, 1, 1, C, H, W)` 独立帧，text repeat+flatten 到 `(B*W, text_len)`。action_head reshape `(B*W, dim)` → `(B, W, dim)` 正确工作

3. **`eval_libero.py` `get_action()`**  
   - Bug: 不做 padding，early timesteps 帧数 < window_size 导致 reshape 失败；且使用多帧格式
   - Fix: pad 到 window_size（复制首帧）；使用 flatten 格式（每帧独立处理），text repeat 到每帧

### 测试结果
- Test 1 (B=2, W=12 flattened): `arm_pred (2,12,6)` ✓
- Test 2 (B=1, W=12 eval mode): `arm_pred (1,12,6)` ✓  
- Test 3 (单帧不 pad): 预期失败 ✓
- GPU 内存: 11.27 GB

### 注意事项
- `factory.py` 的 `from_pretrained` 需要 MPT 权重文件（当前目录只有 config）。训练时需要下载 MPT 权重或改用 `from_config` + OpenFlamingo checkpoint 加载
- 当前测试用随机权重，实际训练需要 OpenFlamingo checkpoint（已有 `/root/autodl-tmp/models/OpenFlamingo-3B-vitl-mpt1b-langinstruct/checkpoint.pt`）
- `train_libero.py` 的 `create_roboflamingo_model` 需要修复 factory 调用（加 `debug=True` 或下载 MPT 权重），否则训练启动会卡在 trust_remote_code 提示

**不启动训练**，等 Director 批准。是否需要同时修复 factory 的 MPT 权重加载问题？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1018289,
  "duration_api_ms": 857135,
  "num_turns": 80,
  "stop_reason": "end_turn",
  "session_id": "f5a34fd0-1027-4aad-b69f-a3a69423a6ca",
  "total_cost_usd": 4.3916267499999995,
  "usage": {
    "input_tokens": 67,
    "cache_creation_input_tokens": 135993,
    "cache_read_input_tokens": 5118095,
    "output_tokens": 39215,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 135993,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 809,
        "cache_read_input_tokens": 130492,
        "cache_creation_input_tokens": 1764,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1764
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1783,
      "outputTokens": 26,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001913,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 67,
      "outputTokens": 39215,
      "cacheReadInputTokens": 5118095,
      "cacheCreationInputTokens": 135993,
      "webSearchRequests": 0,
      "costUSD": 4.389713749999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e395a2fc-6305-44b1-9537-c370f2440c5c"
}
```

</details>

---
