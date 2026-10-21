"""Ontology scalability benchmark: compilation time + inference overhead across ontology scales.

Part 1 (CPU): Compile benchmark for 4 ontology scales (SciERC, DocRED, Large-100, XLarge-200)
Part 2 (GPU): Inference overhead benchmark with Qwen3-8B (constrained vs unconstrained)
"""

import json
import os
import sys
import time
import random
import traceback
from pathlib import Path

os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

import peft.import_utils as _piu
_piu.is_gptqmodel_available = lambda: False

PROJECT_ROOT = Path("/root/schema_semantic_constrained_ie")
sys.path.insert(0, str(PROJECT_ROOT))

MODEL_PATH = "/root/autodl-tmp/models/Qwen3-8B-link"
SYNTHETIC_DIR = PROJECT_ROOT / "data" / "synthetic"
SCIERC_ONTOLOGY = PROJECT_ROOT / "ontology_constraints.json"
DOCRED_ONTOLOGY = PROJECT_ROOT / "data" / "docred" / "ontology_constraints_docred.json"

SCALES = {
    "small_scierc": {"source": "real", "path": SCIERC_ONTOLOGY},
    "medium_docred": {"source": "real", "path": DOCRED_ONTOLOGY},
    "large_100": {"source": "synthetic", "n_entity": 100, "n_relation": 500},
    "xlarge_200": {"source": "synthetic", "n_entity": 200, "n_relation": 1000},
}

COMPILE_REPEATS = 5
INFERENCE_DOCS = 10


def generate_synthetic_ontology(n_entity: int, n_relation: int, seed: int = 42) -> dict:
    rng = random.Random(seed)
    entity_types = [f"Type_{i:03d}" for i in range(1, n_entity + 1)]
    relation_types = [f"rel_{i:03d}" for i in range(1, n_relation + 1)]

    relation_constraints = {}
    for rtype in relation_types:
        n_head = rng.randint(2, 5)
        n_tail = rng.randint(2, 5)
        heads = rng.sample(entity_types, min(n_head, len(entity_types)))
        tails = rng.sample(entity_types, min(n_tail, len(entity_types)))
        pairs = []
        for h in heads:
            for t in tails:
                pairs.append([h, t])
        relation_constraints[rtype] = {
            "valid_pairs": pairs,
            "stats": {"total": len(pairs), "pair_distribution": {}}
        }

    return {
        "entity_types": entity_types,
        "relation_types": relation_types,
        "relation_constraints": relation_constraints,
    }


def save_synthetic_ontologies():
    SYNTHETIC_DIR.mkdir(parents=True, exist_ok=True)
    for scale_name, cfg in SCALES.items():
        if cfg["source"] != "synthetic":
            continue
        ontology = generate_synthetic_ontology(cfg["n_entity"], cfg["n_relation"])
        out_path = SYNTHETIC_DIR / f"ontology_{scale_name}.json"
        with open(out_path, "w") as f:
            json.dump(ontology, f, indent=2)
        print(f"  Saved {out_path} ({len(ontology['entity_types'])} entities, {len(ontology['relation_types'])} relations)")


def get_ontology_path(scale_name: str) -> Path:
    cfg = SCALES[scale_name]
    if cfg["source"] == "real":
        return Path(cfg["path"])
    return SYNTHETIC_DIR / f"ontology_{scale_name}.json"


def count_ontology_stats(path: Path) -> dict:
    with open(path) as f:
        data = json.load(f)
    n_entity = len(data["entity_types"])
    rtypes = data.get("relation_types", [])
    if isinstance(rtypes, dict):
        n_relation = len(rtypes)
    else:
        n_relation = len(rtypes)
    n_constraints = sum(
        len(rc["valid_pairs"])
        for rc in data.get("relation_constraints", {}).values()
    )
    return {"n_entity": n_entity, "n_relation": n_relation, "n_constraint_pairs": n_constraints}


# ─── Part 1: Compile Benchmark ───────────────────────────────────────────────

def run_compile_benchmark(tokenizer):
    from compiler.ontology_compiler import OntologyCompiler

    results = {}
    for scale_name in SCALES:
        path = get_ontology_path(scale_name)
        stats = count_ontology_stats(path)
        print(f"\n  [{scale_name}] {stats['n_entity']} entities, {stats['n_relation']} relations, {stats['n_constraint_pairs']} constraint pairs")

        grammar_times = []
        semantic_times = []
        total_times = []
        prefix_map_sizes = []

        for trial in range(COMPILE_REPEATS):
            t0 = time.perf_counter()
            compiler = OntologyCompiler(path)

            t1 = time.perf_counter()
            compiler.compile_type_constraints(tokenizer)
            t2 = time.perf_counter()
            semantic_time = t2 - t1

            compiled_grammar = compiler.compile_xgrammar(tokenizer)
            t3 = time.perf_counter()
            grammar_time = t3 - t2

            total_time = t3 - t0

            n_prefix_entries = len(compiler.spec.entity_type_first_token) + len(compiler.spec.relation_type_token_ids)
            prefix_map_size_bytes = sys.getsizeof(compiler.spec.entity_type_first_token) + sys.getsizeof(compiler.spec.relation_type_token_ids)
            for v in compiler.spec.entity_type_token_ids.values():
                prefix_map_size_bytes += sys.getsizeof(v)
            for v in compiler.spec.relation_type_token_ids.values():
                prefix_map_size_bytes += sys.getsizeof(v)

            grammar_times.append(grammar_time)
            semantic_times.append(semantic_time)
            total_times.append(total_time)
            prefix_map_sizes.append(n_prefix_entries)

        results[scale_name] = {
            **stats,
            "grammar_compile_s": sum(grammar_times) / len(grammar_times),
            "semantic_compile_s": sum(semantic_times) / len(semantic_times),
            "total_compile_s": sum(total_times) / len(total_times),
            "grammar_compile_std": (sum((x - sum(grammar_times)/len(grammar_times))**2 for x in grammar_times) / len(grammar_times)) ** 0.5,
            "semantic_compile_std": (sum((x - sum(semantic_times)/len(semantic_times))**2 for x in semantic_times) / len(semantic_times)) ** 0.5,
            "total_compile_std": (sum((x - sum(total_times)/len(total_times))**2 for x in total_times) / len(total_times)) ** 0.5,
            "prefix_map_entries": prefix_map_sizes[0],
        }
        r = results[scale_name]
        print(f"    Grammar:  {r['grammar_compile_s']:.4f}s +/- {r['grammar_compile_std']:.4f}")
        print(f"    Semantic: {r['semantic_compile_s']:.4f}s +/- {r['semantic_compile_std']:.4f}")
        print(f"    Total:    {r['total_compile_s']:.4f}s +/- {r['total_compile_std']:.4f}")
        print(f"    Prefix map entries: {r['prefix_map_entries']}")

    return results


# ─── Part 2: Inference Overhead Benchmark ─────────────────────────────────────

DUMMY_DOCS = [
    "The neural network model was trained on the ImageNet dataset using stochastic gradient descent. Transfer learning improved accuracy significantly.",
    "Researchers at MIT developed a novel algorithm for protein folding prediction. The method uses graph neural networks to capture structural patterns.",
    "Climate change has accelerated glacier retreat in the Antarctic region. Scientists measured a 15% decrease in ice coverage over the past decade.",
    "The quantum computing chip demonstrated error correction capabilities at scale. IBM reported a breakthrough in qubit stability and coherence time.",
    "Natural language processing models have shown remarkable performance on text classification tasks. BERT and GPT-based architectures dominate the benchmarks.",
    "The pharmaceutical company announced positive Phase III trial results for the cancer drug. Overall survival rates improved by 23% compared to placebo.",
    "Machine learning algorithms detected anomalous patterns in financial transactions. The fraud detection system processed over one million transactions per second.",
    "Astronomers discovered a new exoplanet orbiting a red dwarf star. The planet's atmosphere contains water vapor and methane signatures.",
    "The autonomous vehicle system uses LiDAR and camera fusion for object detection. Real-time processing enables safe navigation in urban environments.",
    "Genome sequencing technology has reduced costs by 99% over the past fifteen years. CRISPR-based gene editing tools enable precise modifications to DNA sequences.",
]


def build_benchmark_messages(text, entity_types, relation_types):
    et_str = ", ".join(entity_types)
    rt_str = ", ".join(relation_types)
    system_msg = (
        f"You are an expert information extraction system. "
        f"Extract entities and relations from the given text.\n\n"
        f"Entity types: {et_str}\n"
        f"Relation types: {rt_str}\n\n"
        f"Output a JSON object with:\n"
        f"- \"entities\": list of {{\"text\": \"...\", \"type\": \"...\"}}\n"
        f"- \"relations\": list of {{\"head\": \"...\", \"tail\": \"...\", \"type\": \"...\", \"head_type\": \"...\", \"tail_type\": \"...\"}}\n\n"
        f"Output ONLY valid JSON, no explanation."
    )
    user_msg = f'Extract all entities and relations from this text:\n\n"{text}"\n\nOutput JSON:'
    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ]


def run_inference_benchmark(model, tokenizer):
    import torch
    from compiler.ontology_compiler import OntologyCompiler
    from compiler.type_mask_processor import TypeConstraintProcessor

    try:
        import xgrammar as xgr
    except ImportError:
        print("  xgrammar not available, skipping inference benchmark")
        return None

    results = {}
    for scale_name in SCALES:
        path = get_ontology_path(scale_name)
        stats = count_ontology_stats(path)
        print(f"\n  [{scale_name}] {stats['n_entity']} entities, {stats['n_relation']} relations")

        compiler = OntologyCompiler(path)
        spec = compiler.spec
        compiler.compile_type_constraints(tokenizer)
        compiled_grammar = compiler.compile_xgrammar(tokenizer)

        entity_types = spec.entity_types
        relation_types = spec.relation_types

        # Warmup
        msgs = build_benchmark_messages(DUMMY_DOCS[0], entity_types, relation_types)
        text = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        inputs = tokenizer(text, return_tensors="pt").to(model.device)
        with torch.no_grad():
            model.generate(**inputs, max_new_tokens=64, do_sample=False)

        # Unconstrained
        unconstrained_times = []
        for i in range(INFERENCE_DOCS):
            msgs = build_benchmark_messages(DUMMY_DOCS[i], entity_types, relation_types)
            text = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
            inputs = tokenizer(text, return_tensors="pt").to(model.device)

            torch.cuda.synchronize()
            t0 = time.perf_counter()
            with torch.no_grad():
                output_ids = model.generate(**inputs, max_new_tokens=256, do_sample=False)
            torch.cuda.synchronize()
            t1 = time.perf_counter()
            unconstrained_times.append(t1 - t0)

        # Constrained (full_s1)
        constrained_times = []
        for i in range(INFERENCE_DOCS):
            msgs = build_benchmark_messages(DUMMY_DOCS[i], entity_types, relation_types)
            text = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
            inputs = tokenizer(text, return_tensors="pt").to(model.device)
            prompt_len = inputs["input_ids"].shape[1]

            processors = [
                xgr.contrib.hf.LogitsProcessor(compiled_grammar),
                TypeConstraintProcessor(spec, tokenizer, prompt_len),
            ]
            vocab_size = len(tokenizer)

            class _VocabTrim:
                def __init__(self, vs):
                    self.vs = vs
                def __call__(self, input_ids, scores):
                    if scores.shape[-1] > self.vs:
                        scores[:, self.vs:] = float("-inf")
                    return scores

            processors.append(_VocabTrim(vocab_size))

            torch.cuda.synchronize()
            t0 = time.perf_counter()
            with torch.no_grad():
                try:
                    output_ids = model.generate(
                        **inputs, max_new_tokens=256, do_sample=False,
                        logits_processor=processors,
                    )
                except Exception as e:
                    print(f"    Constrained generation failed for doc {i}: {e}")
                    constrained_times.append(float("nan"))
                    continue
            torch.cuda.synchronize()
            t1 = time.perf_counter()
            constrained_times.append(t1 - t0)

        import math
        valid_constrained = [t for t in constrained_times if not math.isnan(t)]

        avg_unconstrained = sum(unconstrained_times) / len(unconstrained_times)
        avg_constrained = sum(valid_constrained) / len(valid_constrained) if valid_constrained else float("nan")
        overhead = avg_constrained / avg_unconstrained if avg_unconstrained > 0 and valid_constrained else float("nan")

        results[scale_name] = {
            **stats,
            "unconstrained_s_per_doc": avg_unconstrained,
            "constrained_s_per_doc": avg_constrained,
            "overhead": overhead,
            "n_failed": len(constrained_times) - len(valid_constrained),
        }
        print(f"    Unconstrained: {avg_unconstrained:.3f} s/doc")
        print(f"    Constrained:   {avg_constrained:.3f} s/doc")
        print(f"    Overhead:      {overhead:.2f}x")
        if results[scale_name]["n_failed"] > 0:
            print(f"    Failed:        {results[scale_name]['n_failed']}/{INFERENCE_DOCS}")

    return results


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Ontology Scalability Benchmark")
    print("=" * 70)

    # Generate synthetic ontologies
    print("\n[Step 1] Generating synthetic ontologies...")
    save_synthetic_ontologies()

    # Load tokenizer (needed for compile benchmark)
    print("\n[Step 2] Loading tokenizer...")
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    print(f"  Tokenizer loaded: {MODEL_PATH}")

    # Part 1: Compile benchmark
    print("\n[Step 3] Running compile benchmark (5 repeats each)...")
    compile_results = run_compile_benchmark(tokenizer)

    # Part 2: Inference overhead
    print("\n[Step 4] Loading model for inference benchmark...")
    import torch
    from transformers import AutoModelForCausalLM

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        device_map="cuda:0",
        trust_remote_code=True,
    )
    model.eval()
    print(f"  Model loaded on {model.device}")

    print("\n[Step 5] Running inference overhead benchmark...")
    inference_results = run_inference_benchmark(model, tokenizer)

    # Print summary
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)

    print("\n--- Table 1: Compile Benchmark ---")
    header = f"{'Scale':<16} {'Entities':>8} {'Relations':>9} {'Grammar(s)':>12} {'Semantic(s)':>12} {'PrefixMap':>10} {'Total(s)':>10}"
    print(header)
    print("-" * len(header))
    for scale_name, r in compile_results.items():
        print(f"{scale_name:<16} {r['n_entity']:>8} {r['n_relation']:>9} {r['grammar_compile_s']:>12.4f} {r['semantic_compile_s']:>12.4f} {r['prefix_map_entries']:>10} {r['total_compile_s']:>10.4f}")

    if inference_results:
        print("\n--- Table 2: Inference Overhead ---")
        header2 = f"{'Scale':<16} {'Entities':>8} {'Relations':>9} {'Unconstr(s)':>12} {'Constr(s)':>12} {'Overhead':>10}"
        print(header2)
        print("-" * len(header2))
        for scale_name, r in inference_results.items():
            print(f"{scale_name:<16} {r['n_entity']:>8} {r['n_relation']:>9} {r['unconstrained_s_per_doc']:>12.3f} {r['constrained_s_per_doc']:>12.3f} {r['overhead']:>10.2f}x")

    # Save JSON results
    output = {
        "compile_benchmark": compile_results,
        "inference_benchmark": inference_results,
        "config": {
            "model": MODEL_PATH,
            "compile_repeats": COMPILE_REPEATS,
            "inference_docs": INFERENCE_DOCS,
            "scales": {k: {kk: str(vv) if isinstance(vv, Path) else vv for kk, vv in v.items()} for k, v in SCALES.items()},
        }
    }
    results_path = PROJECT_ROOT / "scripts" / "ontology_scalability_results.json"
    with open(results_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to {results_path}")


if __name__ == "__main__":
    main()
