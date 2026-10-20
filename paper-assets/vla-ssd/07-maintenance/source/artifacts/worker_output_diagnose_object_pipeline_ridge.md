# 诊断报告：object_pipeline_ridge 失败分析

## 失败的确切步骤和完整 traceback

**失败位置**：脚本第 534 行，`PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)`

**原因**：`trust_remote_code=True` 触发 HF Hub 下载自定义 Python 文件 `processing_prismatic.py`。cron 启动命令未执行 `source /etc/network_turbo`，AutoDL 实例直连 HuggingFace 不通（`[Errno 101] Network is unreachable`）。

**注意**：模型权重（4个 checkpoint shards）从本地缓存加载成功，不需要网络。仅 processor 的 dynamic module 文件需要从 HF 下载。

**Traceback 链**：
```
main() (line 614)
  → processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)  (line 534)
    → processing_utils.py:_get_arguments_from_pretrained
      → image_processing_auto.py:from_pretrained
        → dynamic_module_utils.py:get_class_from_dynamic_module
          → dynamic_module_utils.py:get_cached_module_file
            → hub.py:cached_file → hf_hub_download
              → OSError: Network is unreachable + LocalEntryNotFoundError (file not in local cache)
```

HF Hub 重试 5 次（1s, 2s, 4s, 8s, 8s），全部失败后抛出 OSError。

## 网络当前状态

| 条件 | HuggingFace 可达性 |
|------|-------------------|
| 无代理 | 不可达 (HTTP 000) |
| `source /etc/network_turbo` 后 | 可达 (HTTP 200) |

AutoDL 实例直连外网不通是常态，必须启用代理。

## 脚本中需要网络访问的位置

| 行号 | 代码 | 是否需要网络 |
|------|------|-------------|
| 26 | `from transformers import AutoModelForVision2Seq, AutoProcessor` | 否（仅 import） |
| 526 | `model = AutoModelForVision2Seq.from_pretrained(CKPT, ...)` | 否（权重已缓存） |
| 534 | `processor = mod.PrismaticProcessor.from_pretrained(CKPT, trust_remote_code=True)` | **是**（dynamic module 文件需下载，首次运行时） |

一旦 `processing_prismatic.py` 被缓存到本地，后续运行也不再需要网络。

## 可复用的中间结果

`/root/autodl-tmp/vla-ssd/results/libero_object/` 已有一次完整运行的结果（pipeline.log 显示 08:46 开始的完整 5-phase 运行）：

| 文件 | 内容 |
|------|------|
| `action_r2_probing.json` | 32 层 Ridge probe R² 结果（L0-L31, img_mean + last_preaction） |
| `counterfactual_combined.json` | Counterfactual 分析结果 |
| `cross_instruction_classification.json` | 10-way 分类结果 |
| `l1_attention_profile.json` | L1 attention profile |
| `rsa_analysis.json` | RSA 分析 |

## v2 运行状态

**v2 当前正在运行**（PID 541379，启动于 15:13），Phase 1 representation extraction 即将完成（Task 9/10, 4900/5000）。模型和 processor 加载成功（说明此次运行时 dynamic module 文件已被缓存，或者运行环境中有网络）。

## 建议

1. **无需重试** — v2 已经在正常运行，等待其完成即可。
2. **根因修复**：cron 的启动命令应加入 `source /etc/network_turbo`，或在脚本开头设置 `TRANSFORMERS_OFFLINE=1`（前提是所有需要的文件已缓存）。
3. **长期方案**：在脚本中加 `local_files_only=True` 参数给 `from_pretrained` 调用，确保不依赖网络。如果本地缓存缺文件则立即 fail-fast，而不是等待重试超时。
