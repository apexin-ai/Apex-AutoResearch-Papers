"""Core tests for the annot_sensitivity package."""

import numpy as np
import pytest
from annot_sensitivity import (
    compute_bias,
    compute_asv,
    recommend_correction,
    correct_naive_plugin,
    correct_dsl,
    correct_ppi,
    correct_mcsimex,
    correct_mla,
    validate_confusion_matrix,
    interpolate_confusion,
    random_confusion_matrix,
    predefined_matrices,
    generate_data,
    make_dummies,
    misclassify,
    ols_with_se,
    TOPOLOGIES,
)


class TestValidateConfusionMatrix:
    def test_identity_valid(self):
        assert validate_confusion_matrix(np.eye(3)) is True

    def test_predefined_valid(self):
        for name, C in predefined_matrices().items():
            assert validate_confusion_matrix(C) is True, f"{name} failed"

    def test_non_square(self):
        assert validate_confusion_matrix(np.ones((2, 3))) is False

    def test_negative_entries(self):
        C = np.array([[1.1, -0.1], [-0.1, 1.1]])
        assert validate_confusion_matrix(C) is False

    def test_not_column_stochastic(self):
        C = np.array([[0.5, 0.5], [0.3, 0.3]])
        assert validate_confusion_matrix(C) is False

    def test_not_array(self):
        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False

    def test_1x1(self):
        assert validate_confusion_matrix(np.array([[1.0]])) is False

    def test_random_valid(self):
        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))
        assert validate_confusion_matrix(C) is True
        assert C.shape == (4, 4)


class TestInterpolateConfusion:
    def test_delta_zero_is_identity(self):
        C0 = predefined_matrices()["symmetric_high"]
        C = interpolate_confusion(C0, 0.0)
        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)

    def test_delta_one_is_C0(self):
        C0 = predefined_matrices()["symmetric_high"]
        C = interpolate_confusion(C0, 1.0)
        np.testing.assert_allclose(C, C0, atol=1e-12)

    def test_intermediate_column_stochastic(self):
        C0 = predefined_matrices()["asymmetric"]
        C = interpolate_confusion(C0, 0.5)
        assert validate_confusion_matrix(C)

    def test_small_delta(self):
        C0 = predefined_matrices()["severe_uniform"]
        C = interpolate_confusion(C0, 0.01)
        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),
                           atol=1e-6)


class TestComputeBias:
    def test_identity_zero_bias(self):
        result = compute_bias("confounding", np.eye(3))
        assert abs(result["bias"]) < 1e-3
        assert abs(result["bias_pct"]) < 0.1

    def test_confounding_nonzero_bias(self):
        C = predefined_matrices()["symmetric_high"]
        result = compute_bias("confounding", C)
        assert abs(result["bias"]) > 0.01
        assert result["topology"] == "confounding"
        assert np.isfinite(result["tau_true"])
        assert np.isfinite(result["tau_biased"])

    def test_all_topologies_run(self):
        C = predefined_matrices()["mild_uniform"]
        for topo in TOPOLOGIES:
            result = compute_bias(topo, C)
            assert result["topology"] == topo
            assert np.isfinite(result["tau_true"])
            assert np.isfinite(result["tau_biased"])

    def test_invalid_topology(self):
        with pytest.raises(ValueError, match="Unknown topology"):
            compute_bias("nonexistent", np.eye(3))

    def test_invalid_C(self):
        with pytest.raises(ValueError, match="column-stochastic"):
            compute_bias("confounding", np.ones((3, 3)))

    def test_worse_C_more_bias(self):
        C_mild = predefined_matrices()["mild_uniform"]
        C_severe = predefined_matrices()["severe_uniform"]
        r_mild = compute_bias("confounding", C_mild)
        r_severe = compute_bias("confounding", C_severe)
        assert abs(r_severe["bias"]) > abs(r_mild["bias"])


class TestComputeASV:
    def test_returns_valid_structure(self):
        C0 = predefined_matrices()["symmetric_high"]
        result = compute_asv("confounding", C0, n_grid=200)
        assert "asv" in result
        assert "bias_curve" in result
        assert "envelope" in result
        assert "deltas" in result
        assert "tau_true" in result
        assert len(result["deltas"]) == 200
        assert len(result["bias_curve"]) == 200
        assert len(result["envelope"]) == 200

    def test_asv_is_positive_or_none(self):
        C0 = predefined_matrices()["symmetric_high"]
        result = compute_asv("confounding", C0, threshold_type="magnitude",
                             threshold_value=0.1, n_grid=200)
        if result["asv"] is not None:
            assert result["asv"] > 0

    def test_envelope_monotone(self):
        C0 = predefined_matrices()["asymmetric"]
        result = compute_asv("mediation", C0, n_grid=200)
        diffs = np.diff(result["envelope"])
        assert np.all(diffs >= -1e-12)

    def test_sign_flip_threshold(self):
        C0 = predefined_matrices()["symmetric_high"]
        result = compute_asv("confounding", C0, threshold_type="sign_flip",
                             n_grid=200)
        assert "asv" in result

    def test_invalid_threshold_type(self):
        C0 = predefined_matrices()["symmetric_high"]
        with pytest.raises(ValueError, match="Unknown threshold_type"):
            compute_asv("confounding", C0, threshold_type="invalid", n_grid=50)


class TestRecommendCorrection:
    def test_with_gold_recommends_ppi(self):
        C = predefined_matrices()["symmetric_high"]
        result = recommend_correction("confounding", C, has_gold=True)
        assert result["recommended"] == "ppi"

    def test_without_gold_confounding_recommends_dsl(self):
        C = predefined_matrices()["symmetric_high"]
        result = recommend_correction("confounding", C, has_gold=False)
        assert result["recommended"] == "dsl"

    def test_without_gold_mediation_recommends_dsl(self):
        C = predefined_matrices()["symmetric_high"]
        result = recommend_correction("mediation", C, has_gold=False)
        assert result["recommended"] == "dsl"

    def test_without_gold_collider_recommends_mcsimex(self):
        C = predefined_matrices()["symmetric_high"]
        result = recommend_correction("collider", C, has_gold=False)
        assert result["recommended"] == "mcsimex"

    def test_without_gold_mbias_recommends_mcsimex(self):
        C = predefined_matrices()["symmetric_high"]
        result = recommend_correction("mbias", C, has_gold=False)
        assert result["recommended"] == "mcsimex"

    def test_ranking_has_all_methods(self):
        C = predefined_matrices()["symmetric_high"]
        result = recommend_correction("confounding", C, has_gold=True)
        methods = {m["method"] for m in result["ranking"]}
        assert methods == {"ppi", "dsl", "mcsimex", "naive_plugin", "mla"}

    def test_notes_nonempty(self):
        C = predefined_matrices()["symmetric_high"]
        result = recommend_correction("collider", C, has_gold=False)
        assert len(result["notes"]) > 0


class TestDGP:
    def test_generate_all_topologies(self):
        for topo in TOPOLOGIES:
            data = generate_data(topo, 100, seed=42)
            assert "Y" in data
            assert "A" in data
            assert len(data["Y"]) == 100

    def test_confounding_has_treatment(self):
        data = generate_data("confounding", 100, seed=42)
        assert "T" in data

    def test_exposure_no_treatment(self):
        data = generate_data("exposure", 100, seed=42)
        assert "T" not in data

    def test_iv_has_instrument(self):
        data = generate_data("iv", 100, seed=42)
        assert "Z" in data

    def test_invalid_topology(self):
        with pytest.raises(ValueError):
            generate_data("invalid", 100)


class TestIVWald:
    """Tests for IV Wald estimator (W1 fix)."""

    def test_identity_zero_bias(self):
        result = compute_bias("iv", np.eye(3))
        assert abs(result["bias"]) < 1e-3

    def test_near_permutation_sign_flip(self):
        C = predefined_matrices()["near_permutation"]
        result = compute_bias("iv", C)
        assert np.sign(result["tau_biased"]) != np.sign(result["tau_true"])

    def test_asv_sign_flip_finite(self):
        C0 = predefined_matrices()["near_permutation"]
        result = compute_asv("iv", C0, threshold_type="sign_flip", n_grid=300)
        assert result["asv"] is not None
        assert result["asv"] > 0

    def test_symmetric_high_moderate_bias(self):
        C = predefined_matrices()["symmetric_high"]
        result = compute_bias("iv", C)
        assert abs(result["bias"]) > 0.01


def _make_confounding_data(N, K, C, rng, gold_frac=0.1):
    """Helper: generate confounding data, misclassify, return test inputs."""
    data = generate_data("confounding", N, seed=int(rng.integers(0, 2**31)))
    T, Y, A = data["T"], data["Y"], data["A"]
    Astar = misclassify(A, C, rng)
    X_other = np.column_stack([np.ones(N), T])
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[: int(gold_frac * N)] = True
    return X_other, Y, A, Astar, gold_mask


class TestCorrectionMethods:
    """Smoke tests + property tests for 5 correction methods."""

    @pytest.fixture
    def confounding_data(self):
        rng = np.random.default_rng(42)
        K = 3
        C = predefined_matrices(K)["symmetric_high"]
        X_other, Y, A, Astar, gold_mask = _make_confounding_data(
            2000, K, C, rng
        )
        return dict(
            X_other=X_other, Y=Y, A=A, Astar=Astar,
            gold_mask=gold_mask, C=C, K=K, rng=rng,
        )

    def test_naive_plugin_smoke(self, confounding_data):
        d = confounding_data
        tau, se, ok = correct_naive_plugin(d["X_other"], d["Y"], d["Astar"],
                                           d["C"], tau_idx=1)
        assert ok is True
        assert np.isfinite(tau)
        assert np.isfinite(se)

    def test_dsl_smoke(self, confounding_data):
        d = confounding_data
        tau, se, ok = correct_dsl(d["X_other"], d["Y"], d["Astar"],
                                  d["A"], d["gold_mask"], tau_idx=1)
        assert ok is True
        assert np.isfinite(tau)
        assert np.isfinite(se)

    def test_ppi_smoke(self, confounding_data):
        d = confounding_data
        tau, se, ok = correct_ppi(d["X_other"], d["Y"], d["Astar"],
                                  d["A"], d["gold_mask"], tau_idx=1,
                                  rng=d["rng"])
        assert ok is True
        assert np.isfinite(tau)
        assert np.isfinite(se)

    def test_mcsimex_smoke(self, confounding_data):
        d = confounding_data
        tau, se, ok = correct_mcsimex(d["X_other"], d["Y"], d["Astar"],
                                      d["C"], tau_idx=1, rng=d["rng"])
        assert ok is True
        assert np.isfinite(tau)

    def test_mla_smoke(self, confounding_data):
        d = confounding_data
        tau, se, ok = correct_mla(d["X_other"], d["Y"], d["Astar"],
                                  d["C"], tau_idx=1)
        assert ok is True
        assert np.isfinite(tau)
        assert np.isfinite(se)

    def test_ppi_bias_reduction(self):
        rng = np.random.default_rng(123)
        K = 3
        C = predefined_matrices(K)["symmetric_high"]
        n_reps = 20
        N = 5000
        uncorrected = np.zeros(n_reps)
        corrected = np.zeros(n_reps)
        tau_true_vals = np.zeros(n_reps)

        for r in range(n_reps):
            data = generate_data("confounding", N,
                                 seed=int(rng.integers(0, 2**31)))
            T, Y, A = data["T"], data["Y"], data["A"]
            Astar = misclassify(A, C, rng)
            X_other = np.column_stack([np.ones(N), T])
            D_star = make_dummies(Astar, K)
            X_unc = np.column_stack([X_other, D_star])
            beta_unc, _ = ols_with_se(X_unc, Y)
            D_true = make_dummies(A, K)
            X_true = np.column_stack([X_other, D_true])
            beta_true, _ = ols_with_se(X_true, Y)
            tau_true_vals[r] = beta_true[1]
            uncorrected[r] = beta_unc[1]

            gold_mask = np.zeros(N, dtype=bool)
            gold_mask[: int(0.1 * N)] = True
            tau_ppi, _, _ = correct_ppi(X_other, Y, Astar, A, gold_mask,
                                        tau_idx=1, rng=rng)
            corrected[r] = tau_ppi

        tau_true_mean = tau_true_vals.mean()
        bias_unc = abs(uncorrected.mean() - tau_true_mean)
        bias_ppi = abs(corrected.mean() - tau_true_mean)
        assert bias_ppi < 0.5 * bias_unc, (
            f"PPI bias {bias_ppi:.4f} not < 50% of uncorrected {bias_unc:.4f}"
        )

    def test_dsl_catastrophic_on_mbias(self):
        rng = np.random.default_rng(77)
        K = 3
        C = predefined_matrices(K)["symmetric_high"]
        N = 3000
        data = generate_data("mbias", N, seed=77)
        T, Y, A = data["T"], data["Y"], data["A"]
        Astar = misclassify(A, C, rng)
        X_other = np.column_stack([np.ones(N), T])
        gold_mask = np.zeros(N, dtype=bool)
        gold_mask[:int(0.1 * N)] = True

        D_star = make_dummies(Astar, K)
        X_unc = np.column_stack([X_other, D_star])
        beta_unc, _ = ols_with_se(X_unc, Y)

        D_true = make_dummies(A, K)
        X_true = np.column_stack([X_other, D_true])
        beta_true, _ = ols_with_se(X_true, Y)
        tau_true = beta_true[1]

        tau_dsl, _, ok = correct_dsl(X_other, Y, Astar, A, gold_mask,
                                     tau_idx=1)
        bias_unc = abs(beta_unc[1] - tau_true)
        bias_dsl = abs(tau_dsl - tau_true)
        assert bias_dsl > bias_unc * 0.8, (
            f"DSL bias {bias_dsl:.4f} not worse than uncorrected {bias_unc:.4f}"
        )

    def test_end_to_end_pipeline(self):
        rng = np.random.default_rng(99)
        K = 3
        C = predefined_matrices(K)["symmetric_high"]
        N = 2000
        data = generate_data("confounding", N, seed=99)
        T, Y, A = data["T"], data["Y"], data["A"]

        r_bias = compute_bias("confounding", C)
        assert abs(r_bias["bias"]) > 0.01

        Astar = misclassify(A, C, rng)
        X_other = np.column_stack([np.ones(N), T])
        gold_mask = np.zeros(N, dtype=bool)
        gold_mask[:int(0.1 * N)] = True

        tau_ppi, se_ppi, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,
                                          tau_idx=1, rng=rng)
        assert ok is True
        assert np.isfinite(tau_ppi)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
