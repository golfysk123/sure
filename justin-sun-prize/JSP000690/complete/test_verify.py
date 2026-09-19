import unittest
from verify import audit, NAMES, is_false_proposition_rejection

class AxiomAuditTests(unittest.TestCase):
    def valid(self):
        return '\n'.join(f"'{n}' depends on axioms: [propext, Classical.choice, Quot.sound]" for n in NAMES)
    def test_all_expected_targets(self):
        self.assertEqual(set(audit(self.valid())), set(NAMES))
    def test_missing_target(self):
        with self.assertRaises(ValueError): audit('\n'.join(self.valid().splitlines()[:-1]))
    def test_sorry_axiom(self):
        with self.assertRaises(ValueError): audit(self.valid().replace('Quot.sound', 'sorryAx', 1))
    def test_native_axiom(self):
        with self.assertRaises(ValueError): audit(self.valid().replace('Quot.sound', 'Lean.ofReduceBool', 1))
    def test_custom_axiom(self):
        with self.assertRaises(ValueError): audit(self.valid().replace('Quot.sound', 'AssumeEverything', 1))
    def test_duplicate_report(self):
        with self.assertRaises(ValueError): audit(self.valid() + '\n' + self.valid().splitlines()[0])
    def test_empty(self):
        with self.assertRaises(ValueError): audit('')


class NegativeControlTests(unittest.TestCase):
    OLD = "Negative.lean:1:30: error: tactic 'decide' proved that the proposition\n  1 = 2\nis false\n"
    NEW = "Negative.lean:1:30: error: Tactic `decide` proved that the proposition\n  1 = 2\nis false\n"
    def test_lean_419(self):
        self.assertTrue(is_false_proposition_rejection(1, self.OLD))
    def test_lean_434(self):
        self.assertTrue(is_false_proposition_rejection(1, self.NEW))
    def test_success_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(0, self.NEW))
    def test_signal_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(-9, self.NEW))
    def test_shell_kill_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(137, self.NEW))
    def test_import_error_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(1, "error: unknown module prefix 'JSP690'"))
    def test_syntax_error_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(1, "error: unexpected token 'example'"))
    def test_extra_error_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(1, self.NEW + "error: unknown identifier\n"))
    def test_missing_proposition_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(1, self.NEW.replace('  1 = 2', '  ')))
    def test_incomplete_diagnostic_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(1, self.NEW.replace('is false', '')))
    def test_unrelated_false_text_is_not_rejection(self):
        self.assertFalse(is_false_proposition_rejection(1, "error: tactic failed; is false"))
    def test_multiline_proposition(self):
        self.assertTrue(is_false_proposition_rejection(1, self.NEW.replace('  1 = 2', '  ¬ Colourable\n    (edges.erase {0, 1, 2}) 2')))

if __name__ == '__main__': unittest.main()
