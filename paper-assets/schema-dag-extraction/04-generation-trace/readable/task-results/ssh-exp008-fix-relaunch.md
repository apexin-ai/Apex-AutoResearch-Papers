# ssh exp008 fix relaunch

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp008-fix-relaunch_20260515T100611_result.json`
- **Structured JSON:** [`0b614f1ed56f0263d4b5.json`](../../sessions/0b/0b614f1ed56f0263d4b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**修复内容**：vLLM EngineCore fork 死锁（PyTorch/NetworkX 在 fork 前已加载）

**方案**：两阶段分离
- `src/sdgd_decompose_cpu.py` — CPU 阶段：4 种 mode 的 graph decomposition，输出 JSON
- `src/sdgd_extract_gpu.py` — GPU 阶段：**vLLM 第一个初始化**，然后加载其他模块，处理所有 mode（一次模型加载）
- `src/run_sdgd_full.sh` — 编排脚本：先跑全部 CPU decomposition，再启动一次 GPU session

**验证**：
- Dry-run (5 samples, sdgd_zero 8 batches) 通过，EngineCore 正常 fork，F1=0.3077
- 旧进程 PID 241208 + 残留 EngineCore 241610 已 kill，GPU 已释放

**全量 exp-008 已启动**：
- PID 254599，log: `artifacts/exp008_run2.log`
- 4 modes (sdgd_zero → single_pass → random_batch → per_type)，1000 samples，Qwen3-32B-FP8
- vLLM 加载 60s，Batch 1/8 extraction 进行中
- 预计总耗时：sdgd_zero ~15min, single_pass ~3min, random_batch ~15min, per_type ~60min → 共约 1.5-2h

---
