# code d021 icl v6 prep

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d021_icl_v6_prep_20260512T194158_result.json`
- **Structured JSON:** [`d61a8ea888db3940bae2.json`](../../sessions/d6/d61a8ea888db3940bae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完成。下面是完整报告。

---

## v6 ICL 收集准备报告

### 1. collect_trajectories_icl.py 参数清单

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--model_name` | `Qwen/Qwen3-14B-AWQ` | HF 模型名或本地路径 |
| `--expert_file` | `data/alfworld_sft.json` | expert 轨迹（3119 条） |
| `--num_icl_examples` | `2` | 每个 task 的 few-shot 示例数 |
| `--output_dir` | `data/trajectories_icl` | 输出目录 |
| `--split` | `train` | train(3321)/dev(140)/test(134) |
| `--temperature` | `0.5` | 采样温度 |
| `--max_steps` | `40` | 单 episode 最大步数 |
| `--max_new_tokens` | `256` | 每次生成 token 上限 |
| `--gpu` | `0` | GPU 编号 |
| `--num_tasks` | `250` | 收集 task 数 |
| `--seed` | `0` | 随机种子（控制 ICL 示例抽样） |
| `--dry_run` | `false` | 只验证 I/O 不加载模型 |
| `--part_num` | `1` | 总分区数（并行用） |
| `--part_idx` | `-1` | 当前分区索引 |

### 2. ICL Few-Shot 策略

脚本已实现 **task-type-aware sampling**：
- `sample_icl_examples()` 优先从 **同 task type** 的 expert 中随机抽取
- 若同类型样本不足，从其他类型补充（优先选**短轨迹**节省 context）
- 每个 task 独立抽样，由 `--seed` 控制 `random.Random` 确定性

Expert 数据分布（3119 条，覆盖全部 6 类型）：

| Task Type | Expert 数 | 占比 |
|-----------|----------|------|
| pick_and_place | 759 | 24.3% |
| pick_two_obj | 662 | 21.2% |
| pick_clean_then_place | 576 | 18.5% |
| pick_cool_then_place | 472 | 15.1% |
| pick_heat_then_place | 371 | 11.9% |
| look_at_obj | 279 | 8.9% |

每个类型都有足够的 expert 样本供 ICL 抽样，无需额外配置文件。

### 3. v5 现状 + v6 收集目标

**v5 数据（已完成）：**
- 321 total, 118 success (36.8%), 202 true failure
- LLM 分类结果（88 条已分类）：planning=79, action=**5**, verification=4

**ICL 预测试（dev, 25 tasks, Qwen3-14B-AWQ）：**

| Task Type | 成功率 | 预期 |
|-----------|--------|------|
| pick_and_place | 100% (6/6) | 太简单，贡献不了失败 |
| look_at_obj | 80% (4/5) | 几乎都成功 |
| pick_two_obj | 0% (0/5) | 全部失败 → 错误样本源 |
| pick_clean_then_place | 0% (0/4) | 全部失败 → 错误样本源 |
| pick_heat_then_place | 0% (0/2) | 全部失败 → 错误样本源 |
| pick_cool_then_place | 0% (0/3) | 全部失败 → 错误样本源 |

**v6 收集目标：**
- 两卡并行，每卡 300 tasks，共 600 tasks
- 预期成功率 ~40%（ICL 提升），~360 failures
- 若 action error 占 ~6% failures → ~20 条 action error（满足 P1 gate 最低需求）
- ICL 应减少 step-1 diverge 比例，产生更多样化的错误模式

### 4. 推荐 v6 配置

- **seed**: `42`（与 v5 seed=0 区分）
- **num_icl_examples**: `2`（默认值，已测试有效）
- **num_tasks**: `300`（per GPU，总 600）
- **temperature**: `0.5`（维持默认）
- **输出路径**: `data/trajectories_v6_icl_cuda0` / `data/trajectories_v6_icl_cuda1`

### 5. 两卡并行启动命令（copy-paste ready）

#### 前置步骤：下载模型（必须先执行）

```bash
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# ModelScope 更快（AutoDL 国内 CDN）
pip install modelscope -q
python -c "
from modelscope import snapshot_download
snapshot_download('Qwen/Qwen3-14B-AWQ', cache_dir='/root/autodl-tmp/models/Qwen3-14B-AWQ')
"
```

#### GPU 0

```bash
cd /root/autodl-tmp/error_diag_dpo_recovery
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache

nohup python src/collect_trajectories_icl.py \
  --model_name /root/autodl-tmp/models/Qwen3-14B-AWQ \
  --gpu 0 \
  --num_tasks 300 \
  --seed 42 \
  --part_num 2 \
  --part_idx 0 \
  --output_dir data/trajectories_v6_icl_cuda0 \
  > /tmp/v6_icl_cuda0.log 2>&1 &
echo "GPU0 PID: $!"
```

#### GPU 1

```bash
cd /root/autodl-tmp/error_diag_dpo_recovery
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache

nohup python src/collect_trajectories_icl.py \
  --model_name /root/autodl-tmp/models/Qwen3-14B-AWQ \
  --gpu 1 \
  --num_tasks 300 \
  --seed 42 \
  --part_num 2 \
  --part_idx 1 \
  --output_dir data/trajectories_v6_icl_cuda1 \
  > /tmp/v6_icl_cuda1.log 2>&1 &
echo "GPU1 PID: $!"
```

#### 监控命令

```bash
# 进度
tail -5 /tmp/v6_icl_cuda0.log
tail -5 /tmp/v6_icl_cuda1.log

# 已收集数量
wc -l data/trajectories_v6_icl_cuda0/train.jsonl data/trajectories_v6_icl_cuda1/train.jsonl

# GPU 占用
nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader
```

### 6. 风险和注意事项

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| **Qwen3-14B-AWQ 不在服务器上** | 阻塞启动 | 需先下载 ~9GB（ModelScope 推荐） |
| 两卡各加载一份 14B-AWQ（~10GB/卡） | 24GB 4090D 可容纳，但 context 长的 ICL prompt 会额外占 VRAM | 默认 max_steps=40 + 2 ICL examples，实测 ICL test 已跑通 |
| action error 占比可能仍低 | 600 tasks ~360 failures 中预期 ~20 action | 若不够，可追加 seed=43 再跑一轮 |
| ALFWorld env 单进程限制 | 两个进程各自独立初始化 env，通过 part_num/part_idx 分区，互不冲突 | 已有机制 |
| v5 数据不被覆盖 | output_dir 独立 (`v6_icl_cuda0/1`) | 已确认路径不冲突 |
| 预估运行时间 | ICL test 25 tasks 约 30min → 300 tasks ≈ 6h per GPU | nohup 后台执行 |

---
