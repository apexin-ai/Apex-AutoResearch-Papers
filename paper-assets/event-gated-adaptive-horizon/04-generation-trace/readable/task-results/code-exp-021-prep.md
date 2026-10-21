# code exp 021 prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_021_prep_20260517T140031_result.json`
- **Structured JSON:** [`60cdda90d6f416cda5df.json`](../../sessions/60/60cdda90d6f416cda5df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 验证完成。总结如下：

## exp_021_full_sgs_cheetah_s1 准备状态：Ready

**启动脚本**：`/root/autodl-tmp/event-gated-adaptive-horizon/scripts/exp_021_full_sgs_cheetah_s1.sh`

**完整命令**：
```bash
CUDA_ID=0 bash scripts/exp_021_full_sgs_cheetah_s1.sh
```

**关键参数**（已验证）：
| 参数 | 值 | 来源 |
|------|------|------|
| task | dmc_cheetah_run | 与 010b 一致 |
| configs | defaults dmc_proprio | 与 010b 一致 |
| gate_enabled | True | 与 010b 一致 |
| gate_fixed_dt | 2 | 与 010b 一致 |
| gate_subsample_max_dt | 2 | 与 010b 一致 |
| imag_horizon | 8 | 与 010b 一致 |
| **full_sgs** | **True** | 与 018v2 一致（010b 没有此参数） |
| seed | 1 | — |
| steps | 105000 | 与 010b/018v2 一致 |
| checkpoint_every | 10000 | — |

**Dry-run 结果**：
- Config 解析正确
- Cheetah Run 环境创建成功（Action Space 6D, proprio mode）
- Model 构建完成（16.9M world model params）
- Prefill + Eval + Training loop 全部正常进入
- SGS 实现通过 `models.py:346` 检查 `full_sgs` flag，在 actor/value 训练时冻结 `dt_embedding.weight`
- 无报错（仅有 deprecated warnings，不影响功能）

**无问题发现**，脚本可直接用于 GPU 分配后提交。

---
