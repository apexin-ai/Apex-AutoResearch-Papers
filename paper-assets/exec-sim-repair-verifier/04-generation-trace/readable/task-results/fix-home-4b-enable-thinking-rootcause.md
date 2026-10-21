# fix home 4b enable thinking rootcause

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_home-4b-enable-thinking-rootcause_20260515T015407_result.json`
- **Structured JSON:** [`21a5ca10cee398dda865.json`](../../sessions/21/21a5ca10cee398dda865.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码状态确认。以下是完整报告。

---

## 产出报告

### 1. Kill 结果
- PID 3199357 已 kill（SIGTERM，无需 SIGKILL）
- GPU 完全释放（nvidia-smi 显示无 compute apps）

### 2. 根因分析：enable_thinking 不是真正根因

**原始代码已经在 chat template 层正确禁用了 thinking**：
- `detect_thinking_support()` 检测到 Qwen3 支持 `enable_thinking` 参数
- 返回 `{"enable_thinking": False}` 作为 `tmpl_kw`
- `apply_chat_template(..., enable_thinking=False)` 预填空 `&lt;think>\n\n&lt;/think>` 块
- 所有已保存的 predictions 的 `gen_text` 都是干净的 "pass"/"fail"，**零 thinking tokens**

**实验验证**：
- Qwen3-4B 的 `generation_config` 默认**不含** `enable_thinking` 字段（不是 True）
- `model.generate(..., enable_thinking=False)` **会 crash**（transformers 4.57.6 的 `_validate_model_kwargs` 报 ValueError）
- 加 `generation_config.enable_thinking = False` 无害但可能也无实际效果

### 3. 代码修改

唯一保留的改动：`load_model()` 中加了 `generation_config.enable_thinking = False`（第 142-143 行），作为防御性措施。

**已回滚**：`model.generate()` 中加 `enable_thinking=False` 会导致 `ValueError: model_kwargs not used: ['enable_thinking']`，已撤回。

### 4. 进程实际不是"卡死"

tmux `eval_8b_val5120_fix` 的日志显示进程**正在正常处理**：
- ~7.5s/batch, batch_size=16, max_seq_length=5120
- running_acc=89.7%
- `repo_cls_v5_ckpt4400_val5120`: 已处理 6544/9335 samples（70%）后被 kill
- `repo_cls_v5_ckpt4400_val5120_v2`: 已处理 2000/9335 samples 后被本次 kill

### 5. Watchdog 分析

Watchdog (180s) 未触发因为**每个 batch 在 180s 内完成**（7.5-7.8s/batch）。Watchdog 实现本身没有 bug。

注意 SIGALRM handler 有一个潜在问题：无法中断 CUDA kernel 调用（信号只在 Python 字节码执行时处理），但线程 watchdog 用 `os._exit(1)` 兜底，在正常情况下是有效的。

### 6. 真正的性能瓶颈

- **flash-attn 未安装**，使用 SDPA fallback
- 9335 test samples × 7.5s/batch ÷ 16 ≈ **73 分钟**总运行时间（4B 模型实际上很快）
- VRAM ~7.5GB 用于 4B 模型（不是 31.7GB）

**建议**：如果观测到 31.7GB VRAM，可能是在运行 8B 模型时（tmux session 名含 "8b"），不是 4B。

---
