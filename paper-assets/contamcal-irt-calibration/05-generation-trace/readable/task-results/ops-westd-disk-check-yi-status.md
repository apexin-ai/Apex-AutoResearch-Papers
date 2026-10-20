# ops westd disk check yi status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-check-yi-status_20260522T131417_result.json`
- **Structured JSON:** [`567ccf405354a2df50eb.json`](../../sessions/56/567ccf405354a2df50eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. 磁盘空间

| 项目 | 大小 |
|------|------|
| 数据盘总量 | 250G |
| 已用 | 248G |
| **剩余** | **2.4G (100% used)** |
| checkpoints/ | 63G |
| .hf_cache/ | 31G |

### 2. Yi 训练状态

- **正在训练**：GPU 0 上运行 Yi-1.5-9B d000_s42，tmux session `yi15_d000`
- **进度**：88/3125 steps（~2.8%），刚跑了 ~6 分钟
- **速度**：~4.3s/step，预计还需 **~3.6 小时**
- **LoRA 配置**：r=16, alpha=32, lr=5e-5 ✓
- **输出目录**：目前 0 bytes（尚未保存 checkpoint）
- 最终 LoRA adapter 预计 ~300-400MB

另外还有一个 Yi-1.5-9B 模型下载进程（ModelScope snapshot_download，PID 633191）仍在运行，但模型 cache 只有 80K 在 `01-ai/` 目录——可能已下载到别的路径（17G 的 `Yi-1.5-9B/` 目录）。

### 3. GPU 使用

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 98% | 46.7G / 95.6G | Yi d000 训练中 |
| 1 | 0% | 0 / 95.6G | **空闲** |
| 2 | 0% | 0 / 95.6G | **空闲** |
| 3 | 0% | 0 / 95.6G | **空闲** |

### 4. 可安全清理的文件/目录

磁盘极度紧张（2.4G），Yi 训练完成后需要保存 checkpoint (~300-400MB)，勉强够用但没有余量。可清理项：

| 目录 | 大小 | 说明 |
|------|------|------|
| `Falcon3-7B-Base_d000_s42/lora_adapter/checkpoint-3125` | ~695M（4个 Falcon 共 2.8G） | 每个都有 `checkpoint-3125` 中间目录，如果已有最终 adapter 可删中间 checkpoint |
| `.hf_cache/Falcon3-7B-Base/` | 14G | 如果 Falcon3 训练全部完成且不再需要 eval，可清理 |
| `.hf_cache/Yi-1.5-9B/` | 17G | Yi 训练完成后可清理 |

**建议优先级**：
1. 确认 Falcon3 4 个 checkpoint 目录是否都只有中间 checkpoint（`checkpoint-3125`）而非最终 adapter。如果最终 adapter 已保存在外层，删中间 checkpoint 可回收 ~2.8G
2. Yi 训练完成后，清理 `.hf_cache/Falcon3-7B-Base/`（14G）是最大释放来源
3. Yi 训练本身的磁盘需求（~400MB）在当前 2.4G 余量内可以完成

---
