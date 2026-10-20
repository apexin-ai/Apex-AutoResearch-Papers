#!/usr/bin/env python3
"""KV eviction benchmark (kv-bench-001): perplexity under KV budget constraints.
Compares CARC-KV (O(1), ours), H2O (O(n)), StreamingLLM (O(1)) + full-cache baseline.
Model: DeepSeek-R1-Distill-Qwen-7B (GQA: 28Q/4KV heads, 28 layers).
"""

import json, math, os, sys, time, logging
import torch
import torch.nn.functional as F

torch.set_grad_enabled(False)

MODEL_PATH = "/root/autodl-tmp/models/deepseek-r1-distill-qwen-7b/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
DEVICE = "cuda:0"
BUDGETS = [0.3, 0.5, 0.7]
MAX_EVAL_TOKENS = 512
OUTPUT_DIR = "/home/sonny/redundancy-compound-sparsity/results/kv_eviction"

CARC_GAMMA = 0.99
H2O_RECENT_WINDOW = 32
STREAMING_NUM_SINKS = 4

os.makedirs(OUTPUT_DIR, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(OUTPUT_DIR, "kv_bench_001.log")),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("kv-bench")

# ==================== Eval Texts (Wikipedia excerpts) ====================

EVAL_TEXTS = [
    "The Turing machine, described by Alan Turing in 1936, is a mathematical model of computation that defines an abstract machine which manipulates symbols on a strip of tape according to a table of rules. Despite its simplicity, the Turing machine can be adapted to simulate the logic of any computer algorithm, and is particularly useful in explaining the functions of a CPU inside a computer. The machine operates on an infinite memory tape divided into discrete cells, each of which can hold a single symbol drawn from a finite alphabet. The machine has a head that can read and write symbols and move the tape left and right one cell at a time. The operation of the machine is fully determined by a finite set of elementary instructions, given as a table of states. Each instruction specifies, given the current state of the machine and the symbol it is reading, what symbol to write, how to move the head, and what state to transition to. Turing machines are equivalent to algorithms, and represent the foundation of modern computer science. Church and Turing independently proved that there is no general method or procedure to determine whether a given statement of first-order logic is universally valid, establishing fundamental limits on what can be computed.",

    "Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy that, through cellular respiration, can later be released to fuel the organism's activities. Some of this chemical energy is stored in carbohydrate molecules, such as sugars and starches, which are synthesized from carbon dioxide and water. In most cases, oxygen is released as a waste product. Most plants, algae, and cyanobacteria perform photosynthesis. Such organisms are called photoautotrophs. The process of photosynthesis is largely responsible for producing and maintaining the oxygen content of the Earth's atmosphere, and supplies most of the biological energy necessary for complex life on Earth. In plants, photosynthesis takes place primarily in leaves, more specifically in the cells of the mesophyll. The amount of light absorbed in the leaf depends on the concentration of chlorophyll and the thickness of the leaf. Although photosynthesis is performed differently by different species, the process always begins when energy from light is absorbed by proteins called reaction centres that contain green chlorophyll and other coloured pigments or chromophores.",

    "The French Revolution was a period of radical political and societal change in France that began with the Estates General of 1789 and ended with the formation of the French Consulate in November 1799. Many of its ideas are considered fundamental principles of liberal democracy, while phrases like liberty, equality, fraternity reappeared in other revolts, such as the 1917 Russian Revolution, and inspired campaigns for the abolition of slavery and universal suffrage. The values and institutions of the Revolution dominate French politics to this day. The Revolution resulted in the suppression of the feudal system, emancipation of the individual, a greater division of landed property, abolition of the privileges of noble birth, and nominal establishment of equality among men. The French Revolution differed from other revolutions in being not merely national, for it aimed at benefiting all humanity. Historians widely regard the Revolution as one of the most important events in human history, and the end of the Early Modern period.",

    "Quantum entanglement is a phenomenon in quantum physics where two particles become interconnected and the quantum state of each particle cannot be described independently of the state of the other, even when separated by a large distance. The topic of quantum entanglement is at the heart of the disparity between classical physics and quantum physics. Entanglement was first described by Erwin Schrodinger in response to a paper by Albert Einstein, Boris Podolsky, and Nathan Rosen, who had proposed the EPR paradox. Einstein memorably dismissed entanglement as spooky action at a distance. Experiments have shown that entangled particles can influence each other instantaneously regardless of distance. Bell test experiments have demonstrated that quantum mechanics violates the inequalities established by Bell's theorem, ruling out local hidden variable theories. Quantum entanglement has practical applications in quantum computing, quantum cryptography, and quantum teleportation. In quantum computing, entanglement is a key resource that enables exponential speedups for certain computational problems.",

    "The human genome is the complete set of nucleic acid sequences for humans, encoded as DNA within the 23 chromosome pairs in cell nuclei and in a small DNA molecule found within individual mitochondria. Human genomes include both protein-coding DNA sequences and various types of DNA that do not encode proteins. The latter is a diverse category that includes DNA coding for non-translated RNA, such as ribosomal RNA, transfer RNA, ribozymes, small nuclear RNAs, and several types of regulatory RNAs. It also includes promoters and their associated gene-regulatory elements, DNA playing structural and replicatory roles, such as scaffolding regions, telomeres, centromeres, and origins of replication, plus large numbers of transposable elements, inserted viral DNA, non-functional pseudogenes, and simple highly repetitive sequences. Introns make up a large percentage of non-coding DNA. The total length of the human reference genome does not represent the sequence of any specific individual genome.",

    "Machine learning is a subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves. The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers to learn automatically without human intervention or assistance and adjust actions accordingly. Classical machine learning is often categorized as supervised learning, unsupervised learning, semi-supervised learning, and reinforcement learning. Supervised learning algorithms build a mathematical model of a set of data that contains both the inputs and the desired outputs. Unsupervised learning algorithms take a set of data that contains only inputs, and find structure in the data, like grouping or clustering of data points.",

    "The theory of plate tectonics states that the outer rigid layer of the Earth, the lithosphere, is divided into a number of large and small tectonic plates that move relative to each other. This theory was developed during the first few decades of the twentieth century from the earlier hypothesis of continental drift proposed by Alfred Wegener. The scientific community initially dismissed Wegener's theory, partly because he could not explain the mechanism driving continental movement. The discovery of seafloor spreading in the 1960s provided the mechanism. Tectonic plates are composed of the oceanic lithosphere and the thicker continental lithosphere, each topped by its own kind of crust. Along convergent plate boundaries, the process of subduction carries the edge of one plate down under the other plate and into the mantle. This process reduces the total surface area of the crust. The production of new seafloor and destruction of old oceanic lithosphere occurs roughly at equal rates.",

    "General relativity, also known as the general theory of relativity, is the geometric theory of gravitation published by Albert Einstein in 1915. It is the current description of gravitation in modern physics. General relativity generalizes special relativity and refines Newton's law of universal gravitation, providing a unified description of gravity as a geometric property of space and time, or four-dimensional spacetime. In particular, the curvature of spacetime is directly related to the energy and momentum of whatever matter and radiation are present. The relation is specified by the Einstein field equations, a system of second-order partial differential equations. Newton's law of universal gravitation, which describes gravity as a force causing any two bodies to be attracted toward each other, is a useful approximation but does not accurately describe gravity in all situations. General relativity has been confirmed by all observations and experiments to date.",

    "The Amazon rainforest, alternatively called the Amazon jungle, is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America. This basin encompasses an area of approximately seven million square kilometers, of which five and a half million square kilometers are covered by the rainforest. This region includes territory belonging to nine nations and three thousand four hundred formally acknowledged indigenous territories. The majority of the forest is contained within Brazil, with significant portions in Peru, Colombia, Venezuela, Ecuador, Bolivia, Guyana, Suriname, and French Guiana. The Amazon represents over half of the planet's remaining rainforests and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated three hundred and ninety billion individual trees divided into sixteen thousand species.",

    "The development of antibiotics in the twentieth century was one of the most significant advances in the history of medicine. Alexander Fleming's discovery of penicillin in 1928 opened the door to a new era of treating bacterial infections that had previously been lethal. Before antibiotics, even minor infections could be fatal, and surgical procedures carried a high risk of post-operative infection. The mass production of penicillin during World War II saved countless lives and transformed military medicine. Since then, numerous classes of antibiotics have been developed, including tetracyclines, aminoglycosides, macrolides, and fluoroquinolones. However, the widespread and often inappropriate use of antibiotics has led to the emergence of antibiotic-resistant bacteria, posing a serious global health threat. The World Health Organization has declared antimicrobial resistance one of the top ten global public health threats facing humanity.",
]


# ==================== Eviction Policies ====================

class NoEvictionPolicy:
    """Baseline: full cache, no eviction."""
    name = "FullCache"
    complexity = "N/A"
    needs_attn = False
    budget = 999999

    def reset(self):
        pass

    def maybe_evict(self, cache, attentions=None):
        return 0


class CARCKVPolicy:
    """CARC-KV: EMA anchor cosine similarity, O(1) per token.
    Evicts the most redundant token (highest sim to anchor).
    Uses layer 0 keys for anchor computation; same indices for all layers.
    """
    name = "CARC-KV"
    complexity = "O(1)"
    needs_attn = False

    def __init__(self, budget, gamma=0.99):
        self.budget = budget
        self.gamma = gamma
        self._anchor = None
        self._scores = []

    def reset(self):
        self._anchor = None
        self._scores = []

    def maybe_evict(self, cache, attentions=None):
        cache_len = cache.layers[0].keys.shape[2]
        device = cache.layers[0].keys.device

        k_new = cache.layers[0].keys[0, :, -1, :].float()

        if self._anchor is None:
            self._anchor = k_new.clone()
            self._scores = [0.0] * cache_len
            return 0

        sim = F.cosine_similarity(k_new, self._anchor, dim=-1).mean().item()
        self._anchor = self.gamma * self._anchor + (1 - self.gamma) * k_new

        while len(self._scores) < cache_len:
            self._scores.append(sim)

        if cache_len <= self.budget:
            return 0

        n_evict = 0
        while len(self._scores) > self.budget:
            cl = len(self._scores)
            recent_protect = min(4, self.budget // 4)
            evictable_end = cl - recent_protect

            if evictable_end <= 1:
                keep = list(range(cl - self.budget, cl))
                self._scores = [self._scores[i] for i in keep]
                keep_t = torch.tensor(keep, dtype=torch.long, device=device)
                _reindex_cache(cache, keep_t)
                n_evict += cl - self.budget
                break

            scores_t = torch.tensor(self._scores[1:evictable_end], device=device)
            evict_pos = scores_t.argmax().item() + 1

            self._scores.pop(evict_pos)
            keep_mask = torch.ones(cl, dtype=torch.bool, device=device)
            keep_mask[evict_pos] = False
            keep_t = keep_mask.nonzero(as_tuple=False).squeeze(-1)
            _reindex_cache(cache, keep_t)
            n_evict += 1

        return n_evict


class H2OPolicy:
    """H2O: Heavy-Hitter Oracle, O(n) per token.
    Accumulates attention scores; keeps heavy hitters + recent window.
    """
    name = "H2O"
    complexity = "O(n)"
    needs_attn = True

    def __init__(self, budget, recent_window=32):
        self.budget = budget
        self.recent_window = recent_window
        self._cum_attn = None

    def reset(self):
        self._cum_attn = None

    def maybe_evict(self, cache, attentions=None):
        cache_len = cache.layers[0].keys.shape[2]
        device = cache.layers[0].keys.device

        if attentions is not None:
            attn_sum = torch.zeros(cache_len, device=device)
            for layer_attn in attentions:
                attn_sum += layer_attn[0].float().mean(dim=0).squeeze(0)[:cache_len]
            attn_sum /= len(attentions)
        else:
            attn_sum = torch.ones(cache_len, device=device) / cache_len

        if self._cum_attn is None:
            self._cum_attn = attn_sum
        else:
            if attn_sum.shape[0] > self._cum_attn.shape[0]:
                self._cum_attn = F.pad(
                    self._cum_attn, (0, attn_sum.shape[0] - self._cum_attn.shape[0])
                )
            self._cum_attn = self._cum_attn + attn_sum

        if cache_len <= self.budget:
            return 0

        cum = self._cum_attn[:cache_len]
        protect_start = max(0, cache_len - self.recent_window)
        heavy_budget = self.budget - (cache_len - protect_start)

        if heavy_budget <= 0:
            keep = torch.arange(cache_len - self.budget, cache_len, device=device)
        else:
            candidates = cum[:protect_start]
            if candidates.numel() > 0:
                topk = candidates.topk(min(heavy_budget, candidates.numel())).indices
            else:
                topk = torch.tensor([], dtype=torch.long, device=device)
            recent = torch.arange(protect_start, cache_len, device=device)
            keep = torch.cat([topk, recent]).sort().values

        n_evict = cache_len - keep.shape[0]
        self._cum_attn = cum[keep]
        _reindex_cache(cache, keep)
        return n_evict


class StreamingLLMPolicy:
    """StreamingLLM: sink tokens + sliding window, O(1) per token."""
    name = "StreamingLLM"
    complexity = "O(1)"
    needs_attn = False

    def __init__(self, budget, num_sinks=4):
        self.budget = budget
        self.num_sinks = num_sinks
        self.window_size = budget - num_sinks
        assert self.window_size > 0, f"Budget {budget} too small for {num_sinks} sinks"

    def reset(self):
        pass

    def maybe_evict(self, cache, attentions=None):
        cache_len = cache.layers[0].keys.shape[2]
        if cache_len <= self.budget:
            return 0

        device = cache.layers[0].keys.device
        sink = torch.arange(self.num_sinks, device=device)
        recent_start = cache_len - self.window_size
        recent = torch.arange(recent_start, cache_len, device=device)
        keep = torch.cat([sink, recent])

        n_evict = cache_len - keep.shape[0]
        _reindex_cache(cache, keep)
        return n_evict


def _reindex_cache(cache, keep_indices):
    """Apply the same keep_indices to all layers of a DynamicCache."""
    for i in range(len(cache.layers)):
        cache.layers[i].keys = cache.layers[i].keys[:, :, keep_indices, :]
        cache.layers[i].values = cache.layers[i].values[:, :, keep_indices, :]


# ==================== Perplexity Evaluation ====================

def compute_ppl(model, tokenizer, texts, policy, max_tokens):
    """Token-by-token perplexity with KV eviction after each step."""
    total_nll = 0.0
    total_tokens = 0
    total_evictions = 0

    for text_idx, text in enumerate(texts):
        ids = tokenizer.encode(text, add_special_tokens=False)
        if len(ids) > max_tokens:
            ids = ids[:max_tokens]
        if len(ids) < 10:
            continue
        ids_t = torch.tensor([ids], device=DEVICE)
        seq_len = ids_t.shape[1]

        policy.reset()
        cache = None

        for t in range(seq_len - 1):
            token = ids_t[:, t : t + 1]
            position_ids = torch.tensor([[t]], device=DEVICE)

            kwargs = dict(
                input_ids=token,
                position_ids=position_ids,
                use_cache=True,
            )
            if cache is not None:
                kwargs["past_key_values"] = cache
            if policy.needs_attn:
                kwargs["output_attentions"] = True

            out = model(**kwargs)
            cache = out.past_key_values
            attentions = out.attentions if policy.needs_attn else None

            logits = out.logits[0, -1]
            target = ids_t[0, t + 1]
            nll = F.cross_entropy(logits.unsqueeze(0), target.unsqueeze(0))
            total_nll += nll.item()
            total_tokens += 1

            n = policy.maybe_evict(cache, attentions)
            total_evictions += n

        if (text_idx + 1) % 3 == 0 or text_idx == len(texts) - 1:
            log.info(
                f"  [{text_idx+1}/{len(texts)}] tokens={total_tokens}, "
                f"PPL={math.exp(total_nll/total_tokens):.2f}, evictions={total_evictions}"
            )

    ppl = math.exp(total_nll / total_tokens) if total_tokens > 0 else float("inf")
    return {
        "ppl": round(ppl, 4),
        "num_tokens": total_tokens,
        "total_evictions": total_evictions,
    }


# ==================== Main ====================

def main():
    t_start = time.time()
    log.info("=" * 60)
    log.info("KV Eviction Benchmark (kv-bench-001)")
    log.info("=" * 60)

    log.info(f"Loading model: {MODEL_PATH}")
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        dtype=torch.bfloat16,
        device_map=DEVICE,
        trust_remote_code=True,
        attn_implementation="eager",
    )
    model.eval()

    cfg = model.config
    num_layers = cfg.num_hidden_layers
    num_kv_heads = cfg.num_key_value_heads
    num_q_heads = cfg.num_attention_heads
    head_dim = cfg.hidden_size // num_q_heads

    log.info(
        f"Model: {num_layers}L, {num_q_heads}Q/{num_kv_heads}KV heads, "
        f"dim={head_dim}, GPU mem={torch.cuda.max_memory_allocated()/1e9:.1f}GB"
    )

    all_results = []

    # --- Baseline ---
    log.info("\n--- FullCache (baseline) ---")
    policy = NoEvictionPolicy()
    t0 = time.time()
    baseline = compute_ppl(model, tokenizer, EVAL_TEXTS, policy, MAX_EVAL_TOKENS)
    wall = time.time() - t0
    baseline_ppl = baseline["ppl"]
    all_results.append(
        {"policy": "FullCache", "budget_ratio": 1.0, "complexity": "N/A",
         **baseline, "ppl_ratio": 1.0, "wall_seconds": round(wall, 1)}
    )
    log.info(f"FullCache PPL={baseline_ppl:.2f} ({wall:.0f}s)")
    torch.cuda.empty_cache()

    # --- Constrained ---
    for budget_ratio in BUDGETS:
        budget = int(MAX_EVAL_TOKENS * budget_ratio)
        log.info(f"\n{'='*50} Budget {budget_ratio:.0%} ({budget} tok) {'='*50}")

        policies = [
            CARCKVPolicy(budget, gamma=CARC_GAMMA),
            H2OPolicy(budget, recent_window=H2O_RECENT_WINDOW),
            StreamingLLMPolicy(budget, num_sinks=STREAMING_NUM_SINKS),
        ]

        for policy in policies:
            log.info(f"\n--- {policy.name} ({policy.complexity}) ---")
            t0 = time.time()
            result = compute_ppl(model, tokenizer, EVAL_TEXTS, policy, MAX_EVAL_TOKENS)
            wall = time.time() - t0

            entry = {
                "policy": policy.name,
                "budget_ratio": budget_ratio,
                "budget_tokens": budget,
                "complexity": policy.complexity,
                **result,
                "ppl_ratio": round(result["ppl"] / baseline_ppl, 4) if baseline_ppl else None,
                "wall_seconds": round(wall, 1),
            }
            all_results.append(entry)
            log.info(
                f"{policy.name}: PPL={result['ppl']:.2f} "
                f"(ratio={entry['ppl_ratio']:.3f}), {wall:.0f}s"
            )
            torch.cuda.empty_cache()

    elapsed = time.time() - t_start

    output = {
        "experiment": "kv-bench-001",
        "model": MODEL_PATH,
        "max_eval_tokens": MAX_EVAL_TOKENS,
        "num_texts": len(EVAL_TEXTS),
        "budgets": BUDGETS,
        "elapsed_seconds": round(elapsed, 1),
        "config": {
            "carc_gamma": CARC_GAMMA,
            "h2o_recent_window": H2O_RECENT_WINDOW,
            "streaming_num_sinks": STREAMING_NUM_SINKS,
            "attn_implementation": "eager",
            "num_layers": num_layers,
            "num_kv_heads": num_kv_heads,
            "num_q_heads": num_q_heads,
            "head_dim": head_dim,
        },
        "results": all_results,
    }

    result_path = os.path.join(OUTPUT_DIR, "kv_bench_001_results.json")
    with open(result_path, "w") as f:
        json.dump(output, f, indent=2)
    log.info(f"\nResults -> {result_path}")

    log.info(f"\n{'Policy':<15} {'Budget':>7} {'PPL':>10} {'Ratio':>7} {'Evict':>8} {'Time':>7}")
    log.info("-" * 58)
    for r in all_results:
        log.info(
            f"{r['policy']:<15} {r['budget_ratio']:>6.0%} "
            f"{r['ppl']:>10.2f} {r.get('ppl_ratio',1.0):>7.3f} "
            f"{r['total_evictions']:>8} {r['wall_seconds']:>6.0f}s"
        )
    log.info(f"\nTotal elapsed: {elapsed:.0f}s")


if __name__ == "__main__":
    main()
