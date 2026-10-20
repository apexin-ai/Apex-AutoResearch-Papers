# code eval pipeline prep

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-prep_20260519T234138_result.json`
- **Structured JSON:** [`db879fc75668becaa762.json`](../../sessions/db/db879fc75668becaa762.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## Eval Pipeline 就绪状态清单

### 1. Eval 脚本 — **READY**
| 文件 | 状态 |
|------|------|
| `run_heatmap_eval.py` | ✅ 完整，含模型加载+推理+评估全流程 |
| `eval_pride.py` | ✅ 完整，支持 JSON/log 两种输入格式 |
| `extract_ground_truth.py` | ✅ 完整，HDF5→ground truth 投影 |
| `heatmap_metrics.py` | ✅ 存在 |
| `launch_eval.sh` | ✅ 一键运行脚本，已配置 conda 激活 |

### 2. 环境依赖 — **READY**
| 依赖 | 状态 |
|------|------|
| robosuite | ✅ 已安装（有 minor warnings，不影响） |
| LIBERO | ✅ 已安装 |
| python | ⚠️ `python3` 不在 PATH，需通过 conda (`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`)。`launch_eval.sh` 已正确配置。 |

### 3. Ground Truth 数据 — **READY**
| 数据 | 状态 |
|------|------|
| LIBERO 数据集 | ✅ `/root/autodl-tmp/LIBERO-datasets/` 含全部 5 个 suite (libero_10, libero_90, libero_goal, libero_object, libero_spatial) |
| HDF5 demo 文件 | ✅ libero_10 有 10 个 task 文件 |
| Ground truth 提取 | 运行时从 HDF5 在线提取，无需预生成 |

### 4. Checkpoint 兼容性 — **READY**
| 检查项 | 状态 |
|--------|------|
| Decoder 保存格式 | ✅ `afford_decoder--{step}_checkpoint.pt`，eval 脚本的 glob pattern `afford_decoder--*_checkpoint.pt` 能匹配 |
| Decoder 架构参数 | ✅ 训练: `AffordanceDecoder(hidden_dim=llm_dim, output_size=128, mid_dim=256)` = eval 完全一致 |
| forward 方法 | ✅ 训练用 `forward_with_features()` (需要中间特征算 L_transfer)，eval 用 `forward()` (只需 heatmap)。两个方法共享同一套权重，互不冲突 |
| 当前 checkpoint | 训练仍在进行中，最新 checkpoint-5000。每 500 步保存一次 |

### 5. 磁盘 — **需关注**
| 分区 | 状态 |
|------|------|
| 根分区 `/` | ⚠️ 30G 中已用 22G (72%)，剩余 8.6G。若 checkpoint 继续写根分区需注意 |
| 数据盘 `/root/autodl-tmp/` | ✅ 350G 中用 125G，剩余 226G |

### 6. 可直接使用的 eval 命令

训练完成后执行:
```bash
bash /root/afford_invar/scripts/evaluation/launch_eval.sh \
  /root/afford_invar/runs/libero_goal_no_noops+transfer+b2+lr0.0005+beta0.1/checkpoint-20000 \
  cuda:1
```

**结论: eval pipeline 全部就绪，无需修复。唯一需要监控的是根分区磁盘空间（每 500 步一个 checkpoint 会累积）。**

---
