## CF Fallback Dry-Run 验证报告

**验证时间**: 2026-05-15
**服务器**: westd-16980
**项目根**: /root/schema_semantic_constrained_ie

### 代码验证
- [x] CF fallback 逻辑存在: **YES**
  - 文件: `compiler/type_mask_processor.py`
- [x] `_cf_fallback_count` 属性: **YES** (L205 初始化, L309/L352 递增, L423-426 logging+reset)
- [x] `_mask_head_type` else 分支 (registered type not in allowed_dr → force registered type): **YES** (L287 函数定义, L304 `if allowed_dr is None or actual_type in allowed_dr`, L306-311 else 分支带 W1 registry-consistent fallback 注释 + counter ++)
- [x] `_mask_tail_type` else 分支: **YES** (L321 函数定义, L349-354 同样的 W1 registry-consistent fallback 逻辑)
- [x] `reset()` fallback logging: **YES** (L419-427: 同时打印 grammar-first 和 CF fallback 计数，然后重置)

### 模型权重
- [x] Qwen3-8B config.json: **YES** (728 bytes)
  - ⚠️ **任务指定路径错误**: 任务命令中 `--model_path /root/autodl-tmp/models/Qwen/Qwen3-8B` **不存在**
  - **实际路径**: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
  - **可用符号链接**: `/root/autodl-tmp/models/Qwen3-8B-link` → 指向上述实际路径
- [x] Llama-3.1-8B-Instruct config.json: **YES** (855 bytes)
  - 路径正确: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct/config.json`

### 数据文件
- [x] scierc test data: **YES** (213898 bytes ≈ 209 KB)
  - ⚠️ **任务指定路径错误**: `data/scierc/test.json` **不存在**，`data/scierc/` 目录本身不存在
  - **实际路径**: `data/processed_data/test.json` (与 `run_phase2_scierc_batch.sh` 一致)
- [x] docred dev data: **YES** (4287303 bytes ≈ 4.1 MB)
  - 路径正确: `data/docred/dev.json`
- [x] scierc constraints: **YES** (29566 bytes ≈ 29 KB)
  - ⚠️ **任务指定路径错误**: `data/scierc/ontology_constraints_scierc.json` **不存在**
  - **实际路径**: `ontology_constraints.json` (项目根，与 `run_phase2_scierc_batch.sh` 一致)
- [x] docred constraints: **YES** (63528 bytes ≈ 62 KB)
  - 路径正确: `data/docred/ontology_constraints_docred.json`

### 输出路径
- [x] 无冲突: **YES**
  - `outputs/` 下不存在任何 `w1_cf_fallback_*.jsonl` 文件

### 脚本
- [x] `--help` 正常: **YES**
  - 支持 `--mode {unconstrained,grammar_only,semantic_only,full_s1,full_s2}`
  - 支持 `--dataset {scierc,docred}`
  - 接受 `--max_new_tokens`, `--device`, `--batch_size`, `--resume` 等参数

### 磁盘
- [x] 可用空间:
  - `/root` (overlay, 30GB): **22 GB 可用** (29% 已用)
  - `/root/autodl-tmp` (250GB, 数据盘): **193 GB 可用** (24% 已用)
  - 输出 jsonl 单次实验通常 < 100MB，空间充足

---

### 结论

**有问题（必须修正命令路径才能启动）**

CF fallback 代码完全就绪，所有模型权重和数据文件都存在，但**任务给出的 4 条命令中有路径错误**，原样执行会立即报 `FileNotFoundError`。需要在 GPU 释放前修正路径：

#### 必须替换的路径（共 3 处）

| 任务命令中的路径 | 实际正确路径 |
|---|---|
| `/root/autodl-tmp/models/Qwen/Qwen3-8B` | `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`（或符号链接 `/root/autodl-tmp/models/Qwen3-8B-link`） |
| `data/scierc/test.json` | `data/processed_data/test.json` |
| `data/scierc/ontology_constraints_scierc.json` | `ontology_constraints.json`（项目根） |

#### 受影响的实验

- **w1_cf_fallback_scierc_pilot**: model_path + data_path + constraints_path **三处都要改**
- **w1_cf_fallback_docred**: model_path **一处要改**（Qwen3-8B）
- **w1_cf_fallback_llama_scierc**: data_path + constraints_path **两处要改**（Llama 路径正确）
- **w1_cf_fallback_llama_docred**: **无需修改**，所有路径正确

#### 修正后的命令示例

```bash
# 1. w1_cf_fallback_scierc_pilot
python3 run_constrained_extraction.py --mode full_s1 --dataset scierc \
  --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/w1_cf_fallback_scierc_pilot.jsonl \
  --device cuda:0 --batch_size 1 --max_new_tokens 2048

# 2. w1_cf_fallback_docred
python3 run_constrained_extraction.py --mode full_s1 --dataset docred \
  --model_path /root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/w1_cf_fallback_docred.jsonl \
  --device cuda:0 --batch_size 1 --max_new_tokens 4096

# 3. w1_cf_fallback_llama_scierc
python3 run_constrained_extraction.py --mode full_s1 --dataset scierc \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_path data/processed_data/test.json \
  --constraints_path ontology_constraints.json \
  --output_path outputs/w1_cf_fallback_llama_scierc.jsonl \
  --device cuda:1 --batch_size 1 --max_new_tokens 4096

# 4. w1_cf_fallback_llama_docred (无需修改)
python3 run_constrained_extraction.py --mode full_s1 --dataset docred \
  --model_path /root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/w1_cf_fallback_llama_docred.jsonl \
  --device cuda:0 --batch_size 1 --max_new_tokens 4096
```

确认上述路径替换后，GPU 释放即可零延迟启动。
