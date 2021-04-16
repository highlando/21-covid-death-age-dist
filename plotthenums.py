import pandas as pd
import numpy as np

import seaborn as sns
# import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set_theme()

diamonds = sns.load_dataset("diamonds")


shname = 'COVID_Todesfälle_KW_AG10'
flname = 'COVID-19_Todesfaelle.xlsx'
cvdths = pd.read_excel(flname, sheet_name=shname, engine='openpyxl')

# f, ax = plt.subplots(figsize=(7, 5))
# sns.despine(f)
# sns.histplot(
#     # cvdths,
#     diamonds,
#     x="Sterbewoche", hue="cut",
#     multiple="stack",
#     palette="light:m_r",
#     edgecolor=".3",
#     linewidth=.5,
#     log_scale=True,
# )
# ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
# ax.set_xticks([500, 1000, 2000, 5000, 10000])

penguins = sns.load_dataset("penguins")

# sns.histplot(data=penguins, x="flipper_length_mm",
#              hue="species", multiple="stack")

print(cvdths)
# print(penguins)


def cleardatalists(pdlist):
    nwlst = []
    for dtpt in pdlist:
        if dtpt == '<4':
            nwlst.append(3)
        else:
            nwlst.append(int(dtpt))
    return np.array(nwlst)


strbwch = cvdths.Sterbewoche.to_list()

categrs = ['90+', '80-89', '70-79', '60-69', '50-59', '40-49',
           '30-39', '20-29', '10-19', '0-9']
categrs.reverse()

datpts = []
for ctgr in categrs:
    curname = 'AG ' + ctgr + ' Jahre'
    datpts.append(cleardatalists(cvdths[curname].to_list()))

abscss = range(len(strbwch))
kwticks = [0, 10, 20, 30, 40, 50]
kwlabels = ['KW{0}'.format(strbwch[kk]) for kk in kwticks]

fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
plt.xticks(ticks=kwticks, labels=kwlabels)
plt.title('Tote in Altersgruppen pro Kalenderwoche in 2020/21')
plt.stackplot(abscss, datpts, labels=categrs)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='Altersgruppen', loc='upper left')
plt.savefig('toteperkw-total.png')

dataptsar = np.array(datpts)
sumdtpts = dataptsar.sum(axis=0)
nrmlzddta = dataptsar / sumdtpts

fig = plt.figure(2, figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
plt.title('Anteile der Altersgruppen pro Kalenderwoche in 2020/21')
plt.xticks(ticks=kwticks, labels=kwlabels)
plt.stackplot(abscss, nrmlzddta, labels=categrs)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title='Altersgruppen', loc='upper left')
plt.savefig('toteperkw-relativ.png')

# print(diamonds)

plt.show()
