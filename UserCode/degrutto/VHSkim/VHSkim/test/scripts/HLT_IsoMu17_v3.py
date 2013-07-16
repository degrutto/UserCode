#! /usr/bin/env python

import sys
import os
import commands
import string


triggerName = "HLT_IsoMu17_v*"
change = False
changerun = "0"

def fib(run):
        global change
        global changerun
        if not change:
	  os.system("rm  poo1 2> error")
	  os.system("rm  ppp 2> error")
          changerun = run
	  os.system("./lumiContext.py hltbyls -name \"%s\" -r %s | grep \",1\" > poo1" % (triggerName, run))
	  os.system("more poo1 | wc -l > ppp")
          f = open("ppp", "r")
          num = int(f.read())
          if num < 1:
            change = True 



L = [160404, 

 160405, 

 160406, 

 160410, 

 160413, 

 160431, 

 160432, 

 160433, 

 160442, 

 160443, 

 160444, 

 160445, 

 160446, 

 160447, 

 160449, 

 160450, 

 160454, 

 160455, 

 160456, 

# 160462, 

# 160463, 

 160497, 

 
 160498, 

 160499, 

 160577, 

 160578, 

 160579, 

 160808, 

 160815, 

 160819, 

 
 160827, 

 160835, 

 
 
 160853, 

 160871, 

 160872, 

 160873, 

 160874, 

 160875, 

 160876, 

 160877, 

 
 160888, 

 160890, 

 160894, 

 160898, 

 160907, 

 160911, 

 160913, 

 160914, 

 160915, 

 160916, 

 160935, 

 160936, 

 160937, 

 160938, 

 160939, 

 160940, 

 160942, 

 160943, 

 160954, 

 160955, 

 160956, 

 160957, 

# 160994, 

 160998, 

 161008, 

 161016, 

# 161020, 

 161103, 

 161106, 

 161107, 

 161113, 

 161116, 

 161117, 

 161119, 

# 161156, 

 161165, 

 161176, 

 161216, 

 161217, 

 161222, 

 161223, 

 161224, 

 161233, 

 161310, 

 161311, 

 161312, 

 162718, 

 162733, 

 162739, 

 
 162742, 

 
 162760, 

 162762, 

 162765, 

 162803, 

 162808, 

# 162810, 

 162811, 

 162822, 

 162825, 

 162826, 

 162827, 

 162828, 

 162909, 

 162917, 

 162924, 

 162925, 

 162926, 

 162929, 

 
 163045, 

 163046, 

 
 163069, 

 163071, 

 163072, 

 163078, 

 163232, 

 163233, 

 163234, 

 163235, 

 163237, 

 163238, 

 163252, 

 163255, 

 163261, 

 163269, 

 163270, 

 163286, 

 163289, 

 163296, 

 163297, 

 163300, 

 163301, 

 163302, 

 163308, 

 163332, 

 163333, 

 163334, 

 163337, 

 163338, 

 163339, 

 163340, 

 
 163358, 

 163369, 

 163370, 

 163371, 

 163372, 

 163374, 

 163375, 

 163376, 

 163378, 

 163385, 

 163387, 

 
 163402, 

 163475, 

 163476, 

 163478, 

 163479, 

 163480, 

 163481, 

 163482, 

 163483, 

 163581, 

 163582, 

 163583, 

 163584, 

 163585, 

 163586, 

 163587, 

 163588, 

 163589, 

 163591, 

 163592, 

 163593, 

 163596, 

 163630, 

 163655, 

 163657, 

 163658, 

 163659, 

 163660, 

 163661, 

 163662, 

 163663, 

 163664, 

 163665, 

 163668, 

 
 163738, 

 163753, 

# 163754, 

 163757, 

 163758, 

 163759, 

 163760, 

 163761, 

 163763, 

 163765, 

 163795, 

 163796, 

 163817, 

 163869, 

 165088, 

 165098, 

 165099, 

 165100, 

 165102, 

 165103, 

 165104, 

 165120, 

 165121, 

 165205, 

 165208, 

 165364, 

 
 165400, 

 165402, 

 165415, 

 165467, 

 165472, 

 165486, 

 165487, 

 165506, 

 165514, 

 165523, 

 165525, 

 165529, 

 165537, 

 165542, 

 165548, 

 165558, 

 165567, 

 165570, 

 165617, 

 165619, 

 165620, 

 165633, 

 165970, 

 165993, 

 166010, 

 166011, 

 166033, 

 166034, 

 166049, 

 166051, 

 166052, 

 166149, 

 166150, 

 166161, 

 166163, 

 166164, 

 166346, 

 166374, 

 166377, 

 166379, 

 166380, 

 166394, 

 166408, 

 166429, 

 166438, 

 166462, 

 166486, 

 166502, 

 166512, 

 166514, 

 166530, 

 166554, 

 166563, 

 
 166565, 

 166699, 

 166701, 

 166763, 

 166781, 

 
 
 166782, 

 166784, 

 166787, 

 166839, 

 166841, 

 166842, 

 166859, 

 166860, 

 166861, 

 166862, 

 166863, 

 166864, 

 166888, 

 166889, 

 166890, 

 166893, 

 166894, 

 166895, 

 166911, 

 166921, 

 166922, 

 166923, 

 166946, 

 166950, 

 166960, 

 166966, 

 166967, 

 167039, 

 167041, 

 167043, 

 167078, 

 167098, 

 167102, 

 167103, 

 167151, 

 167281, 

 167282, 

 167284, 

 167551, 

 167673, 

 167674, 

 167675, 

 167676, 

 167740, 

 167746, 

 167754, 

 167784, 

 167786, 

 167807, 

 
 167830, 

 167898, 

 167913, 

 169985, 

 169991, 

 170000, 

 
 170040, 

 
 170044, 

 170249, 

 170255, 

 170286, 

 170292, 

 170298, 

 170303, 

 170304, 

 170307, 

 170348, 

 170354, 

 170376, 

 170378, 

 170380, 

 170382, 

 170397, 

 170406, 

 170452, 

 170527, 

 170722, 

 170759, 

 170826, 

 170842, 

 170854, 

 170876, 

 170896, 

 170899, 

 170901, 

 171050, 

 171091, 

 171098, 

 171102, 

 171106, 

 171116, 

 171117, 

 
 171156, 

 171178, 

 171219, 

 171274, 

 171282, 

 171315, 

 171369, 

 171446, 

 171484, 

 171578, 

 171812, 

 171875, 

 171876, 

 171879, 

 171880, 

 171890, 

 171895, 

 
 171897, 

 
 
 
 
 
 171921, 

 171926, 

 172014, 

 172024, 

 172033, 

 172163, 

 172208, 

 172252, 

 172254, 

 172255, 

 172268, 

 172286, 

 172389, 

 172399, 

 172400, 

 172401, 

 172411, 

 172478, 

 172485, 

 172488, 

 
 
 
 
 
 
 
 172495, 

 172497, 

 172507, 

 
 172619, 

 172620, 

 172630, 

 172635, 

 172778, 

 172791, 

 172798, 

 172799, 

 172801, 

 172802, 

 172819, 

 172822, 

 172824, 

 172847, 

 172865, 

 172868, 

 172949, 

 172951, 

 172952, 

 172992, 

 
 
 
 172998, 

 172999, 

 173198, 

 173236, 

 173240, 

 173241, 

 173243, 

 173244, 

 173380, 

 173381, 

 173389, 

 173406, 

 173430, 

 173431, 

 173438, 

 173439, 

 173657, 

 173658, 

 173659, 

 173660, 

 173661, 

 173662, 

 173663, 

 173664, 

 173692, 

 175832, 

 175833, 

 175834, 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 175835, 

 175837, 

 175857, 

 175858, 

 175860, 

 175863, 

 175865, 

 175866, 

 175872, 

 175873, 

 175874, 

 175875, 

 175877, 

 175881, 

 175886, 

 175887, 

 175888, 

 175906, 

 175910, 

 175921, 

 175971, 

 175973, 

 175974, 

 175975, 

 175976, 

 175990, 

 176023, 

 176161, 

 176163, 

 176165, 

 176166, 

 176167, 

 176169, 

 176201, 

 176202, 

 176206, 

 176207, 

 176286, 

 176289, 

 176304, 

 176308, 

 176309, 

 176461, 

 176463, 

 176464, 

 176465, 

 176466, 

 176467, 

 176468, 

 176469, 

 176470, 

 176545, 

 176547, 

 176548, 

 176697, 

 176701, 

 176702, 

 176765, 

 176771, 

 176795, 

 176796, 

 176797, 

 176799, 

 176801, 

 176805, 

 176807, 

 176841, 

 176842, 

 176844, 

 176848, 

 176850, 

 176860, 

 176868, 

 176885, 

 176886, 

 176889, 

 176928, 

 176929, 

 176933, 

 176959, 

 176982, 

 177053, 

 177074, 

 177088, 

 177095, 

 177096, 

 177131, 

 177138, 

 177139, 

 177140, 

 177141, 

 177183, 

 177184, 

 177201, 

 177222, 

 177313, 

 177317, 

 177318, 

 177319, 

 177449, 

 177452, 

 177507, 

 177509, 

 177515, 

 177718, 

 177719, 

 177730, 

 177776, 

 177782, 

 177783, 

 177785, 

 177786, 

 177788, 

 177789, 

 177790, 

 177791, 

 177875, 

 177878, 

 178078, 

 178098, 

 178099, 

 178100, 

 178101, 

 178102, 

 178110, 

 178116, 

 178151, 

 178160, 

 178162, 

 178203, 

 178207, 

 178208, 

 178365, 

 178367, 

 
 
 
 
 
 
 178380, 

 178420, 

 178421, 

 178424, 

 178479, 

 178667, 

 178675, 

 178677, 

 178703, 

 178708, 

 178712, 

 178724, 

 178731, 

 178738, 

 178786, 

 178803, 

 178840, 

 178854, 

 178866, 

 178871, 

 178920, 

 178970, 

 178985, 

 179315, 

 179348, 

 179411, 

 179434, 

 179452, 

 179476, 

 179497, 

 179547, 

 179558, 

 179563, 

 179816, 

 179823, 

 179827, 

 179828, 

 179889, 

 179959, 

 179977, 

 144]

for item in L:
        fib(item)


print("Prescale Changed in Run #%s" % changerun)