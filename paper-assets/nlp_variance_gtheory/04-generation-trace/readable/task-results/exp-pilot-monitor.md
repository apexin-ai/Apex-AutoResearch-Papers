# exp pilot monitor

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pilot_monitor_20260520T231630_result.json`
- **Structured JSON:** [`54fb6e7e024da8807241.json`](../../sessions/54/54fb6e7e024da8807241.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因明确了。

---

**Pilot 完成状态：全部失败**

三个进程全部在启动时立即崩溃，原因相同：

**错误：** vLLM 无法加载模型 `Qwen/Qwen3-8B-Instruct`
- 本地路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B-Instruct/` 存在但**为空**（模型未下载）
- 远程 HF mirror (`hf-mirror.com`) 返回 **401 认证错误** — "Repository Not Found / Invalid username or password"

```
- float32 (GPU 0): 0 records [失败]
- bfloat16 (GPU 1): 0 records [失败]
- float16 (GPU 2): 0 records [失败]
总计：0 records
enforce_eager：未到达该阶段
错误：401 HF mirror 认证失败，模型未下载
```

**需要修复：**
1. 先下载模型到本地。推荐用 ModelScope（AutoDL 上 HF 下载极慢且需认证）：
   ```bash
   pip install modelscope
   python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen3-8B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')"
   ```
2. 实验脚本中 `model_path` 改为本地绝对路径（如 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B-Instruct`），而非 HF repo ID
3. 重新启动三个 pilot 进程

是否现在执行模型下载和重新运行？

---
