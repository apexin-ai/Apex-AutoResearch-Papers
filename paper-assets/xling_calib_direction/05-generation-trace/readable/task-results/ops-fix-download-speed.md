# ops fix download speed

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_download_speed_20260520T214824_result.json`
- **Structured JSON:** [`f2d94dcd704d8ebb046e.json`](../../sessions/f2/f2d94dcd704d8ebb046e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据充足，可以出报告了。

---

## 修复报告

### 1. 旧下载进程终止确认
| 进程 | 旧 PID | 状态 |
|------|--------|------|
| Qwen3 (ModelScope) | 28071 | **已终止** |
| Llama4 (hf download + xet) | 28924 | **已终止** |

### 2. 新下载方式和 PID
| 模型 | 方式 | PID | 状态 |
|------|------|-----|------|
| Qwen3-235B-A22B-GPTQ-Int4 | HF Mirror (`snapshot_download`) | **32724** | 运行中 |
| Llama4-Scout-W4A16 | HF Mirror (`snapshot_download`) | **32019** | 运行中 |

两个下载均设置 `HF_HUB_DISABLE_XET=1`，避免 xet bridge 超时。

### 3. 实测下载速度
基于多次采样（T2-T6, ~150 秒跨度）：

| 模型 | 旧速度 | 新速度 | 提升 |
|------|--------|--------|------|
| Qwen3 | ~5 MB/s (ModelScope) | ~3 MB/s (带宽共享中) | 等 Llama4 完成后预计 12 MB/s |
| Llama4 | **卡死** (xet timeout) | ~8 MB/s | 从不可用到正常 |

合计带宽 ~11-12 MB/s，两个下载并行共享。

### 4. 预估完成时间

| 模型 | 总大小 | 已下载 | 剩余 | 预估完成 |
|------|--------|--------|------|----------|
| Llama4 | 64.9 GB | 15.1 GB | 49.8 GB | **~1.7h**（@8 MB/s） |
| Qwen3 | 124.6 GB | 0.2 GB | 124.4 GB | **~4.2h**（前期 3MB/s + Llama4 完成后 12MB/s） |

**全部完成预估：约 4.2 小时（原预估 55 小时，缩短 92%）。**

### 5. 续传起点
- Llama4: 15.1 GB 已下载（8 个 .incomplete 文件，1.3-2.0 GB 各）
- Qwen3: 从 0 重新开始（ModelScope 的 `._____temp` 格式与 HF 不兼容，已清理释放空间）

### 6. 磁盘使用
- 数据盘 `/root/autodl-tmp`: **350 GB 总 / 105 GB 已用 / 246 GB 可用**
- 两模型总需 189.5 GB，剩余空间充足

### 监控命令
```bash
# 检查进度
tail -5 /root/autodl-tmp/download_qwen3_hfmirror.log
tail -5 /root/autodl-tmp/download_llama4_hfmirror.log
du -sh /root/autodl-tmp/models/Qwen3-235B-A22B-GPTQ-Int4/ /root/autodl-tmp/models/Llama4-Scout-W4A16/

# 检查进程存活
ps -p 32724 32019 -o pid,etime,rss
```

---
