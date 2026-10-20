# code sprint day1 configs

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sprint_day1_configs_20260518T161655_result.json`
- **Structured JSON:** [`9f652cffe7c431186d36.json`](../../sessions/9f/9f652cffe7c431186d36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 产出

### 三个位置均已部署
| 位置 | 路径 |
|------|------|
| 本地 | `configs/sprint_day1/` |
| westd-19828 | `/root/autodl-tmp/distrib_canary_collapse/configs/sprint_day1/` |
| westd-17855 | `/root/autodl-tmp/distrib_canary_collapse/configs/sprint_day1/` |

### 17 个实验脚本 + README.md
- 17 个 `.sh` 文件，每个包含完整 `bash -c "..."` 命令，可直接传给 `submit_training_job`
- `README.md` 含实验列表、4-wave GPU 调度方案、依赖关系

### 参数映射
| 用户指定 | 实际使用 |
|---------|---------|
| `data_strategy=accumulate` | `--accumulate` flag |
| `--bf16` | **不存在**，未使用 |
| `--optimizer` | **不存在**，有 `--optim` 但未使用 |
| `--gradient_checkpointing` | 已为 OPT-1.3b、Pythia-1.4b 自动添加 |
| `TRANSFORMERS_OFFLINE=1` | 未添加（新服务器无缓存需在线下载） |

### 所有参数均经 `--help` 验证存在，无不存在参数。

---
