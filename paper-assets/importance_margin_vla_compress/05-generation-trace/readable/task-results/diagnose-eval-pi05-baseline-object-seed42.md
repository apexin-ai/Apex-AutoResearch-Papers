# diagnose eval pi05 baseline object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_baseline_object_seed42_20260521T044551_result.json`
- **Structured JSON:** [`8d5054c8cded160ad58d.json`](../../sessions/8d/8d5054c8cded160ad58d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。两次运行情况：

**Run 1（job 提交，10:38，runs/ log）— 崩溃，EXIT_CODE=1**：
- 未执行 `source /etc/network_turbo`，网络不通
- `AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224')` 无法访问 HuggingFace
- 本地也没有 paligemma tokenizer 缓存

**Run 2（手动重跑，11:31，logs/ log）— 正在跑但 0% SR**：
- 网络通了，tokenizer 加载成功
- 跑完 T0-T5 全部 0/50=0%，进程在 T5 之后消失（GPU 1 已释放）
- 日志无 Traceback，可能是 SIGHUP（SSH 断连）或 MuJoCo segfault

```json
{"root_cause":"ValueError: Failed to instantiate processor step 'tokenizer_processor' ... OSError: Can't load the configuration of 'google/paligemma-3b-pt-224' — 因为 AutoDL 未执行 source /etc/network_turbo 导致网络不通，HF tokenizer 无法下载且本地无缓存","error_type":"infrastructure","fix_steps":["启动命令前加 source /etc/network_turbo 开启网络代理","或预下载 paligemma tokenizer 到本地: python -c \"from transformers import AutoTokenizer; t=AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224'); t.save_pretrained('/root/autodl-tmp/.hf_cache/paligemma-3b-pt-224')\" 然后修改代码用本地路径","设置 HF_HOME=/root/autodl-tmp/.hf_cache 确保缓存持久化","重跑实验建议用 nohup 或 tmux 避免 SSH 断连杀进程","注意：即使修复基础设施问题，该社区 checkpoint 在所有任务上 SR=0%，需要排查模型本身是否可用"],"can_auto_fix":true,"full_traceback":"File eval_pi05_pruning_libero.py:284 main() -> line 149 make_pre_post_processors() -> factory.py:288 PolicyProcessorPipeline.from_pretrained() -> pipeline.py:572 _build_steps_with_overrides() -> pipeline.py:777 _instantiate_step() -> pipeline.py:908 ValueError: Failed to instantiate 'tokenizer_processor' -> tokenizer_processor.py:111 AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224') -> OSError: Can't load the configuration of 'google/paligemma-3b-pt-224' [Errno 101] Network is unreachable"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "ValueError: Failed to instantiate processor step 'tokenizer_processor' ... OSError: Can't load the configuration of 'google/paligemma-3b-pt-224' — 因为 AutoDL 未执行 source /etc/network_turbo 导致网络不通，HF tokenizer 无法下载且本地无缓存",
    "error_type": "infrastructure",
    "fix_steps": [
      "启动命令前加 source /etc/network_turbo 开启网络代理",
      "或预下载 paligemma tokenizer 到本地: python -c \"from transformers import AutoTokenizer; t=AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224'); t.save_pretrained('/root/autodl-tmp/.hf_cache/paligemma-3b-pt-224')\" 然后修改代码用本地路径",
      "设置 HF_HOME=/root/autodl-tmp/.hf_cache 确保缓存持久化",
      "重跑实验建议用 nohup 或 tmux 避免 SSH 断连杀进程",
      "注意：即使修复基础设施问题，该社区 checkpoint 在所有任务上 SR=0%，需要排查模型本身是否可用"
    ],
    "can_auto_fix": true,
    "full_traceback": "File eval_pi05_pruning_libero.py:284 main() -> line 149 make_pre_post_processors() -> factory.py:288 PolicyProcessorPipeline.from_pretrained() -> pipeline.py:572 _build_steps_with_overrides() -> pipeline.py:777 _instantiate_step() -> pipeline.py:908 ValueError: Failed to instantiate 'tokenizer_processor' -> tokenizer_processor.py:111 AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224') -> OSError: Can't load the configuration of 'google/paligemma-3b-pt-224' [Errno 101] Network is unreachable"
  }
}
```

</details>

---
