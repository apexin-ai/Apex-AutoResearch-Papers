# ssh m023 verify standard 15 v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_m023_verify_standard_15_v3_20260520T215909_result.json`
- **Structured JSON:** [`a6d536ae2695c777905a.json`](../../sessions/a6/a6d536ae2695c777905a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

**两个实验正在启动中，处于模型加载阶段，暂无报错。**

| 检查项 | seed123 (PID 287784) | seed456 (PID 287862) |
|--------|---------------------|---------------------|
| 进程状态 | 存活，Python 子进程 287789 CPU 514% | 存活，Python 子进程 287867 CPU 483% |
| GPU 显存 | cuda:2 = **3 MiB**（未上卡） | cuda:3 = **3 MiB**（未上卡） |
| Log 最后输出 | `Loading pruned model from .../sft_standard_15` → `Non-uniform MLP detected` | 同左 |
| 网络错误 | 无 | 无 |

**分析**：
- 两个进程刚启动约 1 分钟，正在 CPU 上加载模型权重（CPU 占用 500%+ 说明在做大文件 mmap/反序列化），尚未将模型搬到 GPU。这是正常行为。
- `HF_HUB_OFFLINE=1` 生效，没有触发任何网络请求 — v2 的下载问题已解决。
- Log 中 `Non-uniform MLP detected: intermediate_size range [8128, 18944]` 确认读到了正确的剪枝模型。
- GPU 0/1 被 GSM8K eval 占用（~30GB each），与本实验无冲突。

**结论**：v3 启动正常，预计 2-3 分钟后模型上卡，GPU 2/3 显存会跳到 ~14-15GB 并开始训练。如需二次确认可稍后再查。

---
