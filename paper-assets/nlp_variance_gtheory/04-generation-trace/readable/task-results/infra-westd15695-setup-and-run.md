# infra westd15695 setup and run

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd15695_setup_and_run_20260521T102428_result.json`
- **Structured JSON:** [`e8693d42ef8195b3e435.json`](../../sessions/e8/e8693d42ef8195b3e435.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 状态汇报

### 环境
| 项目 | 状态 |
|------|------|
| Python | 3.12.3 (conda base) |
| PyTorch | 2.11.0+cu130 |
| vLLM | 0.21.0 |
| CUDA | 13.0 / toolkit 12.8 |
| GPU | **1× NVIDIA RTX PRO 6000 Blackwell (98GB VRAM)** |

**注意**: 实例只有 1 个 GPU（非预期的 4 个），已调整为串行运行。

### GPU 信息
- 型号: NVIDIA RTX PRO 6000 Blackwell Server Edition
- 显存: 98GB — 单卡足以运行 9B 模型 (bf16 ~18GB)
- 计算能力: 12.0 (Blackwell)

### 项目文件
已从 westd-32570 传输：src/ (inference/design/config/data modules) + data/ (mmlu_items_exp001.json, few_shot_exp001.json)

### 设计矩阵
- `results/design_yi.csv`: 432 conditions (bf16 × 3 temps × 6 prompts × 6 seeds × 4 orderings)
- `results/design_olmo.csv`: 432 conditions（同上）

### 模型下载进度
7 路 wget 并行下载中，总速度 ~3.5 MB/s：
- **Yi-1.5-9B-Chat**: ~400MB / ~18GB (4 shards)
- **OLMo-2-1124-7B-Instruct**: ~650MB / ~14GB (3 shards)
- **预计完成**: ~2-3 小时

### 推理计划
`auto_start.sh` (PID 7309) 正在后台运行，会：
1. 每分钟检查 wget 是否全部完成
2. 验证模型分片完整性
3. 先跑 Yi (432 conditions, GPU 0) → 再跑 OLMo (432 conditions, GPU 0)

### 监控命令
```bash
# 查看下载进度
cat /tmp/auto_start.log

# 查看模型大小
du -sh /root/autodl-tmp/.hf_cache/01ai/ /root/autodl-tmp/.hf_cache/allenai/

# 查看推理日志（启动后）
tail -f results/exp001_yi/run.log
```

---
