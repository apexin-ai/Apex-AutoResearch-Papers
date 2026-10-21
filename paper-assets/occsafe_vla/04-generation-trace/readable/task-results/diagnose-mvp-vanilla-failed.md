# diagnose mvp vanilla failed

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_vanilla_failed_20260520T072518_result.json`
- **Structured JSON:** [`efcec32147441d40ae2c.json`](../../sessions/ef/efcec32147441d40ae2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 错误类型
**网络不可达 + HF 缓存路径未配置**

### 具体错误消息
```
OSError: [Errno 101] Network is unreachable
```
```
OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it 
in the cached files and it looks like openvla/openvla-7b is not the path to a directory 
containing a file named config.json.
```

崩溃位置：`finetune.py:877`
```python
processor = AutoProcessor.from_pretrained(cfg.vla_path, trust_remote_code=True)
```

### 根因分析

两个实验错误完全一致，因果链如下：

1. **`vla_path` 默认值是 HF Hub ID** `"openvla/openvla-7b"`（非本地路径）
2. 代码 L856 调 `model_is_on_hf_hub(cfg.vla_path)` 尝试连 HF Hub → **网络不通**，返回 False
3. 因为返回 False，`snapshot_download` 未执行，`cfg.vla_path` **仍为** `"openvla/openvla-7b"`
4. L877 `AutoProcessor.from_pretrained("openvla/openvla-7b")` → 本地找不到这个相对路径，网络也不通 → **崩溃**

模型实际已缓存在两个位置：
- `/root/autodl-tmp/models/openvla-7b/config.json` ✅
- `/root/autodl-tmp/.hf_cache/hub/models--openvla--openvla-7b/` ✅

但启动时 **`HF_HOME` 未设置**（env 中没有），HF 库查默认路径 `~/.cache/huggingface/` 找不到缓存。

### 修复建议

**方案 A（推荐）**：启动命令加 `--vla_path /root/autodl-tmp/models/openvla-7b`，直接指向本地模型目录，跳过 HF Hub 检查。

**方案 B**：在启动脚本中 export `HF_HOME=/root/autodl-tmp/.hf_cache`，让 `from_pretrained` 能从 HF 缓存命中。

**方案 C**：启动前 `source /etc/network_turbo` 开代理（AutoDL 典型做法），但训练期间保持网络依赖不稳定，不建议。

---
