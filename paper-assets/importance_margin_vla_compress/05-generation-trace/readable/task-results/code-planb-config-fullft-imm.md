# code planb config fullft imm

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_planb_config_fullft_imm_20260516T192900_result.json`
- **Structured JSON:** [`d1cb42ecdb668aeec3c0.json`](../../sessions/d1/d1cb42ecdb668aeec3c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是产出总结：

---

## 产出

### 1. 配置文件已创建
`/root/autodl-tmp/importance_margin_vla_compress/configs/libero_imm_twostage_fullft.yaml`

### 2. YAML 验证通过
```
YAML OK
```

### 3. train_twostage.py 兼容性报告

**当前代码不支持 Full FT 模式，需要以下修改：**

| 行号 | 问题 | 需改动 |
|------|------|--------|
| L105-109 | `get_lora_params()` 按 `"lora_"` in name 筛选参数。Full FT 模式 `lora.rank=0` 时无 LoRA 参数，返回空列表 | 需增加 Full FT 分支：获取 expert 全部参数（非 ACIS） |
| L128-140 | `verify_grad_state()` 断言 LoRA params 数量 > 0。Full FT 时 LoRA 为空会导致 Stage2 断言失败 | 需按 `train_mode` 区分验证逻辑 |
| L144-156 | `verify_gradients_after_backward()` 同上，硬编码检查 LoRA grad | 同上 |
| L367-370 | Stage 1 `freeze_params(lora_params)` — Full FT 模式应改为 freeze expert params（所有非 ACIS 的可训参数） | 需根据 `train_mode` 选择 freeze 对象 |
| L437-443 | Stage 2 `unfreeze_params(lora_params)` + `optimizer2 = make_stage_optimizer(lora_params, ...)` — Full FT 模式应 unfreeze expert params 并优化它们 | 需新增 `get_expert_params(model)` 函数替代 `get_lora_params` |

**核心修改思路：**
1. 新增 `get_expert_params(model)` — 返回 `model.policy` 中 expert 相关参数（排除 vision encoder 和 ACIS）
2. 在 main 中读取 `twostage_cfg.get("train_mode", "twostage")`，根据模式选择 Stage1 freeze 的对象和 Stage2 训练的对象
3. 验证函数需按 mode 分支：LoRA 模式检查 lora params，Full FT 模式检查 expert params

---
