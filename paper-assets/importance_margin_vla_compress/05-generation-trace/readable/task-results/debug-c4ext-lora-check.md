# debug c4ext lora check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_c4ext_lora_check_20260519T184221_result.json`
- **Structured JSON:** [`b69266f382250670db0f.json`](../../sessions/b6/b69266f382250670db0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：LoRA 确实被错误启用了

### 事实

| 项目 | 值 |
|------|-----|
| **LoRA 是否启用** | **是** |
| **控制参数** | `configs/openvla_smart_compress_m128.yaml` → `lora.enabled: true` |
| **LoRA 配置** | r=16, alpha=32, target_modules=[q_proj, v_proj], dropout=0.05 |
| **LoRA 参数量** | 8,388,608 (8.4M) — 日志确认 |
| **VTC 参数量** | 403,308,544 (403M) |
| **总可训练** | 411,697,152 (411M = VTC 403M + LoRA 8.4M) |

### 问题确认

Config 文件头部注释写着 `Trainable: VisionTokenCompressor + LoRA adapters on LLM`，说明这个 config 本身就是 **VTC+LoRA 联合训练**的配置，不是 VTC-only。

训练刚启动不久（02:38 启动，目前约 step 100/100000），还在极早期。

### 建议

**需要停止当前训练**，将 config 中 `lora.enabled` 改为 `false` 后重启。损失很小——才跑了约 100 步（<0.1%）。

需要我执行停止和修改操作吗？

---
