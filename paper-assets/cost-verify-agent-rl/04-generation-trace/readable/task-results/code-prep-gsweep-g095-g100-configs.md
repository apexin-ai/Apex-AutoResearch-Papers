# code prep gsweep g095 g100 configs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-gsweep-g095-g100-configs_20260518T082201_result.json`
- **Structured JSON:** [`f9420067bf1f65c89ce2.json`](../../sessions/f9/f9420067bf1f65c89ce2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总：

---

### Config 文件
| 文件 | 路径 | gamma |
|------|------|-------|
| g095 | `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_gamma_sweep_g095_h5.yaml` | 0.95 |
| g100 | `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_gamma_sweep_g100_h5.yaml` | 1.0 |

### 启动脚本
`/root/autodl-tmp/cost-verify-agent-rl/RAGEN/launch_gsweep.sh`

### 启动命令
```bash
# g095
bash launch_gsweep.sh g095 "2,3"
# 等价于:
python train.py --config-name _alfworld_gamma_sweep_g095_h5 seed.train=10000 trainer.experiment_name=gsweep-g095-h5-seed1 system.CUDA_VISIBLE_DEVICES="2,3"

# g100
bash launch_gsweep.sh g100 "2,3"
# 等价于:
python train.py --config-name _alfworld_gamma_sweep_g100_h5 seed.train=10000 trainer.experiment_name=gsweep-g100-h5-seed1 system.CUDA_VISIBLE_DEVICES="2,3"
```

### 验证结果
| 项目 | 状态 |
|------|------|
| YAML 语法 | 通过 |
| Hydra config 加载 (--cfg job) | g095 通过, g100 通过 |
| SFT 模型路径 (`qwen3_exp021_ragen_sft_v4`) | 存在 (symlink) |
| Checkpoint 输出目录 | 已创建: `gsweep-g095-h5/`, `gsweep-g100-h5/` |
| 磁盘空间 | 45G 可用 (83% used) |

两个 config 除 `algorithm.gamma` 和 checkpoint 路径外与 g080 完全一致，`high_level_gamma` 保持 0.95 不变。

---
