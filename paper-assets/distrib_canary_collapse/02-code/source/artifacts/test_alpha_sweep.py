"""Dry-run test for synthetic_ratio (alpha-sweep) data mixing logic.

Validates that mix_datasets bidirectional subsampling and accumulate mode
work correctly for various synthetic_ratio values without requiring GPU.
Run: python test_alpha_sweep.py
"""

import random
import sys

from datasets import Dataset, concatenate_datasets


# ---------- inline copy of mix_datasets from iterative_train.py ----------

def mix_datasets(real_dataset, synthetic_dataset, synthetic_ratio, seed):
    if synthetic_ratio >= 1.0:
        return synthetic_dataset
    if synthetic_ratio <= 0.0:
        return real_dataset

    needed_syn = int(len(real_dataset) * synthetic_ratio / (1 - synthetic_ratio))
    if needed_syn <= len(synthetic_dataset):
        syn_subset = synthetic_dataset.shuffle(seed=seed).select(range(needed_syn))
        real_subset = real_dataset
    else:
        needed_real = int(len(synthetic_dataset) * (1 - synthetic_ratio) / synthetic_ratio)
        needed_real = min(needed_real, len(real_dataset))
        real_subset = real_dataset.shuffle(seed=seed).select(range(needed_real))
        syn_subset = synthetic_dataset

    actual_ratio = len(syn_subset) / (len(syn_subset) + len(real_subset))
    print(f"    Mix: {len(syn_subset)} syn + {len(real_subset)} real = {actual_ratio:.4f}")
    return concatenate_datasets([real_subset, syn_subset]).shuffle(seed=seed)


# ---------- helpers ----------

def make_dataset(prefix, n):
    return Dataset.from_dict({"text": [f"{prefix}_{i}" for i in range(n)]})


def get_prefixes(ds):
    return {t.rsplit("_", 1)[0] for t in ds["text"]}


def count_by_prefix(ds, prefix):
    return sum(1 for t in ds["text"] if t.startswith(prefix))


# ---------- tests ----------

def test_ratio_1():
    real = make_dataset("real", 100)
    syn = make_dataset("syn", 50)
    mixed = mix_datasets(real, syn, 1.0, seed=0)
    assert len(mixed) == 50, f"ratio=1.0 should return only synthetic, got {len(mixed)}"
    assert get_prefixes(mixed) == {"syn"}
    print("  PASS ratio=1.0 → pure synthetic")


def test_ratio_0():
    real = make_dataset("real", 100)
    syn = make_dataset("syn", 50)
    mixed = mix_datasets(real, syn, 0.0, seed=0)
    assert len(mixed) == 100, f"ratio=0.0 should return only real, got {len(mixed)}"
    assert get_prefixes(mixed) == {"real"}
    print("  PASS ratio=0.0 → pure real")


def test_ratio_050():
    real = make_dataset("real", 200)
    syn = make_dataset("syn", 200)
    mixed = mix_datasets(real, syn, 0.5, seed=0)
    prefixes = get_prefixes(mixed)
    assert prefixes == {"real", "syn"}, f"Expected both prefixes, got {prefixes}"
    n_syn = count_by_prefix(mixed, "syn")
    n_real = count_by_prefix(mixed, "real")
    actual_ratio = n_syn / (n_syn + n_real)
    assert abs(actual_ratio - 0.5) < 0.01, f"ratio=0.5 actual={actual_ratio:.3f}"
    assert n_real == 200, f"All real should be kept, got {n_real}"
    print(f"  PASS ratio=0.5 → {n_syn} syn + {n_real} real = {len(mixed)} total (actual ratio={actual_ratio:.3f})")


def test_ratio_025():
    real = make_dataset("real", 500)
    syn = make_dataset("syn", 200)
    mixed = mix_datasets(real, syn, 0.25, seed=0)
    n_syn = count_by_prefix(mixed, "syn")
    n_real = count_by_prefix(mixed, "real")
    actual_ratio = n_syn / (n_syn + n_real)
    assert abs(actual_ratio - 0.25) < 0.01, f"ratio=0.25 actual={actual_ratio:.3f}"
    assert n_real == 500, f"All real should be kept, got {n_real}"
    print(f"  PASS ratio=0.25 → {n_syn} syn + {n_real} real (actual ratio={actual_ratio:.3f})")


def test_ratio_090():
    real = make_dataset("real", 10)
    syn = make_dataset("syn", 90)
    mixed = mix_datasets(real, syn, 0.90, seed=0)
    n_syn = count_by_prefix(mixed, "syn")
    n_real = count_by_prefix(mixed, "real")
    actual_ratio = n_syn / (n_syn + n_real)
    assert abs(actual_ratio - 0.90) < 0.02, f"ratio=0.90 actual={actual_ratio:.3f}"
    assert n_real == 10, f"All real should be kept, got {n_real}"
    print(f"  PASS ratio=0.90 → {n_syn} syn + {n_real} real (actual ratio={actual_ratio:.3f})")


def test_ratio_025_precise():
    """real=50, syn=50, ratio=0.25 → low α: keep real=50, syn≈17."""
    real = make_dataset("real", 50)
    syn = make_dataset("syn", 50)
    mixed = mix_datasets(real, syn, 0.25, seed=0)
    n_syn = count_by_prefix(mixed, "syn")
    n_real = count_by_prefix(mixed, "real")
    assert n_real == 50, f"All real should be kept, got {n_real}"
    expected_syn = int(50 * 0.25 / 0.75)  # 16
    assert n_syn == expected_syn, f"Expected {expected_syn} syn, got {n_syn}"
    actual_ratio = n_syn / (n_syn + n_real)
    assert abs(actual_ratio - 0.25) < 0.02, f"ratio should be ~0.25, got {actual_ratio:.3f}"
    print(f"  PASS ratio=0.25 precise → {n_syn} syn + {n_real} real (actual ratio={actual_ratio:.3f})")


def test_ratio_075_precise():
    """real=50, syn=50, ratio=0.75 → high α: keep syn=50, subsample real≈17."""
    real = make_dataset("real", 50)
    syn = make_dataset("syn", 50)
    mixed = mix_datasets(real, syn, 0.75, seed=0)
    n_syn = count_by_prefix(mixed, "syn")
    n_real = count_by_prefix(mixed, "real")
    assert n_syn == 50, f"All syn should be kept, got {n_syn}"
    expected_real = int(50 * 0.25 / 0.75)  # 16
    assert n_real == expected_real, f"Expected {expected_real} real, got {n_real}"
    actual_ratio = n_syn / (n_syn + n_real)
    assert abs(actual_ratio - 0.75) < 0.02, f"ratio should be ~0.75, got {actual_ratio:.3f}"
    print(f"  PASS ratio=0.75 precise → {n_syn} syn + {n_real} real (actual ratio={actual_ratio:.3f})")


def test_ratio_090_precise():
    """real=50, syn=200, ratio=0.90 → high α: keep syn=200, subsample real≈22."""
    real = make_dataset("real", 50)
    syn = make_dataset("syn", 200)
    mixed = mix_datasets(real, syn, 0.90, seed=0)
    n_syn = count_by_prefix(mixed, "syn")
    n_real = count_by_prefix(mixed, "real")
    assert n_syn == 200, f"All syn should be kept, got {n_syn}"
    expected_real = int(200 * 0.10 / 0.90)  # 22
    assert n_real == expected_real, f"Expected {expected_real} real, got {n_real}"
    actual_ratio = n_syn / (n_syn + n_real)
    assert abs(actual_ratio - 0.90) < 0.02, f"ratio should be ~0.90, got {actual_ratio:.3f}"
    print(f"  PASS ratio=0.90 precise → {n_syn} syn + {n_real} real (actual ratio={actual_ratio:.3f})")


def test_ratio_050_balanced():
    """real=50, syn=50, ratio=0.50 → exactly balanced."""
    real = make_dataset("real", 50)
    syn = make_dataset("syn", 50)
    mixed = mix_datasets(real, syn, 0.50, seed=0)
    n_syn = count_by_prefix(mixed, "syn")
    n_real = count_by_prefix(mixed, "real")
    assert n_syn == 50, f"Expected 50 syn, got {n_syn}"
    assert n_real == 50, f"Expected 50 real, got {n_real}"
    actual_ratio = n_syn / (n_syn + n_real)
    assert actual_ratio == 0.5, f"ratio should be exactly 0.50, got {actual_ratio:.3f}"
    print(f"  PASS ratio=0.50 balanced → {n_syn} syn + {n_real} real (actual ratio={actual_ratio:.3f})")


def test_accumulate_ratio_stable():
    """Accumulate mode with ratio=0.50: low α path each gen, ratio stays stable."""
    real = make_dataset("real", 100)
    synthetic_pool = []
    for gen in range(1, 4):
        gen_syn = make_dataset(f"gen{gen}", 100)
        synthetic_pool.append(gen_syn)
        pooled = concatenate_datasets(synthetic_pool)
        mixed = mix_datasets(real, pooled, 0.5, seed=gen)
        n_syn = sum(1 for t in mixed["text"] if not t.startswith("real"))
        n_real = count_by_prefix(mixed, "real")
        actual_ratio = n_syn / (n_syn + n_real)
        assert n_real == 100, f"gen {gen}: all real should be kept, got {n_real}"
        assert abs(actual_ratio - 0.50) < 0.01, \
            f"gen {gen}: ratio should be ~0.50, got {actual_ratio:.3f}"
        print(f"  PASS accumulate gen {gen}: {n_syn} syn + {n_real} real (ratio={actual_ratio:.3f})")


def test_accumulate_mode():
    """Simulate --accumulate with high α path: pool grows, real subsampled to match."""
    real = make_dataset("real", 200)
    synthetic_pool = []
    for gen in range(1, 4):
        gen_syn = make_dataset(f"gen{gen}", 20)
        synthetic_pool.append(gen_syn)
        pooled = concatenate_datasets(synthetic_pool)
        mixed = mix_datasets(real, pooled, 0.5, seed=gen)
        n_syn = sum(1 for t in mixed["text"] if not t.startswith("real"))
        n_real = count_by_prefix(mixed, "real")
        actual_ratio = n_syn / (n_syn + n_real)
        expected_syn = 20 * gen
        assert n_syn == expected_syn, f"gen {gen}: expected {expected_syn} syn, got {n_syn}"
        assert n_real == expected_syn, f"gen {gen}: real should match syn={expected_syn}, got {n_real}"
        assert abs(actual_ratio - 0.50) < 0.01, \
            f"gen {gen}: ratio should be ~0.50, got {actual_ratio:.3f}"
        print(f"  PASS accumulate gen {gen}: pool={expected_syn} syn + {n_real} real = {len(mixed)} total (ratio={actual_ratio:.3f})")


def test_no_accumulate_mode():
    """Default mode: only current generation synthetic data, high α path subsamples real."""
    real = make_dataset("real", 200)
    for gen in range(1, 4):
        gen_syn = make_dataset(f"gen{gen}", 20)
        mixed = mix_datasets(real, gen_syn, 0.5, seed=gen)
        n_syn = sum(1 for t in mixed["text"] if not t.startswith("real"))
        n_real = count_by_prefix(mixed, "real")
        actual_ratio = n_syn / (n_syn + n_real)
        assert n_syn == 20, f"gen {gen}: expected 20 syn, got {n_syn}"
        assert n_real == 20, f"gen {gen}: real should be subsampled to 20, got {n_real}"
        gen_prefixes = {t.rsplit("_", 1)[0] for t in mixed["text"] if not t.startswith("real")}
        assert gen_prefixes == {f"gen{gen}"}, f"Should only have gen{gen} data, got {gen_prefixes}"
        print(f"  PASS no-accumulate gen {gen}: 20 syn (gen{gen} only) + {n_real} real (ratio={actual_ratio:.3f})")


def test_determinism():
    """Same seed produces same mix."""
    real = make_dataset("real", 200)
    syn = make_dataset("syn", 200)
    m1 = mix_datasets(real, syn, 0.5, seed=42)
    m2 = mix_datasets(real, syn, 0.5, seed=42)
    assert m1["text"] == m2["text"], "Same seed should produce identical mix"
    m3 = mix_datasets(real, syn, 0.5, seed=99)
    assert m3["text"] != m1["text"], "Different seed should produce different mix"
    print("  PASS deterministic with same seed")


def test_alpha_sweep_full():
    """Sweep all target ratios, verify actual ratio within tolerance."""
    real = make_dataset("real", 100)
    syn = make_dataset("syn", 300)
    ratios = [0.0, 0.25, 0.50, 0.75, 0.90, 1.0]
    for ratio in ratios:
        mixed = mix_datasets(real, syn, ratio, seed=42)
        if ratio == 0.0:
            assert get_prefixes(mixed) == {"real"}
            print(f"  PASS sweep ratio={ratio:.2f} → pure real")
            continue
        if ratio == 1.0:
            assert get_prefixes(mixed) == {"syn"}
            print(f"  PASS sweep ratio={ratio:.2f} → pure synthetic")
            continue
        n_syn = count_by_prefix(mixed, "syn")
        n_real = count_by_prefix(mixed, "real")
        actual_ratio = n_syn / (n_syn + n_real)
        assert abs(actual_ratio - ratio) < 0.05, \
            f"ratio={ratio}: actual={actual_ratio:.3f}, diff={abs(actual_ratio-ratio):.3f} >= 0.05"
        print(f"  PASS sweep ratio={ratio:.2f} → {n_syn} syn + {n_real} real (actual={actual_ratio:.3f})")


# ---------- main ----------

if __name__ == "__main__":
    print("=== Alpha-sweep dry-run tests ===\n")

    tests = [
        ("ratio=1.0 (pure synthetic)", test_ratio_1),
        ("ratio=0.0 (pure real)", test_ratio_0),
        ("ratio=0.50", test_ratio_050),
        ("ratio=0.25", test_ratio_025),
        ("ratio=0.90", test_ratio_090),
        ("ratio=0.25 precise (real=50, syn=50)", test_ratio_025_precise),
        ("ratio=0.75 precise (real=50, syn=50)", test_ratio_075_precise),
        ("ratio=0.90 precise (real=50, syn=200)", test_ratio_090_precise),
        ("ratio=0.50 balanced (real=50, syn=50)", test_ratio_050_balanced),
        ("accumulate ratio stability", test_accumulate_ratio_stable),
        ("accumulate mode (high α path)", test_accumulate_mode),
        ("no-accumulate mode (default)", test_no_accumulate_mode),
        ("determinism", test_determinism),
        ("alpha-sweep full coverage", test_alpha_sweep_full),
    ]

    passed = 0
    failed = 0
    for name, fn in tests:
        print(f"[{name}]")
        try:
            fn()
            passed += 1
        except AssertionError as e:
            print(f"  FAIL: {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {type(e).__name__}: {e}")
            failed += 1

    print(f"\n=== {passed}/{passed+failed} tests passed ===")
    sys.exit(0 if failed == 0 else 1)
