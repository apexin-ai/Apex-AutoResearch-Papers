# code plan 800fix openvla issues

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_800fix-openvla-issues_20260517T141327_result.json`
- **Structured JSON:** [`30cbd37dea4dab01da5e.json`](../../sessions/30/30cbd37dea4dab01da5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 Issue 处理完毕。总结：

### Issue A: Object Checkpoint
- 找到官方 checkpoint `openvla/openvla-7b-finetuned-libero-object`（LoRA r=32 fine-tune）
- 正在通过 `hf-mirror.com` 下载到 `/root/autodl-tmp/models/openvla-libero-object/`（当前 2.0/~15GB）
- 发现 bjb1-18228 无法直连 huggingface.co，必须设 `HF_ENDPOINT=https://hf-mirror.com`

### Issue B: 特征提取
- 实现了 forward hook on `language_model.model.layers[31]`
- 发现 transformers 5.8.0 的 `generate()` prefill 不经过标准 forward hooks，改为捕获第一个 decode step 的 hidden state（通过 KV cache 编码了完整 observation）
- 验证通过：shape=(1, 4096)，norm=4256，非零，cosine_sim=1.0

### Issue C: 维度参数化
- `utils.py` 新增 `VLA_CONFIGS` + `get_vla_config()`
- `openvla_eval.py` 重写，支持所有 CRM modes，维度从 config 读取
- OpenVLA CRM 维度：action_dim=6, obs_dim=4096, unc_dim=8（vs SmolVLA: 30, 960, 40）

### 剩余风险
1. 下载完成后需验证模型加载（含自定义 modeling_prismatic.py）
2. OpenVLA CRM 需从零训练（维度不兼容 SmolVLA checkpoint）
3. K=10 inference ~5s（10次完整 autoregressive），远慢于 SmolVLA ~1s

---
