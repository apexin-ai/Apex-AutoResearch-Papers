# Llama-70B Download Check

**时间**: 2026-05-24 06:56 UTC

## 状态：进行中

### 进程
- PID 179639: **running** (elapsed 36min, ModelScope snapshot_download)

### 文件完整性

**Final dir** (`LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4/`):
- safetensors: **3/9 完成** (model-00004, 00005, 00006，各 4.55G)
- tokenizer: present (tokenizer.json 8.7M, tokenizer_config.json 55K)
- config.json: **missing**
- USE_POLICY.md: present
- total size: 14G

**Temp dir** (`._____temp/LLM-Research/Meta-Llama-3.1-70B-Instruct-AWQ-INT4/`):
- safetensors: **4/9 下载中**
  - model-00001: 2.19G/4.63G (47%)
  - model-00003: 2.28G/4.55G (50%)
  - model-00007: 2.16G/4.55G (47%)
  - model-00009: 1.91G/1.96G (97%, 即将完成)
- total size: 16G

**未开始**: model-00002, model-00008 (各约 4.5G)

- incomplete files: none
- HF cache: 无相关 safetensors

### 磁盘
- /root/autodl-tmp: 231G/250G used (93%), **20G available**
- models 目录总大小: 173G
- 预计还需下载: ~14G (2个未开始的 shard + 当前4个剩余部分)
- ⚠️ 磁盘空间充足（20G > 14G remaining + temp cleanup）

### 下载日志末尾
```
Downloading [model-00001-of-00009.safetensors]:  47%  2.17G/4.63G [36:03<1:42:50, 428kB/s]
Downloading [model-00009-of-00009.safetensors]:  96%  1.88G/1.96G [16:19<02:36, 509kB/s]
Downloading [model-00007-of-00009.safetensors]:  47%  2.14G/4.55G [36:03<1:39:39, 433kB/s]
Downloading [model-00003-of-00009.safetensors]:  50%  2.27G/4.55G [36:05<1:38:12, 417kB/s]
```

### 结论

下载仍在进行中，速度约 420-510 KB/s/stream（4路并行）。

- 当前批次（4个文件）预计 ~1h40m 完成
- model-00009 约 3 分钟内完成，之后 model-00002 开始下载
- model-00002 和 model-00008 各需 ~2.5-3h
- **总预计完成时间：约 3-4.5 小时后**（取决于并行调度）
- config.json 等小文件预计在最后阶段下载
