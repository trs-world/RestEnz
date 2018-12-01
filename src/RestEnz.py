import re
import requests
import json


class RestEnz:

    def __init__(self, dna):
        self.dna = dna

    def __add__(self, other):
        if isinstance(other, RestEnz):
            other = other.get_dna()
        if re.match('.*[^A|G|C|T|U|N]', str(other)) is not None:
            raise NotCodonError()
        return str(self.dna + other)

    def cut(self, start, last, reverse=False):
        if reverse is True:
            mock = start[::-1]
            start = last[::-1]
            last = mock
        restriction_enzyme = start + last
        split_dna = str(self.dna).split(restriction_enzyme)
        tail = False
        cut_dna = list()
        cut_dna.append(split_dna.pop(0) + start)
        for dna in split_dna:
            cut_dna.append(last + dna + start)
        cut_dna[-1] = cut_dna[-1][:-len(start)]
        return cut_dna

    # convert ATGC => TACG
    def reverse(self):
        return RestEnz(self.dna.reverse_complement()[::-1])

    def get_dna(self):
        return self.dna

    @staticmethod
    def get_restriction_enzyme(name):
        with open('../config.yml') as f:
            url = f.read() + '?name=' + name
            html = requests.get(url).text
            get_json = json.loads(html)
            return get_json


class NotCodonError(Exception):

    def __str__(self):
        return 'not codon included'
