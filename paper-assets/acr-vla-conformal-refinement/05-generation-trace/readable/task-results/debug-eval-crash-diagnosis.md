# debug eval crash diagnosis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_eval-crash-diagnosis_20260513T104708_result.json`
- **Structured JSON:** [`89410cb487442b017de2.json`](../../sessions/89/89410cb487442b017de2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地没有 src/ 目录，代码只在服务器上。修改已直接在服务器完成。

## 诊断结果

### 崩溃根因

**`AutoProcessor.from_pretrained` 联网失败。** SmolVLA 加载时，`transformers` 库尝试从 HuggingFace 下载 `chat_template.jinja` 文件。AutoDL 服务器默认网络不通（`[Errno 101] Network is unreachable`），导致：

1. 模型加载过程中 HTTP 重试超时
2. `RuntimeError: Cannot send a request, as the client has been closed.`
3. 最终 `OSError: Can't load processor for 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct'`

之前用 `tee` 重定向时，stderr 缓冲+退出码掩盖 → 看起来像"无声崩溃"。

### 已排除的问题
- MuJoCo/robosuite 兼容性 → 正常（50 步 step 无崩溃）
- 同时创建 10 个 LIBERO 环境 → 正常
- GPU OOM → 4090 有 24GB，SmolVLA 仅占 0.94GB
- LIBERO assets → 完整可用

### 已实施修复（evaluate.py）

1. **L34-35**: `os.environ.setdefault("HF_HUB_OFFLINE", "1")` + `TRANSFORMERS_OFFLINE=1` — 强制离线模式，跳过 HF 网络检查
2. **L204-211**: `rollout_single` 中 `env.step()` 包裹 `try/except` — 捕获运行时异常并打印 traceback
3. **L341-345**: SIGSEGV handler — 捕获潜在的 MuJoCo segfault 并输出信号编号

### 验证结果
离线模式下完成 50 步 rollout，全程 GPU 稳定 0.94GB，**无崩溃**。

### 运行 evaluate.py 的正确方式
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/acr-vla-conformal-refinement
python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 1 2>&1
```
不要用 `tee`，用 `2>&1` 合并 stderr 到 stdout。`-u` 关闭 Python 输出缓冲。`HF_HUB_OFFLINE=1` 已内置在脚本中。

---
