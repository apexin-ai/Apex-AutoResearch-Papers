# westd-48478 Repo-level CWM 训练就绪检查报告

**日期**: 2026-05-12
**服务器**: seetacloud-westd-4x5090 (connect.westd.seetacloud.com:48478)

## 结论：⚠️ 可以跑，但需要注意 2 个问题

---

## 1. 磁盘空间

| 分区 | 总量 | 已用 | 可用 | 挂载 |
|------|------|------|------|------|
| 根分区 (overlay) | 30G | 20G | **11G** | `/` (含 `/home/sonny/`) |
| 数据盘 (XFS) | ~250G | ~107G | **~143G** | `/root/autodl-tmp/` |

- 项目目录 `/home/sonny/exec-sim-repair-verifier/`: **4.5G**
- 训练数据 `data/swebench_full/`: **1.1G**
- Qwen3-4B 模型: `/root/.cache/huggingface/hub/Qwen/Qwen3-4B` (7.6G)

**⚠️ 风险**: 根分区只剩 11G，之前 v3 就是磁盘满死的。脚本 `output_dir` 默认写 `/root/autodl-tmp/checkpoints_repo_cwm/`（数据盘，143G free），checkpoint 不会塞满根分区。**必须设 `HF_HOME=/root/autodl-tmp/.hf_cache`**，否则 HF datasets cache 可能写到根分区。

## 2. GPU 状态

| GPU | 型号 | 显存 | 占用 | 状态 |
|-----|------|------|------|------|
| cuda:0 | RTX 5090 | 32G | 0 MiB | 空闲 |
| cuda:1 | RTX 5090 | 32G | 0 MiB | 空闲 |
| cuda:2 | RTX 5090 | 32G | 0 MiB | **空闲 ✅** |
| cuda:3 | RTX 5090 | 32G | 0 MiB | **空闲 ✅** |

CUDA 13.0, Driver 580.105.08。4 张卡全部空闲，无进程占用。

## 3. 环境

- **Python**: 3.12 (miniconda3 at `/root/miniconda3`)
- **PyTorch**: 2.10.0+cu128 ✅
- **transformers**: 已安装 ✅
- **peft**: 已安装 ✅
- **accelerate**: 已安装 ✅
- **Qwen3-4B**: 已下载 (7.6G) ✅

## 4. 训练代码和数据

- `train_repo_cwm.py`: **存在 ✅**
- `data/swebench_full/swebench_train.jsonl`: **70,748 条 ✅**
- `data/swebench_full/swebench_val.jsonl`: **9,335 条 ✅**
- `swebench_pertest_data/`: **不存在**（但脚本不需要它，读的是 `data/swebench_full/`）
- `checkpoints_repo_cwm/`: 空目录（之前 v3 失败后清空了）

## 5. RAM

- 总量: **754G**, 可用: **617G**
- cgroup 限制: **~360G**
- 4B 模型 + 70k 样本单进程训练需 ~100-150G peak → **充足 ✅**
- **禁止并行训练两个模型**（v3 OOM 教训：两个 4B + 2×70k 超过 360G cgroup 限制）

## 6. SSH 连接问题

`westd-48478` 配置的密码**认证失败**，只有 `seetacloud-westd-4x5090` 能连通。两者指向同一台机器，但 `westd-48478` 的加密密码可能过期。后续操作需用 `seetacloud-westd-4x5090` 作为 server name。

---

## 建议的训练启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

export HF_HOME=/root/autodl-tmp/.hf_cache
export TRANSFORMERS_CACHE=/root/autodl-tmp/.hf_cache
export TMPDIR=/root/autodl-tmp/tmp
mkdir -p $TMPDIR

CUDA_VISIBLE_DEVICES=2 nohup python /home/sonny/exec-sim-repair-verifier/train_repo_cwm.py \
    --device cuda:0 \
    --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B \
    --data_dir /home/sonny/exec-sim-repair-verifier/data/swebench_full \
    --output_dir /root/autodl-tmp/checkpoints_repo_cwm/ \
    --run_name repo-cwm-4b-v4 \
    --save_steps 200 \
    > /root/autodl-tmp/train_repo_cwm.log 2>&1 &

# CUDA_VISIBLE_DEVICES=2 使物理 cuda:2 映射为进程内 cuda:0
# 如果想用 cuda:3，改为 CUDA_VISIBLE_DEVICES=3
```

## Checklist

- [x] GPU 空闲 (cuda:2, cuda:3 均可用)
- [x] 训练代码存在
- [x] 训练数据存在 (80k 条)
- [x] ML 依赖已装 (torch/transformers/peft/accelerate)
- [x] 模型已下载 (Qwen3-4B)
- [x] RAM 充足 (360G cgroup, 单进程 ok)
- [x] 数据盘空间充足 (143G free)
- [⚠️] 根分区紧张 (11G free) — 必须设 HF_HOME 到数据盘
- [⚠️] SSH: 需用 `seetacloud-westd-4x5090` 连接，`westd-48478` 认证失败
