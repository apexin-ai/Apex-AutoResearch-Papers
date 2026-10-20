# diagnose tracvla spatial pipeline

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_tracvla_spatial_pipeline_20260521T021542_result.json`
- **Structured JSON:** [`7f43b9a037cc090f07d6.json`](../../sessions/7f/7f43b9a037cc090f07d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告

### 根因

**两个独立问题叠加：**

**问题 1（主要）：untrained 模型未预下载，网络不通导致加载失败**

脚本逻辑（第 638-641 行）：先检查本地缓存 `UNTRAINED_CACHE` 目录下有无 `config.json`，没有则从 HuggingFace 在线下载 `microsoft/Phi-3-vision-128k-instruct`。

实际情况：
- `/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/config.json` **不存在**
- 缓存目录内只有 tokenizer 文件和两个 `.incomplete` 的 blob（10MB + 20MB），模型权重未下载完
- 网络不通（`[Errno 101] Network is unreachable`），HF 重试 5 次后失败
- 脚本 catch 了异常，打印 `Skipping untrained condition`，只跑了 trained 一半

**问题 2（次要）：EXIT_CODE=129 (SIGHUP)**

进程收到 SIGHUP 信号。但 trained 条件的 4 个结果文件已全部生成（`action_r2_probing.json`, `counterfactual_combined.json`, `cross_instruction_classification.json`, `l1_attention_profile.json`），说明 trained 条件实际跑完了。SIGHUP 发生在脚本结束阶段或之后。

### 关键日志摘录

```
[Errno 101] Network is unreachable

[10:09:05]   ERROR loading untrained model: We couldn't connect to 
'https://huggingface.co' to load this file, couldn't find it in the 
cached files and it looks like microsoft/Phi-3-vision-128k-instruct 
is not the path to a directory containing a file named config.json.

[10:09:05]   Skipping untrained condition
[10:09:05] All done in 4.2 min
EXIT_CODE=129
```

### 当前状态

| 条件 | 状态 | 结果文件 |
|------|------|----------|
| trained | **完成** | 4 个 JSON 全部生成 |
| untrained | **跳过** | 目录不存在 |

### 修复方案

1. **先下载 untrained 模型到本地**（在网络通的时候）：
   ```bash
   source /etc/network_turbo
   export HF_HOME=/root/autodl-tmp/.hf_cache
   python3 -c "
   from transformers import AutoModelForCausalLM, AutoProcessor
   m = AutoModelForCausalLM.from_pretrained('microsoft/Phi-3-vision-128k-instruct', 
       trust_remote_code=True, torch_dtype='auto',
       cache_dir='/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/')
   m.save_pretrained('/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/')
   p = AutoProcessor.from_pretrained('microsoft/Phi-3-vision-128k-instruct',
       trust_remote_code=True,
       cache_dir='/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/')
   p.save_pretrained('/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/')
   "
   ```
   下载完后 `config.json` 会存在，脚本会自动走本地路径。

2. **只重跑 untrained 条件**（trained 已完成，无需重跑）：
   ```bash
   tmux new -s tracvla
   python /root/autodl-tmp/vla-ssd/scripts/tracvla_spatial_full_pipeline.py --conditions untrained
   ```

3. **用 tmux 防止 SIGHUP**。

### 能否直接重试

不能直接重试——先要把 untrained 模型下载到本地。下载完成后，只需跑 `--conditions untrained`，trained 的结果可以复用。

---
