from src import RestEnz as re
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
import unittest
import sys
sys.path.append('../src')

ATGC = 'ATGC'
CGTA = 'CGTA'
ATGC_plus_CGTA = ATGC + CGTA
ATGC_DNA = re.RestEnz(Seq(ATGC, IUPAC.unambiguous_dna))
CGTA_DNA = re.RestEnz(Seq(CGTA, IUPAC.unambiguous_dna))


class RestEnzTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(ATGC_plus_CGTA, ATGC_DNA + CGTA_DNA)

    def test_cut(self):
        dna = re.RestEnz(Seq('GACGTC', IUPAC.unambiguous_dna))
        # 突出末端
        restriction_dna = ['GACGT', 'C']
        self.assertEqual(['GACGT', 'C'], dna.cut(restriction_dna[0], restriction_dna[1], reverse=False))
        self.assertEqual(['C', 'TGCAG'], dna.reverse().cut(restriction_dna[0], restriction_dna[1], reverse=True))

        # 平滑末端
        restriction_dna = ['GAT', 'ATC']
        dna = re.RestEnz(Seq('GATATC', IUPAC.unambiguous_dna))
        self.assertEqual(['GAT', 'ATC'], dna.cut(restriction_dna[0], restriction_dna[1], reverse=False))
        self.assertEqual(['CTA', 'TAG'], dna.reverse().cut(restriction_dna[0], restriction_dna[1], reverse=True))

    def test_reverse(self):
        self.assertEqual('TACG', str(ATGC_DNA.reverse().get_dna()))

    def test_get_dna(self):
        get_dna = ATGC_DNA.get_dna()
        self.assertEqual(True, get_dna == Seq(ATGC, IUPAC.unambiguous_dna))

    # set api on the server
    def test_get_restriction_enzyme(self):
        BamH_1 = re.RestEnz('').get_restriction_enzyme('BamH_1')
        self.assertEqual('BamH_1', BamH_1['name'])
        self.assertEqual([{'first': 'G', 'last': 'GATCC', 'whole': 'GGATCC'}], BamH_1['recognition_site'])
        self.assertEqual(1, BamH_1['total_site'])
