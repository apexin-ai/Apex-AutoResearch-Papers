# setup cqa1 full env

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_cqa1_full_env_20260516T132736_result.json`
- **Structured JSON:** [`e36d77865df2e94c8977.json`](../../sessions/e3/e36d77865df2e94c8977.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cqa1-33015 环境搭建状态总结：**

| 阶段 | 状态 | 详情 |
|------|------|------|
| Phase 0: 连接+探测 | ✅ | 4× RTX 4090 24GB, CUDA 12.4, Python 3.12 |
| Phase 1: 基础环境 | ✅ | conda base, pip 26.1.1, PyTorch + flash-attn |
| Phase 2: 项目依赖 | ✅ | transformers, lerobot (groot patch), num2words 等 |
| Phase 3: 代码同步 | ✅ | 从 westd-27271 tar+scp 完成，含 train_expert_only 逻辑 |
| Phase 4: LIBERO 数据集 | 🔄 87% | PID 4330, 333/383 files, ~32GB/~37GB, 磁盘充裕(206GB剩余) |
| Phase 5: Full FT 配置 | ✅ | `configs/libero_full_ft.yaml` 已创建并同步 |
| Phase 6: Dry-run 验证 | ✅ | 两个配置均通过 |

**Dry-run 结果：**

| 配置 | 可训练参数 | 占比 | 训练目标 |
|------|-----------|------|---------|
| Full Expert FT | 99,880,992 / 450,046,176 | **22.2%** | lm_expert 全部 + projections (155 modules) |
| LoRA baseline | 1,485,312 / 451,531,488 | **0.3%** | lm_expert q/v_proj LoRA adapters (74 modules) |

LIBERO 数据集下载预计 5-10 分钟内完成，完成后即可开始训练。

---
