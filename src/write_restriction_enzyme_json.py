import json

if __name__ == '__main__':
    name_1 = ['Aat_Ⅱ', 'Acc_1', 'Acc_Ⅱ', 'Acc_Ⅲ', 'Afa_1', 'Afl_Ⅱ', 'Alu_1', 'Aor13H_I', 'Aor51H_I', 'Apa_1', 'ApaL_1', 'Ava_1', 'Ava_Ⅱ', 'Avi_Ⅱ', 'Bal_1']
    name_2 = ['BamH_1', 'Ban_Ⅱ', 'Bbe_1', 'Bcn_1', 'Bgl_Ⅱ', 'Bln_1', 'BmeT110', 'BmgT120', 'Bpu1102', 'BspT104', 'Bsp1286', 'Bsp1407', 'BssH_Ⅱ']
    name_3 = ['Bst1107', 'Cfr10_1', 'Cfr13_1', 'Cla_1', 'Cpo_1', 'Dra_1', 'Eae_1', 'EcoO109', 'EcoR_1', 'EcoR_Ⅴ']
    name_4 = ['EcoT14_1', 'EcoT22_1', 'Eco52_1', 'Eco81_1', 'Fba_1', 'Hae_Ⅱ', 'Haa_Ⅲ', 'Hap_Ⅱ', 'Hinc_Ⅱ', 'Hind_Ⅲ', 'Hin1_1', 'Hpa_1', 'Kpn_1']
    name_5 = ['Mfl_1', 'Mlu_1']
    name_6 = ['Mun_1', 'Mva_1', 'Nae_1', 'Nco_1', 'Nde_1', 'Nhe_1', 'Not_1', 'Nru_1']
    name_7 = ['PmaC_1', 'PshB_1', 'Psp1406_1', 'Pst_1']
    name_8 = ['Pvu_1', 'Pvu_Ⅱ', 'RspRS_Ⅱ', 'Sas_1', 'Sac_Ⅱ', 'Sal_1', 'Sau3A_1', 'Sca_1', 'Sma_1', 'Smi_1', 'Spe_1', 'Sse8387_1', 'Ssp_1', 'Stu_1', 'Taq_1']
    name_9 = ['Xba_1', 'Xho_1', 'Xsp_1']
    name_list = []
    name_list = name_1 + name_2 + name_3 + name_4 + name_5 + name_6 + name_7 + name_8 + name_9

    Aat_Ⅱ = [
        ['GACGTC', 'GACGT', 'C']
    ]
    Acc_1 = [
        ['GTAGAC', 'GT', 'AGAC'],
        ['GTATAC', 'GT', 'ATAC'],
        ['GTCGAC', 'GT', 'CGAC'],
        ['GTCTAC', 'GT', 'CTAC']
    ]
    Acc_Ⅱ = [
        ['CGCG', 'CG', 'CG']
    ]
    Acc_Ⅲ = [
        ['TCCGGA', 'T', 'CCGGA']
    ]
    Afa_1 = [
        ['GTAC', 'GT', 'AC']
    ]
    Afl_Ⅱ = [
        ['CTTAAG', 'C', 'TTAAG']
    ]
    Alu_1 = [
        ['AGCT', 'AG', 'CT']
    ]
    Aor13H_1 = [
        ['TCCGGA', 'T', 'CCGGA']
    ]
    Aor51H_1 = [
        ['AGCGCT', 'AGC', 'GCT']
    ]
    Apa_1 = [
        ['GGGCCC', 'GGGCC', 'C']
    ]
    ApaL_1 = [
        ['GTGCAC', 'G', 'TGCAC']
    ]
    Ava_1 = [
        ['CCCGAG', 'C', 'CCGAG'],
        ['CCCGGG', 'C', 'CCGGG'],
        ['CTCGAG', 'C', 'TCGAG'],
        ['CTCGGG', 'C', 'TCGGG']
    ]
    Ava_Ⅱ = [
        ['GGACC', 'G', 'GACC'],
        ['GGTCC', 'G', 'GTCC']
    ]
    Avi_Ⅱ = [
        ['TGCGCA', 'TGC', 'GCA']
    ]
    Bal_1 = [
        ['TGGCCA', 'TGG', 'CCA']
    ]

    BamH_1 = [
        ['GGATCC', 'G', 'GATCC']
    ]
    Ban_Ⅱ = [
        ['GAGCCC', 'GAGCC', 'C'],
        ['GAGCTC', 'GAGCT', 'C'],
        ['GGGCCC', 'GGGCC', 'C'],
        ['GGGCTC', 'GGGCT', 'C']
    ]
    Bbe_1 = [
        ['GGCGCC', 'GGCGC', 'C']
    ]
    Bcn_1 = [
        ['CCGGG', 'CC', 'GGG'],
        ['CCCGG', 'CC', 'CGG']
    ]
    Bgl_Ⅱ = [
        ['AGATCT', 'A', 'GATCT']
    ]
    Bln_1 = [
        ['CCTAGG', 'C', 'CTAGG']
    ]
    BmeT110 = [
        ['CCCGAG', 'C', 'CCGAG'],
        ['CCCGGG', 'C', 'CCGGG'],
        ['CTCGAG', 'C', 'TCGAG'],
        ['CTCGGG', 'C', 'TCGGG']
    ]
    BmgT120 = [
        ['GGACC', 'G', 'GACC'],
        ['GGCCC', 'G', 'GCCC'],
        ['GGGCC', 'G', 'GGCC'],
        ['GGTCC', 'G', 'GTCC']
    ]
    Bpu1102 = [
        ['GCTAAGC', 'GC', 'TAAGC'],
        ['GCTTAGC', 'GC', 'TTAGC'],
        ['GCTGAGC', 'GC', 'TGAGC'],
        ['GCTCAGC', 'GC', 'TCAGC']
    ]
    BspT104 = [
        ['TTCGAA', 'TT', 'CGAA']
    ]
    Bsp1286 = [
        ['GDGCHC', 'GDGCH', 'C'],
        ['GDGCHC', 'GDGCH', 'C'],
        ['GDGCHC', 'GDGCH', 'C'],
    ]
    Bsp1407 = [
        ['TGTACA', 'T', 'GTACA']
    ]
    BssH_Ⅱ = [
        ['GCGCGC', 'G', 'CGCGC']
    ]

    Bst1107 = [
        ['GTATAC', 'GTA', 'TAC']
    ]
    Cfr10_１ = [
        ['ACCGGC', 'A', 'CCGGC'],
        ['GCCGGT', 'G', 'CCGGT'],
    ]
    Cfr13_1 = [
        ['GGACC', 'G', 'GACC'],
        ['GGTCC', 'G', 'GTCC'],
        ['GGGCC', 'G', 'GGCC'],
        ['GGCCC', 'G', 'GCCC'],
    ]
    Cla_1 = [
        ['ATCGAT', 'AT', 'CGAT']
    ]
    Cpo_1 = [
        ['CGGACCG', 'CG', 'GACCG'],
        ['CGGTCCG', 'CG', 'GTCCG'],
    ]
    Dra_1 = [
        ['TTTAAA', 'TTT', 'AAA']
    ]
    Eae_1 = [
        ['CGGCCA', 'C', 'GGCCA'],
        ['CGGCCG', 'C', 'GGCCG'],
        ['TGGCCA', 'T', 'GGCCA'],
        ['TGGCCG', 'T', 'GGCCG']
    ]

    EcoO109 = [
        ['AGGNCCC', 'AG', 'GNCCC'],
        ['AGGNCCT', 'AG', 'GNCCT'],
        ['GGGNCCC', 'GG', 'GNCCC'],
        ['GGGNCCT', 'GG', 'GNCCT']
    ]
    EcoR_1 = [
        ['GAATTC', 'G', 'AATTC']
    ]
    EcoR_Ⅴ = [
        ['GATATC', 'GAT', 'ATC']
    ]
    EcoT14 = [
        ['CCAAGG', 'C', 'CAAGG'],
        ['CCATGG', 'C', 'CATGG'],
        ['CCTAGG', 'C', 'CTAGG'],
        ['CCTTGG', 'C', 'CTTGG']
    ]
    EcoT22 = [
        ['ATGCAT', 'ATGCA', 'T']
    ]
    Eco52_1 = [
        ['CGGCCG', 'C', 'GGCCG']
    ]
    Eco81_1 = [
        ['CCTAAGG', 'CC', 'TAAGG'],
        ['CCTTAGG', 'CC', 'TTAGG'],
        ['CCTGAGG', 'CC', 'TGAGG'],
        ['CCTCAGG', 'CC', 'TCAGG'],
    ]
    Fba_1 = [
        ['TGATCA', 'T', 'GATCA']
    ]
    Hae_Ⅱ = [
        ['AGCGCC', 'AGCGC', 'C'],
        ['AGCGCT', 'AGCGC', 'T'],
        ['GGCGCC', 'GGCGC', 'C'],
        ['GGCGCT', 'GGCGC', 'T'],
    ]
    Hae_Ⅲ = [
        ['GGCC', 'GG', 'CC']
    ]
    Hap_Ⅱ = [
        ['CCGG', 'C', 'CGG']
    ]
    Hinc_Ⅱ = [
        ['GTCAAC', 'GTC', 'AAC'],
        ['GTCGAC', 'GTC', 'GAC'],
        ['GTTAAC', 'GTT', 'AAC'],
        ['GTTGAC', 'GTT', 'GAC'],
    ]
    Hind_Ⅲ = [
        ['AAGCTT', 'A', 'AGCTT']
    ]
    Hin1_1 = [
        ['GACGCC', 'GA', 'CGCC'],
        ['GACGTC', 'GA', 'CGTC'],
        ['GGCGCC', 'GG', 'CGCC'],
        ['GGCGTC', 'GG', 'CGTC'],
    ]
    Hpa_1 = [
        ['GTTAAC', 'GTT', 'AAC']
    ]
    Kpn_1 = [
        ['GGTACC', 'GGTAC', 'C']
    ]


    Mfl_1 = [
        ['AGATCC', 'A', 'GATCC'],
        ['AGATCT', 'A', 'GATCT'],
        ['GGATCC', 'G', 'GATCC'],
        ['GGATCT', 'G', 'GATCT'],
    ]
    Mlu_1 = [
        ['ACGCGT', 'A', 'CGCGT']
    ]

    Mun_1 = [
        ['CAATTG', 'C', 'AATTG']
    ]
    Mva_1 = [
        ['CCWGG', 'CC', 'WGG']
    ]
    Nae_1 = [
        ['GCCGGC', 'GCC', 'GGC']
    ]
    Nco_1 = [
        ['CCATGG', 'C', 'CATGG']
    ]
    Nde_1 = [
        ['CATATG', 'CA', 'TATG']
    ]
    Nhe_1 = [
        ['GCTAGC', 'G', 'CTAGC']
    ]
    Not_1 = [
        ['GCGGCCGC', 'GC', 'GGCCGC']
    ]
    Nru_1 = [
        ['TCGCGA', 'TCG', 'CGA']
    ]

    PmaC_1 = [
        ['CACGTG', 'CAC', 'GTG']
    ]
    PshB_1 = [
        ['AACGTT', 'AA', 'CGTT']
    ]
    Pst_1 = [
        ['CTGCAG', 'CTGCA', 'G']
    ]

    Pvu_1 = [
        ['CGATCG', 'CGAT', 'CG']
    ]
    Pvu_Ⅱ = [
        ['CAGCTG', 'CAG', 'CTG']
    ]
    RspRS_Ⅱ = [
        ['TTAA', 'T', 'TAA']
    ]
    Sac_1 = [
        ['GAGCTC', 'GAGCT', 'C']
    ]
    Sac_Ⅱ = [
        ['CCGCGG', 'CCGC', 'GG']
    ]
    Sal_1 = [
        ['GTCGAC', 'G', 'TCGAC']
    ]

    Sau3A_1 = [
        ['GATC', '', 'GATC']
    ]
    Sca_1 = [
        ['AGTACT', 'AGT', 'ACT']
    ]
    Sma_1 = [
        ['CCCGGG', 'CCC', 'GGG']
    ]
    Smi_1 = [
        ['ATTTAAAT', 'ATTT', 'AAAT']
    ]
    Spe_1 = [
        ['ACTAGT', 'A', 'CTAGT']
    ]
    Sse8387 = [
        ['CCTGCAGG', 'CCTGCA', 'GG']
    ]
    Ssp_1 = [
        ['AATATT', 'AAT', 'ATT']
    ]
    Stu_1 = [
        ['AGGCCT', 'AGG', 'CCT']
    ]
    Taq_1 = [
        ['TCGA', 'T', 'CGA']
    ]

    Xba_1 = [
        ['TCTAGA', 'T', 'CTAGA']
    ]
    Xho_1 = [
        ['CTCGAG', 'C', 'TCGAG']
    ]
    Xsp_1 = [
        ['CTAG', 'C', 'TAG']
    ]
    restriction_enzymes = [Aat_Ⅱ, Acc_1, Acc_Ⅱ, Acc_Ⅲ, Afa_1, Afl_Ⅱ, Alu_1, Aor13H_1, Aor51H_1, Apa_1, ApaL_1, Ava_1,
                          Ava_Ⅱ, Avi_Ⅱ, Bal_1, BamH_1, Ban_Ⅱ, Bbe_1, Bcn_1, Bgl_Ⅱ, Bln_1, BmeT110, BmgT120, Bpu1102,
                          BspT104, Bsp1286, Bsp1407, BssH_Ⅱ, Bst1107, Cfr10_１, Cfr13_1, Cla_1, Cpo_1, Dra_1, Eae_1,
                          EcoO109, EcoR_1, EcoR_Ⅴ, EcoT14, EcoT22, Eco52_1, Eco81_1, Fba_1, Hae_Ⅱ, Hae_Ⅲ, Hap_Ⅱ, Hinc_Ⅱ,
                          Hinc_Ⅱ, Hind_Ⅲ, Hin1_1, Hpa_1, Kpn_1, Mfl_1, Mlu_1, Mun_1, Mva_1, Nae_1, Nco_1, Nde_1, Nhe_1,
                          Not_1, Nru_1, PmaC_1, PshB_1, Pst_1, Pvu_1, Pvu_Ⅱ, RspRS_Ⅱ, Sac_1, Sac_Ⅱ, Sal_1, Sau3A_1,
                          Sca_1, Sma_1, Smi_1, Spe_1, Sse8387, Ssp_1, Stu_1, Taq_1, Xba_1, Xho_1, Xsp_1]

    enzyme_list = []
    for enzyme, name in zip(restriction_enzymes, name_list):
        recognition_site = []
        total_site = 0
        for recog_arr in enzyme:
            arr = {
                'whole': recog_arr[0],
                'first': recog_arr[1],
                'last': recog_arr[2]
            }
            recognition_site.append(arr)
            total_site += 1
        enzyme_list.append({'name': name, 'total_site': total_site, 'recognition_site': recognition_site})
    f = open('../restriction_enzymes.json', 'w')
    json.dump(enzyme_list, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))
