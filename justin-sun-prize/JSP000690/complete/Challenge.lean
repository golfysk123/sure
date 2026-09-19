import JSP690

/-!
Statement-facing interface: no new definitions, axioms or bit encodings.
The mathematical construction is Ruiliang Li's chromatic example.
This does not address the separate transversal-number interpretation.
-/
namespace JSP690Challenge

theorem original_problem :
    ∃ H : Finset (Finset (Fin 9)),
      H.card = 22 ∧
      (∀ e ∈ H, e.card = 3) ∧
      (∀ v : Fin 9, 7 ≤ (H.filter (fun e => v ∈ e)).card) ∧
      (∃ v : Fin 9, (H.filter (fun e => v ∈ e)).card = 7) ∧
      (∃ c : Fin 9 → Fin 3,
        ∀ e ∈ H, ∃ u ∈ e, ∃ v ∈ e, c u ≠ c v) ∧
      (∀ k : Nat, k < 3 → ¬ ∃ c : Fin 9 → Fin k,
        ∀ e ∈ H, ∃ u ∈ e, ∃ v ∈ e, c u ≠ c v) ∧
      (∀ (U : Finset (Fin 9)) (F : Finset (Finset (Fin 9))),
        F ⊆ H → (∀ e ∈ F, e ⊆ U) → (U ≠ Finset.univ ∨ F ≠ H) →
        ∃ c : {v : Fin 9 // v ∈ U} → Fin 2,
          ∀ e ∈ F, ∃ u v : {x : Fin 9 // x ∈ U},
            u.val ∈ e ∧ v.val ∈ e ∧ c u ≠ c v) := by
  simpa only [JSP690.Colourable, JSP690.Proper, JSP690.ProperOn, JSP690.degree]
    using JSP690.chromatic_original_problem

#print axioms original_problem
end JSP690Challenge
