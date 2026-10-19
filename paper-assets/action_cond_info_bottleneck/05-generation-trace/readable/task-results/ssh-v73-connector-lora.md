# ssh v73 connector lora

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v73-connector-lora_20260517T165805_result.json`
- **Structured JSON:** [`428c6b691f9e07932b7a.json`](../../sessions/42/428c6b691f9e07932b7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部测试通过。

## 验证结果汇总

**1. Connector 结构**
- 单个 Linear 层：`connector.modality_projection.proj` = `nn.Linear(12288, 960, bias=False)`
- 12288 = vision_hidden_size (3072) * scale_factor^2 (4)

**2. Trainable params：228,993 (0.05%)**
| 参数 | shape | 数量 |
|------|-------|------|
| lora_A | [8, 12288] | 98,304 |
| lora_B | [960, 8] | 7,680 |
| scorer MLP | - | 123,009 |
| **总计** | | **228,993** |

**3. 验证结果：全 PASS**
- scale=0 时 output 精确等于 baseline（diff=0.00）
- B=0 初始化时 LoRA 贡献为零（diff=0.00）
- 非零 LoRA 时有贡献（diff=9.38e-02）

**4. 修改的文件**
- `acib/config.py`：添加 `connector_lora` freeze mode + `lora_rank`/`lora_scale` 字段
- `acib/acib_policy.py`：添加 `LoRALinear` 类 + `connector_lora` freeze 分支 + `_apply_lora_to_connector` + select_action 中 alpha=0 时禁用 LoRA
- `scripts/train_acib.py`：添加 CLI 参数 + config 传递
- `scripts/run_v73_connector_lora.sh`：训练脚本

**无需讨论的设计决策**：connector 只有一个 Linear，实现直接对应。hook 中 `connector_lora` 与 `connector_scorer` 走同一分支（不 detach），LoRA 梯度可正常回传。

---
