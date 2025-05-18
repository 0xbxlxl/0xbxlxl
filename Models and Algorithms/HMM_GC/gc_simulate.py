# -*- coding: utf-8 -*-

"""

Created on Wed Nov 14  16:58:07 2024

@author: P. Meinicke

"""

#%%

import numpy as np
import numpy.random as nr

n_states = 2 # normal (background) and abnormal (foreground) GC-content 
seq_len = 100000 # short sequence for fast results (with reasonable programming ;)

prob_backg_vec = np.array([0.29, 0.21, 0.21, 0.29]) # "background" low/medium-GC genomic ("normal") content   
prob_foreg_vec = np.array([0.16, 0.34, 0.34, 0.16]) # "foreground" high-GC ("island") content 
emiss_prob_mat = np.array((prob_backg_vec, prob_foreg_vec))
trans_prob_mat = np.array(([0.999, 0.001], [0.005, 0.995]))


i_state = 0 # 0: background, 1: foreground - you could choose it randomly, but let's start with some "normal" content :)
bg_alphabet_vec = np.array(list('acgt'))
fg_alphabet_vec = np.array(list('ACGT'))
alphabet_mat = np.array((bg_alphabet_vec,fg_alphabet_vec))

np.random.seed(42) # do not change this!

#%%
seq_labeled = ''
seq_unlabeled = ''

# not the most efficient way, but just for generation of one sequence this should be ok ;)
state_vec = np.zeros(seq_len)
for i_seq in range(seq_len):
    state_vec[i_seq] = i_state
    i_alph = np.argmax(nr.multinomial(1, emiss_prob_mat[i_state]))
    seq_labeled += str(alphabet_mat[i_state][i_alph][0]) 
    seq_unlabeled += str(fg_alphabet_vec[i_alph][0]) 
    i_state = np.argmax(nr.multinomial(1, trans_prob_mat[i_state]))
     
# print(seq_labeled) # ground truth for performance analysis                      
# print(seq_unlabeled) # input to HMM-based state prediction

seq_vec = np.array(list(seq_unlabeled)) # sequence to be analyzed
gc_content = np.mean(seq_vec == 'C') + np.mean(seq_vec == 'G') # overall GC-content

# -*- coding: utf-8 -*-

"""

Created on Wed Nov 14  16:58:07 2024

@author: P. Meinicke

"""

#%%

import numpy as np
import numpy.random as nr

n_states = 2 # normal (background) and abnormal (foreground) GC-content 
seq_len = 100000 # short sequence for fast results (with reasonable programming ;)

prob_backg_vec = np.array([0.29, 0.21, 0.21, 0.29]) # "background" low/medium-GC genomic ("normal") content   
prob_foreg_vec = np.array([0.16, 0.34, 0.34, 0.16]) # "foreground" high-GC ("island") content 
emiss_prob_mat = np.array((prob_backg_vec, prob_foreg_vec))
trans_prob_mat = np.array(([0.999, 0.001], [0.005, 0.995]))


i_state = 0 # 0: background, 1: foreground - you could choose it randomly, but let's start with some "normal" content :)
bg_alphabet_vec = np.array(list('acgt'))
fg_alphabet_vec = np.array(list('ACGT'))
alphabet_mat = np.array((bg_alphabet_vec,fg_alphabet_vec))

np.random.seed(42) # do not change this!

#%%
seq_labeled = ''
seq_unlabeled = ''

# not the most efficient way, but just for generation of one sequence this should be ok ;)
state_vec = np.zeros(seq_len)
for i_seq in range(seq_len):
    state_vec[i_seq] = i_state
    i_alph = np.argmax(nr.multinomial(1, emiss_prob_mat[i_state]))
    seq_labeled += str(alphabet_mat[i_state][i_alph][0]) 
    seq_unlabeled += str(fg_alphabet_vec[i_alph][0]) 
    i_state = np.argmax(nr.multinomial(1, trans_prob_mat[i_state]))
     
# print(seq_labeled) # ground truth for performance analysis                      
# print(seq_unlabeled) # input to HMM-based state prediction

seq_vec = np.array(list(seq_unlabeled)) # sequence to be analyzed
gc_content = np.mean(seq_vec == 'C') + np.mean(seq_vec == 'G') # overall GC-content

# Save outputs to files
with open("seq_labeled.txt", "w") as f:
    f.write(seq_labeled)

with open("seq_unlabeled.txt", "w") as f:
    f.write(seq_unlabeled)

with open("state_vec.txt", "w") as f:
    f.write(",".join(map(str, state_vec.astype(int))))




