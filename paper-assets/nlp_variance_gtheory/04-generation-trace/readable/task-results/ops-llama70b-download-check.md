# ops llama70b download check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama70b_download_check_20260523T110628_result.json`
- **Structured JSON:** [`c92bd5e6b4dc968dfc45.json`](../../sessions/c9/c92bd5e6b4dc968dfc45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 下载状态报告

**进程**: 存活。PID 318630/318664 运行 ~5h06m。

**实际下载路径**（非预期的 `/root/autodl-tmp/models/` ）:
- 完成文件: `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-70B-Instruct/`
- 临时文件: `/root/autodl-tmp/.hf_cache/._____temp/LLM-Research/Meta-Llama-3.1-70B-Instruct/`

**Safetensors 进度** (30 个分片):
| 状态 | 文件 | 大小 |
|------|------|------|
| 已完成 | model-00001, model-00002 | 8.7G |
| 下载中 | model-00003 ~ model-00010 (8个) | 6.8G / ~37G |
| 未开始 | model-00011 ~ model-00030 (20个) | ~90G |

**⚠️ 关键问题: `ignore_file_pattern` 未生效**
正在同时下载 7 个 `original/consolidated.*.pth` 文件，已占 **108G**（各文件 60-98% 完成，总计约 131G）。这些文件是不需要的，白白消耗带宽和磁盘空间。

**磁盘空间**:
- 数据盘: 350G 总 / 132G 已用 / **219G 可用**
- HF cache 当前: 125G
- 预计总需: ~266G（safetensors ~135G + pth ~131G）→ 空间够但很紧

**速度**: safetensors ~1-2 MB/s/文件，pth ~500KB/s/文件。

**预计剩余时间**: ~3-4 小时（safetensors + pth 共享带宽）。

**建议**: 
- 让下载跑完（pth 已下载 108G 的 80%+，杀掉浪费）
- 下载完成后删除 pth 文件释放 ~131G 空间
- 下载完成后创建软链接 `/root/autodl-tmp/models/Llama-3.1-70B-Instruct/ → /root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-70B-Instruct/`

---
