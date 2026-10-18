# diagnose eval pi05 random k09 strict fail

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k09_strict_fail_20260527T091150_result.json`
- **Structured JSON:** [`7bb280711755319b45af.json`](../../sessions/7b/7bb280711755319b45af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验是**同一根因**：网络不可达导致 tokenizer 初始化失败。

## 诊断结果

**失败根因**: `httpx.ConnectError: [Errno 101] Network is unreachable`

调用链：`eval_pi05_pruning_libero.py:325` → `make_pre_post_processors()` → `AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224")` → 尝试连接 HuggingFace Hub → 网络不通。

两个实验都在模型加载完成后、eval 开始前崩溃（加载 4.1B 模型花了 ~2 分钟，之后立刻触发 tokenizer 下载失败）。

**Partial 结果**: **无**。两个实验都没有进入任何 task 的 eval 循环，0 个 episode 完成。

## 原因分析

AutoDL 实例的公网访问需要 `source /etc/network_turbo` 开启代理，但启动命令里没有这一步。之前其他实验可能已经在 shell session 里 source 过，但这次的 tmux/bash 环境没有继承。

或者更根本的解决方案：tokenizer 应该从本地缓存加载（`HF_HUB_OFFLINE=1`），而不是每次都联网查询。

## 重跑建议

1. **快速修复**：启动命令前加 `source /etc/network_turbo`，重跑即可
2. **更稳健的修复**：预先下载 `google/paligemma-3b-pt-224` tokenizer 到本地，设置 `HF_HUB_OFFLINE=1` 或 `TRANSFORMERS_OFFLINE=1`，避免依赖网络
3. 这是环境问题，不是代码 bug，可以直接重跑

---
