# infra env setup eto

**error type pref optim** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup-eto_20260514T094706_result.json`
- **Structured JSON:** [`5429a544834ccf154d4a.json`](../../sessions/54/5429a544834ccf154d4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。环境搭建完成。

## 环境搭建结果

| 组件 | 版本/状态 |
|---|---|
| **Python** | 3.12.3 (conda base) |
| **PyTorch** | 2.10.0+cu128, CUDA=True |
| **GPU** | 2 × NVIDIA RTX PRO 6000 Blackwell 94GB |
| **CUDA** | 12.8 (nvcc), 驱动 595.58.03 |
| **transformers** | 4.37.2 |
| **trl** | 0.7.7 |
| **peft** | 0.7.1 |
| **accelerate** | 1.13.0 |
| **wandb** | 0.26.0 |
| **datasets** | 4.8.4 |
| **alfworld** | 0.4.2 |
| **flash-attn** | 未安装（Blackwell sm_120 不支持编译，PyTorch SDPA 可替代） |

**ETO 仓库**: `/root/error_type_pref_optim/ETO/`，结构完整（envs, eval_agent, fastchat）

**ETO 训练数据**: alfworld_sft (3119), sciworld_sft (1483), webshop_sft (1824)

**ALFWorld 数据**: `/root/autodl-tmp/alfworld_data/`，包含 train, valid_seen, valid_unseen, valid_train

**环境变量**（已写入 .bashrc）:
- `ALFWORLD_DATA=/root/autodl-tmp/alfworld_data`
- `HF_HOME=/root/autodl-tmp/.hf_cache`

**注意事项**:
- 关键包（transformers, peft, trl, tokenizers, huggingface-hub）版本已固定。后续 `pip install` 其他包时加 `--no-deps` 以防版本被覆盖
- flash-attn 在 Blackwell GPU 上无法编译，需在 ETO 代码中禁用 flash attention 或依赖 PyTorch 内置 SDPA

---
