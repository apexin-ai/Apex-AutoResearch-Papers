# code check dataset and logprob readiness

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_dataset_and_logprob_readiness_20260514T114258_result.json`
- **Structured JSON:** [`a0147697570787c2bc04.json`](../../sessions/a0/a0147697570787c2bc04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 就绪状态

- [ ] **run_mvp_pilot.py 多数据集支持: NO** — `--dataset` 参数存在但 `choices=["scierc", "ace05"]`，未包含 conll2003/wnut17。数据加载路由也只处理这两个数据集。
- [x] **CoNLL-2003 转换脚本: YES** — `convert_conll2003.py` 已存在于远程服务器，`data/conll2003/` 下有 train/dev/test.json + llmfactory_train.json
- [x] **WNUT-17 转换脚本: YES** — `convert_wnut17.py` 已存在于远程服务器，`data/wnut17/` 下有 train/dev/test.json + llmfactory_train.json
- [x] **logprob 推理脚本: YES (基本完成，但硬编码 SciERC)** — `extract_logprobs.py` 130 行，功能完整（N=8 stochastic + 1 greedy + logprob 提取），但模型路径、测试数据路径、schema hint 全部硬编码为 SciERC
- [x] **GPU 空闲: YES (3/4)** — GPU 0-2 空闲 (0%, 2MiB)；GPU 3 显示 100% util 但仅 2MiB 内存占用（可能是残留进程）
- [x] **底层支持已就绪** — `data_utils.py` 已有 `load_conll2003()` (L297) 和 `load_wnut17()` (L317)；`sampling.py` 已有 `CONLL2003_SCHEMA_HINT` (L242) 和 `WNUT17_SCHEMA_HINT` (L246)

## 需要的前置工作

1. **修改 `run_mvp_pilot.py`**（阻塞 exp-002/003）：
   - `choices` 列表加入 `"conll2003"`, `"wnut17"`
   - 数据加载分支加入 `load_conll2003` / `load_wnut17` 调用
   - schema hint 自动解析加入 `CONLL2003_SCHEMA_HINT` / `WNUT17_SCHEMA_HINT`
   - import 补上 `load_conll2003`, `load_wnut17`, `CONLL2003_SCHEMA_HINT`, `WNUT17_SCHEMA_HINT`

2. **参数化 `extract_logprobs.py`**（阻塞 logprob 实验）：
   - 当前 MODEL / TEST_DATA / SCHEMA_HINT 全部硬编码为 SciERC
   - 需要加 `--dataset` / `--model_path` 等 CLI 参数，或至少支持通过环境变量配置

3. **排查 GPU 3** — 100% util + 2MiB 内存不正常，建议 `kill` 残留进程后确认恢复空闲

---
