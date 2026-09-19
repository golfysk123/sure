import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Pi

/-!
Independent formalization of the chromatic reading of JSP-000690 / Erdős 834.
Mathematical witness: Ruiliang Li, arXiv:2512.24850v1, equation (5).
No mathematical discovery or first-formalization priority is claimed.
-/
set_option maxRecDepth 200000
set_option maxHeartbeats 16000000

namespace JSP690
abbrev V := Fin 9
abbrev Hypergraph (α : Type) := Finset (Finset α)

def edges : Hypergraph V := {
  {0,1,2},{0,1,8},{0,2,7},{0,3,5},{0,3,7},{0,3,8},
  {0,4,6},{0,4,7},{0,4,8},{0,5,6},{1,2,5},{1,2,6},
  {1,3,8},{1,4,8},{1,5,6},{2,3,7},{2,4,7},{2,5,6},
  {3,5,7},{3,5,8},{4,6,7},{4,6,8}}

/-- Weak proper colouring: every hyperedge contains two differently coloured vertices. -/
def Proper {α : Type} (H : Hypergraph α) {k : Nat} (c : α → Fin k) : Prop :=
  ∀ e ∈ H, ∃ u ∈ e, ∃ v ∈ e, c u ≠ c v

instance {α : Type} [DecidableEq α] (H : Hypergraph α) {k : Nat} (c : α → Fin k) :
    Decidable (Proper H c) := by unfold Proper; infer_instance

/-- Quantifies over *all* colouring functions, not sampled integer encodings. -/
def Colourable {α : Type} (H : Hypergraph α) (k : Nat) : Prop :=
  ∃ c : α → Fin k, Proper H c

instance {α : Type} [Fintype α] [DecidableEq α] (H : Hypergraph α) (k : Nat) :
    Decidable (Colourable H k) := by unfold Colourable; infer_instance

def degree {α : Type} [DecidableEq α] (H : Hypergraph α) (v : α) : Nat :=
  (H.filter (fun e => v ∈ e)).card

def triColour (v : V) : Fin 3 :=
  if v = 0 then 0 else if v = 1 then 1 else if v = 2 then 2 else
  if v = 3 then 0 else if v = 4 then 0 else if v = 5 then 1 else
  if v = 6 then 2 else if v = 7 then 1 else 2

theorem edge_count : edges.card = 22 := by decide

theorem three_uniform : ∀ e ∈ edges, e.card = 3 := by decide

theorem min_degree : ∀ v : V, 7 ≤ degree edges v := by decide

theorem degree_zero : degree edges 0 = 10 := by decide

theorem min_degree_attained : ∃ v : V, degree edges v = 7 := by decide

theorem three_colourable : Colourable edges 3 := by
  exact ⟨triColour, by decide⟩

theorem not_two_colourable : ¬ Colourable edges 2 := by decide



/-- A concrete colouring used only to supply witnesses; no completeness claim is needed. -/
def colourMask (m : Nat) (v : V) : Fin 2 :=
  ⟨m / (2 ^ v.val) % 2, Nat.mod_lt _ (by decide)⟩

theorem every_edge_deletion : ∀ e ∈ edges, Colourable (edges.erase e) 2 := by
  intro e he
  simp only [edges, Finset.mem_insert, Finset.mem_singleton] at he
  rcases he with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact ⟨colourMask 31, by decide⟩
  · exact ⟨colourMask 60, by decide⟩
  · exact ⟨colourMask 58, by decide⟩
  · exact ⟨colourMask 59, by decide⟩
  · exact ⟨colourMask 203, by decide⟩
  · exact ⟨colourMask 178, by decide⟩
  · exact ⟨colourMask 91, by decide⟩
  · exact ⟨colourMask 179, by decide⟩
  · exact ⟨colourMask 202, by decide⟩
  · exact ⟨colourMask 30, by decide⟩
  · exact ⟨colourMask 62, by decide⟩
  · exact ⟨colourMask 94, by decide⟩
  · exact ⟨colourMask 53, by decide⟩
  · exact ⟨colourMask 77, by decide⟩
  · exact ⟨colourMask 29, by decide⟩
  · exact ⟨colourMask 51, by decide⟩
  · exact ⟨colourMask 75, by decide⟩
  · exact ⟨colourMask 27, by decide⟩
  · exact ⟨colourMask 186, by decide⟩
  · exact ⟨colourMask 195, by decide⟩
  · exact ⟨colourMask 218, by decide⟩
  · exact ⟨colourMask 163, by decide⟩

/-- Restricting the edge family preserves a proper colouring. -/
theorem proper_mono {α : Type} {F H : Hypergraph α} {k : Nat} {c : α → Fin k}
    (hFH : F ⊆ H) (hc : Proper H c) : Proper F c := by
  intro e he
  exact hc e (hFH he)

theorem colourable_of_strict_subset (F : Hypergraph V) (h : F ⊂ edges) :
    Colourable F 2 := by
  obtain ⟨hsub, hne⟩ := Finset.ssubset_iff_subset_ne.mp h
  have hnot : ¬ edges ⊆ F := by
    intro hback
    exact hne (Finset.Subset.antisymm hsub hback)
  obtain ⟨e, he, hef⟩ := Finset.not_subset.mp hnot
  obtain ⟨c, hc⟩ := every_edge_deletion e he
  refine ⟨c, proper_mono ?_ hc⟩
  intro f hf
  apply Finset.mem_erase.mpr
  refine ⟨?_, hsub hf⟩
  intro hfe
  exact hef (hfe ▸ hf)

theorem full_support : ∀ v : V, ∃ e ∈ edges, v ∈ e := by
  intro v
  have hpos : 0 < (edges.filter (fun e => v ∈ e)).card := by
    have hd := min_degree v
    change 7 ≤ (edges.filter (fun e => v ∈ e)).card at hd
    omega
  obtain ⟨e, he⟩ := Finset.card_pos.mp hpos
  exact ⟨e, (Finset.mem_filter.mp he).1, (Finset.mem_filter.mp he).2⟩

/-- Proper colouring on the *actual remaining vertex subtype*. -/
def ProperOn (U : Finset V) (F : Hypergraph V) {k : Nat}
    (c : {v : V // v ∈ U} → Fin k) : Prop :=
  ∀ e ∈ F, ∃ u v : {x : V // x ∈ U},
    u.val ∈ e ∧ v.val ∈ e ∧ c u ≠ c v

/-- Every proper subhypergraph, allowing arbitrary vertex and/or edge removal, is 2-colourable. -/
theorem every_proper_subhypergraph
    (U : Finset V) (F : Hypergraph V)
    (hF : F ⊆ edges)
    (hsupport : ∀ e ∈ F, e ⊆ U)
    (hproper : U ≠ Finset.univ ∨ F ≠ edges) :
    ∃ c : {v : V // v ∈ U} → Fin 2, ProperOn U F c := by
  have hneq : F ≠ edges := by
    intro hEq
    rcases hproper with hU | hE
    · apply hU
      apply Finset.Subset.antisymm (Finset.subset_univ U)
      intro v _
      obtain ⟨e, he, hv⟩ := full_support v
      exact hsupport e (hEq ▸ he) hv
    · exact hE hEq
  obtain ⟨c, hc⟩ := colourable_of_strict_subset F
    (Finset.ssubset_iff_subset_ne.mpr ⟨hF, hneq⟩)
  refine ⟨fun v => c v.val, ?_⟩
  intro e he
  obtain ⟨u, hu, v, hv, hne⟩ := hc e he
  exact ⟨⟨u, hsupport e he hu⟩, ⟨v, hsupport e he hv⟩, hu, hv, hne⟩

theorem no_smaller_colour_count : ∀ k < 3, ¬ Colourable edges k := by
  intro k hk
  have hcases : k = 0 ∨ k = 1 ∨ k = 2 := by omega
  rcases hcases with rfl | rfl | rfl
  · decide
  · decide
  · exact not_two_colourable

/-- A finite simple, 3-uniform, critically 3-chromatic witness with minimum degree exactly 7. -/
theorem chromatic_original_problem :
    ∃ H : Hypergraph (Fin 9),
      H.card = 22 ∧
      (∀ e ∈ H, e.card = 3) ∧
      (∀ v, 7 ≤ degree H v) ∧
      (∃ v, degree H v = 7) ∧
      Colourable H 3 ∧
      (∀ k < 3, ¬ Colourable H k) ∧
      (∀ (U : Finset V) (F : Hypergraph V), F ⊆ H →
        (∀ e ∈ F, e ⊆ U) → (U ≠ Finset.univ ∨ F ≠ H) →
        ∃ c : {v : V // v ∈ U} → Fin 2, ProperOn U F c) := by
  exact ⟨edges, edge_count, three_uniform, min_degree, min_degree_attained,
    three_colourable, no_smaller_colour_count, every_proper_subhypergraph⟩

#print axioms chromatic_original_problem
#print axioms every_proper_subhypergraph
#print axioms not_two_colourable
end JSP690
