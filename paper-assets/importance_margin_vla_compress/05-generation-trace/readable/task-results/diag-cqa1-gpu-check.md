# diag cqa1 gpu check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cqa1_gpu_check_20260525T070304_result.json`
- **Structured JSON:** [`7de0e21db45f7570549b.json`](../../sessions/7d/7de0e21db45f7570549b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### GPU 状态（4 张 RTX 4090 / 24GB）
| GPU | Util | Memory |
|-----|------|--------|
| 0–3 | **0%** | **0 MiB / 24GB** |

全部空闲，无任何 Python 训练/eval 进程。仅有系统自带的 supervisord/tensorboard/jupyter。

### 进程 & Tmux 状态
- **无 GPU 进程**：`ps aux | grep python` 仅返回系统服务（tensorboard、jupyter-lab、tensorboard_data_server），无 eval/training 进程
- **僵尸 tmux session**：`eval_pi05_l2norm_k03_goal_seed42`（May 24 启动）仍残留，但底下的 Python 子进程已退出，shell 壳还在挂着

### 实验状态：**情况B — 4 个 cliff batch (k=0.85) 实验全部挂掉，失败原因相同**

最近 4 个实验（13:42–13:44，几乎同时失败）：
- `eval_pi05_random_k085_long_seed42_postfix_v3`
- `eval_pi05_l2norm_k085_long_seed42_postfix_v3`
- `eval_pi05_l2norm_k085_object_seed42_postfix_v2`
- `eval_pi05_random_k085_goal_seed42_postfix_v3`

**根因**（4 个日志尾部完全一致）：
```
httpx.ConnectError: [Errno 99] Cannot assign requested address
ValueError: Failed to instantiate processor step 'tokenizer_processor'
  with config: ... 'tokenizer_name': 'google/paligemma-3b-pt-224'
EXIT_CODE=1
```

调用栈定位在 `eval_pi05_pruning_libero.py:160` → `make_pre_post_processors` → `PolicyProcessorPipeline.from_pretrained` → 试图通过 httpx 联网拉 `google/paligemma-3b-pt-224` 的 tokenizer。

**关键观察**：尽管脚本设置了 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`，lerobot 的 `PolicyProcessorPipeline` 在加载 `tokenizer_processor` 时**绕过了这些 offline 标志**，直接走 httpx 联网。`[Errno 99] Cannot assign requested address` 是网络层错误（端口耗尽或代理未启用），不是 GPU/CUDA 问题。

### 已完成的有效结果
JSON 结果目录中**没有 `*postfix_v3*` 对应的 JSON 文件**——4 个 k=0.85 cliff batch 实验都在 tokenizer 加载阶段就失败了，没有跑到 episode 评估，**没有产出任何结果**。

### 建议下一步
1. 清理僵尸 tmux session：`tmux kill-session -t eval_pi05_l2norm_k03_goal_seed42`
2. 修复 tokenizer 离线加载：在 eval 脚本中预先用 `AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224", local_files_only=True)` 触发缓存读取，或检查 `/root/autodl-tmp/.hf_cache/models--google--paligemma-3b-pt-224` 是否存在
3. 也可在脚本启动前 `source /etc/network_turbo` 启用代理，避免 httpx 连接失败
4. 重启失败的 4 个 k=0.85 实验

---
