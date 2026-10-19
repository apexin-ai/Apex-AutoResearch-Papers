# code exp003 eval script

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003-eval-script_20260520T092621_result.json`
- **Structured JSON:** [`507eda25a7039912ad91.json`](../../sessions/50/507eda25a7039912ad91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本验证通过。

## 产出报告

### 脚本路径
| 服务器 | 路径 |
|--------|------|
| **westd-29046** | `/root/contrastive_entrain_calib/scripts/eval_exp003_d027.sh` |
| **westd-28034** | `/root/contrastive_entrain_calib/scripts/eval_exp003_d027.sh` |

### 用法
```bash
# 传 step 编号
bash scripts/eval_exp003_d027.sh 8000

# 或传完整 checkpoint 路径
bash scripts/eval_exp003_d027.sh /root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-8000

# 指定 GPU（默认 GPU 0）
GPU=3 bash scripts/eval_exp003_d027.sh 8000
```

### 建议在哪跑

**推荐 westd-29046**（训练完成后 GPU 空出，checkpoint 本地无需 scp）。当前已有 checkpoint-500 到 checkpoint-5000，max_steps=8000。

如果 29046 GPU 不释放，用 **westd-28034 GPU 0 或 GPU 3**（当前空闲），但需先 scp checkpoint（单个 adapter ~245MB）：
```bash
# 在 28034 上 scp（需确认 29046 的 SSH 端口/地址可达）
mkdir -p /root/contrastive_entrain_calib/checkpoints/exp003/
scp -r <29046_host>:/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-8000 \
    /root/contrastive_entrain_calib/checkpoints/exp003/checkpoint-8000
```

### 训练进度
- 当前 checkpoint：5000/8000（62.5%），最新 checkpoint-5000 生成于 May 20 16:46
- save_steps=500，预计还有 checkpoint-5500, 6000, 6500, 7000, 7500, 8000

---
