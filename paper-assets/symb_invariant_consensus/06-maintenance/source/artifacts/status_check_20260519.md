# 实验状态检查 2026-05-19 19:19 UTC

## 摘要

| 状态 | 数量 | 实验 |
|------|------|------|
| RUNNING | 6 | exp-048, exp-062, exp-064, exp-065, exp-066, exp-068 |
| FINISHED | 2 | exp-063, exp-067 |

Registry 显示 10 个 RUNNING，实际 6 个在跑、2 个已完成。exp-066 未在 registry 检查列表中但实际在跑。

---

## westd-25068 (4x RTX PRO 6000 Blackwell)

### nvidia-smi

| GPU | 状态 | 显存 | 利用率 | PID | 进程 |
|-----|------|------|--------|-----|------|
| cuda:0 | 占用 | 88292/97887 MiB | 96% | 190753 | VLLM (Qwen2.5-7B, port 8010, exp-065) |
| cuda:1 | 占用 | 88240/97887 MiB | 97% | 189895 | VLLM (Qwen2.5-14B, port 8011, exp-066) |
| cuda:2 | **空闲** | 0 MiB | 0% | - | - |
| cuda:3 | 占用 | 88106/97887 MiB | 96% | 192666 | VLLM (Gemma-27B, port 8003, exp-062) |

### tmux sessions

```
exp033_run    (01:48)  ← 旧 session
exp034_run    (01:48)  ← 旧 session
exp035_run    (01:48)  ← 旧 session
exp062_vllm   (16:53)
exp062_run    (17:02)
exp065_vllm   (16:50)
exp065_run    (16:53)
exp066_vllm   (16:50)
exp066_run    (16:56)
model_dl_25068 (01:02)  ← 旧 session
```

### 实验状态

| 实验 | 模型 | GPU | 状态 | 进度 | 备注 |
|------|------|-----|------|------|------|
| exp-062 | Gemma-3-27B-IT | cuda:3 | **RUNNING** | 80/204 (39%) | FOLIO, port 8003 |
| exp-065 | Qwen2.5-7B | cuda:0 | **RUNNING** | 262/600 (44%) | PW600, port 8010 |
| exp-066 | Qwen2.5-14B | cuda:1 | **RUNNING** | 198/204 (97%) | FOLIO seed123, port 8011, 即将完成 |
| exp-067 | Mistral-7B | - | **FINISHED** | 204/204 | 结果: `exp067_mistral_folio_seed789/exp067_results.json` (314KB) |

### 空闲 GPU: cuda:2

---

## westd-16639 (4x RTX PRO 6000 Blackwell)

### nvidia-smi

| GPU | 状态 | 显存 | 利用率 | PID | 进程 |
|-----|------|------|--------|-----|------|
| cuda:0 | **空闲** | 0 MiB | 0% | - | - |
| cuda:1 | 占用 | 88278/97887 MiB | 97% | 142896 | VLLM (Qwen3-14B, port 8001, exp-068) |
| cuda:2 | 占用 | 88246/97887 MiB | 95% | 125544 | VLLM (DeepSeek-R1-Qwen3-8B, port 8002, exp-064) |
| cuda:3 | 占用 | 88254/97887 MiB | 97% | 76474 | VLLM (LLaMA-8B, port 8003, exp-048) |

### tmux sessions

```
exp048_vllm   (10:19)
exp048_run    (10:20)
exp064_vllm   (16:44)
exp064_run    (16:56)
exp068_vllm   (19:08)
exp068_run    (19:13)
```

### 实验状态

| 实验 | 模型 | GPU | 状态 | 进度 | 备注 |
|------|------|-----|------|------|------|
| exp-048 | LLaMA-3.1-8B | cuda:3 | **RUNNING** | 419/600 (70%) | PW600, port 8003 |
| exp-063 | LLaMA-3.1-8B | - | **FINISHED** | 204/204 | FOLIO, SICA=61.8%, SC=66.2% |
| exp-064 | DeepSeek-R1-Qwen3-8B | cuda:2 | **RUNNING** | 52/204 (25%) | FOLIO, port 8002 |
| exp-068 | Qwen3-14B | cuda:1 | **RUNNING** | 11/200 (6%) | LogiQA200, port 8001, 刚启动 |

### 空闲 GPU: cuda:0

---

## 结果文件检查

| 实验 | 文件路径 | 存在 | 大小 |
|------|----------|------|------|
| exp-063 | `results/exp-063-llama8b-folio204-16639/results.json` | ✅ | 300,757 bytes |
| exp-067 | `results/exp067_mistral_folio_seed789/exp067_results.json` | ✅ | 314,648 bytes |
| exp-068 | `results/exp068_qwen3_logiqa200/exp068_results.json` | ✅ 部分 | 15,496 bytes (运行中) |

## 空闲 GPU 汇总

| 服务器 | 空闲 GPU |
|--------|----------|
| westd-25068 | cuda:2 |
| westd-16639 | cuda:0 |

共 2 张空闲 GPU 可用。
