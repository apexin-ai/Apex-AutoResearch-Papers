# diagnose eval pi05 random k09 strict fail

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k09_strict_fail_20260527T091307_result.json`
- **Structured JSON:** [`0c4035577b0e5941219b.json`](../../sessions/0c/0c4035577b0e5941219b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败根因**：`[Errno 101] Network is unreachable` — `transformers` 加载 tokenizer `google/paligemma-3b-pt-224` 时，`_patch_mistral_regex()` 内部调用 `model_info()` 向 HuggingFace Hub 发起网络请求，但服务器网络不通。

**两个实验同一原因**：是，完全相同的 traceback。

**部分结果**：无。两个实验都在初始化阶段（模型加载完、构建 preprocessor 时）就崩溃了，未进入任何 evaluation episode。

**GPU 当前状态**：
| GPU | 状态 | 显存占用 | 利用率 |
|-----|------|----------|--------|
| 0 | **空闲可用** | 1MiB | 0% |
| 1 | **空闲可用** | 1MiB | 0% |
| 2 | 占用 | 10796MiB | 48% |
| 3 | 占用 | 10364MiB | 53% |

**修复方案**：重跑前需要做以下之一（推荐两者都做）：
1. 启动脚本中加 `source /etc/network_turbo`（修复 AutoDL 网络）
2. 设置 `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1` 环境变量（tokenizer 文件已在本地缓存，不需要联网）

方案 2 更稳健——即使网络恢复后也避免初始化时的无意义网络请求。是否需要我立即修复并重跑？

---
