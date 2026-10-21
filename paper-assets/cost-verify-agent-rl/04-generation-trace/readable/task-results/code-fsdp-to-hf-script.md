# code fsdp to hf script

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fsdp_to_hf_script_20260514T090354_result.json`
- **Structured JSON:** [`3101b01b9215a61e73e2.json`](../../sessions/31/3101b01b9215a61e73e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出

**脚本**：`/root/cost-verify-agent-rl/RAGEN/scripts/convert_fsdp_to_hf.py` 已就绪（服务器 + 本地同步）

**验证结果**：
- dry-run 通过，311 参数全部正确重建，shape 匹配 Qwen3-1.7B config
- 完整转换测试通过：`AutoModelForCausalLM.from_pretrained()` 加载成功，forward pass 正常
- 转换耗时 **~14 秒**（CPU-only，无需 GPU）
- 输出大小 **~4 GB**（bf16）

**用法**（Phase A checkpoint 出来后）：
```bash
python scripts/convert_fsdp_to_hf.py \
    --input-dir /root/autodl-tmp/checkpoints/&lt;exp>/global_step_N/actor \
    --output-dir /root/autodl-tmp/models/qwen3-1.7b-grpo \
    --dtype bf16
```

---
