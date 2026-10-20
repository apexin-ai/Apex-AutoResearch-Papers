# infra env setup

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup_20260519T161651_result.json`
- **Structured JSON:** [`25c7b7db7f37ae14f0d7.json`](../../sessions/25/25c7b7db7f37ae14f0d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建完成。汇报如下：

---

### 环境搭建结果

**1. Python/CUDA/PyTorch**
| 组件 | 版本 |
|------|------|
| Python | 3.12.3 (conda base) |
| CUDA Driver | 13.0 (Driver 580.95.05) |
| PyTorch | 2.8.0+cu128, `cuda=True` |

**2. GPU 确认**
- 4× NVIDIA RTX PRO 6000 Blackwell Server Edition, 每卡 94GB（共 376GB 显存）

**3. 代码库**
| Repo | 状态 | 大小 |
|------|------|------|
| openvla-oft | clone 成功，`pip install -e . --no-deps` 完成 | 1.8M |
| LIBERO | clone 成功，`pip install -e .` 完成 | 639M |

**4. 依赖安装**
| 包 | 版本 | 状态 |
|---|---|---|
| transformers (openvla-oft fork) | 4.40.1 | OK |
| accelerate | 1.13.0 | OK |
| einops | 0.8.2 | OK |
| wandb | 0.27.0 | OK |
| peft | 0.11.1 | OK |
| timm | 1.0.27 | OK |
| diffusers | 0.30.3 | OK |
| flash-attn | 2.8.3 | OK |
| tensorflow | 2.21.0 | OK |
| datasets | 4.8.5 | OK |
| dlimp | 0.0.1 (--no-deps) | OK |

**5. 磁盘**
- 根分区：30G 总计，5.1G 已用（17%），25G 可用
- conda 环境：11G
- 无 autodl-tmp 数据盘，大模型/数据集需注意磁盘空间

**6. 注意事项**
- openvla-oft 的 pyproject.toml 固定 `torch==2.2.0`/`torchvision==0.17.0`/`timm==0.9.10`，与当前环境不兼容（pip 有 warning），但不影响运行。如遇 API 不兼容，需要对代码做适配
- dlimp 固定 `tensorflow==2.15.0`，实际装的是 2.21.0，可能有 API 差异
- 启用网络加速需 `source /etc/network_turbo`

---
