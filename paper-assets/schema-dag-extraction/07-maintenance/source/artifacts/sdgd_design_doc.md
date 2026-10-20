# SDGD Framework — Algorithm Design & Code Skeleton

## 1. Algorithm Flow

### Input
- `types: Dict[str, str]` — type name → description (e.g., `configs/few_nerd_types.json`, 66 entries)
- `embeddings: Tensor[N, D]` — type embeddings from Qwen3-32B mean-pool (N=66, D=5120), loaded from `artifacts/type_embeddings.pt`
- `τ: float` — confusability threshold (from Contribution A: θ* where degradation becomes significant)
- `model: LLM` — vLLM engine (Qwen3-32B-FP8)
- `samples: List[Dict]` — test samples with `text` field
- `confusion_matrix: Optional[Tensor[N, N]]` — empirical confusion counts from calibration (SDGD-cal only)

### Output
- `predictions: List[Dict]` — merged predictions across all batches, format: `[{"sample_id": int, "predictions": [{"text": str, "type": str}]}]`

### Pseudocode

```
function SDGD(types, embeddings, τ, model, samples, confusion_matrix=None):
    # Step 1: Pairwise confusability matrix
    if confusion_matrix is not None:                      # SDGD-cal
        C = normalize_confusion(confusion_matrix)         # symmetric, [0,1]
    else:                                                 # SDGD-zero
        C = cosine_similarity(embeddings, embeddings)     # [N, N]

    # Step 2: Thresholded adjacency graph
    A = (C > τ) & ~eye(N)                                # binary adjacency
    G = Graph(nodes=types.keys(), edges=A.nonzero())

    # Step 3: Greedy graph coloring → type batches
    coloring = greedy_color(G, strategy="largest_first")  # {type: color_id}
    batches = group_by_color(coloring)                    # {color_id: [type_names]}

    # Step 4: Per-batch extraction
    all_predictions = []
    for batch_id, batch_types in batches.items():
        prompts = [build_prompt(s["text"], types, batch_types) for s in samples]
        schema = build_json_schema(batch_types)
        outputs = model.generate(prompts, guided_decoding=schema)
        preds = parse_outputs(outputs, batch_id, batch_types)
        all_predictions.append(preds)

    # Step 5: Merge across batches
    merged = merge_predictions(all_predictions)
    return merged
```

## 2. Key Design Decisions

### 2.1 SDGD-zero vs SDGD-cal

| | SDGD-zero | SDGD-cal |
|---|---|---|
| Confusability source | Embedding cosine similarity | Empirical confusion matrix from k calibration examples |
| Data requirement | None (zero-shot) | 5-10 labeled examples per type |
| Quality | Proxy — embedding similarity ≈ semantic confusability | Ground truth — measures actual model confusion |
| Cost | Free (embeddings precomputed) | k × N_types extraction calls for calibration |
| When to use | No labeled data; rapid schema adaptation | Labeled data available; maximum accuracy |

**Calibration procedure (SDGD-cal)**:
```
function compute_empirical_confusion(types, model, calibration_samples):
    # Run single-pass extraction with ALL types on calibration set
    preds = extract(model, calibration_samples, all_types=types)
    
    # Build confusion matrix: C[i,j] = count of gold type-i predicted as type-j
    C = zeros(N, N)
    for sample in calibration_samples:
        for gold_entity in sample.entities:
            matched_pred = find_best_match(gold_entity, preds[sample.id])
            if matched_pred:
                i = type_index[gold_entity.type]
                j = type_index[matched_pred.type]
                C[i, j] += 1
    
    # Symmetrize and normalize
    C_sym = (C + C.T) / 2
    row_sums = C_sym.sum(dim=1, keepdim=True).clamp(min=1)
    return C_sym / row_sums
```

### 2.2 Threshold τ Selection

**Primary method: Adaptive threshold（数据集无关）**

`τ = mean(C_upper_tri) + k · std(C_upper_tri)`，k 是唯一超参数。

- 自适应于不同 schema 的 embedding 分布，避免循环性问题（不从目标数据集推导阈值）
- Few-NERD Qwen3 embeddings: mean=0.7837, std=0.0653 → k=1.0 时 τ ≈ 0.85
- 默认 k=1.0，通过 k sweep 消融确定最优值

**Oracle threshold baseline（上界对比用）**:
- 从 Few-NERD BCS-quality curve 推导的固定 τ∈[0.82, 0.88]
- 仅用于 Few-NERD 上的上界对比实验，**不可用于跨域验证**（exp-009 等）
- 论文中明确标注为 "oracle" 以区分

**跨域验证要求**:
- exp-009（ACE05/MAVEN）等跨域实验 **必须** 使用 adaptive threshold
- 不同数据集的 embedding 分布不同，固定 τ 无意义

**消融计划**: k sweep {0.5, 1.0, 1.5, 2.0}，在 adaptive framework 内做。报告每个 k 下的：τ 值、batch 数量、F1、vs single-pass Δ。

### 2.3 Graph Coloring Algorithm

**选择: Greedy (largest_first)**

理由：
- IE schema 图很小（Few-NERD 66 nodes, ACE05 58 nodes, 最大 MAVEN 168 nodes）
- Greedy coloring 时间复杂度 O(V²)，对 168 nodes 微秒级
- Optimal coloring 是 NP-hard，但 greedy 在稀疏图（τ 控制密度）上接近最优
- NetworkX `greedy_color` 直接可用，strategy="largest_first" 优先处理高度节点

**Batch 数量预估** (Few-NERD, τ=0.85):
- 同 coarse category 内 subtypes 基本都 > 0.85（如 person-* 8 个 subtypes 互相 BCS > 0.88）
- 预计 chromatic number ≈ 8-10（≈ max clique size in thresholded graph）
- 对比 single-pass (1 batch, 66 types) 和 per-type (66 batches)

### 2.4 Merge Strategy

**Primary: Simple union**（适用于 NER）
```
function merge_predictions(batch_predictions):
    merged = defaultdict(list)
    for batch_preds in batch_predictions:
        for pred in batch_preds:
            merged[pred.sample_id].extend(pred.predictions)
    return merged
```

NER batch 之间 type 集合不重叠（graph coloring 保证），所以不存在同一 span 被不同 batch 提取为不同 type 的冲突。唯一可能的重复：同一 span 被提取为同一 type（hallucination）。

**Conflict resolution（RE/EE 跨层时需要）**:
- 同一 (text, type) pair 出现在多个 batch → deduplicate
- 同一 span 不同 type → 保留 confidence 最高的（如果 model 提供 logprob）或保留全部（交给 evaluator）

当前 NER-only 阶段用 simple union 即可。

## 3. Module Structure

```
src/sdgd/
  __init__.py           # Public API: sdgd_extract()
  similarity.py         # Pairwise confusability computation
  graph.py              # Threshold graph construction + coloring
  decompose.py          # Main decomposition orchestrator
  merge.py              # Result merging across batches
  evaluate.py           # SDGD-specific evaluation & comparison
```

### 3.1 `similarity.py`

```python
"""Pairwise confusability matrix computation."""
import torch
import torch.nn.functional as F
from typing import Dict, Optional, Tuple, List

def load_type_embeddings(path: str) -> Tuple[torch.Tensor, List[str]]:
    """Load precomputed type embeddings.
    
    Returns:
        embeddings: [N, D] tensor (N=66, D=5120 for Qwen3)
        type_names: ordered list of type names matching embedding rows
    """
    ...

def cosine_similarity_matrix(embeddings: torch.Tensor) -> torch.Tensor:
    """Compute pairwise cosine similarity. Returns [N, N] matrix in [0, 1]."""
    normed = F.normalize(embeddings, dim=1)
    return normed @ normed.T

def normalize_confusion_matrix(C: torch.Tensor) -> torch.Tensor:
    """Symmetrize and normalize raw confusion counts to [0, 1].
    
    C[i,j] = count of gold type-i predicted as type-j.
    Output: symmetric matrix, diagonal zeroed, max-normalized.
    """
    ...

def compute_confusability(
    embeddings: torch.Tensor,
    confusion_matrix: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    """Unified confusability computation.
    
    SDGD-zero: uses embedding cosine similarity.
    SDGD-cal: uses normalized empirical confusion matrix.
    """
    if confusion_matrix is not None:
        return normalize_confusion_matrix(confusion_matrix)
    return cosine_similarity_matrix(embeddings)
```

### 3.2 `graph.py`

```python
"""Confusability graph construction and coloring."""
import networkx as nx
import torch
from typing import Dict, List, Tuple

def build_confusability_graph(
    conf_matrix: torch.Tensor,
    type_names: List[str],
    threshold: float,
) -> nx.Graph:
    """Build thresholded undirected graph.
    
    Edge (i, j) exists iff conf_matrix[i, j] > threshold and i != j.
    Edge weight = conf_matrix[i, j].
    """
    ...

def color_graph(
    G: nx.Graph,
    strategy: str = "largest_first",
) -> Dict[str, int]:
    """Greedy graph coloring. Returns {type_name: color_id}."""
    return nx.coloring.greedy_color(G, strategy=strategy)

def coloring_to_batches(coloring: Dict[str, int]) -> Dict[int, List[str]]:
    """Convert coloring assignment to batch groups. Returns {batch_id: [type_names]}."""
    batches = {}
    for type_name, color_id in coloring.items():
        batches.setdefault(color_id, []).append(type_name)
    return batches

def compute_batch_bcs(
    batches: Dict[int, List[str]],
    conf_matrix: torch.Tensor,
    type_names: List[str],
) -> Dict[int, float]:
    """Compute BCS (max pairwise confusability) for each batch."""
    ...

def graph_stats(G: nx.Graph, batches: Dict[int, List[str]]) -> Dict:
    """Summary stats: num_batches, avg_batch_size, max_bcs, edge_density."""
    ...
```

### 3.3 `decompose.py`

```python
"""Main SDGD decomposition orchestrator."""
from typing import Dict, List, Optional
from .similarity import load_type_embeddings, compute_confusability
from .graph import build_confusability_graph, color_graph, coloring_to_batches

class SDGDDecomposer:
    def __init__(
        self,
        type_definitions: Dict[str, str],
        embedding_path: str,
        threshold: float,
        confusion_matrix: Optional[torch.Tensor] = None,
    ):
        self.type_definitions = type_definitions
        self.embeddings, self.type_names = load_type_embeddings(embedding_path)
        self.threshold = threshold
        self.conf_matrix = compute_confusability(
            self.embeddings, confusion_matrix
        )
        self._build_batches()

    def _build_batches(self):
        """Construct confusability graph and compute coloring."""
        self.graph = build_confusability_graph(
            self.conf_matrix, self.type_names, self.threshold
        )
        coloring = color_graph(self.graph)
        self.batches = coloring_to_batches(coloring)

    @property
    def num_batches(self) -> int:
        return len(self.batches)

    def get_batch_types(self, batch_id: int) -> List[str]:
        return self.batches[batch_id]

    def get_batch_definitions(self, batch_id: int) -> Dict[str, str]:
        """Return {type_name: description} for a batch, ready for prompt construction."""
        return {t: self.type_definitions[t] for t in self.batches[batch_id]}
```

**Integration with existing `run_extraction.py`**:

```python
# In the extraction loop — replaces fixed batch composition
from sdgd.decompose import SDGDDecomposer

decomposer = SDGDDecomposer(
    type_definitions=load_json("configs/few_nerd_types.json"),
    embedding_path="artifacts/type_embeddings.pt",
    threshold=0.85,
)

all_predictions = []
for batch_id in range(decomposer.num_batches):
    batch_types = decomposer.get_batch_types(batch_id)
    batch_schema = build_json_schema(batch_types)       # existing function
    prompts = [build_prompt(s["text"], type_definitions, batch_types) 
               for s in samples]                         # existing function
    outputs = llm.generate(prompts, SamplingParams(
        max_tokens=1024, temperature=0.0,
        guided_decoding=GuidedDecodingParams(json=batch_schema),
    ))
    preds = parse_outputs(outputs, batch_id, batch_types) # existing function
    all_predictions.extend(preds)

merged = merge_predictions(all_predictions)               # new: sdgd.merge
```

### 3.4 `merge.py`

```python
"""Result merging across batches."""
from collections import defaultdict
from typing import Dict, List

def merge_predictions(
    batch_predictions: List[List[Dict]],
    strategy: str = "union",
) -> List[Dict]:
    """Merge predictions from multiple batches.
    
    Strategies:
      - "union": simple concatenation (NER, types don't overlap across batches)
      - "dedup": union + remove exact (text, type) duplicates per sample
    
    Input format per batch: [{"sample_id": int, "predictions": [{"text": str, "type": str}]}]
    Output: same format, one entry per sample_id with all predictions merged.
    """
    merged = defaultdict(list)
    for batch_preds in batch_predictions:
        for entry in batch_preds:
            merged[entry["sample_id"]].extend(entry["predictions"])

    if strategy == "dedup":
        for sid in merged:
            seen = set()
            deduped = []
            for p in merged[sid]:
                key = (p["text"], p["type"])
                if key not in seen:
                    seen.add(key)
                    deduped.append(p)
            merged[sid] = deduped

    return [{"sample_id": sid, "predictions": preds} 
            for sid, preds in sorted(merged.items())]
```

### 3.5 `evaluate.py`

```python
"""SDGD-specific evaluation and comparison."""
from typing import Dict, List, Tuple

def evaluate_sdgd(
    predictions: List[Dict],
    samples: List[Dict],
    batches: Dict[int, List[str]],
) -> Dict:
    """Evaluate SDGD extraction using text_match_eval.
    
    Returns:
      - overall: micro P/R/F1 across all types
      - per_batch: P/R/F1 per batch (with BCS annotation)
      - per_type: P/R/F1 per type
    """
    # Reuses text_match_eval from src/text_match_reeval.py
    ...

def compare_methods(
    results: Dict[str, Dict],
    method_names: List[str] = None,
) -> Dict:
    """Compare SDGD against baselines.
    
    Expected keys in results:
      - "single_pass": all 66 types in one batch
      - "per_type": 66 separate calls (UniNER-style)
      - "random_k": random batching, same k as SDGD
      - "sdgd_zero": SDGD with embedding similarity
      - "sdgd_cal": SDGD with empirical confusion matrix
    
    Returns: comparison table with F1, API calls, latency.
    """
    ...

def compute_api_cost(
    num_batches: int,
    num_samples: int,
    avg_prompt_tokens: int,
    avg_completion_tokens: int,
) -> Dict:
    """Estimate API cost / vLLM throughput for different methods."""
    ...
```

## 4. Interfaces with Existing Code

### 4.1 Prompt Construction (from `run_extraction.py`)

SDGD 不修改 prompt 构建逻辑，只控制传入的 `type_subset` 参数：

```python
# Existing interface — unchanged
build_prompt(input_text: str, type_definitions: Dict[str, str], type_subset: List[str]) -> str
build_json_schema(batch_types: List[str]) -> dict
```

SDGD 通过 `decomposer.get_batch_types(batch_id)` 提供 `type_subset`。

### 4.2 vLLM Inference (from `run_extraction.py`)

复用现有 vLLM 初始化和调用逻辑。SDGD 只是在外层循环 batch：

```python
# Existing: single batch, all types
outputs = llm.generate(prompts, sampling_params)

# SDGD: loop over batches, each with subset types + constrained schema
for batch_id in range(decomposer.num_batches):
    batch_schema = build_json_schema(decomposer.get_batch_types(batch_id))
    outputs = llm.generate(prompts, SamplingParams(..., guided_decoding=GuidedDecodingParams(json=batch_schema)))
```

关键：vLLM engine 只初始化一次，batch 间复用。每个 batch 的 JSON schema 不同（type enum 不同）。

### 4.3 Evaluation (from `text_match_reeval.py`)

```python
# Existing interface
text_match_eval(pred_entries, samples, batch_types) -> (prf_dict, per_type_dict)
```

SDGD evaluate 调用方式：
- **Per-batch evaluation**: 每个 SDGD batch 独立调用 `text_match_eval`，得到 per-batch metrics（可与 BCS 做相关分析）
- **Overall evaluation**: merge 后对全部 types 调用一次 `text_match_eval`，得到 SDGD 总体 F1

### 4.4 Type Embeddings

```
/root/schema-dag-extraction/artifacts/type_embeddings.pt
```
- Format: `{"embeddings": Tensor[66, 5120], "type_names": List[str]}`（需确认实际格式）
- Qwen3-32B mean-pooled last hidden states
- 已验证：BCS range 0.5309, mean=0.7837, std=0.0653

## 5. Baseline Methods for Comparison

| Method | Batches | Types/Batch | BCS Control | API Calls |
|--------|---------|-------------|-------------|-----------|
| Single-pass | 1 | 66 | None (max BCS) | N |
| Per-type (UniNER) | 66 | 1 | 0 (trivially) | 66N |
| Random-k | k (= SDGD's k) | ~66/k | Random | kN |
| SDGD-zero | k (from coloring) | Variable | ≤ τ | kN |
| SDGD-cal | k' (from coloring) | Variable | ≤ τ | k'N + calibration |

Random-k 是关键消融——与 SDGD 相同 batch 数量但随机分组。F1 差异直接量化 confusability-aware grouping 的价值。

## 6. Implementation Notes

1. **Graph coloring 确定性**: `nx.greedy_color` 受节点遍历顺序影响。固定 `type_names` 排序以保证可复现。

2. **Threshold sensitivity**: τ 轻微变化可能改变 batch 数量（图密度突变）。评估时报告 τ vs num_batches 曲线。

3. **vLLM batch 效率**: 每个 SDGD batch 对全部 1000 samples 做推理。总推理次数 = k × 1000。对比 per-type 的 66 × 1000 = 66k 次。SDGD 如果 k ≈ 10，则 10k 次，6.6x speedup over per-type。

4. **Prompt v2**: SDGD 必须使用 exp003a 的 prompt v2（text-only, anti-hallucination instruction），不要用 v1（含 char offset 要求）。

5. **Empty batch handling**: 某些 batch 可能只包含低频 type（测试集中无 gold entity）。仍需执行推理（可能提取到 entity），但评估时 gold=0 的 batch 不参与 F1 计算。

6. **Dependency on exp003a**: 实际代码编写等 exp003a 完成确认数据干净后再开始。当前 document 为设计阶段。
